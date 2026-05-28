# Anthropic 官网风格简历 Style Guide

## 设计理念
Anthropic 的视觉语言核心：**暖色调中性色系 + 克制的排版 + 大量留白 + 编辑感美学**。不用纯白纯黑，所有灰度都带暖黄底色。

---

## 色板

### 主色调（暖灰体系）
| 用途 | 色值 | 说明 |
|------|------|------|
| 页面背景 | `#faf9f5` | 象牙白，非纯白 |
| 正文文字 | `#1a1918` | 暖黑，非纯黑 |
| 次要文字 | `#5e5d59` | 暖灰 |
| 辅助文字 | `#87867f` | 云灰 |
| 分割线/边框 | `#e8e6dc` | 象牙深色 |
| 卡片/区块背景 | `#f0eee6` | 象牙中色 |

### 品牌强调色
| 名称 | 色值 | 用途 |
|------|------|------|
| Clay（陶土色） | `#d97757` | 主强调色，用于关键标记、链接、装饰线 |
| Olive（橄榄绿） | `#788c5d` | 辅助点缀 |
| Sky（天蓝） | `#6a9bcc` | 交互/链接备选 |
| Heather（薰衣草）| `#cbcadb` | 轻装饰 |

---

## 字体

Anthropic 使用自有字体（AnthropicSans/Serif/Mono），简历中用公开可用的近似替代：

| 角色 | Anthropic原版 | 替代方案 |
|------|-------------|---------|
| 标题 serif | Copernicus / AnthropicSerif | `'Source Serif 4'`, `Georgia`, `serif` |
| 正文 sans | StyreneA / AnthropicSans | `'Inter'`, `'DM Sans'`, `-apple-system`, `sans-serif` |
| 代码/标签 | JetBrainsMono / AnthropicMono | `'JetBrains Mono'`, `'SF Mono'`, `monospace` |

### 字号（A4简历适配）
| 元素 | 字号 | 字重 | 行高 |
|------|------|------|------|
| 姓名 | 20-22px | 600 | 1.0 |
| 求职意向 | 10px | 500 letter-spacing: 3px | 1.2 |
| Section 标题 | 9px uppercase | 600 letter-spacing: 2.5px | 1.0 |
| 正文/bullet | 9.5px | 400 | 1.4 |
| 次要信息 | 9px | 400 | 1.35 |
| 技能标签 | 9px | 500 | - |

---

## 布局特征

- **左对齐为主**，不居中
- **大量留白**，section之间用空间区隔而非粗线
- **分割线极细**：0.5px solid `#e8e6dc`
- **装饰极简**：仅用一根陶土色细线（2-3px宽）作为品牌标识
- **无阴影、无圆角卡片**：纯平面设计
- **时间轴不用圆点**：用缩进和字号层级区分

## 关键CSS变量

```css
:root {
  /* 色板 */
  --bg-page: #faf9f5;
  --bg-section: #f0eee6;
  --color-text: #1a1918;
  --color-text-sub: #5e5d59;
  --color-text-muted: #87867f;
  --color-accent: #d97757;
  --color-border: #e8e6dc;

  /* 字体 */
  --font-serif: 'Source Serif 4', Georgia, serif;
  --font-sans: 'Inter', 'DM Sans', -apple-system, 'PingFang SC', sans-serif;
  --font-mono: 'JetBrains Mono', 'SF Mono', monospace;
}
```

## 设计要素对照

| Anthropic特征 | 简历应用 |
|-------------|---------|
| 象牙白背景 `#faf9f5` | 页面底色，非纯白 |
| 暖黑文字 `#1a1918` | 正文颜色 |
| 陶土色强调 `#d97757` | 姓名下装饰线、section标题、技能标签下划线 |
| Serif标题+Sans正文 | 姓名用serif，其余用sans |
| 极细分割线 | 0.5px border 区隔section |
| 大写+宽字距标题 | SKILLS / EXPERIENCE 等section标题 |
| 克制留白 | section间距12-16px，不拥挤 |
| 无装饰 | 不用图标、不用彩色背景块、不用圆角卡片 |
