# Simplex AI / Lev8 背景调查报告

> 调查日期：2026-04-17
> 目标主体：Simplex AI（新加坡实体）+ 研发中心：中国杭州
> 旗舰产品：**Lev8**（AI-first GTM / People Intelligence 平台）
> 信息来源：AWS 官方案例、公司博客、GlobeNewswire、CB Insights、TipRanks、LinkedIn、X (Twitter)

---

## 一、公司速览（Fact Sheet）

| 维度 | 内容 |
|---|---|
| **公司名** | Simplex AI |
| **产品名** | Lev8（lev8.com） |
| **成立时间** | 2025 年 |
| **注册主体/总部** | 新加坡（**112 Robinson Road, Suite 03-01, Robinson 112, Singapore 068902**） |
| **研发中心** | 中国 · 杭州（核心研发/工程团队驻地） |
| **公司定位** | AI-native 实时人才/客户情报公司（Real-Time People Intelligence / AI GTM） |
| **核心理念** | "Simplify the complex with AI"（用 AI 简化复杂） |
| **融资阶段** | 种子轮（Seed） |
| **最新融资** | **$6M USD**，领投方 **GL Ventures（高瓴创投）**，2026 年 1 月公告 |
| **产品正式上线** | 2026-01-15（Lev8 Launch Day） |
| **目标市场** | 全球（海外为主，ToB SaaS） |

---

## 二、组织结构与“新加坡主体 + 杭州研发”模式解读

Simplex AI 采用当下一线中国 AI 初创典型的 **“出海双层架构”**：

- **新加坡公司（主体）**：承接海外融资（GL Ventures 美元基金）、对外签约、数据合规（GDPR / CCPA）、客户付费通道。
- **杭州研发中心**：承担核心算法、模型训练、工程落地。依托杭州 AI 人才红利（DeepSeek、阿里达摩院、蚂蚁、网易、vivo GenAI 等生态外溢）。

这种结构的优势在于：海外客户和美元资本可规避中国数据跨境合规复杂度；同时保留中国工程师密度高、模型研发成本低的优势。是 2024–2026 年 AI SaaS 出海公司（如 Manus、Monica、HeyGen 早期等）的主流路径。

---

## 三、核心团队（关键人物）

| 角色 | 姓名 | 关键背景 |
|---|---|---|
| **CEO** | **Tony Zhang（张某）** | **DeepSeek V1 与 VL（Vision-Language）模型核心贡献者**。是公司最重要的“技术旗帜”，直接解释了为何 GL Ventures 愿意在种子轮重仓。 |
| **CTO** | **Pan（潘某）** | **InternLM / InternLM-XComposer（书生·浦语）核心开发者**之一。上海 AI Lab 多模态模型背景。 |
| **核心团队成员** | — | 来自 **DeepSeek、Microsoft Research、上海 AI Lab** 等顶级 AI 研究机构。 |

> **解读**：团队画像为 **“研究型 AI Lab 出来的工程创业团队”**，技术壁垒偏 LLM + 多模态搜索 + Agent，与产品形态（神经语义搜索 + 实时信号引擎）高度匹配。这是 GL Ventures 敢于 Lead 种子轮 $6M（高于普通种子轮均值 ~$2–3M）的核心原因。

---

## 四、产品 Lev8 详解

### 4.1 产品定位
Lev8 是一款 **AI-first B2B GTM 情报平台**，对标（但路径不同于）ZoomInfo、Clay、Apollo 等传统 GTM 工具。它把 **整个开放互联网转化为一个实时、可行动的情报引擎**，帮助团队在"买方意图出现的瞬间"识别并触达决策人。

一句话概括：**“从静态联系人数据库，升级为实时意图雷达（AI Radar for Companies Ready to Buy）”**。

### 4.2 目标客户（ICP）
- **销售团队（Sales）** —— 高价值潜在客户发现与触达
- **招聘团队（Recruiting）** —— 被动候选人识别、人才流动信号
- **创业者（Founders）** —— 市场情报、战略合作伙伴发现
- **投资人（Investors）** —— 早期标的发现、deal sourcing
- **市场团队（Marketing）** —— 精准分层、ABM

