# Accio 产品调研 — 阿里国际 AI Agent 平台

> 调研目的：面试阿里国际 Accio 团队 Agent 开发岗位，理解产品全貌与技术架构。
> 更新时间：2026-04-01

---

## 一、产品概览

**Accio** 是阿里国际站推出的 AI 驱动全球贸易平台，名字取自《哈利波特》的召唤咒语。目标是用 AI Agent 自动化跨境贸易全链路，降低中小企业（尤其是一人公司、Solo Founder）的全球贸易门槛。

- **目标用户**：欧美中小企业主、独立站卖家、一人公司创业者（约 40% 的中小企业是独立运营者）
- **核心痛点**：跨境贸易涉及市场调研、选品、供应商筛选、RFQ 谈判、合规报关、建站运营等大量跨专业环节，传统人工流程耗时数周
- **当前规模**：全球月活超过 **1000 万**
- **独立域名**：Accio.com（2026.03 上线）

---

## 二、产品演进路线（三个阶段）

| 阶段 | 时间 | 产品形态 | 核心能力 |
|------|------|---------|---------|
| **Accio Search** | 2024.11 | B2B AI 搜索引擎 | 自然语言描述需求 → 多轮对话理解采购意图 → 推荐供应商和商品 |
| **Accio Agent** | 2025.08 | 国际贸易 AI Agent | 自动化 70% 人工采购流程：方案生成、供应商筛选、RFQ 自动化、报价评估 |
| **Accio Work** | 2026.03 | 企业级 Multi-Agent 平台 | 多专家 Agent 协同、30 分钟快速建站、全链路自动化运营、No-Code 工作台 |

**演进逻辑**：AI Search（理解意图）→ AI Agent（执行单任务）→ Multi-Agent Platform（编排多 Agent 协作）

---

## 三、核心功能拆解

### Accio Search
- 用户用自然语言描述需求，系统通过多轮对话理解真实采购意图
- 基于 B2B 行业知识拆解需求、调研市场、推荐供应商和商品
- AI 重构的商品百科页面

### Accio Agent
- **采购方案生成**：把产品概念转化为详细采购简报（规格、数量、预算、时间线、认证要求）
- **供应商筛选**：自动审核产能、质量信号、评价、合规资质
- **RFQ 自动化**：自动生成并发送 RFQ 给预筛选供应商
- **报价评估**：按价格、交期、MOQ、质量、物流等维度排序打分
- **决策支持**：生成带理由摘要的候选短名单

### Accio Work（最新、最重要）
- **多专家 Agent 团队**：选品专家、视觉设计师、营销策划、客服主管等角色 Agent 协同
- **30 分钟快速建站**：自动完成 Shopify 等平台店铺搭建、商品上架（批量生成标题/描述/SEO 关键词）、Logo 和 Banner 设计
- **全链路自动化运营**：自主发帖、投广告、寻找供应商并谈判采购
- **合规自动化**：管理 100+ 市场的 VAT 申报、退税、海关文档
- **技能库**：电商与供应链 19 个技能 + 营销与内容 20 个技能
- **48 个第三方平台集成**：Gmail、X、LinkedIn、Instagram、GitHub 等；TikTok、Meta Ads 即将推出
- **可自定义 Skills**：用户可将独有流程封装为可复用的"技能"

---

## 四、底层技术架构推测

### 大模型基座
- 主要基于阿里自研 **Qwen 系列模型**（正在从 DeepSeek R1 切换至 Qwen3）
- Accio Work 也在使用 **Claude 模型**（Anthropic），说明是**多模型路由架构**
- 2025.02 曾接入 **DeepSeek 推理模型**，用于深度研究功能

### 核心技术栈

