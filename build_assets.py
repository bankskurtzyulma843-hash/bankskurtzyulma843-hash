"""Build original profile artwork with the Python standard library."""
from pathlib import Path
from xml.sax.saxutils import escape
OUT = Path(__file__).parent / 'assets' / 'v2'
OUT.mkdir(parents=True, exist_ok=True)
FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Microsoft YaHei',sans-serif"
MONO = "'SFMono-Regular',Consolas,'Liberation Mono','PingFang SC',monospace"

def text(x, y, value, size=22, fill='currentColor', weight=400, mono=False, extra=''):
    return f'<text x="{x}" y="{y}" font-family="{MONO if mono else FONT}" font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{escape(value)}</text>'

def save(name, width, height, title, body):
    (OUT / name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title)}">\n<title>{escape(title)}</title>\n{body}\n</svg>\n', encoding='utf-8')

for mode in ('light', 'dark'):
    dark = mode == 'dark'
    bg = '#111820' if dark else '#F8FAFC'
    top = '#1A242F' if dark else '#EEF2F5'
    ink = '#EAF0F5' if dark else '#202D3B'
    muted = '#A6B4C4' if dark else '#586A7C'
    line = '#344251' if dark else '#D9E1E8'
    accent = '#83D7BA' if dark else '#267C67'
    blue = '#91BFF7' if dark else '#376FA8'
    terminal = f'''<defs><clipPath id="window"><rect x="1" y="1" width="1278" height="378" rx="22"/></clipPath></defs>
<rect x="1" y="1" width="1278" height="378" rx="22" fill="{bg}" stroke="{line}" stroke-width="2"/>
<path d="M0 0H1280V58H0Z" fill="{top}" clip-path="url(#window)"/>
<path d="M1 58H1279" stroke="{line}"/>
<circle cx="31" cy="29" r="7" fill="#E97771"/><circle cx="56" cy="29" r="7" fill="#E8BE59"/><circle cx="81" cy="29" r="7" fill="#6CBD94"/>
{text(640, 35, 'yibai — portfolio', 17, muted, mono=True, extra='text-anchor="middle"')}
{text(50, 108, 'yibai ~ % whoami', 22, blue, 600, True)}
{text(50, 164, '一百 · AI 产品经理', 39, ink, 600)}
{text(52, 199, 'AI PRODUCT MANAGER', 17, muted, mono=True, extra='letter-spacing="2"')}
{text(50, 256, 'yibai ~ % ls projects/', 22, blue, 600, True)}
{text(50, 294, '产品原型 / 产品拆解 / 交互实验', 23, ink)}
<path d="M50 321H1230" stroke="{line}"/>
{text(50, 354, '查看项目与产品思考', 19, accent, 500)}
{text(1230, 355, '↗', 28, accent, 500, extra='text-anchor="end"')}
<g fill="none" stroke="{accent}" opacity=".15" stroke-width="1.5">
<rect x="978" y="104" width="184" height="156" rx="12"/><path d="M1002 128H1096M1002 147H1064M1002 232H1139"/>
<rect x="1004" y="177" width="34" height="34" rx="5"/><rect x="1054" y="177" width="34" height="34" rx="5"/><rect x="1104" y="177" width="34" height="34" rx="5"/></g>'''
    save(f'terminal-{mode}.svg', 1280, 380, '一百 · AI 产品经理 · 查看项目与产品思考', terminal)
    cards = [
        ('nanmenwai', '01 / PRODUCT PROTOTYPE', '南门外', '校园互动叙事原型', '故事选择、人物关系与进度保存。', '探索模型扩写与本地规则的协作。', '产品原型 · 本地运行', accent),
        ('teardown', '02 / PRODUCT RESEARCH', '产品架构拆解', '可复用的产品分析 Skill', '从用户、技术、模型、数据出发，', '把产品判断关联到可核查的证据。', '分析方法 · 开源 Skill', blue),
    ]
    for key, label, title, subtitle, desc1, desc2, tag, color in cards:
        body = f'''<rect x="1" y="1" width="618" height="304" rx="17" fill="{bg}" stroke="{line}" stroke-width="2"/>
<rect x="29" y="29" width="4" height="20" rx="2" fill="{color}"/>
{text(45, 45, label, 16, muted, mono=True)}
{text(32, 100, title, 34, ink, 600)}
{text(32, 137, subtitle, 21, color, 500)}
{text(32, 184, desc1, 21, muted)}
{text(32, 217, desc2, 21, muted)}
<path d="M32 245H588" stroke="{line}"/>
{text(32, 279, tag, 18, muted)}
{text(586, 280, '↗', 26, color, extra='text-anchor="end"')}'''
        save(f'{key}-{mode}.svg', 620, 306, f'{title} · {subtitle}。{desc1}{desc2}', body)
    stars = [(929, 51), (1038, 88), (1166, 48), (965, 151), (1093, 174), (1224, 134)]
    constellation = f'<path d="M929 51L1038 88L1166 48M1038 88L965 151L1093 174L1224 134" fill="none" stroke="{line}" stroke-width="2"/>'
    constellation += ''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="{accent}"/>' for x, y in stars)
    book = f'<path d="M1031 109Q1057 98 1080 112Q1103 98 1129 109V148Q1102 137 1080 151Q1058 137 1031 148Z M1080 112V151" fill="{bg}" stroke="{accent}" stroke-width="2"/>'
    story = f'''<rect x="1" y="1" width="1278" height="238" rx="17" fill="{bg}" stroke="{line}" stroke-width="2"/>
<rect x="33" y="27" width="4" height="20" rx="2" fill="{accent}"/>
{text(49, 43, '03 / INTERACTIVE EXPERIMENT', 16, muted, mono=True)}
{text(36, 94, '人生之书 · 大学篇', 34, ink, 600)}
{text(36, 136, '从星河到书本，探索大学四年的情景叙事与选择。', 22, muted)}
{text(36, 170, '书本开场 · 四年星图 · 情景选择 · 记忆记录', 20, muted)}
<path d="M36 189H1244" stroke="{line}"/>
{text(36, 219, '交互实验 · 基于 BlueYard 场景扩展', 18, muted)}
{text(1244, 220, '查看项目 ↗', 19, accent, 500, extra='text-anchor="end"')}
{constellation}{book}'''
    save(f'life-book-{mode}.svg', 1280, 240, '人生之书 · 大学篇。基于 BlueYard 场景扩展的校园叙事与交互实验。', story)
print('Built 8 SVG assets with light and dark variants.')
