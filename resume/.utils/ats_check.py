#!/usr/bin/env python3
"""
ATS 友好度检测脚本
用法: python3 ats_check.py <pdf文件路径>

检测项目:
1. 文本是否可提取（非扫描件）
2. 关键字段是否完整（姓名、电话、邮箱、技能关键词）
3. 文本顺序是否合理（并排布局可能导致乱序）
4. 特殊字符/乱码检测
"""

import sys
import re
import pdfplumber


def extract_text(pdf_path):
    """提取 PDF 全部文本"""
    full_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n"
    return full_text


def check_ats(pdf_path):
    print(f"\n{'='*60}")
    print(f"  ATS 友好度检测: {pdf_path}")
    print(f"{'='*60}\n")

    text = extract_text(pdf_path)
    issues = []
    passes = []

    # --- 1. 基础文本提取 ---
    if not text.strip():
        print("❌ 致命: PDF 无法提取任何文本（可能是图片/扫描件）")
        print("   ATS 完全无法读取此文件。")
        return
    passes.append("文本可提取")

    print(f"📄 提取到 {len(text)} 个字符\n")

    # --- 2. 关键字段检测 ---
    checks = {
        "姓名(何伟杰)": r"何伟杰",
        "电话": r"1354424844[6]",
        "邮箱": r"heweijie0306@gmail\.com",
        "GitHub": r"github",
    }

    print("── 关键字段 ──")
    for label, pattern in checks.items():
        if re.search(pattern, text, re.IGNORECASE):
            passes.append(label)
            print(f"  ✅ {label}")
        else:
            issues.append(f"缺失: {label}")
            print(f"  ❌ {label} — 未找到")

    # --- 3. 技能关键词 (高频 JD 词) ---
    keywords = [
        "Agent", "RAG", "MCP", "LangChain", "LangGraph",
        "Python", "TypeScript", "React", "FastAPI",
        "Prompt Engineering", "Tool Calling",
        "Claude", "OpenAI",
        "Context Engineering", "ReAct",
    ]

    print("\n── 技能关键词 (ATS 匹配) ──")
    found_kw = []
    missing_kw = []
    for kw in keywords:
        if re.search(re.escape(kw), text, re.IGNORECASE):
            found_kw.append(kw)
        else:
            missing_kw.append(kw)

    print(f"  ✅ 命中 {len(found_kw)}/{len(keywords)}: {', '.join(found_kw)}")
    if missing_kw:
        print(f"  ⚠️  未匹配: {', '.join(missing_kw)}")

    # --- 4. 文本顺序检查 ---
    print("\n── 文本顺序 ──")
    # 检查关键段落是否按正确顺序出现
    section_order = ["个人总结", "专业技能", "工作经历", "项目经历", "教育背景"]
    # 也检查英文版
    section_order_en = ["Summary", "Skills", "Experience", "Project", "Education"]

    positions = {}
    for s in section_order + section_order_en:
        match = re.search(re.escape(s), text)
        if match:
            positions[s] = match.start()

    if positions:
        sorted_sections = sorted(positions.items(), key=lambda x: x[1])
        prev_pos = -1
        order_ok = True
        for name, pos in sorted_sections:
            if pos < prev_pos:
                order_ok = False
            prev_pos = pos

        if order_ok:
            passes.append("段落顺序正确")
            print(f"  ✅ 段落顺序正确: {' → '.join(s for s, _ in sorted_sections)}")
        else:
            issues.append("段落顺序异常（可能并排布局导致）")
            print(f"  ❌ 段落顺序异常!")
            print(f"     检测到顺序: {' → '.join(s for s, _ in sorted_sections)}")
    else:
        issues.append("未检测到标准段落标题")
        print("  ⚠️  未检测到标准段落标题")

    # --- 5. 乱码/特殊字符检测 ---
    print("\n── 特殊字符 ──")
    # 检查常见的 PDF 转换乱码
    garbled = re.findall(r'[\ufffd\ufffe\uffff]', text)
    weird_sequences = re.findall(r'[^\w\s\u4e00-\u9fff\u3000-\u303f\uff00-\uffef.,;:!?@#$%^&*()_+\-=\[\]{}|\\/<>~`\'\"·•—–…℃°±×÷→←↑↓]', text)
    if not garbled and len(weird_sequences) < 5:
        passes.append("无乱码")
        print("  ✅ 未检测到明显乱码")
    else:
        issues.append(f"发现 {len(garbled)} 个乱码字符, {len(weird_sequences)} 个异常字符")
        print(f"  ⚠️  发现 {len(garbled)} 个乱码, {len(weird_sequences)} 个异常字符")

    # --- 6. 总结 ---
    print(f"\n{'='*60}")
    score = len(passes) / (len(passes) + len(issues)) * 100 if (passes or issues) else 0
    print(f"  ATS 友好度评分: {score:.0f}% ({len(passes)} 通过 / {len(issues)} 问题)")
    print(f"{'='*60}")

    if issues:
        print("\n⚠️  需要关注:")
        for i in issues:
            print(f"   - {i}")

    print("\n── 提取的原始文本 (前 1500 字) ──")
    print(text[:1500])
    print("..." if len(text) > 1500 else "")
    print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 ats_check.py <pdf文件路径>")
        print("示例: python3 ats_check.py ~/Desktop/resume.pdf")
        sys.exit(1)
    check_ats(sys.argv[1])
