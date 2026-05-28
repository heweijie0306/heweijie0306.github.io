# 风格 B：结构化专业风 (Structured Professional)

> 设计关键词：**层级清晰、色条引导、信息分区、大厂既视感**

---

## 设计理念

像一份精心设计的产品 PRD 文档——有清晰的信息层级和视觉引导。通过左侧色条、浅色背景块和微妙的层次变化，让 HR 在 6 秒扫读中精准捕获关键信息。这是最"标准答案"式的大厂简历风格。

---

## 视觉规范

### 配色方案
| 用途 | 色值 | 说明 |
|------|------|------|
| 主文字 | `#111827` | 深墨色 |
| 次文字 | `#6b7280` | 中灰 |
| 辅助文字 | `#9ca3af` | 浅灰，用于最次要信息 |
| 页面背景 | `#f9fafb` | 极浅灰底（打印时为白色） |
| 内容区背景 | `#ffffff` | 白色卡片 |
| 主题色 | `#0f766e` | 深青色 (Teal)，沉稳但有辨识度 |
| 主题色浅底 | `#f0fdfa` | 极浅青，用于 header 背景和标签底色 |
| 边框 | `#e5e7eb` | 浅灰边框 |

### 字体
```css
font-family: 'Noto Sans SC', 'Inter', -apple-system, 'PingFang SC', sans-serif;
```
- **姓名**：26px, `font-weight: 700`
- **Section 标题**：15px, `font-weight: 700`, 颜色 `#0f766e`
- **公司/项目名**：14.5px, `font-weight: 600`
- **正文**：13px, `font-weight: 400`, `line-height: 1.75`
- **标签文字**：11.5px, `font-weight: 500`

### 布局
- **整体**：单栏，A4 尺寸
- **页边距**：上 `16mm`，下 `16mm`，左右 `20mm`
- **Section 间距**：`20px`
- **条目间距**：`14px`

### 核心视觉元素

1. **Header 区（顶部）**
   - 整个 header 区域使用 `#f0fdfa`（极浅青）背景色块
   - 左侧：姓名 + 求职意向（意向用 `font-size: 14px` + 主题色）
   - 右侧：联系信息纵向排列（每行一个，带小 inline icon：📞 📧 🔗 📍）
   - 使用 flexbox 左右分栏
   - header 底部用 `3px solid #0f766e` 粗线收尾

2. **个人总结区**
   - 独立一个浅灰底（`#f9fafb`）圆角区块（`border-radius: 6px`）
   - `padding: 14px 18px`
   - 文字 `font-size: 13px`，`color: #374151`
   - 左侧一条 `3px solid #0f766e` 竖线（`border-left`）

3. **Section 标题**
   - 格式：中文 + 英文（如「工作经历 Work Experience」）
   - 左侧带 `3px` 宽、`18px` 高的主题色竖条（用 `border-left` 或 `::before` 伪元素）
   - 标题文字 `padding-left: 10px`
   - 标题下方 `8px` 处一条 `1px dashed #e5e7eb` 虚线

4. **公司/项目行**
   - 上层：**公司名（加粗 + 主题色）** | 职位（正常色）
   - 下层或右对齐：时间区间（浅灰色，`font-size: 12px`）
   - 公司行下方紧跟一行淡灰斜体的业务一句话描述

5. **正文 bullet points**
   - 使用自定义方形 bullet：`▸`（主题色）
   - 或用 `4px × 4px` 的主题色小方块（`::before` 伪元素，`border-radius: 1px`）
   - `padding-left: 14px`

6. **技能标签**
   - 使用 inline-block 标签样式
   - 背景 `#f0fdfa`，边框 `1px solid #99f6e4`，圆角 `4px`
   - 文字颜色 `#0f766e`，`padding: 2px 8px`
   - 标签间距 `6px`
   - 这是整份简历唯一允许"稍有设计感"的地方

7. **项目经历高亮**
   - 「项目背景」那一行用 `background: #f9fafb` + `padding: 8px 12px` + `border-radius: 4px` 做一个浅底色条
   - 与正文 bullet 形成视觉层次区分

8. **加粗文字**
   - `font-weight: 600`
   - 技术栈/框架名称额外加 `color: #0f766e`（主题色），形成视觉锚点

### 装饰元素
- ✅ Header 区浅色背景块
- ✅ Section 标题左侧色条
- ✅ 个人总结区的 border-left 引用样式
- ✅ 技能标签的 pill/badge 样式
- ❌ 无阴影（`box-shadow: none`）
- ❌ 无图片/头像
- ❌ 无渐变色

### 打印适配
```css
@media print {
  body { background: white; }
  .header { background: #f0fdfa !important; -webkit-print-color-adjust: exact; }
  .skill-tag { border: 1px solid #ccc; background: #f5f5f5; color: #333; }
}
```

---

## 整体气质描述

> 如果这份简历是一个人，他穿的是：**修身深蓝西装 + 白衬衫（不打领带）+ 一块低调的手表**。
> 不张扬但你一眼就看出这人是"有体系的"、"靠谱的"、"在大厂干过的"。信息呈现有章法，阅读毫不费力。

---

## 参考对标

- Notion 的文档排版层级感
- 飞书文档的结构化阅读体验
- 字节跳动内部简历模板的信息密度与清晰度