### 4.3 核心功能模块
1. **Intent-Driven Neural Search**（意图驱动神经搜索引擎）—— 自然语言查询，覆盖数百万公司与个人 Profile。
2. **Real-Time Signal Intelligence**（实时信号情报）—— 监听融资、招聘动向、Tech Stack 变化、高管变动、产品发布等高意图事件。
3. **Contact Enrichment**（联系人富化）—— 自动补全邮箱、电话、社交账号等 verified contact 信息。
4. **Two-Sided Platform Flywheel** —— 搜索与执行闭环：发现 → 富化 → 触发外联。
5. **Company Discovery** —— 组织结构、扩张路径映射。

### 4.4 产品宣称性能指标（官方 PR 口径，需留存验证）
- **10×** 更快的潜客发现速度
- **90%** 匹配准确率（对比人工研究）
- **70%** 研究成本降低
- **95%** 联系人验证准确率

### 4.5 定价
| 版本 | 目标用户 |
|---|---|
| **Free** | 单用户试用 / POC |
| **Starter** | 小型外联团队 |
| **Pro** | 中大型销售/招聘/投资团队（多 workflow 并行） |

### 4.6 合规
GDPR、CCPA 合规，数据加密与访问控制。

---

## 五、技术栈（源自 AWS 官方案例）

Simplex AI 是 AWS 官方公开案例的客户，技术栈透明度较高：

- **基础设施**：AWS（海外），Kubernetes 编排
- **核心服务**：
  - **Amazon Bedrock**（基础大模型推理）
  - **Amazon OpenSearch Service**（向量/语义检索）
  - **Amazon EC2**（计算）
  - **Amazon EFS**（文件存储）
- **关键技术挑战**：数据库搜索的 **高并发 + 低响应延迟**；需要同时处理 **1,000–2,000 个并发大模型 workload**。
- **运维效率**：通过 CLI 自动化大幅降低 O&M 成本。

> **解读**：技术栈典型的"海外 AI SaaS"配置，**未见中国云厂商组件**，印证海外主体与海外客户服务定位。核心技术竞争力在于 **大规模并发语义搜索 + Agent 编排** 能力。

---

## 六、融资与资本背书

| 时间 | 轮次 | 金额 | 领投 | 来源 |
|---|---|---|---|---|
| 2026-01 | **Seed** | **$6M USD** | **GL Ventures（高瓴创投）** | GlobeNewswire / Yahoo Finance / LinkedIn 多渠道披露 |

### 投资人解读
- **GL Ventures**：高瓴资本旗下早期基金，过往在 AI 基础设施、Agent、SaaS 领域重注（如曾布局月之暗面、硅基流动等）。
- **信号意义**：顶级美元基金 **领投** 种子轮 $6M，高于 AI 应用层种子轮均值（通常 $1.5–3M），表明 **团队背景与技术叙事** 受一线机构认可。

---

## 七、市场竞争格局

据第三方观察（X 平台 @aakashgupta 等 GTM 分析师），GTM Intelligence 赛道正**二元分化**：

| 阵营 | 代表公司 | 特征 |
|---|---|---|
| **静态数据库巨头** | ZoomInfo（4.2 亿+ 联系人，$15K+/年合同，17 年数据积累） | 规模大、数据全、但更新慢、价格高 |
| **AI-first 动态情报** | **Lev8**、Clay、Common Room | 实时信号、AI 原生、Agentic、价格亲民 |

Lev8 的差异化定位：**不与 ZoomInfo 拼数据库体量，拼"意图信号的时效性 + AI 语义检索的精准度"**。

---

## 八、风险与关注点（面试/合作前需澄清）

1. ⚠️ **团队公开信息有限**：除 CEO Tony Zhang、CTO Pan 外，其他 C-level 与核心工程师未在公开渠道披露具体履历，需在面谈中进一步核实。
2. ⚠️ **杭州实体性质**：公开渠道未见杭州公司工商主体披露，需确认杭州团队是以 **WFOE（外商独资）** 还是 **ODI 返投** 还是 **劳务外包** 形式运作，涉及员工劳动合同主体、股权期权（是新加坡 ESOP 还是境内激励）。
3. ⚠️ **中美/中新数据合规**：虽宣称 GDPR/CCPA 合规，但作为"从中国团队服务欧美客户"的 SaaS，未来若进入 **企业级/金融/医疗** 客户，跨境数据传输（CAC 安全评估）是潜在瓶颈。
4. ⚠️ **产品上线时间短**：Lev8 正式上线仅在 2026-01-15，**PMF（产品市场契合）尚未被充分验证**。官方宣称的 10× / 90% / 70% 等性能指标属 PR 数据，需客户 case study 背书。
5. ⚠️ **赛道拥挤**：Clay、Apollo、Common Room、Koala、UserGems、Warmly 等在 GTM Intelligence 已占位；差异化能否持续需要观察。
6. ✅ **正向信号**：技术团队强（DeepSeek 系 + 上海 AI Lab 系 + MSR 系）、资方背书强（高瓴 Lead）、切入点清晰（real-time intent + agentic search）、海外定位减少中国商业化难度。

