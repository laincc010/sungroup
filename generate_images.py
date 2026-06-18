#!/usr/bin/env python3
"""
孙氏集团企业官网 - 配图生成脚本
生成 LOGO、Banner、案例、资质等全部配图
"""
import os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE_DIR = r"e:\all-project\html-project\project1\images"
os.makedirs(BASE_DIR, exist_ok=True)

# ============================================
# Color Palette (Deep Dark + Rainbow)
# ============================================
BG_DARK    = (10, 14, 23)
BG_MID     = (17, 24, 39)
C_ORANGE   = (255, 107, 53)
C_GOLD     = (255, 215, 0)
C_GREEN    = (0, 210, 160)
C_BLUE     = (74, 144, 217)
C_PURPLE   = (123, 79, 191)
C_ROSE     = (233, 30, 123)
C_WHITE    = (255, 255, 255)
C_GRAY     = (176, 184, 200)
RAINBOW    = [C_ORANGE, C_GOLD, C_GREEN, C_BLUE, C_PURPLE, C_ROSE]

# Try to load a font, fallback to default
FONT_BOLD = None
FONT_REGULAR = None
for fp in ["C:/Windows/Fonts/msyhbd.ttf", "C:/Windows/Fonts/simhei.ttf",
           "C:/Windows/Fonts/arialbd.ttf", "C:/Windows/Fonts/arial.ttf"]:
    try:
        FONT_BOLD = ImageFont.truetype(fp, size=40)
        break
    except: pass


def font(size, bold=True):
    """Get font at given size. Falls back gracefully."""
    try:
        fp = "C:/Windows/Fonts/msyhbd.ttf" if bold else "C:/Windows/Fonts/msyh.ttf"
        return ImageFont.truetype(fp, size=size)
    except:
        try:
            return ImageFont.truetype("C:/Windows/Fonts/simhei.ttf", size=size)
        except:
            return ImageFont.load_default()


def rainbow_gradient(width, height, angle=0, alpha=False):
    """Create a rainbow gradient image."""
    img = Image.new('RGBA' if alpha else 'RGB', (width, height))
    px = img.load()
    import math
    rad = math.radians(angle)
    n = len(RAINBOW)
    for y in range(height):
        for x in range(width):
            t = ((x * math.cos(rad) + y * math.sin(rad)) / max(width, height))
            t = (t % 1.0) * n
            idx = int(t)
            frac = t - idx
            c1 = RAINBOW[idx % n]
            c2 = RAINBOW[(idx + 1) % n]
            r = int(c1[0] * (1 - frac) + c2[0] * frac)
            g = int(c1[1] * (1 - frac) + c2[1] * frac)
            b = int(c1[2] * (1 - frac) + c2[2] * frac)
            px[x, y] = (r, g, b, 255) if alpha else (r, g, b)
    return img


def dark_overlay(img, opacity=0.6):
    """Apply dark overlay to an image."""
    overlay = Image.new('RGBA', img.size, (10, 14, 23, int(255 * opacity)))
    img_rgba = img.convert('RGBA')
    return Image.alpha_composite(img_rgba, overlay)


