# 风格 C：现代 Editorial 风 (Modern Editorial)

> 设计关键词：**杂志排版、大标题、呼吸感、高级质感、个人品牌**

---

## 设计理念

像一份科技杂志的人物专栏——既有专业深度，又有设计审美。这是三个方案中视觉表现力最强的，适合投递注重"产品感"和"审美力"的团队（如 AI 产品公司、设计工具公司、创业公司 CTO 直筛场景）。在保持 ATS 兼容的前提下，最大化展示个人品牌调性。

---

## 视觉规范

### 配色方案
| 用途 | 色值 | 说明 |
|------|------|------|
| 主文字 | `#18181b` | 近黑（Zinc-900） |
| 次文字 | `#71717a` | 中灰（Zinc-500） |
| 背景 | `#ffffff` | 纯白 |
| 主题色 | `#7c3aed` | 紫色 (Violet-600)，有科技感又有个性 |
| 主题色浅 | `#ede9fe` | 极浅紫，背景用 |
| 主题色深 | `#4c1d95` | 深紫，hover 态或极少量使用 |
| 暖灰 | `#fafaf9` | 极浅暖灰底色（Stone-50） |
| 分割线 | `#e4e4e7` | 锌灰 |

### 字体
```css
/* 标题用衬线体，正文用无衬线体，形成对比 */
--font-heading: 'Playfair Display', 'Noto Serif SC', Georgia, serif;
--font-body: 'Inter', 'Noto Sans SC', -apple-system, sans-serif;
```
- **姓名**：32px, `font-family: var(--font-heading)`, `font-weight: 700`, `letter-spacing: 1px`
- **求职意向**：14px, 无衬线体, `font-weight: 500`, `color: #7c3aed`
- **Section 标题**：12px, 无衬线体, `font-weight: 700`, `text-transform: uppercase`, `letter-spacing: 3px`, 颜色 `#7c3aed`
- **公司/项目名**：15px, 衬线体, `font-weight: 600`
- **正文**：13px, 无衬线体, `line-height: 1.8`

### 布局
- **整体**：单栏主体，A4 尺寸
- **页边距**：上 `24mm`，下 `20mm`，左 `30mm`，右 `25mm`（左边距略宽，营造杂志留白感）
- **Section 间距**：`28px`
- **条目间距**：`16px`

### 核心视觉元素

1. **Header 区（顶部）—— 杂志封面感**
   - 姓名使用衬线体，32px，居左
   - 姓名下紧跟一条 `40px` 宽的 `3px solid #7c3aed` 短横线（装饰性，非全宽）
   - 短横线下方：求职意向，主题色
   - 再下方：联系信息一行排列，`font-size: 12px`，灰色，用 `|` 分隔
   - Header 区整体下方 `32px` 留白后进入正文

2. **个人总结区 —— Pull Quote 风格**
   - 左侧一条 `3px solid #7c3aed` 竖线
   - 文字 `font-size: 14px`，`font-style: italic`，`color: #3f3f46`
   - `padding-left: 20px`
   - 像杂志里的 pull quote（提拉引用），形成视觉焦点

3. **Section 标题 —— 大写字母 + 装饰线**
   - 全大写英文（如 `EXPERIENCE`），`letter-spacing: 3px`，主题色
   - 中文跟在后面，`font-size: 11px`，灰色（如 `工作经历`）
   - 标题右侧延伸一条细线到页面边缘：用 `flex` + `::after` 伪元素画一条 `1px solid #e4e4e7` 的线
   - 形成 "标题——线" 的经典 editorial 排版

4. **时间轴式项目排列**
   - 日期放在左侧固定宽度区域（`width: 90px`），`font-size: 12px`，灰色，`text-align: right`
   - 内容放在右侧，左侧有一条 `1px solid #e4e4e7` 的竖线连接各条目
   - 竖线上，每个条目起始位置有一个 `8px × 8px` 的主题色圆点（`border-radius: 50%`）
   - 形成轻量时间轴视觉，但不过分

5. **正文 bullet points**
   - 使用 `—`（em dash）作为 bullet 符号，颜色 `#7c3aed`
   - 或使用细长的 `2px × 12px` 竖线条（主题色）作为自定义 bullet
   - `padding-left: 16px`

6. **技能标签 —— 下划线风格**
   - **不使用** pill/badge 样式
   - 技术栈名称用 `font-weight: 600` + `border-bottom: 2px solid #ede9fe`（浅紫下划线）
   - 悬停时下划线变为实色 `#7c3aed`（仅限屏幕阅读时）
   - 技能分类用小标题区分，每类一行

7. **项目背景**
   - 用 `font-size: 12.5px`，`color: #71717a`，不加背景色
   - 与正文 bullet 靠字号和颜色做区分
   - 保持"呼吸感"

8. **加粗文字**
   - `font-weight: 600`
   - 重要的技术栈/框架名用主题色文字 `#7c3aed`
   - 关键数据（如 "5%+"、"150%"）用 `font-weight: 700` + `#18181b` 纯黑加粗

### 装饰元素
- ✅ 姓名下方的短装饰线
- ✅ Section 标题旁的延伸细线
- ✅ 时间轴圆点 + 竖线（轻量）
- ✅ Pull Quote 式个人总结
- ✅ 衬线 + 无衬线体的混排对比
- ❌ 无色块填充
- ❌ 无阴影
- ❌ 无图片/头像
- ❌ 无渐变

### 打印适配
```css
@media print {
  body { background: white; margin: 0; }
  .timeline-dot { background: #7c3aed !important; -webkit-print-color-adjust: exact; }
  .section-line::after { border-color: #d4d4d8; }
  a { color: #18181b; text-decoration: none; }
}
```

---

## 整体气质描述

> 如果这份简历是一个人，他穿的是：**黑色修身高领 + 深紫色围巾 + 白色极简帆布袋里装着一本《Monocle》杂志**。
> 他不只是一个工程师，他是一个有审美、有品位、对"产品美感"有执念的工程师。适合投给那些创始人自己也很在意设计的公司。

---

## 参考对标

- Monocle 杂志的排版与留白
- Stripe 官网的 editorial 风格
- Vercel 的品牌设计语言（紫黑白配色）

---

## ⚠️ 适用场景提示

此风格视觉表现力最强，**最适合**：
- 创业公司直接投给 CEO/CTO
- 注重设计和产品审美的 AI 公司
- 作为个人作品集 / Portfolio 页面的简历

**需谨慎使用于**：
- 传统大厂 HR 初筛（可能觉得"太花了"）
- 纯后端/算法岗投递
