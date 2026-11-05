# -*- coding: utf-8 -*-
"""基于仓库扫描器封面生成驱动盘清理标记封面"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import os

REPO = Path(__file__).resolve().parents[1]

# 底图与 logo 均为本地素材，不入库；按需用环境变量指定
SRC = Path(os.environ.get("COVER_SRC", REPO / "assets" / "src" / "cover_base.png"))
DST = Path(os.environ.get("COVER_DST", REPO / "disc_cleanup" / "assets" / "ui" / "cover.png"))
if not SRC.is_file():
    raise SystemExit(
        "缺少底图：请用环境变量 COVER_SRC 指定一张 600x376 的底图"
        f"（当前期望 {SRC}）"
    )

CYAN = (63, 224, 208)
GRAY = (168, 185, 190)
WHITE = (240, 246, 247)

im = Image.open(SRC).convert("RGBA")
W, H = im.size  # 600x376

# ---- 1) 抹掉左侧原文字区：按列采样背景做渐变填充 + 边缘羽化 ----
x0, y0, x1, y1 = 30, 58, 332, 254
overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
od = overlay.load()
FEATHER = 22
for x in range(x0, x1):
    tp = im.getpixel((x, max(y0 - 7, 0)))
    bp = im.getpixel((x, min(y1 + 7, H - 1)))
    for y in range(y0, y1):
        t = (y - y0) / (y1 - y0)
        r = int(tp[0] + (bp[0] - tp[0]) * t)
        g = int(tp[1] + (bp[1] - tp[1]) * t)
        b = int(tp[2] + (bp[2] - tp[2]) * t)
        # 边缘 alpha 羽化
        a = 255
        if x - x0 < FEATHER:
            a = int(255 * (x - x0) / FEATHER)
        elif x1 - 1 - x < FEATHER:
            a = int(255 * (x1 - 1 - x) / FEATHER)
        ay = a
        if y - y0 < FEATHER:
            ay = min(ay, int(a * (y - y0) / FEATHER))
        elif y1 - 1 - y < FEATHER:
            ay = min(ay, int(a * (y1 - 1 - y) / FEATHER))
        od[x, y] = (r, g, b, ay)
im = Image.alpha_composite(im, overlay)

draw = ImageDraw.Draw(im)

# ---- 2) 新标题文字 ----
def font(path, size, index=0):
    try:
        return ImageFont.truetype(path, size, index=index)
    except Exception:
        return ImageFont.load_default()

ARIAL = r"C:\Windows\Fonts\arialbd.ttf"
MSYH = r"C:\Windows\Fonts\msyhbd.ttc"
if not os.path.exists(MSYH):
    MSYH = r"C:\Windows\Fonts\msyh.ttc"

f_disc = font(ARIAL, 46)
f_clean = font(ARIAL, 46)
f_sub = font(MSYH, 22)
f_badge = font(MSYH, 17)

draw.text((42, 62), "DISC", font=f_disc, fill=WHITE)
draw.text((42, 112), "CLEANUP", font=f_clean, fill=CYAN)
draw.text((43, 170), "驱动盘清理标记", font=f_sub, fill=GRAY)

# ---- 3) 徽章（同款描边圆角胶囊） ----
def badge(x, y, text):
    tw = draw.textlength(text, font=f_badge)
    pad_x, pad_y = 11, 6
    bx0, by0 = x, y
    bx1, by1 = x + tw + pad_x * 2, y + 17 + pad_y * 2
    draw.rounded_rectangle([bx0, by0, bx1, by1], radius=9, outline=CYAN, width=2)
    draw.text((bx0 + pad_x, by0 + pad_y - 1), text, font=f_badge, fill=CYAN)
    return bx1

bx = badge(42, 212, "规则决策")
badge(bx + 14, 212, "自动标记")

# ---- 4) 垃圾桶徽章：右侧圆环右下角 ----
cx, cy, R = 512, 292, 40
draw.ellipse([cx - R, cy - R, cx + R, cy + R], fill=(10, 22, 24, 255), outline=CYAN, width=3)
# 外圈淡光
draw.ellipse([cx - R - 6, cy - R - 6, cx + R + 6, cy + R + 6], outline=(63, 224, 208, 90), width=1)

tc = CYAN  # 垃圾桶颜色
lw = 4
# 桶盖
draw.rounded_rectangle([cx - 20, cy - 18, cx + 20, cy - 10], radius=4, fill=tc)
# 盖提手
draw.rounded_rectangle([cx - 7, cy - 24, cx + 7, cy - 17], radius=3, fill=tc)
# 桶身（略梯形 -> 用多边形）
body = [(cx - 16, cy - 6), (cx + 16, cy - 6), (cx + 12, cy + 22), (cx - 12, cy + 22)]
draw.polygon(body, fill=tc)
# 桶身竖条纹（用背景色挖槽）
slat = (10, 22, 24)
for dx in (-8, 0, 8):
    draw.rectangle([cx + dx - 2, cy - 2, cx + dx + 2, cy + 16], fill=slat)

os.makedirs(os.path.dirname(DST), exist_ok=True)
im.convert("RGB").save(DST)
print("saved", DST, im.size)
