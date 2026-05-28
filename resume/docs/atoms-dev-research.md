# Atoms.dev / DeepWisdom 深度赋智 -- 面试调研文档

> 调研时间：2026-04-02  
> 目标：为面试准备提供全面公司/产品/技术/竞争信息

---

## 一、公司基本信息

| 项目 | 详情 |
|------|------|
| **公司全称** | 厦门深度赋智科技有限公司（DeepWisdom） |
| **产品名** | Atoms（atoms.dev），前身为 MGX / MetaGPTX |
| **成立时间** | 2019年 |
| **创始人/CEO** | 吴承霖（Wu Chenglin） |
| **总部** | 中国厦门 |
| **办公地点** | 厦门（总部）、深圳、上海；计划开设硅谷办公室（选址在曾容纳Google/PayPal/Logitech的大楼，紧邻斯坦福大学） |
| **团队规模** | ~80人（截至2026年初），计划扩至100-120人 |
| **核心研发团队** | <15人核心成员覆盖前端、后端、算法和测试 |
| **融资情况** | A轮 + A+轮共 **3100万美元（约2.2亿人民币）** |
| **投资方** | 蚂蚁集团（领投A轮）、凯辉基金/Cathay Capital（领投A+轮）、百度风投（BV）、锦秋基金、MindWorks Capital、概念资本 |
| **公司阶段** | 成长期（A+轮），国内 coding agent 赛道融资额最大的公司 |

---

## 二、创始人背景

**吴承霖（Wu Chenglin）**：
- 曾任**腾讯最年轻的T3.3级高级研究员**，主导大规模推荐系统、搜索引擎、知识图谱等服务数十亿用户的项目
- 此前在**华为**从事AI部署相关工作
- 2018年入选**福布斯中国30岁以下精英榜**和**胡润30岁以下创业领袖榜**
- 2019年创办DeepWisdom，最初从事ToB AI服务（2019-2022年），后转型为Agent平台
- 核心理念：**"想法+AI就是一家公司"**，推动"超级个体时代"
- 学术实力：号称审阅约20万篇arXiv论文，精读2100篇，9篇论文投稿NeurIPS其中5篇被录用、3篇口头报告

---

## 三、产品是什么？解决什么问题？

### Atoms = AI原生创业平台

**核心定位**：不是传统的AI编程辅助工具（如Cursor），而是一个**多Agent协作的端到端业务构建平台**。用户用自然语言描述想法，Atoms调度一整支AI团队从调研、设计、开发、部署到运营全流程完成。

**解决的核心痛点**：
- 让**非技术人员**（solo founder/个人创业者）也能从0到1构建完整可商用的产品
- 将传统需要数周/数月的产品开发周期压缩到**数分钟**
- 内置支付、认证、数据库、部署等基础设施，产品生成即可上线运营

### 产品演进路径
1. **MetaGPT**（2023年6月开源）-- 首个开源多Agent协作框架，GitHub 58,800+ stars
2. **OpenManus** -- 开源Agent系统，5名团队成员3小时内复现Manus功能
3. **MGX / MetaGPTX**（2025年2月上线）-- 首月即突破100万美元ARR
4. **Atoms**（2026年1月13日品牌升级上线）-- 当前主力商业产品

---

## 四、核心功能与产品形态

### 7大AI Agent角色（模拟完整产品团队）

| Agent | 角色 | 职责 |
|-------|------|------|
| **Mike** | Team Leader | 端到端执行计划，协调其他Agent |
| **Emma** | Product Manager | 将想法转化为产品规格 |
| **Bob** | Architect | 设计系统架构蓝图 |
| **Alex** | Engineer | 构建生产级全栈应用（前后端、数据库、基础设施） |
| **Iris** | Researcher | 市场调研、趋势分析、想法验证；生成报告/图表/音频/社媒内容 |
| **Sarah** | SEO Specialist | SEO优化、meta标签、sitemap、内容结构 |
| **David** | Data Analyst | 用户行为分析与转化率追踪 |