def add_noise(img, amount=15):
    """Add subtle noise texture for realism."""
    import random
    px = img.load()
    w, h = img.size
    for _ in range(w * h // 50):
        x = random.randint(0, w - 1)
        y = random.randint(0, h - 1)
        r, g, b = px[x, y][:3]
        n = random.randint(-amount, amount)
        px[x, y] = (max(0, min(255, r + n)),
                    max(0, min(255, g + n)),
                    max(0, min(255, b + n)))
    return img


def glow_circle(draw, cx, cy, r, color, opacity=60):
    """Draw a glowing circle with radial gradient effect."""
    for i in range(r, 0, -2):
        alpha = int(opacity * (i / r))
        draw.ellipse([cx - i, cy - i, cx + i, cy + i],
                     fill=(*color, alpha))


# ============================================
# 1. LOGO (500x200)
# ============================================
print("Generating LOGO...")
logo = Image.new('RGBA', (500, 200), (0, 0, 0, 0))
draw = ImageDraw.Draw(logo)

# Rainbow glow behind logo
for i, (cx, cy) in enumerate([(130, 80), (250, 100), (370, 80)]):
    glow_circle(draw, cx, cy, 60, RAINBOW[i], 30)

# "SUN GROUP" text with rainbow gradient
try:
    f_big = font(72, True)
    f_small = font(28, False)
    # Draw SUN GROUP letter by letter with rainbow colors
    letters = list("SUN  GROUP")
    x_pos = 30
    for i, ch in enumerate(letters):
        color = RAINBOW[i % len(RAINBOW)]
        if ch != ' ':
            draw.text((x_pos, 30), ch, fill=color, font=f_big)
        x_pos += 50 if ch != ' ' else 25
    # 孙氏集团
    draw.text((100, 115), "孙氏集团", fill=C_GRAY, font=f_small)
    # Subtitle
    f_xs = font(16, False)
    draw.text((80, 160), "SUN  GROUP  ·  链接全球  物流天下", fill=C_GRAY, font=f_xs)
except Exception as e:
    print(f"  Font issue, using fallback: {e}")
    draw.text((80, 50), "SUN GROUP", fill=C_ORANGE, font=font(48))
    draw.text((150, 110), "孙氏集团", fill=C_WHITE, font=font(24))

logo.save(os.path.join(BASE_DIR, "logo.png"))
print("  -> images/logo.png")

# ============================================
# 2. FAVICON (32x32)
# ============================================
favicon = Image.new('RGBA', (32, 32), (0, 0, 0, 0))
d = ImageDraw.Draw(favicon)
d.ellipse([2, 2, 30, 30], fill=C_ORANGE)
d.ellipse([2, 2, 30, 30], outline=C_GOLD, width=1)
# "S" letter
try:
    f_fav = font(20, True)
    d.text((8, 3), "S", fill=C_WHITE, font=f_fav)
except:
    d.text((10, 5), "S", fill=C_WHITE)
favicon.save(os.path.join(BASE_DIR, "favicon.ico"))
print("  -> images/favicon.ico")

# ============================================
# 3. BANNER 配图 (1920x900)
# ============================================
print("Generating Banner images...")
os.makedirs(os.path.join(BASE_DIR, "banner"), exist_ok=True)

banner_configs = [
    ("slide-1.jpg", "链接全球  物流天下",
     ["GLOBAL LOGISTICS", "国际海运 · 空运 · 陆运 · 仓储", "20年深耕 · 60+国家覆盖"]),
    ("slide-2.jpg", "智慧供应链  解决方案",
     ["SMART SUPPLY CHAIN", "从港口到门 · 仓储到配送", "一站式全链路服务"]),
    ("slide-3.jpg", "信赖之选  共赢未来",
     ["TRUSTED BY 5000+", "年吞吐量超百万吨", "专业团队 · 24h响应"]),
]

for filename, title, subtitles in banner_configs:
    img = Image.new('RGB', (1920, 900), BG_DARK)
    px = img.load()

    # Base: dark gradient with colored accents
    for y in range(900):
        ratio = y / 900
        r = int(BG_DARK[0] + (20 * ratio))
        g = int(BG_DARK[1] + (15 * ratio))
        b = int(BG_DARK[2] + (25 * ratio))
        for x in range(1920):
            px[x, y] = (r, g, b)

    draw = ImageDraw.Draw(img)

    # Large diagonal rainbow light beam
    for i in range(6):
        cx = 400 + i * 200
        cy = 300 + i * 80
        color = RAINBOW[i]
        # Large soft glow
        for r in range(500, 100, -50):
            alpha = int(15 * (r / 500))
            # Just draw a large ellipse with low opacity by blending
            draw.ellipse([cx - r, cy - r, cx + r, cy + r],
                         fill=(*color, alpha) if hasattr(ImageDraw, 'ellipse_alpha') else color,
                         outline=None)

    # Grid/network lines (logistics theme)
    for i in range(0, 1920, 80):
        draw.line([(i, 0), (i + 200, 900)], fill=(*C_BLUE, 8), width=1)
    for i in range(0, 900, 80):
        draw.line([(0, i), (1920, i + 150)], fill=(*C_PURPLE, 5), width=1)

    # Highlight circles (like destination nodes on a map)
    import random
    random.seed(42)
    dots = [(random.randint(100, 1700), random.randint(100, 700)) for _ in range(25)]
    for dx, dy in dots:
        glow_circle(draw, dx, dy, random.randint(8, 20), RAINBOW[random.randint(0, 5)], 80)
        draw.ellipse([dx - 3, dy - 3, dx + 3, dy + 3], fill=C_GOLD)

    # Connecting lines between nearby dots
    for i, (x1, y1) in enumerate(dots):
        for j, (x2, y2) in enumerate(dots[i+1:], i+1):
            dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            if dist < 250:
                draw.line([(x1, y1), (x2, y2)], fill=(*C_GRAY, 20), width=1)

    # Dark gradient overlay from bottom
    for y in range(900):
        alpha = int(200 * (y / 900)) if y > 500 else 0
        if alpha > 0:
            for x in range(1920):
                r, g, b = px[x, y]
                px[x, y] = (max(0, r - alpha // 8), max(0, g - alpha // 8), max(0, b - alpha // 8))

    # Title text (large, centered)
    try:
        f_title = font(80, True)
        f_sub1 = font(28, False)
        f_sub2 = font(20, False)

        # Text shadow / glow
        bbox = draw.textbbox((0, 0), title, font=f_title)
        tw = bbox[2] - bbox[0]
        tx = (1920 - tw) // 2
        ty = 350

        # Draw colored glow behind text
        for off in range(8, 2, -2):
            glow_color = RAINBOW[off % len(RAINBOW)]
            draw.text((tx - off, ty - off), title, fill=(*glow_color, 20), font=f_title)
            draw.text((tx + off, ty + off), title, fill=(*glow_color, 20), font=f_title)

        # Main text in white
        draw.text((tx, ty), title, fill=C_WHITE, font=f_title)

        # Subtitles
        for i, sub in enumerate(subtitles):
            bbox2 = draw.textbbox((0, 0), sub, font=f_sub1 if i == 0 else f_sub2)
            sw = bbox2[2] - bbox2[0]
            sx = (1920 - sw) // 2
            color = RAINBOW[(i + 1) % len(RAINBOW)] if i == 0 else C_GRAY
            draw.text((sx, ty + 100 + i * 45), sub, fill=color, font=f_sub1 if i == 0 else f_sub2)
    except Exception as e:
        print(f"  Text render fallback: {e}")
        f_d = font(50, True)
        draw.text((700, 400), title, fill=C_WHITE, font=f_d)

    # Save
    filepath = os.path.join(BASE_DIR, "banner", filename)
    img = add_noise(img, 8)
    img.save(filepath, quality=85)
    print(f"  -> images/banner/{filename}")

# ============================================
# 4. ABOUT - 集团总部 (800x500)
# ============================================
print("Generating About image...")
os.makedirs(os.path.join(BASE_DIR, "about"), exist_ok=True)

img = Image.new('RGB', (800, 500), BG_DARK)
draw = ImageDraw.Draw(img)
px = img.load()

# Gradient sky
for y in range(500):
    for x in range(800):
        t = y / 500
        r = int(BG_DARK[0] * (1 - t) + 30 * t)
        g = int(BG_DARK[1] * (1 - t) + 40 * t)
        b = int(BG_DARK[2] * (1 - t) + 60 * t)
        px[x, y] = (r, g, b)

# Building silhouette
building_color = (25, 30, 50)
draw.polygon([(300, 420), (500, 420), (500, 180), (400, 120), (300, 180)],
             fill=building_color, outline=(60, 65, 80))
# Windows
for row_y in range(200, 400, 35):
    for col_x in range(320, 480, 40):
        draw.rectangle([col_x, row_y, col_x + 20, row_y + 18],
                       fill=(*C_BLUE, 100), outline=(*C_BLUE, 60))
# Side buildings
draw.rectangle([180, 350, 280, 420], fill=(20, 25, 45), outline=(55, 60, 75))
draw.rectangle([520, 320, 640, 420], fill=(20, 25, 45), outline=(55, 60, 75))
for row_y in range(335, 400, 20):
    for col_x in range(195, 270, 20):
        draw.rectangle([col_x, row_y, col_x + 10, row_y + 10], fill=(*C_GOLD, 60))
for row_y in range(340, 400, 20):
    for col_x in range(535, 630, 20):
        draw.rectangle([col_x, row_y, col_x + 10, row_y + 10], fill=(*C_GOLD, 60))

# Ground
draw.rectangle([0, 420, 800, 500], fill=(5, 9, 18))

# Rainbow accent line on main building
for i, y in enumerate(range(120, 180, 10)):
    c = RAINBOW[i % len(RAINBOW)]
    draw.line([(400, y), (500, y)], fill=c, width=3)

# "SUN GROUP" on building
try:
    f_b = font(24, True)
    draw.text((410, 140), "SUN GROUP\n孙氏集团", fill=C_WHITE, font=font(14))
except:
    pass

# Sun glow
glow_circle(draw, 400, 80, 60, C_GOLD, 80)
glow_circle(draw, 400, 80, 30, C_ORANGE, 120)

# Ground lights
for gx in range(50, 750, 80):
    glow_circle(draw, gx, 430, 30, RAINBOW[(gx // 80) % len(RAINBOW)], 40)

img = add_noise(img, 6)
img.save(os.path.join(BASE_DIR, "about", "headquarters.jpg"), quality=85)
print("  -> images/about/headquarters.jpg")

# ============================================
# 5. CASE STUDY THUMBNAILS (800x500)
# ============================================
print("Generating Case Study images...")
os.makedirs(os.path.join(BASE_DIR, "cases"), exist_ok=True)

case_configs = [
    ("case-1.jpg", "国际海运", C_BLUE, ["Container Ship", "Global Ports", "50万TEU/年"]),
    ("case-2.jpg", "航空货运", C_ROSE, ["Air Cargo", "48h Global Delivery", "3000+ Missions"]),
    ("case-3.jpg", "跨境电商", C_GREEN, ["E-Commerce Logistics", "100K+ Daily Orders", "99.5% Delivery"]),
    ("case-4.jpg", "仓储配送", C_PURPLE, ["Smart Warehouse", "50万m² Storage", "WMS System"]),
    ("case-5.jpg", "供应链管理", C_BLUE, ["Supply Chain", "2M Tons/Year", "Full Coverage"]),
    ("case-6.jpg", "陆运物流", C_GOLD, ["Rail & Truck", "50+ Trains/Month", "Europe-Asia"]),
]

for filename, title, accent, labels in case_configs:
    img = Image.new('RGB', (800, 500), BG_DARK)
    px = img.load()
    draw = ImageDraw.Draw(img)

    # Accent color gradient background
    for y in range(500):
        t = y / 500
        for x in range(800):
            xt = x / 800
            r = int(BG_DARK[0] + (accent[0] - BG_DARK[0]) * 0.3 * (1 - abs(xt - 0.5) * 2) * (1 - t))
            g = int(BG_DARK[1] + (accent[1] - BG_DARK[1]) * 0.3 * (1 - abs(xt - 0.5) * 2) * (1 - t))
            b = int(BG_DARK[2] + (accent[2] - BG_DARK[2]) * 0.3 * (1 - abs(xt - 0.5) * 2) * (1 - t))
            px[x, y] = (max(0, min(255, r)), max(0, min(255, g)), max(0, min(255, b)))

    # Geometric abstract shapes
    import random
    random.seed(hash(title) % 10000)
    for _ in range(5):
        cx = random.randint(100, 700)
        cy = random.randint(100, 400)
        r = random.randint(40, 120)
        glow_circle(draw, cx, cy, r, accent, 25)

    # Grid lines (logistics network)
    for gi in range(0, 800, 60):
        draw.line([(gi, 0), (gi + 100, 500)], fill=(*accent, 10), width=1)

    # Title overlay
    try:
        f_t = font(36, True)
        f_s = font(18, False)
        # Dark title bar at bottom
        for y in range(380, 500):
            alpha = (y - 380) / 120
            for x in range(800):
                pr, pg, pb = px[x, y]
                px[x, y] = (int(pr * (1 - alpha * 0.7)),
                            int(pg * (1 - alpha * 0.7)),
                            int(pb * (1 - alpha * 0.7)))

        draw.text((30, 400), title, fill=accent, font=f_t)
        for i, label in enumerate(labels):
            draw.text((30, 440 + i * 22), label, fill=C_GRAY, font=f_s)
    except:
        pass

    img = add_noise(img, 6)
    img.save(os.path.join(BASE_DIR, "cases", filename), quality=85)
    print(f"  -> images/cases/{filename}")

# ============================================
# 6. HONOR CERTIFICATES (600x800)
# ============================================
print("Generating Certificate images...")
os.makedirs(os.path.join(BASE_DIR, "honor"), exist_ok=True)

cert_configs = [
    ("cert-1.jpg", "营业执照", C_ORANGE, "统一社会信用代码\n91310000MA1XXXXXXX"),
    ("cert-2.jpg", "ISO 9001认证", C_GOLD, "质量管理体系认证\nGB/T 19001-2016"),
    ("cert-3.jpg", "AAAAA级物流企业", C_GREEN, "中国物流与采购联合会\n认证等级：AAAAA"),
    ("cert-4.jpg", "最佳物流服务商", C_BLUE, "2025年度最佳物流服务商\n中国物流行业协会"),
    ("cert-5.jpg", "海关AEO认证", C_PURPLE, "Authorized Economic Operator\n海关高级认证企业"),
    ("cert-6.jpg", "5A级诚信企业", C_ROSE, "企业信用等级：AAAAA\n诚信经营示范企业"),
    ("cert-7.jpg", "绿色物流认证", C_GREEN, "绿色物流示范企业\n节能减排先进单位"),
    ("cert-8.jpg", "货运代理资质", C_ORANGE, "国际货运代理企业\n一级资质"),
]

for filename, title, accent, desc in cert_configs:
    img = Image.new('RGB', (600, 800), (240, 238, 230))  # paper color
    px = img.load()
    draw = ImageDraw.Draw(img)

    # Aged paper texture
    import random
    random.seed(hash(filename) % 10000)
    for _ in range(2000):
        x = random.randint(0, 599)
        y = random.randint(0, 799)
        n = random.randint(-8, 8)
        r, g, b = px[x, y]
        px[x, y] = (max(0, min(255, r + n)),
                    max(0, min(255, g + n)),
                    max(0, min(255, b + n)))

    # Ornate border
    border_color = (180, 160, 120)
    for i in range(4):
        draw.rectangle([20 + i, 20 + i, 580 - i, 780 - i], outline=border_color)
    # Inner gold border
    draw.rectangle([30, 30, 570, 770], outline=(200, 180, 100), width=2)

    # Decorative corners
    for cx, cy in [(40, 40), (560, 40), (40, 760), (560, 760)]:
        draw.arc([cx - 20, cy - 20, cx + 20, cy + 20], 0, 360, fill=border_color, width=3)

    # Title area with colored ribbon
    draw.rectangle([50, 100, 550, 180], fill=accent)
    for i in range(6):
        y_ribbon = 95 + i * 15
        draw.line([(50, y_ribbon), (550, y_ribbon)], fill=RAINBOW[i % len(RAINBOW)], width=2)
    for i in range(6):
        y_ribbon = 185 + i * 3
        draw.line([(50, y_ribbon), (550, y_ribbon)], fill=RAINBOW[i % len(RAINBOW)], width=2)

    # Emblem circle
    draw.ellipse([250, 220, 350, 320], outline=accent, width=3)
    draw.ellipse([260, 230, 340, 310], fill=accent)
    try:
        f_em = font(36, True)
        draw.text((278, 248), "S", fill=(255, 255, 255), font=f_em)
    except:
        draw.text((285, 255), "S", fill=(255, 255, 255))

    # Certificate title
    try:
        f_ct = font(30, True)
        f_cd = font(16, False)
        f_cn = font(18, False)

        draw.text((300, 135), title, fill=(255, 255, 255), font=f_ct,
                  anchor="mt" if hasattr(draw, 'textbbox') else None)

        # Description text
        lines = desc.split('\n')
        for i, line in enumerate(lines):
            draw.text((300, 380 + i * 35), line.strip(), fill=(80, 80, 80), font=f_cn,
                      anchor="mt" if hasattr(draw, 'textbbox') else None)

        # Official text
        draw.text((300, 520), "特发此证，以资证明", fill=(100, 100, 100), font=f_cn)
        draw.text((300, 600), "孙氏集团", fill=accent, font=font(24, True))
        draw.text((300, 650), "2026年6月", fill=(120, 120, 120), font=f_cd)

        # Seal
        draw.ellipse([440, 560, 560, 680], outline=(200, 50, 50), width=3)
        draw.text((500, 610), "孙氏集团", fill=(200, 50, 50), font=font(14))
    except Exception as e:
        print(f"  Font fallback for cert: {e}")

    img.save(os.path.join(BASE_DIR, "honor", filename), quality=90)
    print(f"  -> images/honor/{filename}")

print("\n✅ 全部配图生成完成！")
print(f"   输出目录: {BASE_DIR}")
