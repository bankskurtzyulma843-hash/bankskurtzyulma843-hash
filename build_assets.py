# -*- coding: utf-8 -*-
"""Build profile assets. Layout reference: github.com/17lijunyi/17lijunyi."""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).parent / "assets" / "v3"
OUT.mkdir(parents=True, exist_ok=True)
# Layout dimensions and visual rhythm follow the supplied reference.
for theme in ('light', 'dark'):
    dark = theme == 'dark'
    bg, top, edge = ('#0d1117', '#161b22', '#30363d') if dark else ('#f8fafb', '#f1f4f6', '#d8e0e7')
    ink, muted, blue, green = ('#c9d1d9', '#8b949e', '#58a6ff', '#56d364') if dark else ('#566573', '#9aa7b3', '#3478c9', '#4aa176')
    lines = [
        (93, '一百 OS — AI Product Portfolio', 'heading'),
        (126, '[ OK ] Load 产品思维内核 product-thinking.ai', ''),
        (157, '[ OK ] Mount /products    产品原型', ''),
        (188, '[ OK ] Mount /research    产品架构拆解', ''),
        (219, '[ OK ] Mount /experiments 交互实验', ''),
        (267, 'yibai@mac ~ % whoami', 'command'),
        (298, '一百 · AI 产品经理', ''),
        (346, 'yibai@mac ~ % open projects.md', 'command'),
    ]
    boot = []
    for i, (y, value, cls) in enumerate(lines):
        content = escape(value).replace('OK', '<tspan class="success">OK</tspan>')
        if cls == 'command':
            content = content.replace('whoami', '<tspan class="normal">whoami</tspan>').replace('open projects.md', '<tspan class="normal">open projects.md</tspan>')
        boot.append(f'<text class="boot {cls}" x="54" y="{y}" style="animation-delay:{.15+.33*i:.2f}s">{content}</text>')
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="520" viewBox="0 0 1000 520" role="img" aria-labelledby="title description" xml:space="preserve">
<title id="title">一百 · AI 产品经理 · 项目启动终端</title>
<desc id="description">产品原型、产品架构拆解与交互实验。点击查看一百的项目索引。</desc>
<style>
text {{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","PingFang SC","Microsoft YaHei",monospace;fill:{ink};font-size:16px}}
.boot {{animation:boot 8s ease-in-out infinite;opacity:0}}
.heading {{font-size:18px;font-weight:700}}
.command {{fill:{blue};font-weight:700}}
.normal {{fill:{ink};font-size:16px}}
.success {{fill:{green};font-weight:700}}
.ready {{fill:{blue};font-size:17px;font-weight:700;animation:ready 8s ease-in-out infinite;opacity:0}}
.invite {{font-size:14px;letter-spacing:1.8px;animation:invite 8s ease-in-out infinite;opacity:0}}
.arrow {{fill:{blue};font-size:22px;animation:arrow 1.4s 3.9s ease-in-out infinite;opacity:0}}
@keyframes boot {{0%,5%{{opacity:0;transform:translateY(5px)}}10%,77%{{opacity:1;transform:translateY(0)}}88%,100%{{opacity:0;transform:translateY(-2px)}}}}
@keyframes ready {{0%,42%{{opacity:0;transform:translateY(5px)}}48%,82%{{opacity:1;transform:translateY(0)}}92%,100%{{opacity:0}}}}
@keyframes invite {{0%,50%,92%,100%{{opacity:0}}57%,84%{{opacity:1}}}}
@keyframes arrow {{0%,100%{{opacity:.35;transform:translateX(0)}}50%{{opacity:1;transform:translateX(7px)}}}}
@media(prefers-reduced-motion:reduce){{.boot,.ready,.invite,.arrow{{animation:none;opacity:1;transform:none}}}}
</style>
<rect x="1" y="1" width="998" height="518" rx="18" fill="{bg}" stroke="{edge}" stroke-width="2"/>
<path d="M19 2H981Q999 2 999 20V51H1V20Q1 2 19 2Z" fill="{top}"/>
<path d="M1 52H999" stroke="{edge}"/>
<circle cx="24" cy="27" r="7" fill="#ef6461"/><circle cx="47" cy="27" r="7" fill="#efbd4e"/><circle cx="70" cy="27" r="7" fill="#55b96f"/>
<text x="500" y="31" text-anchor="middle" style="fill:{muted};font-size:12px;letter-spacing:.8px">yibai@mac — portfolio — 100×30</text>
{''.join(boot)}
<text class="ready" x="54" y="389">SYSTEM READY</text>
<text class="invite" x="500" y="448" text-anchor="middle">点击查看项目索引 · 一百</text>
<text class="arrow" x="500" y="483" text-anchor="middle">→</text>
</svg>
'''
    (OUT / f'portfolio-launch-{theme}.svg').write_text(svg)

projects = [
    ("nanmenwai", "南门外 · 校园互动叙事", ["从入学到毕业的故事选择、人物关系与手记回看。", "本地规则管理状态，探索模型扩写与失败回退。"], "HTML", "#e34c26"),
    ("life-book", "人生之书 · 大学篇", ["从星河到书本，探索大学四年的情景与选择。", "基于 BlueYard 场景扩展叙事，支持记忆记录。"], "HTML", "#e34c26"),
    ("teardown", "产品架构拆解", ["基于真实证据，从用户、技术、模型、数据四层", "拆解产品，整理成可复用的分析工作流。"], "Skill", "#8250df"),
]
for theme in ("light", "dark"):
    bg, border, muted, link = (
        ("#ffffff", "#d1d9e0", "#59636e", "#0969da")
        if theme == "light"
        else ("#0d1117", "#30363d", "#8b949e", "#58a6ff")
    )
    for key, title, lines, language, dot in projects:
        desc = "".join(lines)
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="620" height="210" viewBox="0 0 620 210" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>
<rect x=".75" y=".75" width="598.5" height="208.5" rx="9" fill="{bg}" stroke="{border}" stroke-width="1.5"/>
<g font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Noto Sans CJK SC,PingFang SC,Microsoft YaHei,sans-serif">
<g transform="translate(24 24)" fill="none" stroke="{muted}" stroke-width="1.7"><path d="M3 2h15v20H3a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2Zm-2 15h17M5 17v7l3-2 3 2v-7"/></g>
<text x="56" y="43" fill="{link}" font-size="22" font-weight="600">{escape(title)}</text>
<rect x="512" y="23" width="64" height="26" rx="13" fill="none" stroke="{border}"/>
<text x="544" y="41" text-anchor="middle" fill="{muted}" font-size="15">Public</text>
<text x="24" y="81" fill="{muted}" font-size="19">{escape(lines[0])}</text>
<text x="24" y="108" fill="{muted}" font-size="19">{escape(lines[1])}</text>
<circle cx="31" cy="177" r="7" fill="{dot}"/>
<text x="47" y="183" fill="{muted}" font-size="17">{language}</text>
<g transform="translate(230 166)" fill="none" stroke="{muted}" stroke-width="1.6"><path d="m10 1 2.8 5.7 6.2.9-4.5 4.4 1.1 6.2-5.6-3-5.6 3 1.1-6.2L1 7.6l6.2-.9Z"/></g>
<text x="258" y="183" fill="{muted}" font-size="17">0</text>
<g transform="translate(350 166)" fill="none" stroke="{muted}" stroke-width="1.6"><circle cx="5" cy="3" r="2.5"/><circle cx="15" cy="3" r="2.5"/><circle cx="10" cy="17" r="2.5"/><path d="M5 5.5V8c0 3 10 3 10 0V5.5M10 10v4.5"/></g>
<text x="378" y="183" fill="{muted}" font-size="17">0</text>
</g></svg>
'''
        (OUT / f"{key}-{theme}.svg").write_text(svg)
print("Built 8 reference-matched SVGs.")

