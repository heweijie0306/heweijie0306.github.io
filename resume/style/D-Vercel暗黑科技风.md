# 风格 D：Vercel 暗黑科技风 (Vercel Dark Tech)

> 设计关键词：**暗色系、高对比、渐变微光、开发者美学、未来感**

---

## 设计理念

直接对标 Vercel / Next.js 官网的设计语言——深黑背景上，白色文字搭配彩色渐变点缀，形成极强的科技感与高级感。这不是传统简历，这是一份「开发者品牌宣言」。适合给技术导向的团队留下"这个人就是我们的人"的深刻印象。

**核心哲学**：Vercel 的设计精髓不是"暗色主题"，而是「在极度克制的深色画布上，用极少量的光来制造焦点」。

---

## 视觉规范

### 配色方案
| 用途 | 色值 | 说明 |
|------|------|------|
| 页面背景 | `#000000` | 纯黑（Vercel 标志性） |
| 内容区背景 | `#0a0a0a` | 极深灰，和纯黑形成微妙层次 |
| 主文字 | `#ededed` | 亮灰白（非纯白，减少刺眼感） |
| 次文字 | `#888888` | 中灰 |
| 弱文字 | `#666666` | 暗灰，日期和最次要信息 |
| 边框/分割线 | `#333333` | 深灰边框，微妙但在场 |
| 悬浮边框 | `#555555` | 略亮灰，hover 态 |
| 强调白 | `#ffffff` | 纯白，仅用于姓名和最关键数据 |
| 渐变色（核心亮点）| `linear-gradient(90deg, #007cf0, #00dfd8, #7928ca, #ff0080)` | Vercel 标志性四色渐变，极少量使用 |
| 渐变备选（冷色）| `linear-gradient(90deg, #007cf0, #00dfd8)` | 蓝-青渐变，更克制的选择 |

### 字体
```css
font-family: 'Geist', 'Inter', -apple-system, 'PingFang SC', 'Noto Sans SC', sans-serif;
```
> Geist 是 Vercel 官方字体。如未加载则 fallback 到 Inter。

- **姓名**：36px, `font-weight: 700`, `color: #ffffff`, `letter-spacing: -0.5px`（Vercel 标志性的负字距）
- **求职意向**：14px, `font-weight: 400`, 使用渐变色文字（`background-clip: text`）
- **Section 标题**：11px, `font-weight: 600`, `text-transform: uppercase`, `letter-spacing: 4px`, `color: #888888`
- **公司/项目名**：15px, `font-weight: 600`, `color: #ededed`
- **正文**：13px, `font-weight: 400`, `line-height: 1.75`, `color: #888888`（正文故意灰，让加粗内容跳出来）
- **日期**：12px, `font-weight: 400`, `color: #666666`, `font-variant-numeric: tabular-nums`

### 布局
- **整体**：单栏，A4 尺寸，`background: #000000`
- **内容区**：居中，`max-width: 680px`，左右自动留白
- **页边距**：上 `28mm`，下 `20mm`，左右由 max-width 自动控制
- **Section 间距**：`32px`
- **条目间距**：`20px`

### 核心视觉元素

1. **Header 区 —— 极简开场**
   - 姓名：36px 纯白大字，`letter-spacing: -0.5px`（紧凑感）
   - 求职意向紧跟其下，使用渐变文字：
   ```css
   .title {
     background: linear-gradient(90deg, #007cf0, #00dfd8, #7928ca, #ff0080);
     -webkit-background-clip: text;
     -webkit-text-fill-color: transparent;
     font-weight: 500;
   }
   ```
   - 联系信息一行排列，用 `·` 分隔，`color: #666666`，`font-size: 12px`
   - Header 下方 `40px` 的纯净留白（不加任何分割线，靠空间分割）

2. **Section 标题 —— 全大写灰色**
   - 全大写英文 + 中文小字（如 `EXPERIENCE 工作经历`）
   - 英文 `letter-spacing: 4px`，`color: #888888`
   - 中文跟随，`font-size: 10px`，`color: #666666`，`margin-left: 8px`
   - 标题下方一条 `1px solid #333333` 的细线，`margin-top: 8px`
   - **不使用色条**，靠大写字母和字间距本身制造存在感

3. **卡片式项目区块**
   - 每个项目/工作经历用一个微妙的卡片包裹：
   ```css
   .card {
     background: #0a0a0a;
     border: 1px solid #333333;
     border-radius: 8px;
     padding: 20px 24px;
     transition: border-color 0.2s;
   }
   ```
   - 卡片之间 `12px` 间距
   - 屏幕阅读时 hover 效果：`border-color: #555555`（打印时无效果）
   - 这是 Vercel Dashboard 的核心视觉语言