| 技术方向 | 推测实现 |
|---------|---------|
| **RAG** | 基于 10 亿+ 商品数据、5000 万+ 供应商数据、实时海关与汇率数据构建的领域 RAG 系统 |
| **Multi-Agent 架构** | 多专家 Agent 协作，接收目标后自动组装跨职能"小队"并行执行 |
| **Agent Orchestration** | 动态编排引擎，根据任务类型调度不同专业 Agent |
| **Tool Use / Function Calling** | RFQ 发送、供应商数据库查询、平台 API 调用、浏览器操作等 |
| **MCP 协议** | Qwen-Agent 已支持 MCP，48 个第三方集成很可能通过类似协议实现 |
| **Local-First 架构** | Accio Work 采用本地优先运行，文件操作、终端命令、浏览器操作在用户本地设备执行 |
| **Human-in-the-Loop** | 关键决策节点（RFQ 确认、资金操作、文件访问）设置人工审批门控 |
| **沙箱执行环境** | 细粒度权限管理，确保 Agent 执行安全可控 |

---

## 五、竞争格局

| 竞品 | 定位 | 相比 Accio 的劣势 |
|------|------|-----------------|
| **Amazon Rufus** | C 端 AI 购物助手 | 仅限 C 端，无 B2B 采购能力；准确率仅 32%；83% 推荐自有商品 |
| **Perplexity Shopping** | AI 搜索 + 购物推荐 | 无端到端交易闭环，无供应商谈判能力 |
| **Shopify AI (Sidekick)** | 卖家运营 AI 助手 | 仅限 Shopify 平台内，无跨平台供应链能力 |
| **Manus 等通用 Agent** | 泛用 Agentic AI | 无跨境贸易领域数据，无供应商网络 |
| **Global Sources 等传统 B2B** | 信息撮合 | 无 AI 能力，人工流程重 |

**Accio 核心壁垒**：阿里 26 年积累的 10 亿+ 商品数据和 5000 万+ 企业数据 + 唯一覆盖"AI 搜索 → Agent 执行 → 全链路运营"的 B2B 贸易 AI 平台。

---

## 六、战略定位

- Accio 是阿里国际 **AI 转型的旗舰产品**，代表从传统 B2B 信息撮合向 AI-native 贸易平台的跃迁
- 2026 届校招 **80% 为 AI 岗位**，全面押注 AI
- 承载将 AliExpress、Lazada、Daraz 等国际电商平台统一 AI 化升级的使命
- 瞄准**欧美中小企业市场**，从信息撮合走向交易闭环 + 运营自动化

---

## 七、近期动态

| 时间 | 事件 |
|------|------|
| 2024.11 | Accio 首次发布，定位 B2B AI 搜索引擎 |
| 2025.02 | 接入 DeepSeek 推理模型，新增深度研究功能 |
| 2025.04 | 启动大规模 AI 人才招聘，推出"Bravo 102"人才计划 |
| 2025.08 | 发布 Accio Agent，9 个月内达到 200 万用户 |
| 2026.03 | 发布 Accio Work 企业级 AI Agent 平台，月活突破 1000 万 |
| 2026.03 | Accio.com 独立域名上线 |
| 进行中 | 底层模型从 DeepSeek R1 切换至 Qwen3 |

---

## 八、我的经验与 Accio 的关联点

| Accio 技术需求 | 我的对口经验 |
|--------------|------------|
| Multi-Agent 编排 | Pageon Agent 架构设计：生成 + 编辑双 Pipeline，主 Agent + 子 Agent 架构 |
| Tool Calling / Function Calling | 自研 Tool Calling 机制 + ReAct Loop 闭环，7 种 S&R 策略 |
| MCP 协议集成 | 开发 stdio MCP Server + HTTP MCP 接入云端数据源（GitHub、Notion） |
| Skills 系统 | MG 视频项目：10 类动画场景沉淀为领域知识文档，运行时注入 Prompt 驱动 Agent |
| Agent 框架迁移与选型 | 完整经历自研 → Claude Code Agent SDK 迁移，理解框架取舍 |
| 多模型路由 | 实际使用过 OpenAI / Claude 多模型，有模型选型评估经验 |
| 从 0 到 1 产品落地 | 独立发起数据架构重构并推动生产落地，转化率提升 150%+ |

### 面试话术参考

当被问到"你对 Accio 的理解"：

