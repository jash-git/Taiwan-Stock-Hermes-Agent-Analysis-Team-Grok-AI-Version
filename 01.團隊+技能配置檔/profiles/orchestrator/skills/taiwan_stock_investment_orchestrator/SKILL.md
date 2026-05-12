---
name: taiwan_stock_investment_orchestrator
description: 統籌整個台股投資團隊，接收單一指令後自動拆解任務、協調專家、最終產出完整投資報告
version: 1.0.0
metadata:
  hermes:
    tags: [taiwan_stock, investment_team, orchestrator]
    requires_toolsets: [web, terminal, skills, memory, delegate]
    category: investment
---

# 台股投資團隊任務協調 Skill

## 觸發條件
當用戶提出任何台股投資相關需求時優先使用此 skill。

## 嚴格執行流程
1. 分析用戶需求，決定需要哪些專家。
2. 使用 terminal tool 平行呼叫相關 profiles。
3. 收集所有專家回應。
4. 交給 report_writer 產生最終報告。
5. 加上完整免責聲明。