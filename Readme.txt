台股Hermes Agent分析團隊grok AI版 (Taiwan Stock Hermes Agent Analysis Team Grok AI Version)

資料來源: https://grok.com/share/bGVnYWN5LWNvcHk_4a9b3b4d-20ed-4ba0-8f62-11ecd228597f
          https://grok.com/share/bGVnYWN5LWNvcHk_90d4ff86-1cb7-49c6-ab4d-42961b38acea
		  ======
		  未實作
		  https://grok.com/share/bGVnYWN5LWNvcHk_bd09e798-33f0-4f86-9e8e-4fac746d5a58
		  https://grok.com/share/bGVnYWN5LWNvcHk_8d94868a-8eb9-467f-b8c2-9a6718b7a57f

# 0. 檔案結構
~/.hermes/
├── SOUL.md                              # (可選) 主預設 Orchestrator
│
├── profiles/
│   ├── orchestrator/                    # 主控中心 (推薦建立)
│   │   ├── SOUL.md
│   │   └── skills/
│   │       └── taiwan_stock_investment_orchestrator/
│   │           └── SKILL.md
│   │
│   ├── market_analyst/
│   │   ├── SOUL.md
│   │   └── skills/
│   │       └── taiwan_market_analysis/
│   │           └── SKILL.md
│   │
│   ├── stock_researcher/
│   │   ├── SOUL.md
│   │   └── skills/
│   │       └── individual_stock_research/
│   │           └── SKILL.md
│   │
│   ├── quant_analyst/
│   │   ├── SOUL.md
│   │   └── skills/
│   │       └── quantitative_technical_analysis/
│   │           └── SKILL.md
│   │
│   ├── risk_manager/
│   │   ├── SOUL.md
│   │   └── skills/
│   │       └── investment_risk_management/
│   │           └── SKILL.md
│   │
│   └── report_writer/
│       ├── SOUL.md
│       └── skills/
│           └── investment_report_writer/
│               └── SKILL.md
│
└── config/          # Hermes 系統設定

==============================

# 1. 建立主 Orchestrator (推薦)
hermes setup # 設定 模型+API KEY : sk-or-v1-606ec3c3bb00d4763f9c1ddcc0e40f16…OOOOOOc2ace28a4ea4563263de3e05df85feab
hermes profile create orchestrator --clone

# 2. 建立其他 profiles
hermes profile create market_analyst --clone
hermes profile create stock_researcher --clone
hermes profile create quant_analyst --clone
hermes profile create risk_manager --clone
hermes profile create report_writer --clone
hermes profile list

 Profile          Model                        Gateway      Alias
 ───────────────    ───────────────────────────    ───────────    ────────────
 ◆default         nvidia/nemotron-3-super-12   stopped      —
  market_analyst  nvidia/nemotron-3-super-12   stopped      market_analyst
  orchestrator    nvidia/nemotron-3-super-12   stopped      orchestrator
  quant_analyst   nvidia/nemotron-3-super-12   stopped      quant_analyst
  report_writer   nvidia/nemotron-3-super-12   stopped      report_writer
  risk_manager    nvidia/nemotron-3-super-12   stopped      risk_manager
  stock_researcher nvidia/nemotron-3-super-12   stopped      stock_researcher


# 3. 建立各 SKILL 目錄
mkdir -p ~/.hermes/profiles/orchestrator/skills/taiwan_stock_investment_orchestrator
mkdir -p ~/.hermes/profiles/market_analyst/skills/taiwan_market_analysis
mkdir -p ~/.hermes/profiles/stock_researcher/skills/individual_stock_research
mkdir -p ~/.hermes/profiles/quant_analyst/skills/quantitative_technical_analysis
mkdir -p ~/.hermes/profiles/risk_manager/skills/investment_risk_management
mkdir -p ~/.hermes/profiles/report_writer/skills/investment_report_writer

# 4. 寫入對應檔案內容

# 5. VM重開機

# 6. 測試主控
hermes -p orchestrator chat
	輸入提問: 你是誰
		Welcome to Hermes Agent! Type your message or /help for commands.
		✦ Tip: /rollback diff 2 previews what changed since checkpoint 2 without restoring anything.


		────────────────────────────────────────
		● 你是誰
		Initializing agent...

		────────────────────────────────────────

		╭─ ⚕ Hermes ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
			我是台股投資智能體團隊的任務調度中心（Orchestrator）。我的職責是接收用戶的單一指令，拆解任務並協調旗下的專家團隊（包括市場分析師、個股研究員、量化分析師、風險管理師和報告撰寫員），最後輸出完整的專業投資報告。我自己不進行深度分析，只負責調度與最終整合，並透過 terminal tool 呼叫各專家 profiles 來完成具體工作。
		╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
		 ⚕ nemotron-3-super-120b-a... │ 16.1K/262.1K │ [█░░░░░░░░░] 6% │ 1m │ ⏲ 26s 
		────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
		orchestrator   
		
	輸入提問: 呼叫 market_analyst 分析目前台股大盤趨勢
		Initializing agent...

		────────────────────────────────────────
		  ┊ 🔀 preparing delegate_task…
		  ┊ 🔀 delegate  分析目前台股大盤趨勢與板塊輪動  328.6s
		  ┊ 💻 preparing terminal…
		  ┊ 💻 $         curl -s "https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=20260512&type=ALL" | head -20  1.8s
		  ┊ 💻 preparing terminal…
		  ┊ 💻 $         curl -s "https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=20260512&type=ALL" | iconv -f big5 -t utf-8 | head -30  11.9s

		╭─ ⚕ Hermes ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
			台股加權指數（發行量加權股價指數）今日收於 41,898.32 點，漲 108.26 點（+0.26%），整體呈現溫和上揚。  
			從盤後指數可觀察到板塊輪動情形：
			
			* 資訊科技指數：82,125.90 點，+525.31 點（+0.64%），為今日最大漲幅板塊，帶動指數上揚。  
			* 未含電子指數：20,445.20 點，-253.73 點（-1.23%），顯示電子類權重股表現強勁，若剔除電子則指數會下跌。  
			* 未含金融指數：38,069.16 點，+163.78 點（+0.43%），高於加權指數漲幅，說明金融類今日相對弱勢，可能拖累大盤。  
			* 其他主要板塊：塑膠化工類 (-1.48%)、生技醫療類 (-1.79%)、化學類 (+1.29%)、電機機械類 (+1.33%) 等呈現分化。  
			
			資金流向近似觀察（以價格變動×成交量粗略估計）：科技板塊買氣活躍，金融板塊賣壓較重，資金略倾向科技與電機機械等週期性產業。
			
			短中期展望  
			* 短線：科技領漲動能尚未衰竭，若能守住 82,000 點關卡，加權指數有望挑戰 42,200–42,500 點區間。  
			* 中線：需關注金融板塊是否企穩；若金融回暖，將提升指數穩健度。同時美洲聯準會政策與中國大陸經濟數據仍是外部變數。  
			* 風險點：科技過熱可能引發獲利了結，電子供應鏈任何負面消息皆可能快速打壓盤面。
			
			> 注意：以上分析基於今日盤後公開資料及歷史模式，僅供參考。投資決策仍需結合基本面、國際面及個別公司面向，並注意風險控制。

# 7. 實際使用
hermes -p orchestrator chat
	輸入提問: 就目前國際局勢，建議台股可進場的買入股票並給出完整分析，並將分析結果輸出成md檔案