4. **公司/项目行**
   - 公司名 `#ededed` 加粗 | 职位 `#888888` 正常
   - 时间右对齐 `#666666`
   - 项目背景用 `font-size: 12.5px`，`color: #666666`，与正文 bullet 拉开层级

5. **正文 bullet points**
   - 使用 `▹` 作为 bullet 符号（Vercel 风格的小三角）
   - bullet 颜色 `#888888`
   - 正文默认 `color: #888888`
   - **加粗内容自动提亮为 `#ededed`**，形成"暗中有光"的扫读体验

6. **技能标签 —— 边框胶囊**
   - Vercel 标志性的深底 + 亮边框胶囊：
   ```css
   .tag {
     display: inline-block;
     background: transparent;
     border: 1px solid #333333;
     border-radius: 9999px;  /* 全圆角胶囊 */
     padding: 3px 12px;
     font-size: 11px;
     color: #ededed;
     margin: 3px 4px;
   }
   ```
   - 核心技能（如 Claude、Agent SDK）的标签边框用渐变色：
   ```css
   .tag-highlight {
     border-image: linear-gradient(90deg, #007cf0, #00dfd8) 1;
     /* 或用 background + mask 方案实现圆角渐变边框 */
   }
   ```

7. **关键数据高亮 —— 渐变文字**
   - 核心业绩数据（如 "5%+"、"150%"、"35%"）使用渐变色文字
   - 这是整份简历最抓眼球的视觉锚点，但因为数量极少（3-5 处），不会过度

8. **链接样式**
   - `color: #007cf0`（Vercel 蓝），无下划线
   - hover 时 `text-decoration: underline`

### 装饰元素
- ✅ 求职意向的渐变文字（标志性元素）
- ✅ 卡片式项目区块（`border: 1px solid #333`）
- ✅ 胶囊标签（全圆角 + 深底亮框）
- ✅ 关键数据的渐变色强调（极少量）
- ✅ 全大写 section 标题的字间距
- ❌ 无实色填充色块
- ❌ 无阴影（`box-shadow: none`）
- ❌ 无图片/头像
- ❌ 无动画（打印介质）
- ❌ 无圆点/色条等传统简历元素

### 打印适配（关键！）
暗色简历打印时**必须反转为亮色**，否则浪费墨水且不可读：
```css
@media print {
  body, .page {
    background: #ffffff !important;
    color: #111111 !important;
  }
  .card {
    background: #ffffff !important;
    border: 1px solid #e5e5e5 !important;
  }
  .title {
    /* 渐变文字打印时退化为深色 */
    background: none !important;
    -webkit-text-fill-color: #111111 !important;
  }
  .tag {
    border-color: #d4d4d4 !important;
    color: #111111 !important;
  }
  .section-title {
    color: #666666 !important;
  }
  .text-secondary {
    color: #666666 !important;
  }
  /* 渐变数据在打印时变为加粗黑色 */
  .data-highlight {
    background: none !important;
    -webkit-text-fill-color: #111111 !important;
    font-weight: 700 !important;
  }
}
```

### 屏幕 vs 打印 双模式说明
| 元素 | 屏幕模式 | 打印模式 |
|------|---------|---------|
| 背景 | `#000000` 纯黑 | `#ffffff` 纯白 |
| 主文字 | `#ededed` 亮灰白 | `#111111` 近黑 |
| 卡片 | 深灰底 + 亮框 | 白底 + 浅灰框 |
| 渐变文字 | 四色渐变 | 退化为纯黑加粗 |
| 标签 | 透明底 + 灰框 | 白底 + 浅灰框 |

---

## 整体气质描述

> 如果这份简历是一个人，他穿的是：**全黑 Arc'teryx 机能外套 + 黑色 AirPods Max + MacBook Pro 上贴着 Vercel 三角贴纸**。
> 他不需要解释自己是做什么的——一看就是前沿技术圈的人。他用的工具、写的代码、甚至简历本身，都在无声地说"我理解现代工程美学"。

---

## 参考对标

- [vercel.com](https://vercel.com) —— 深黑 + 渐变微光
- [nextjs.org](https://nextjs.org) —— 全大写标题 + 灰色层级
- Vercel Dashboard —— 卡片式布局 + `#333` 边框
- [linear.app](https://linear.app) —— 暗色 + 极致克制

---

## ⚠️ 适用场景提示

**最适合**：
- 以**电子版/屏幕阅读**为主的投递场景（邮件附件、在线链接）
- 技术导向公司、开发者工具团队、AI 创业公司
- 作为个人网站 / Portfolio 中的在线简历页面
- 直接发给 CTO / Tech Lead 看的场景

**需注意**：
- 打印版会自动切换为亮色模式，视觉效果会「降级」（但仍然好看）
- 部分 ATS 系统可能对深色背景解析不佳，建议**同时准备一份风格 A 或 B 的亮色版**作为正式投递用
- 如果 HR 要求"Word 格式简历"，此风格不适用