---

## 九、面试/求职者视角的建议（如用于面试准备）

### 可深挖的业务/技术话题
- **Intent-Driven Neural Search 的技术架构**：向量检索 + LLM 重排 + Agent 规划的三层设计。
- **Signal 实时化**：如何构建百万级公司/个人实体的 **准实时 ETL 管道**？OpenSearch + 自研 crawler 的 trade-off？
- **并发 1K–2K 大模型 workload**：如何做模型缓存 / batching / KV 复用 / 降本？
- **Lev8 vs ZoomInfo vs Clay**：产品取舍与护城河。

### 可聊的业务关切
- **ICP 与首批 Design Partner**：签了哪些标杆客户？销售团队 / 猎头机构 / VC / ？
- **Pricing 竞争力**：相比 ZoomInfo 年费万刀级，Lev8 Pro 定价区间？
- **中国团队的角色**：研发为主还是覆盖商业化？是否有国内落地计划？
- **期权与 offer 结构**：新加坡主体发期权 vs 国内主体，税与归属机制差异。

### 加分项
- 熟悉 **DeepSeek / InternLM 系列模型** 的工程细节（创始团队背景）。
- 熟悉 **LangChain / LlamaIndex / Agent 编排框架** + **RAG 生产化踩坑经验**。
- 有 **海外 ToB SaaS 工程化**（多租户、Billing、SOC2、GDPR）或 **大规模 Web Crawler + 实体消歧** 经验者优先。

---

## 十、结论

**Simplex AI / Lev8 是一家"新加坡主体 + 杭州研发"架构的、出海型 AI GTM 初创公司**，具备以下关键特征：

- 🟢 **技术团队强（DeepSeek + InternLM 核心贡献者）** —— 稀缺
- 🟢 **资方背书（GL Ventures Lead $6M Seed）** —— 一线机构认可
- 🟢 **赛道清晰（AI-native GTM Intelligence）** —— 2026 年热点赛道
- 🟡 **产品早期（上线 3 个月）** —— PMF 待验证
- 🟡 **公开信息有限** —— 建议面谈时就杭州实体、股权结构、客户列表进一步澄清

整体评估：**团队质量与资本质量均属种子轮一线水平，产品市场验证期，适合风险偏好较高、看重"团队 + 赛道"的候选人或合作方。**

---

## 参考来源（Sources）

- [Simplex AI Secures $6M in Funding to Redefine Real-Time People Intelligence with Lev8 — GlobeNewswire / StreetInsider](https://www.streetinsider.com/Globe+Newswire/Simplex+AI+Secures+$6M+in+Funding+to+Redefine+Real-Time+People+Intelligence+with+Lev8/25876904.html)
- [GL Ventures Officially Leads Simplex AI's Seed Round Investment — Lev8 Blog](https://lev8.com/blog/gl-ventures-investment)
- [AWS Supercharges Simplex AI to Overcome Concurrency, O&M, and Scaling Challenges — AWS 官方案例](https://aws.amazon.com/solutions/case-studies/simplex-ai/)
- [Lev8 — Products, Competitors, Financials, Employees, HQ — CB Insights](https://www.cbinsights.com/company/lev8)
- [Lev8 官网 — Your AI Radar for Companies Ready to Buy](https://lev8.com)
- [Simplex AI Raises $6 Million to Launch Lev8 — TipRanks](https://www.tipranks.com/news/private-companies/simplex-ai-raises-6-million-to-launch-real-time-people-intelligence-platform-lev8)
- [Simplex AI Secures $6M in Funding — Yahoo Finance SG](https://sg.finance.yahoo.com/news/simplex-ai-secures-6m-funding-025500596.html)
- [Aakash Gupta on X — Lev8 launch analysis & competitive landscape](https://x.com/aakashgupta/status/2022926843641278708)
- [Lev8 Asset Profile — Preqin](https://www.preqin.com/data/profile/asset/lev8/786613)