### 核心能力
- **全栈应用生成**：前端UI + 后端逻辑 + 数据库（Supabase PostgreSQL）+ 用户认证（Email/OAuth）+ 行级安全 + 文件存储
- **一键支付集成**：Stripe支付、订阅、Webhook
- **即时部署**：Atoms Cloud托管，含CDN、SSL、自定义域名
- **Race Mode**：同时运行多个AI迭代方案，构建精度提升3x（Max计划可用）
- **Visual Editor**：可视化编辑器 + "Select to Chat"自然语言微调
- **Deep Research**：商业调研能力据称超过Gemini 2.5 Pro和OpenAI o3

### 定价

| 计划 | 价格 | Credits |
|------|------|---------|
| **Free** | $0 | 25 credits/周期，每日上限15 credits |
| **Pro** | $20/月 | 更多credits，专业功能 |
| **Max** | $100/月 | 顶级性能，Race Mode，完整功能 |

---

## 五、技术架构与AI/Agent技术

### 底层框架
- **MetaGPT**：基于SOP（标准操作流程）的多Agent协作框架，Agent按专业角色分工，通过结构化工作流协作并持续评估
- **OpenManus**：灵活的开源Agent系统，扩展了MetaGPT的能力边界
- 开源组织 **Foundation Agents** 累计GitHub stars超过 **150,000+**

### 技术特点
- **多模型支持**：使用DeepSeek、Qwen等开源模型，而非仅依赖闭源模型，成本仅为竞品的**1/10**
- **多Agent架构**：不同于单Agent系统，Atoms让多个专业Agent协作完成复杂任务
- 自有Benchmark评测得分 **0.8-0.9+**（声称竞品仅0.4+）
- 学术论文发表于 **NeurIPS、ICLR、ACL** 等顶会

### 对面试的启示（关键技术话题）
- Multi-Agent Orchestration（多Agent编排）
- SOP-based Agent Collaboration（基于SOP的Agent协作）
- Agent Role Specialization（Agent角色专业化分工）
- Code Generation + Full-stack Deployment Pipeline
- Cost-effective LLM routing（多模型调度降低成本）

---

## 六、商业模式

1. **SaaS订阅制**：Free / Pro($20/月) / Max($100/月) 三档，基于Credit消耗
2. **目标用户**：Solo Founder、个人创业者、Non-technical Builder、小团队
3. **增长数据**：
   - 首月零推广费实现 **$1M+ ARR**
   - 全球注册用户 **50万+**（上线一个月内）
   - 2025年9月：**月访问120万，日产应用1万+**
   - 连续4周蝉联 **Product Hunt 周榜第一**
4. **愿景**："AI版字节跳动" -- 不只是工具，而是AI驱动的创业基础设施

---

## 七、竞争格局分析

### Atoms的差异化定位

| 维度 | Atoms | Cursor/Windsurf | Lovable/Bolt | Devin |
|------|-------|-----------------|--------------|-------|
| **目标用户** | Non-coder / Solo Founder | 专业开发者 | 快速原型/MVP | 开发团队 |
| **产品形态** | 多Agent协作平台 | AI增强IDE | AI App Builder | AI SWE Agent |
| **核心能力** | 端到端业务构建 | 代码编辑辅助 | 前端/全栈生成 | 自主编程执行 |
| **商业闭环** | 内置支付/部署/SEO/分析 | 无 | 部分 | 无 |
| **技术路线** | 多Agent + 开源模型 | 单Agent + 闭源模型 | 单Agent | 单Agent |
| **成本** | 低（开源模型） | 中 | 中 | 高 |

### 主要竞品
- **国际**：Lovable、Replit、Bolt.new、v0 by Vercel、Devin
- **国内**：Manus（竞争最直接，但Atoms强调开源血统和成本优势）
- **开发者工具类**：Cursor、Windsurf、GitHub Copilot（定位不同，面向开发者而非创业者）