> "Accio 从 AI Search 演进到 Agent 再到 Accio Work 的 Multi-Agent 平台，本质上是在做一件事：**把跨境贸易的专家知识编码为 Agent 能力**。我在 Pageon 做的事情逻辑上很相似——把设计领域的专家知识编码为 Agent 的 Skills 系统。技术上，我做过完整的 Agent 底座自研到 SDK 迁移，落地了 MCP 协议的 Tool 层解耦，这些和 Accio Work 的多 Agent 协作架构需求是直接对口的。"

---

## 九、核心功能优化思路（招商/导购/搜索推荐）

### 招商（供应商侧）

核心问题：怎么让优质供应商更高效地入驻和被匹配到？

- **智能供应商画像构建**：Agent 自动从非结构化数据（验厂报告、邮件往来、第三方评级）中提取和结构化供应商信息（产能、认证、历史交易、响应速度），而不是让供应商手动填表
- **供应商冷启动**：新入驻供应商没有交易数据，Agent 通过主动"面试"——向供应商发结构化问题，快速补全能力标签，解决冷启动排序问题
- **动态准入与分级**：不是一次审核定终身，Agent 持续监控交期履约率、退款率、响应时效，动态调整等级和曝光权重

### 导购（买家侧）

核心问题：B2B 买家需求模糊且专业，怎么引导到精准匹配？

- **多轮意图澄清**：B2B 买家可能说"我要做一个户外家具品牌"，Agent 需要像资深采购顾问一样追问：材质？目标市场？预算？认证要求？MOQ？——**把模糊意图拆解为可检索的结构化采购规格**
- **需求-能力匹配而非关键词匹配**：匹配的不是商品 SKU，而是供应商的供给能力。"你要解决什么问题，我帮你找谁能解决"
- **采购方案推荐**：不只推荐单品，而是推荐"采购方案"——包含供应商组合、价格区间预估、交期规划、替代方案。这是 Agent 相比传统推荐系统的核心差异点

### 搜索推荐

核心问题：B2B 搜索 query 复杂、意图多维，传统倒排索引远远不够。

- **混合检索架构**：语义搜索（理解"环保可降解餐具"的含义）+ 结构化过滤（FDA 认证、MOQ<500、交期<30天）+ 供应商能力图谱（产地、出口经验）三层叠加
- **搜索结果是报告而非列表**：B2B 搜索结果应该是结构化的市场调研——Top 供应商对比、价格区间分析、产地分布、认证覆盖。这正是 Accio Search 的"AI 重构商品百科页面"
- **深度个性化**：不是基于浏览行为"猜你喜欢"，而是基于买家业务画像（品类、目标市场、采购偏好、预算量级），Agent 长期记忆实现深度个性化

### 三者联动的 Agent 闭环

传统电商中招商、导购、推荐三块是割裂的。Agent 架构能打通为一个闭环：

```
买家意图（导购 Agent 澄清）
    → 搜索匹配（检索 Agent 混合召回 + 排序）
        → 供应商推荐（招商侧的能力图谱提供数据）
            → RFQ/谈判（执行 Agent）
                → 交易反馈回流（优化供应商评级 + 买家画像）
```

Agent 有意图理解、多步规划和工具调用能力，可以在一次对话中完成从"理解需求"到"匹配供应商"到"发起询盘"的全链路。

---

## 参考来源

- [Alibaba International Launches Accio Work (PR Newswire)](https://www.prnewswire.com/apac/news-releases/alibaba-international-launches-accio-work-an-enterprise-ai-agent-for-global-businesses-302721781.html)
- [TechNode: Accio Work AI agent builds online stores in 30 minutes](https://technode.com/2026/03/24/alibaba-international-launches-accio-work-ai-agent-says-it-can-build-online-stores-in-30-minutes/)
- [Accio Agent Transforms B2B Sourcing (Scalevise)](https://scalevise.com/resources/accio-agent-alibaba-b2b-ai-sourcing/)
- [阿里国际 Accio Work 深度解析 (AIGC.bar)](https://www.aigc.bar/AI%E8%B5%84%E8%AE%AF%E6%96%87%E7%AB%A0/2026/03/25/alibaba-accio-work-ai-ecommerce-agent-guide)
- [量子位: 阿里国际推出 B2B AI 搜索引擎 Accio](https://www.qbitai.com/2024/11/219815.html)
