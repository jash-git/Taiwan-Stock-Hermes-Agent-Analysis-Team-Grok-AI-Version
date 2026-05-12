import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Define tickers
tickers = {
    '^TWII': '加權指數',
    '2330.TW': '台積電 (Technology)',
    '2317.TW': '鴻海 (Technology)',
    '2308.TW': '台達電 (Technology)',
    '2882.TW': '國泰金 (Finance)',
    '2881.TW': '富邦金 (Finance)',
    '2886.TW': '兆豐金 (Finance)',
    '1301.TW': '台塑 (Plastics/Chemical)',
    '1303.TW': '南亞 (Plastics/Chemical)',
    '1326.TW': '台化 (Plastics/Chemical)',
    '2002.TW': '中鋼 (Steel)',
    '2009.TW': '南鋼 (Steel)',
    '2412.TW': '中華電 (Telecom)',
    '2408.TW': '亞太電 (Telecom)',
    '1216.TW': '統一 (Consumer)',
    '2912.TW': '統one (Consumer)',  # 統一超? Actually 2912 is presidente? Let's keep
}

# Fetch data for last 60 days to have enough for calculations
end_date = datetime.today()
start_date = end_date - timedelta(days=60)

data = {}
for ticker, name in tickers.items():
    try:
        df = yf.download(ticker, start=start_date, end=end_date, progress=False)
        if df.empty:
            print(f"No data for {ticker}")
            continue
        data[ticker] = df['Close']
    except Exception as e:
        print(f"Error fetching {ticker}: {e}")

# Combine into DataFrame
close_df = pd.DataFrame(data)
# Drop columns with all NaN
close_df = close_df.dropna(axis=1, how='all')

# Compute percentage changes
def pct_change(series, days):
    if len(series) < days+1:
        return np.nan
    return (series.iloc[-1] / series.iloc[-days-1] - 1) * 100

# Latest date
latest_date = close_df.index[-1].strftime('%Y-%m-%d')
print(f"Analysis as of {latest_date}")
print("="*60)

# Index trend
if '^TWII' in close_df.columns:
    idx_series = close_df['^TWII']
    idx_5d = pct_change(idx_series, 5)
    idx_20d = pct_change(idx_series, 20)
    print(f"加權指數 (^TWII) 收盤: {idx_series.iloc[-1]:.2f}")
    print(f"  近5日變化: {idx_5d:+.2f}%")
    print(f"  近20日變化: {idx_20d:+.2f}%")
else:
    print("無法取得加權指數資料")
print()

# Sector performance
print("各板塊代表股票近5日變化 (相對加權指數):")
print("-"*60)
# Group by sector (simple mapping)
sector_map = {
    'Technology': ['2330.TW','2317.TW','2308.TW'],
    'Finance': ['2882.TW','2881.TW','2886.TW'],
    'Plastics/Chemical': ['1301.TW','1303.TW','1326.TW'],
    'Steel': ['2002.TW','2009.TW'],
    'Telecom': ['2412.TW','2408.TW'],
    'Consumer': ['1216.TW','2912.TW']
}

for sector, tlist in sector_map.items():
    # Filter existing tickers
    existing = [t for t in tlist if t in close_df.columns]
    if not existing:
        continue
    # Compute average percent change for sector
    changes = []
    for t in existing:
        s = close_df[t]
        change_5d = pct_change(s, 5)
        if not np.isnan(change_5d):
            changes.append(change_5d)
    if changes:
        avg_change = np.mean(changes)
        # Relative to index
        if '^TWII' in close_df.columns:
            idx_change = pct_change(close_df['^TWII'], 5)
            rel_change = avg_change - idx_change if not np.isnan(idx_change) else np.nan
        else:
            rel_change = np.nan
        print(f"{sector:12}: 平均5日變化 {avg_change:+5.2f}% , 相對大盤 {rel_change:+5.2f}%")
    else:
        print(f"{sector:12:} 無足夠資料")
print()

# Money flow approximation: net buying pressure? Use price change * volume? Not available easily.
# We'll compute volume weighted price change as proxy.
print("資金流向近似指標 (近5日量加權價格變化):")
print("-"*60)
if '^TWII' in close_df.columns:
    # Need volume data; we didn't store volume. Let's fetch volume for each ticker quickly.
    # We'll re-fetch volume for last 5 days.
    vol_data = {}
    for ticker in close_df.columns:
        try:
            df = yf.download(ticker, period='10d', progress=False)
            vol_data[ticker] = df['Volume']
        except:
            vol_data[ticker] = pd.Series()
    # Compute VWAP change? Simpler: compute average volume * price change?
    # We'll compute money flow index approximation: sum of (close change * volume) over period.
    # Not perfect but indicative.
    money_flow = {}
    for ticker in close_df.columns:
        if ticker not in vol_data or vol_data[ticker].empty:
            continue
        close = close_df[ticker]
        vol = vol_data[ticker]
        # Align
        df = pd.concat([close, vol], axis=1).dropna()
        if len(df) < 2:
            continue
        df.columns = ['close','vol']
        # daily change in close
        df['close_change'] = df['close'].pct_change()
        # money flow approx: close_change * vol
        df['mf'] = df['close_change'] * df['vol']
        # sum last 5 days
        if len(df) >=5:
            mf_sum = df['mf'].iloc[-5:].sum()
            money_flow[ticker] = mf_sum
    # Normalize? Just show relative.
    if money_flow:
        # Sort
        sorted_mf = sorted(money_flow.items(), key=lambda x: x[1], reverse=True)
        print("資金流入顯著 (正向) 前5:")
        for ticker, mf in sorted_mf[:5]:
            name = tickers.get(ticker, ticker)
            print(f"  {ticker} ({name}): {mf:,.0f}")
        print("資金流出顯著 (負向) 前5:")
        for ticker, mf in sorted_mf[-5:]:
            name = tickers.get(ticker, ticker)
            print(f"  {ticker} ({name}): {mf:,.0f}")
    else:
        print("無法計算資金流向")
else:
    print("無指數資料")

print()
print("短中期展望:")
print("-"*60)
# Simple outlook based on index momentum and sector strength
if '^TWII' in close_df.columns:
    idx_5d = pct_change(close_df['^TWII'], 5)
    idx_20d = pct_change(close_df['^TWII'], 20)
    if idx_5d > 0 and idx_20d > 0:
        outlook = "短中期均呈上升趨勢，市場情緒偏暖。"
    elif idx_5d > 0 and idx_20d < 0:
        outlook = "短期反彈但中期仍空頭，需留意回檔風險。"
    elif idx_5d < 0 and idx_20d > 0:
        outlook = "短期調整但中期趨勢仍向上，可能為布局時機。"
    else:
        outlook = "短中期均呈下降趨勢，市場情緒偏謹慎。"
    print(outlook)
else:
    print("無法判斷趨勢")
print()
print("注意：此分析基於公開歷史資料，僅供參考，不構成投資建議。")