### Atoms核心竞争优势
1. **开源生态护城河**：MetaGPT + OpenManus + Foundation Agents 累计15万+ stars
2. **端到端商业化**：不只生成代码原型，而是可直接运营的完整产品
3. **成本优势**：使用开源模型，成本为闭源竞品的1/10
4. **学术实力**：顶会论文背书，技术深度有保障
5. **增长数据亮眼**：零推广首月$1M ARR，Product Hunt 4连冠

---

## 八、近期动态与新闻

- **2026年1月13日**：MGX品牌升级为Atoms，正式发布
- **2026年1月**：A+轮融资完成，凯辉基金领投，累计融资3100万美元
- **2025年2月**：MGX/MetaGPTX上线，首月$1M ARR
- **2025年**：蚂蚁集团领投A轮融资
- **计划中**：开设硅谷办公室，全球化扩张

---

## 九、招聘信息

### 招聘渠道
- 官方招聘页面：**join.deepwisdom.ai**
- 猎聘：厦门深度赋智科技有限公司
- 偏好从**用户社区**和**Hackathon参与者**中招聘（CEO原话："真实约束下的表现比简历更能说明问题"）

### 推测中的核心岗位方向
- 前端工程师
- 后端工程师
- 全栈工程师
- 算法工程师（Agent/Multi-Agent方向）
- AI Agent研发工程师

### 团队特点
- 核心团队<15人，覆盖前后端+算法+测试
- 重效率、轻层级，强调管理质量而非人数
- CEO认为不应追求"一人公司"式精简，而是在竞争加剧的环境中通过效率取胜

---

## 十、面试准备要点

### 你应该了解的核心知识点
1. **Multi-Agent系统的设计原则** -- MetaGPT的SOP协作模式是核心技术DNA
2. **Vibe Coding** -- 自然语言驱动开发的新范式，Atoms是中国该赛道头部玩家
3. **Agent角色分工与编排** -- 如何让多个专业Agent高效协作而非互相冲突
4. **开源模型成本优化** -- DeepSeek/Qwen等开源模型的工程化应用
5. **端到端部署流水线** -- 从代码生成到Supabase数据库+Stripe支付+CDN部署的自动化

### 可以展示共鸣的话题
- "超级个体时代"愿景 -- AI赋能非技术人员创业
- 开源精神与社区运营（Foundation Agents 15万stars的运营方法论）
- 用实际约束下的表现证明能力（vs 纯简历筛选）
- "硅基生产力终将全面超过碳基劳动力，人的价值在于判断、审美和选择"

### 可能被问到的问题
- 你对Multi-Agent架构vs单Agent架构的看法？各自优劣？
- 如何降低多Agent协作中的成本（token消耗）？
- Agent系统中的错误传播和质量保证如何设计？
- 你如何看待Vibe Coding的发展前景和局限性？
- 对比Manus和Atoms的技术路线差异？

---

## 信息可信度说明

| 信息类别 | 可信度 | 备注 |
|----------|--------|------|
| 公司基本信息 | 高 | 多个权威媒体交叉验证（36kr、KrAsia等） |
| 融资金额和投资方 | 高 | 36kr、Cathay Capital官方确认 |
| 产品功能与定价 | 高 | 官网与多个评测站一致 |
| 增长数据（ARR/用户数） | 中 | 来自CEO采访，未经第三方审计 |
| 技术Benchmark对比 | 低 | 仅自有Benchmark，未见独立第三方验证 |
| 具体招聘岗位 | 低 | 招聘页面内容未能成功抓取，系推测 |
| 硅谷办公室计划 | 中 | 来自CEO采访，属规划阶段 |

---

*Sources: KrAsia, 36kr, Unite.AI, 新浪财经, 腾讯新闻, Cathay Capital, Product Hunt, Barchart/OpenPR*
