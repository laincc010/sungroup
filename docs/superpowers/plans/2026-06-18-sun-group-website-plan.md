# 孙氏集团企业官网实施计划

> **执行方式:** 使用 superpowers:executing-plans 在本地按任务顺序实施。步骤使用 `- [ ]` checkbox 语法跟踪。

**目标:** 构建孙氏集团单页企业官网，包含 10 大模块 + 导航 + 页脚，深邃暗金彩虹配色，全端响应式。

**架构:** 纯静态 HTML5 单页，Bootstrap 5.3 栅格布局，CSS Variables 管理彩虹色系统，AOS + Swiper + 原生 JS 驱动动效。

**技术栈:** HTML5, CSS3, Bootstrap 5.3, Font Awesome 6, Swiper.js, AOS.js, 原生 ES6 JavaScript

## 全局约束

- 所有 CDN 资源从 jsdelivr 加载
- 彩虹色仅作点缀，深色基底为主
- 占位图片用 CSS 渐变 / SVG 生成，无版权风险
- 字体族：Microsoft YaHei, Source Han Sans SC, Roboto, sans-serif
- 兼容 Chrome 90+, Edge 90+, Firefox 88+, Safari 14+
- 单页结构，所有 section 在 index.html 中

---

### Task 1: 项目脚手架 + HTML 骨架

**文件:**
- Create: `index.html`
- Create: `css/style.css`
- Create: `css/responsive.css`
- Create: `js/main.js`
- Create: `README.md`

**产出:** 可打开的空白页面，CDN 全部加载成功，文件骨架就位

- [ ] **Step 1: 创建 index.html 完整骨架**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="孙氏集团 - 国际物流与贸易综合服务商。提供海运、空运、陆运、仓储、跨境电商物流一站式解决方案。链接全球，物流天下。">
  <meta name="keywords" content="孙氏集团,国际物流,贸易,海运,空运,仓储,跨境电商物流,供应链">
  <title>孙氏集团 | 国际物流与贸易综合服务商</title>

  <!-- Bootstrap 5.3 CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <!-- Font Awesome 6 -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.5.1/css/all.min.css">
  <!-- Swiper CSS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css">
  <!-- AOS CSS -->
  <link href="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.css" rel="stylesheet">

  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/responsive.css">
  <link rel="icon" href="images/favicon.ico" type="image/x-icon">
</head>
<body>

  <!-- Navigation -->
  <nav id="navbar">...</nav>

  <!-- Hero Banner -->
  <section id="home">...</section>

  <!-- About -->
  <section id="about">...</section>

  <!-- Products -->
  <section id="products">...</section>

  <!-- Data Dashboard -->
  <section id="stats">...</section>

  <!-- Cases -->
  <section id="cases">...</section>

  <!-- News -->
  <section id="news">...</section>

  <!-- Honor -->
  <section id="honor">...</section>

  <!-- Recruitment -->
  <section id="recruit">...</section>

  <!-- Reviews -->
  <section id="reviews">...</section>

  <!-- Contact -->
  <section id="contact">...</section>

  <!-- Footer -->
  <footer id="footer">...</footer>

  <!-- Floating Toolbar -->
  <div id="floating-toolbar">...</div>

  <!-- Bootstrap JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  <!-- Swiper JS -->
  <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
  <!-- AOS JS -->
  <script src="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.js"></script>

  <script src="js/main.js"></script>
</body>
</html>
```

- [ ] **Step 2: 创建 CSS 变量基础文件**

`css/style.css`:
```css
/* ============================================
   孙氏集团企业官网 - 主样式表
   设计: 深邃暗金 + 彩虹渐变
   ============================================ */

/* --- CSS Variables --- */
:root {
  /* Rainbow Accent Colors */
  --primary:        #FF6B35;
  --secondary:      #FFD700;
  --accent-green:   #00D2A0;
  --accent-blue:    #4A90D9;
  --accent-purple:  #7B4FBF;
  --accent-rose:    #E91E7B;

  /* Dark Base */
  --bg-primary:     #0A0E17;
  --bg-secondary:   #111827;
  --bg-tertiary:    #1A1F2E;
  --bg-glass:       rgba(255, 255, 255, 0.04);

  /* Text */
  --text-primary:   #FFFFFF;
  --text-secondary: #B0B8C8;
  --text-muted:     #6B7280;

  /* Gradients */
  --gradient-rainbow: linear-gradient(90deg,
    #FF6B35, #FFD700, #00D2A0, #4A90D9, #7B4FBF, #E91E7B);
  --gradient-dark: linear-gradient(180deg, #0A0E17 0%, #111827 100%);

  /* Spacing */
  --section-padding: 100px 0;
  --container-max: 1320px;

  /* Border Radius */
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 20px;

  /* Transitions */
  --transition-fast: 0.2s ease;
  --transition-smooth: 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

/* --- Reset & Base --- */
* { margin: 0; padding: 0; box-sizing: border-box; }

html {
  scroll-behavior: smooth;
  scroll-padding-top: 80px;
}

body {
  font-family: "Microsoft YaHei", "Source Han Sans SC", "Roboto", sans-serif;
  background-color: var(--bg-primary);
  color: var(--text-secondary);
  line-height: 1.6;
  overflow-x: hidden;
}

/* --- Utility Classes --- */
.section-padding { padding: var(--section-padding); }
.bg-primary-dark { background-color: var(--bg-primary); }
.bg-secondary-dark { background-color: var(--bg-secondary); }
.bg-tertiary-dark { background-color: var(--bg-tertiary); }
.text-primary { color: var(--text-primary); }
.text-secondary { color: var(--text-secondary); }
.text-muted { color: var(--text-muted); }

.rainbow-divider {
  height: 2px;
  background: var(--gradient-rainbow);
  border: none;
  opacity: 0.6;
}

.container-custom {
  max-width: var(--container-max);
  margin: 0 auto;
  padding: 0 15px;
}

.section-title {
  font-size: 2.25rem;
  font-weight: 600;
  color: var(--text-primary);
  text-align: center;
  margin-bottom: 15px;
  position: relative;
}

.section-subtitle {
  font-size: 1rem;
  color: var(--text-muted);
  text-align: center;
  margin-bottom: 50px;
  letter-spacing: 2px;
}

.section-title::after {
  content: '';
  display: block;
  width: 60px;
  height: 3px;
  background: var(--gradient-rainbow);
  margin: 15px auto 0;
  border-radius: 2px;
}

/* Scrollbar */
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: var(--bg-primary); }
::-webkit-scrollbar-thumb { background: var(--bg-tertiary); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: var(--primary); }
```

- [ ] **Step 3: 创建空白的 responsive.css 和 main.js**

`css/responsive.css`:
```css
/* ============================================
   响应式适配样式
   ============================================ */
```

`js/main.js`:
```js
/**
 * 孙氏集团企业官网 - 主脚本
 * 导航、动画、计数器、灯箱、表单等功能
 */
'use strict';

// AOS 初始化
document.addEventListener('DOMContentLoaded', function() {
  AOS.init({
    duration: 800,
    easing: 'ease-out',
    once: true,
    offset: 100
  });
});
```

- [ ] **Step 4: 创建 README.md**

```markdown
# 孙氏集团企业官网

## 快速开始
直接用浏览器打开 `index.html` 即可预览。

## 修改内容
- **公司名称**: 全局搜索 `孙氏集团` 替换
- **联系电话**: 搜索 `400-888-XXXX` 替换
- **地址**: 搜索 `上海市浦东新区` 替换
- **图片**: 替换 `images/` 目录下对应图片

## 文件结构
- index.html - 主页面
- css/style.css - 核心样式
- css/responsive.css - 响应式
- js/main.js - 交互脚本
- images/ - 图片素材
```

- [ ] **Step 5: 提交**

```bash
git add -A && git commit -m "feat: project scaffolding with CDN setup and CSS variables"
```

---

### Task 2: 导航栏

**文件:**
- Modify: `index.html` (nav 部分)
- Modify: `css/style.css` (追加导航样式)
- Modify: `js/main.js` (追加导航逻辑)

- [ ] **Step 1: 写入导航栏 HTML**

`index.html` 中 `<nav id="navbar">...</nav>` 替换为:
```html
<nav id="navbar" class="navbar navbar-expand-lg fixed-top">
  <div class="container-custom">
    <a class="navbar-brand" href="#home">
      <span class="brand-text">SUN GROUP</span>
      <span class="brand-cn">孙氏集团</span>
    </a>
    <button class="navbar-toggler" type="button" id="navToggle" aria-label="导航菜单">
      <span class="toggler-bar"></span>
      <span class="toggler-bar"></span>
      <span class="toggler-bar"></span>
    </button>
    <div class="collapse navbar-collapse" id="navMenu">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item"><a class="nav-link active" href="#home">首页</a></li>
        <li class="nav-item"><a class="nav-link" href="#about">关于我们</a></li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">
            业务中心
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#products">国际海运</a></li>
            <li><a class="dropdown-item" href="#products">航空货运</a></li>
            <li><a class="dropdown-item" href="#products">陆运物流</a></li>
            <li><a class="dropdown-item" href="#products">仓储配送</a></li>
            <li><a class="dropdown-item" href="#products">跨境电商</a></li>
            <li><a class="dropdown-item" href="#products">供应链管理</a></li>
          </ul>
        </li>
        <li class="nav-item"><a class="nav-link" href="#cases">案例展示</a></li>
        <li class="nav-item"><a class="nav-link" href="#news">新闻资讯</a></li>
        <li class="nav-item"><a class="nav-link" href="#honor">荣誉资质</a></li>
        <li class="nav-item"><a class="nav-link" href="#contact">联系我们</a></li>
      </ul>
    </div>
  </div>
  <div class="navbar-rainbow-line"></div>
</nav>
```

- [ ] **Step 2: 写入导航栏 CSS**

追加到 `css/style.css`:
```css
/* ============================================
   Navigation
   ============================================ */
#navbar {
  background: rgba(10, 14, 23, 0.85);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  padding: 15px 0;
  transition: var(--transition-smooth);
  z-index: 1000;
}

#navbar.scrolled {
  padding: 10px 0;
  background: rgba(10, 14, 23, 0.95);
}

.navbar-rainbow-line {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: var(--gradient-rainbow);
  opacity: 0;
  transition: opacity 0.4s ease;
}

#navbar.scrolled .navbar-rainbow-line {
  opacity: 1;
}

.navbar-brand {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
}

.brand-text {
  font-family: "Roboto", sans-serif;
  font-size: 1.4rem;
  font-weight: 700;
  letter-spacing: 3px;
  background: var(--gradient-rainbow);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.brand-cn {
  font-size: 0.9rem;
  color: var(--text-secondary);
  letter-spacing: 4px;
  padding-left: 12px;
  border-left: 1px solid rgba(255, 255, 255, 0.2);
}

.nav-link {
  color: var(--text-secondary) !important;
  font-size: 0.9rem;
  padding: 8px 16px !important;
  transition: var(--transition-fast);
  position: relative;
}

.nav-link:hover,
.nav-link.active {
  color: var(--primary) !important;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 0;
  height: 2px;
  background: var(--primary);
  transition: width 0.3s ease;
}

.nav-link:hover::after,
.nav-link.active::after {
  width: 60%;
}

/* Dropdown */
.dropdown-menu {
  background: rgba(17, 24, 39, 0.95);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: var(--radius-sm);
  padding: 8px 0;
}

.dropdown-item {
  color: var(--text-secondary);
  font-size: 0.85rem;
  padding: 8px 20px;
  transition: var(--transition-fast);
}

.dropdown-item:hover {
  background: rgba(255, 107, 53, 0.1);
  color: var(--primary);
}

/* Toggler */
.navbar-toggler {
  border: none;
  padding: 0;
  width: 30px;
  height: 24px;
  position: relative;
  background: none;
  cursor: pointer;
}

.navbar-toggler:focus {
  box-shadow: none;
}

.toggler-bar {
  display: block;
  width: 100%;
  height: 2px;
  background: var(--text-primary);
  position: absolute;
  transition: var(--transition-smooth);
}

.toggler-bar:nth-child(1) { top: 0; }
.toggler-bar:nth-child(2) { top: 11px; }
.toggler-bar:nth-child(3) { top: 22px; }

.navbar-toggler.active .toggler-bar:nth-child(1) {
  top: 11px;
  transform: rotate(45deg);
}
.navbar-toggler.active .toggler-bar:nth-child(2) {
  opacity: 0;
}
.navbar-toggler.active .toggler-bar:nth-child(3) {
  top: 11px;
  transform: rotate(-45deg);
}
```

- [ ] **Step 3: 写入导航栏 JS**

追加到 `js/main.js`:
```js
// ============================================
// Navigation
// ============================================
const navbar = document.getElementById('navbar');
const navToggle = document.getElementById('navToggle');
const navLinks = document.querySelectorAll('.nav-link');

// Scroll effect
window.addEventListener('scroll', function() {
  if (window.scrollY > 50) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
});

// Mobile toggle
navToggle.addEventListener('click', function() {
  this.classList.toggle('active');
});

// Active link on scroll
window.addEventListener('scroll', function() {
  const sections = document.querySelectorAll('section[id]');
  let current = '';
  sections.forEach(section => {
    const sectionTop = section.offsetTop - 100;
    if (window.scrollY >= sectionTop) {
      current = section.getAttribute('id');
    }
  });
  navLinks.forEach(link => {
    link.classList.remove('active');
    if (link.getAttribute('href') === '#' + current) {
      link.classList.add('active');
    }
  });
});

// Smooth close mobile menu on link click
navLinks.forEach(link => {
  link.addEventListener('click', () => {
    if (navToggle.classList.contains('active')) {
      navToggle.click();
    }
  });
});
```

- [ ] **Step 4: 提交**

```bash
git add -A && git commit -m "feat: add navigation bar with scroll effect and mobile toggle"
```

---

### Task 3: Hero Banner 全屏轮播

**文件:**
- Modify: `index.html` (hero section)
- Modify: `css/style.css` (hero 样式)
- Modify: `js/main.js` (Swiper 初始化)

- [ ] **Step 1: Hero HTML**

```html
<section id="home" class="hero-section">
  <div class="swiper hero-swiper">
    <div class="swiper-wrapper">

      <!-- Slide 1 -->
      <div class="swiper-slide hero-slide slide-1">
        <div class="hero-overlay"></div>
        <div class="hero-content" data-aos="fade-up">
          <p class="hero-tagline">GLOBAL LOGISTICS LEADER</p>
          <h1 class="hero-title">链接全球 <span class="highlight">物流天下</span></h1>
          <p class="hero-desc">孙氏集团 · 国际物流与贸易综合服务商<br>20年深耕，服务覆盖全球60+国家</p>
          <div class="hero-btns">
            <a href="#contact" class="btn btn-primary-custom">立即咨询 <i class="fas fa-arrow-right"></i></a>
            <a href="#about" class="btn btn-outline-custom">了解更多</a>
          </div>
        </div>
      </div>

      <!-- Slide 2 -->
      <div class="swiper-slide hero-slide slide-2">
        <div class="hero-overlay"></div>
        <div class="hero-content">
          <p class="hero-tagline">SMART SUPPLY CHAIN</p>
          <h1 class="hero-title">智慧供应链 <span class="highlight">解决方案</span></h1>
          <p class="hero-desc">从港口到门，从仓储到配送，一站式全链路服务</p>
          <div class="hero-btns">
            <a href="#products" class="btn btn-primary-custom">探索业务 <i class="fas fa-arrow-right"></i></a>
            <a href="#cases" class="btn btn-outline-custom">查看案例</a>
          </div>
        </div>
      </div>

      <!-- Slide 3 -->
      <div class="swiper-slide hero-slide slide-3">
        <div class="hero-overlay"></div>
        <div class="hero-content">
          <p class="hero-tagline">TRUSTED BY 5000+ CLIENTS</p>
          <h1 class="hero-title">信赖之选 <span class="highlight">共赢未来</span></h1>
          <p class="hero-desc">5000+企业客户的选择，年吞吐量超百万吨</p>
          <div class="hero-btns">
            <a href="#contact" class="btn btn-primary-custom">合作洽谈 <i class="fas fa-arrow-right"></i></a>
            <a href="#about" class="btn btn-outline-custom">集团实力</a>
          </div>
        </div>
      </div>

    </div>
    <!-- Pagination -->
    <div class="swiper-pagination"></div>
    <!-- Navigation arrows -->
    <div class="swiper-button-prev"></div>
    <div class="swiper-button-next"></div>
  </div>
  <!-- Scroll indicator -->
  <div class="scroll-indicator">
    <span>向下滚动</span>
    <div class="scroll-mouse">
      <div class="scroll-wheel"></div>
    </div>
  </div>
</section>
```

- [ ] **Step 2: Hero CSS**

追加到 `css/style.css`:
```css
/* ============================================
   Hero Section
   ============================================ */
.hero-section {
  position: relative;
  width: 100%;
  height: 100vh;
  min-height: 600px;
  overflow: hidden;
}

.hero-swiper,
.hero-slide {
  width: 100%;
  height: 100%;
}

.hero-slide {
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: center;
}

.slide-1 {
  background: linear-gradient(135deg, #0A0E17 0%, #1a1040 30%, #0a1a30 60%, #0A0E17 100%);
}
.slide-2 {
  background: linear-gradient(135deg, #0A0E17 0%, #1a1525 30%, #0f1a2e 60%, #0A0E17 100%);
}
.slide-3 {
  background: linear-gradient(135deg, #0A0E17 0%, #1a0f25 30%, #0d1a28 60%, #0A0E17 100%);
}

/* Animated rainbow accent on hero */
.hero-slide::before {
  content: '';
  position: absolute;
  top: -50%;
  right: -30%;
  width: 800px;
  height: 800px;
  background: radial-gradient(circle,
    rgba(255, 107, 53, 0.15) 0%,
    rgba(255, 215, 0, 0.08) 30%,
    rgba(74, 144, 217, 0.05) 60%,
    transparent 100%);
  animation: heroGlow 8s ease-in-out infinite alternate;
  pointer-events: none;
}

.hero-slide::after {
  content: '';
  position: absolute;
  bottom: -30%;
  left: -20%;
  width: 600px;
  height: 600px;
  background: radial-gradient(circle,
    rgba(123, 79, 191, 0.12) 0%,
    rgba(233, 30, 123, 0.06) 40%,
    transparent 100%);
  animation: heroGlow 6s ease-in-out 2s infinite alternate;
  pointer-events: none;
}

@keyframes heroGlow {
  0% { transform: scale(1) translate(0, 0); opacity: 0.6; }
  100% { transform: scale(1.3) translate(-5%, 5%); opacity: 1; }
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg,
    rgba(10, 14, 23, 0.3) 0%,
    rgba(10, 14, 23, 0.5) 50%,
    rgba(10, 14, 23, 0.9) 100%);
  z-index: 1;
}

.hero-content {
  position: relative;
  z-index: 2;
  text-align: center;
  padding: 0 20px;
  max-width: 800px;
}

.hero-tagline {
  font-family: "Roboto", sans-serif;
  font-size: 0.85rem;
  letter-spacing: 6px;
  color: var(--primary);
  margin-bottom: 20px;
  animation: fadeInUp 1s ease 0.2s both;
}

.hero-title {
  font-size: 3.5rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 20px;
  line-height: 1.3;
  animation: fadeInUp 1s ease 0.4s both;
}

.hero-title .highlight {
  background: var(--gradient-rainbow);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-desc {
  font-size: 1.1rem;
  color: var(--text-secondary);
  margin-bottom: 35px;
  line-height: 1.8;
  animation: fadeInUp 1s ease 0.6s both;
}

.hero-btns {
  display: flex;
  gap: 20px;
  justify-content: center;
  flex-wrap: wrap;
  animation: fadeInUp 1s ease 0.8s both;
}

.btn-primary-custom {
  background: var(--primary);
  color: #fff;
  padding: 14px 36px;
  border-radius: 50px;
  font-size: 1rem;
  font-weight: 500;
  text-decoration: none;
  border: none;
  transition: var(--transition-smooth);
  display: inline-flex;
  align-items: center;
  gap: 8px;
}

.btn-primary-custom:hover {
  background: #ff8255;
  transform: translateY(-2px);
  box-shadow: 0 10px 30px rgba(255, 107, 53, 0.3);
  color: #fff;
}

.btn-outline-custom {
  background: transparent;
  color: #fff;
  padding: 14px 36px;
  border-radius: 50px;
  font-size: 1rem;
  font-weight: 500;
  text-decoration: none;
  border: 1.5px solid rgba(255, 255, 255, 0.3);
  transition: var(--transition-smooth);
}

.btn-outline-custom:hover {
  border-color: #fff;
  background: rgba(255, 255, 255, 0.05);
  color: #fff;
}

/* Swiper overrides */
.hero-swiper .swiper-pagination-bullet {
  width: 12px;
  height: 12px;
  background: rgba(255, 255, 255, 0.4);
  opacity: 1;
}

.hero-swiper .swiper-pagination-bullet-active {
  background: var(--primary);
}

.hero-swiper .swiper-button-prev,
.hero-swiper .swiper-button-next {
  color: rgba(255, 255, 255, 0.6);
  transition: var(--transition-fast);
}

.hero-swiper .swiper-button-prev:hover,
.hero-swiper .swiper-button-next:hover {
  color: var(--primary);
}

/* Scroll indicator */
.scroll-indicator {
  position: absolute;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 3;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  color: var(--text-muted);
  font-size: 0.75rem;
  letter-spacing: 2px;
}

.scroll-mouse {
  width: 24px;
  height: 38px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-radius: 12px;
  display: flex;
  justify-content: center;
}

.scroll-wheel {
  width: 4px;
  height: 8px;
  background: var(--primary);
  border-radius: 2px;
  margin-top: 6px;
  animation: scrollWheel 1.5s ease-in-out infinite;
}

@keyframes scrollWheel {
  0% { transform: translateY(0); opacity: 1; }
  100% { transform: translateY(12px); opacity: 0; }
}

@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}
```

- [ ] **Step 3: Hero JS**

追加到 `js/main.js`:
```js
// ============================================
// Hero Swiper
// ============================================
const heroSwiper = new Swiper('.hero-swiper', {
  loop: true,
  autoplay: {
    delay: 5000,
    disableOnInteraction: false,
  },
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  effect: 'fade',
  fadeEffect: { crossFade: true },
  speed: 1000,
});
```

- [ ] **Step 4: 提交**

```bash
git add -A && git commit -m "feat: add hero banner with Swiper carousel and animated gradients"
```

---

### Task 4: 关于我们 Section

**文件:**
- Modify: `index.html` (about section)
- Modify: `css/style.css` (about 样式)

- [ ] **Step 1: About HTML**

```html
<section id="about" class="section-padding bg-primary-dark">
  <div class="container-custom">
    <h2 class="section-title" data-aos="fade-up">关于孙氏集团</h2>
    <p class="section-subtitle" data-aos="fade-up" data-aos-delay="100">ABOUT SUN GROUP</p>

    <div class="row align-items-center mb-5">
      <div class="col-lg-6" data-aos="fade-right">
        <div class="about-image-wrapper">
          <div class="about-image-placeholder">
            <i class="fas fa-building"></i>
            <span>集团总部</span>
          </div>
          <div class="about-image-glow"></div>
        </div>
      </div>
      <div class="col-lg-6" data-aos="fade-left">
        <h3 class="about-heading">立足中国 <span class="highlight">通达全球</span></h3>
        <p class="about-text">
          孙氏集团成立于2005年，总部位于上海浦东新区，是一家集国际海运、航空货运、
          陆运物流、仓储配送、跨境电商物流及供应链管理于一体的综合性贸易物流企业。
        </p>
        <p class="about-text">
          集团现有员工2000余人，在全球设有30+分支机构和服务网点，
          业务覆盖欧洲、北美、东南亚、中东、非洲等60多个国家和地区，
          年货物吞吐量超百万吨，服务客户超5000家。
        </p>
        <div class="about-stats-mini">
          <div class="stat-mini-item">
            <span class="stat-mini-num">20+</span>
            <span class="stat-mini-label">年行业经验</span>
          </div>
          <div class="stat-mini-item">
            <span class="stat-mini-num">30+</span>
            <span class="stat-mini-label">全球分支机构</span>
          </div>
          <div class="stat-mini-item">
            <span class="stat-mini-num">60+</span>
            <span class="stat-mini-label">覆盖国家</span>
          </div>
        </div>
      </div>
    </div>

    <!-- 企业文化卡片 -->
    <div class="row g-4 mt-4">
      <div class="col-md-4" data-aos="fade-up" data-aos-delay="0">
        <div class="culture-card">
          <div class="culture-icon" style="--accent: var(--primary)"><i class="fas fa-eye"></i></div>
          <h4>企业愿景</h4>
          <p>成为全球领先的智慧物流与供应链服务商，让世界贸易更高效</p>
        </div>
      </div>
      <div class="col-md-4" data-aos="fade-up" data-aos-delay="100">
        <div class="culture-card">
          <div class="culture-icon" style="--accent: var(--secondary)"><i class="fas fa-bullseye"></i></div>
          <h4>企业使命</h4>
          <p>以专业物流服务链接全球商机，为客户创造价值，为员工成就梦想</p>
        </div>
      </div>
      <div class="col-md-4" data-aos="fade-up" data-aos-delay="200">
        <div class="culture-card">
          <div class="culture-icon" style="--accent: var(--accent-green)"><i class="fas fa-handshake"></i></div>
          <h4>核心价值</h4>
          <p>诚信为本、效率为先、创新驱动、合作共赢</p>
        </div>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 2: About CSS**

追加到 `css/style.css`:
```css
/* ============================================
   About Section
   ============================================ */
.about-image-wrapper {
  position: relative;
  width: 100%;
}

.about-image-placeholder {
  width: 100%;
  height: 400px;
  background: linear-gradient(135deg, var(--bg-tertiary), #1a2740);
  border-radius: var(--radius-lg);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 15px;
  border: 1px solid rgba(255, 255, 255, 0.06);
  position: relative;
  z-index: 1;
}

.about-image-placeholder i {
  font-size: 3rem;
  color: var(--primary);
  opacity: 0.5;
}

.about-image-placeholder span {
  color: var(--text-muted);
  letter-spacing: 4px;
  font-size: 0.9rem;
}

.about-image-glow {
  position: absolute;
  bottom: -20px;
  left: 20px;
  right: -20px;
  height: 60%;
  background: var(--gradient-rainbow);
  border-radius: var(--radius-lg);
  opacity: 0.08;
  filter: blur(40px);
  z-index: 0;
}

.about-heading {
  font-size: 1.8rem;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 20px;
}

.about-heading .highlight {
  background: var(--gradient-rainbow);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.about-text {
  color: var(--text-secondary);
  line-height: 1.8;
  margin-bottom: 15px;
}

.about-stats-mini {
  display: flex;
  gap: 40px;
  margin-top: 30px;
}

.stat-mini-item {
  display: flex;
  flex-direction: column;
}

.stat-mini-num {
  font-size: 2rem;
  font-weight: 700;
  background: var(--gradient-rainbow);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.stat-mini-label {
  font-size: 0.8rem;
  color: var(--text-muted);
}

/* Culture Cards */
.culture-card {
  background: var(--bg-glass);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: var(--radius-md);
  padding: 40px 30px;
  text-align: center;
  transition: var(--transition-smooth);
}

.culture-card:hover {
  transform: translateY(-8px);
  border-color: rgba(255, 255, 255, 0.12);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3),
              0 0 0 1px var(--accent, var(--primary)) inset;
}

.culture-icon {
  width: 70px;
  height: 70px;
  margin: 0 auto 20px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.04);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  color: var(--accent, var(--primary));
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.culture-card h4 {
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 10px;
}

.culture-card p {
  font-size: 0.9rem;
  color: var(--text-secondary);
  line-height: 1.6;
}
```

- [ ] **Step 3: 提交**

```bash
git add -A && git commit -m "feat: add about section with culture cards"
```

---

### Task 5: 业务中心 Section

**文件:**
- Modify: `index.html` (products section)
- Modify: `css/style.css` (products 样式)

- [ ] **Step 1: Products HTML**

```html
<section id="products" class="section-padding bg-secondary-dark">
  <div class="container-custom">
    <h2 class="section-title" data-aos="fade-up">业务中心</h2>
    <p class="section-subtitle" data-aos="fade-up" data-aos-delay="100">OUR SERVICES</p>

    <div class="row g-4">
      <div class="col-lg-4 col-md-6" data-aos="fade-up" data-aos-delay="0">
        <div class="service-card">
          <div class="service-icon" style="--accent: var(--accent-blue)">
            <i class="fas fa-ship"></i>
          </div>
          <h4>国际海运</h4>
          <p>覆盖全球主要港口，提供整箱FCL、拼箱LCL、散杂货运输服务，与马士基、中远等船东深度合作。</p>
          <a href="#contact" class="service-link">了解更多 <i class="fas fa-chevron-right"></i></a>
          <div class="service-card-glow"></div>
        </div>
      </div>
      <div class="col-lg-4 col-md-6" data-aos="fade-up" data-aos-delay="100">
        <div class="service-card">
          <div class="service-icon" style="--accent: var(--accent-rose)">
            <i class="fas fa-plane"></i>
          </div>
          <h4>航空货运</h4>
          <p>签约国航、东航、南航等主要航司，提供直飞、中转、包机等灵活方案，确保货物快速抵达。</p>
          <a href="#contact" class="service-link">了解更多 <i class="fas fa-chevron-right"></i></a>
          <div class="service-card-glow"></div>
        </div>
      </div>
      <div class="col-lg-4 col-md-6" data-aos="fade-up" data-aos-delay="200">
        <div class="service-card">
          <div class="service-icon" style="--accent: var(--primary)">
            <i class="fas fa-truck"></i>
          </div>
          <h4>陆运物流</h4>
          <p>自有车队+合作运力，覆盖全国干支线运输、城市配送、中欧班列、跨境卡车等陆路运输服务。</p>
          <a href="#contact" class="service-link">了解更多 <i class="fas fa-chevron-right"></i></a>
          <div class="service-card-glow"></div>
        </div>
      </div>
      <div class="col-lg-4 col-md-6" data-aos="fade-up" data-aos-delay="0">
        <div class="service-card">
          <div class="service-icon" style="--accent: var(--accent-purple)">
            <i class="fas fa-warehouse"></i>
          </div>
          <h4>仓储配送</h4>
          <p>全国布局现代化仓储中心50+万㎡，配备WMS智能管理系统，提供分拣、包装、配送一体化服务。</p>
          <a href="#contact" class="service-link">了解更多 <i class="fas fa-chevron-right"></i></a>
          <div class="service-card-glow"></div>
        </div>
      </div>
      <div class="col-lg-4 col-md-6" data-aos="fade-up" data-aos-delay="100">
        <div class="service-card">
          <div class="service-icon" style="--accent: var(--accent-green)">
            <i class="fas fa-globe"></i>
          </div>
          <h4>跨境电商物流</h4>
          <p>FBA头程、海外仓一件代发、国际小包专线，为跨境电商卖家提供全链路物流解决方案。</p>
          <a href="#contact" class="service-link">了解更多 <i class="fas fa-chevron-right"></i></a>
          <div class="service-card-glow"></div>
        </div>
      </div>
      <div class="col-lg-4 col-md-6" data-aos="fade-up" data-aos-delay="200">
        <div class="service-card">
          <div class="service-icon" style="--accent: var(--secondary)">
            <i class="fas fa-diagram-project"></i>
          </div>
          <h4>供应链管理</h4>
          <p>为企业提供端到端供应链优化方案，涵盖采购物流、VMI库存管理、分销配送、逆向物流等。</p>
          <a href="#contact" class="service-link">了解更多 <i class="fas fa-chevron-right"></i></a>
          <div class="service-card-glow"></div>
        </div>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 2: Products CSS**

追加到 `css/style.css`:
```css
/* ============================================
   Services / Products Section
   ============================================ */
.service-card {
  background: var(--bg-glass);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: var(--radius-lg);
  padding: 40px 30px;
  position: relative;
  overflow: hidden;
  transition: var(--transition-smooth);
  height: 100%;
}

.service-card:hover {
  transform: translateY(-8px) scale(1.02);
  border-color: rgba(255, 255, 255, 0.12);
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4),
              0 0 60px rgba(var(--accent-r, 255), var(--accent-g, 107), var(--accent-b, 53), 0.08);
}

.service-icon {
  width: 65px;
  height: 65px;
  border-radius: var(--radius-md);
  background: rgba(255, 255, 255, 0.03);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.6rem;
  color: var(--accent, var(--primary));
  margin-bottom: 20px;
  border: 1px solid rgba(255, 255, 255, 0.06);
  transition: var(--transition-smooth);
}

.service-card:hover .service-icon {
  background: var(--accent, var(--primary));
  color: #fff;
  box-shadow: 0 0 30px rgba(var(--accent-r, 255), var(--accent-g, 107), var(--accent-b, 53), 0.3);
}

.service-card h4 {
  font-size: 1.2rem;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 12px;
}

.service-card p {
  font-size: 0.9rem;
  color: var(--text-secondary);
  line-height: 1.7;
  margin-bottom: 20px;
}

.service-link {
  color: var(--accent, var(--primary));
  text-decoration: none;
  font-size: 0.85rem;
  font-weight: 500;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: gap 0.3s ease;
}

.service-link:hover {
  gap: 12px;
  color: var(--accent, var(--primary));
}

.service-card-glow {
  position: absolute;
  top: -50%;
  right: -50%;
  width: 200px;
  height: 200px;
  background: radial-gradient(circle,
    var(--accent, var(--primary)) 0%,
    transparent 70%);
  opacity: 0;
  transition: opacity 0.5s ease;
  pointer-events: none;
}

.service-card:hover .service-card-glow {
  opacity: 0.06;
}
```

- [ ] **Step 3: 提交**

```bash
git add -A && git commit -m "feat: add products/services section with glassmorphism cards"
```

---

### Task 6: 数据看板 + 数字滚动

**文件:**
- Modify: `index.html` (stats section)
- Modify: `css/style.css` (stats 样式)
- Modify: `js/main.js` (counter 逻辑)

- [ ] **Step 1: Stats HTML**

```html
<section id="stats" class="stats-section">
  <div class="stats-overlay"></div>
  <div class="container-custom">
    <div class="row g-4">
      <div class="col-lg-3 col-6" data-aos="fade-up" data-aos-delay="0">
        <div class="stat-card">
          <div class="stat-icon"><i class="fas fa-calendar-check"></i></div>
          <div class="stat-number" data-target="20">0</div>
          <div class="stat-suffix">年</div>
          <div class="stat-label">行业深耕</div>
          <div class="stat-bar" style="--bar-color: var(--primary)"></div>
        </div>
      </div>
      <div class="col-lg-3 col-6" data-aos="fade-up" data-aos-delay="100">
        <div class="stat-card">
          <div class="stat-icon"><i class="fas fa-users"></i></div>
          <div class="stat-number" data-target="2000">0</div>
          <div class="stat-suffix">+</div>
          <div class="stat-label">专业员工</div>
          <div class="stat-bar" style="--bar-color: var(--secondary)"></div>
        </div>
      </div>
      <div class="col-lg-3 col-6" data-aos="fade-up" data-aos-delay="200">
        <div class="stat-card">
          <div class="stat-icon"><i class="fas fa-building"></i></div>
          <div class="stat-number" data-target="5000">0</div>
          <div class="stat-suffix">+</div>
          <div class="stat-label">合作客户</div>
          <div class="stat-bar" style="--bar-color: var(--accent-green)"></div>
        </div>
      </div>
      <div class="col-lg-3 col-6" data-aos="fade-up" data-aos-delay="300">
        <div class="stat-card">
          <div class="stat-icon"><i class="fas fa-earth-asia"></i></div>
          <div class="stat-number" data-target="60">0</div>
          <div class="stat-suffix">+</div>
          <div class="stat-label">覆盖国家</div>
          <div class="stat-bar" style="--bar-color: var(--accent-blue)"></div>
        </div>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 2: Stats CSS**

追加到 `css/style.css`:
```css
/* ============================================
   Stats / Data Dashboard
   ============================================ */
.stats-section {
  position: relative;
  padding: 80px 0;
  background: linear-gradient(180deg, var(--bg-secondary) 0%, #0d111f 100%);
  overflow: hidden;
}

/* Animated background particles */
.stats-section::before {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  background:
    radial-gradient(circle at 20% 50%, rgba(255, 107, 53, 0.06) 0%, transparent 50%),
    radial-gradient(circle at 80% 50%, rgba(74, 144, 217, 0.06) 0%, transparent 50%);
  pointer-events: none;
}

.stat-card {
  text-align: center;
  padding: 40px 20px;
  position: relative;
  z-index: 1;
}

.stat-icon {
  font-size: 2rem;
  color: var(--primary);
  margin-bottom: 15px;
  opacity: 0.7;
}

.stat-number {
  font-size: 3.5rem;
  font-weight: 700;
  color: var(--secondary);
  display: inline;
  font-family: "Roboto", sans-serif;
}

.stat-suffix {
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--secondary);
  display: inline;
  margin-left: 2px;
}

.stat-label {
  display: block;
  font-size: 0.9rem;
  color: var(--text-muted);
  margin-top: 8px;
  letter-spacing: 3px;
}

.stat-bar {
  width: 60px;
  height: 3px;
  background: var(--bar-color, var(--primary));
  margin: 20px auto 0;
  border-radius: 2px;
  transition: width 1.5s ease 0.5s;
  width: 0;
}

.stat-bar.animated {
  width: 60px;
}
```

- [ ] **Step 3: Counter JS**

追加到 `js/main.js`:
```js
// ============================================
// Counter Animation
// ============================================
function animateCounters() {
  const counters = document.querySelectorAll('.stat-number');
  const bars = document.querySelectorAll('.stat-bar');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const counter = entry.target;
        const target = parseInt(counter.getAttribute('data-target'));
        const duration = 2000;
        const startTime = performance.now();

        function update(currentTime) {
          const elapsed = currentTime - startTime;
          const progress = Math.min(elapsed / duration, 1);
          // Ease out cubic
          const eased = 1 - Math.pow(1 - progress, 3);
          counter.textContent = Math.floor(eased * target);

          if (progress < 1) {
            requestAnimationFrame(update);
          } else {
            counter.textContent = target;
          }
        }

        requestAnimationFrame(update);
        observer.unobserve(counter);

        // Animate bars
        bars.forEach(bar => bar.classList.add('animated'));
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(counter => observer.observe(counter));
}

document.addEventListener('DOMContentLoaded', animateCounters);
```

- [ ] **Step 4: 提交**

```bash
git add -A && git commit -m "feat: add stats dashboard with animated counters"
```

---

### Task 7: 案例展示 + 灯箱

**文件:**
- Modify: `index.html` (cases section)
- Modify: `css/style.css` (cases + lightbox 样式)
- Modify: `js/main.js` (lightbox 逻辑)

- [ ] **Step 1: Cases HTML**

```html
<section id="cases" class="section-padding bg-primary-dark">
  <div class="container-custom">
    <h2 class="section-title" data-aos="fade-up">案例展示</h2>
    <p class="section-subtitle" data-aos="fade-up" data-aos-delay="100">CASE STUDIES</p>

    <div class="row g-4">
      <div class="col-lg-4 col-md-6" data-aos="fade-up" data-aos-delay="0">
        <div class="case-card" onclick="openLightbox(0)">
          <div class="case-thumb case-thumb-1">
            <div class="case-overlay"><span><i class="fas fa-search-plus"></i> 查看详情</span></div>
          </div>
          <div class="case-info">
            <span class="case-tag" style="--tag-color: var(--primary)">国际海运</span>
            <h4>某电子制造企业全球供应链项目</h4>
            <p>年运输量50万TEU，覆盖欧美亚30+目的港</p>
          </div>
        </div>
      </div>
      <div class="col-lg-4 col-md-6" data-aos="fade-up" data-aos-delay="100">
        <div class="case-card" onclick="openLightbox(1)">
          <div class="case-thumb case-thumb-2">
            <div class="case-overlay"><span><i class="fas fa-search-plus"></i> 查看详情</span></div>
          </div>
          <div class="case-info">
            <span class="case-tag" style="--tag-color: var(--accent-rose)">航空货运</span>
            <h4>汽车零部件紧急空运方案</h4>
            <p>48小时全球达，保障生产线零停工</p>
          </div>
        </div>
      </div>
      <div class="col-lg-4 col-md-6" data-aos="fade-up" data-aos-delay="200">
        <div class="case-card" onclick="openLightbox(2)">
          <div class="case-thumb case-thumb-3">
            <div class="case-overlay"><span><i class="fas fa-search-plus"></i> 查看详情</span></div>
          </div>
          <div class="case-info">
            <span class="case-tag" style="--tag-color: var(--accent-green)">跨境电商</span>
            <h4>头部电商平台东南亚物流专线</h4>
            <p>日均处理10万+订单，签收率达99.5%</p>
          </div>
        </div>
      </div>
      <div class="col-lg-4 col-md-6" data-aos="fade-up" data-aos-delay="0">
        <div class="case-card" onclick="openLightbox(3)">
          <div class="case-thumb case-thumb-4">
            <div class="case-overlay"><span><i class="fas fa-search-plus"></i> 查看详情</span></div>
          </div>
          <div class="case-info">
            <span class="case-tag" style="--tag-color: var(--accent-purple)">仓储配送</span>
            <h4>大型零售商全国仓储网络优化</h4>
            <p>5大区域仓，库存周转率提升40%</p>
          </div>
        </div>
      </div>
      <div class="col-lg-4 col-md-6" data-aos="fade-up" data-aos-delay="100">
        <div class="case-card" onclick="openLightbox(4)">
          <div class="case-thumb case-thumb-5">
            <div class="case-overlay"><span><i class="fas fa-search-plus"></i> 查看详情</span></div>
          </div>
          <div class="case-info">
            <span class="case-tag" style="--tag-color: var(--accent-blue)">供应链管理</span>
            <h4>大宗商品进口全链路服务</h4>
            <p>年进口量200万吨，关务时效缩短30%</p>
          </div>
        </div>
      </div>
      <div class="col-lg-4 col-md-6" data-aos="fade-up" data-aos-delay="200">
        <div class="case-card" onclick="openLightbox(5)">
          <div class="case-thumb case-thumb-6">
            <div class="case-overlay"><span><i class="fas fa-search-plus"></i> 查看详情</span></div>
          </div>
          <div class="case-info">
            <span class="case-tag" style="--tag-color: var(--secondary)">陆运物流</span>
            <h4>中欧班列常态化运输项目</h4>
            <p>月发运50+班列，中亚/欧洲全覆盖</p>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Lightbox -->
  <div id="lightbox" class="lightbox">
    <span class="lightbox-close" onclick="closeLightbox()">&times;</span>
    <button class="lightbox-prev" onclick="changeLightbox(-1)"><i class="fas fa-chevron-left"></i></button>
    <button class="lightbox-next" onclick="changeLightbox(1)"><i class="fas fa-chevron-right"></i></button>
    <div class="lightbox-content" id="lightboxContent"></div>
  </div>
</section>
```

- [ ] **Step 2: Cases + Lightbox CSS**

追加到 `css/style.css`:
```css
/* ============================================
   Case Studies
   ============================================ */
.case-card {
  background: var(--bg-glass);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: var(--radius-lg);
  overflow: hidden;
  cursor: pointer;
  transition: var(--transition-smooth);
}

.case-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
}

.case-thumb {
  height: 220px;
  position: relative;
  overflow: hidden;
}

.case-thumb-1 { background: linear-gradient(135deg, #1a2a40, #0d3b66); }
.case-thumb-2 { background: linear-gradient(135deg, #2a1a30, #4a1942); }
.case-thumb-3 { background: linear-gradient(135deg, #1a3025, #0d4a2e); }
.case-thumb-4 { background: linear-gradient(135deg, #2a1a35, #3d1a6e); }
.case-thumb-5 { background: linear-gradient(135deg, #1a2530, #1a3d5c); }
.case-thumb-6 { background: linear-gradient(135deg, #2a251a, #4a3d0d); }

.case-thumb::before {
  content: '\f0d1';
  font-family: 'Font Awesome 6 Free';
  font-weight: 900;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 3rem;
  color: rgba(255, 255, 255, 0.06);
}

.case-overlay {
  position: absolute;
  inset: 0;
  background: rgba(10, 14, 23, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: var(--transition-smooth);
}

.case-overlay span {
  color: #fff;
  font-size: 0.9rem;
  padding: 10px 24px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 50px;
}

.case-card:hover .case-overlay {
  opacity: 1;
}

.case-info {
  padding: 20px;
}

.case-tag {
  display: inline-block;
  font-size: 0.75rem;
  padding: 4px 12px;
  border-radius: 50px;
  background: rgba(var(--tag-r, 255), var(--tag-g, 107), var(--tag-b, 53), 0.1);
  color: var(--tag-color, var(--primary));
  margin-bottom: 10px;
  letter-spacing: 1px;
}

.case-info h4 {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 8px;
}

.case-info p {
  font-size: 0.85rem;
  color: var(--text-muted);
  margin-bottom: 0;
}

/* Lightbox */
.lightbox {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.95);
  z-index: 9999;
  align-items: center;
  justify-content: center;
}

.lightbox.active {
  display: flex;
}

.lightbox-close {
  position: absolute;
  top: 20px;
  right: 30px;
  font-size: 2.5rem;
  color: #fff;
  cursor: pointer;
  z-index: 10;
  transition: var(--transition-fast);
}

.lightbox-close:hover {
  color: var(--primary);
}

.lightbox-prev,
.lightbox-next {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(255, 255, 255, 0.1);
  border: none;
  color: #fff;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  font-size: 1.2rem;
  cursor: pointer;
  transition: var(--transition-fast);
  z-index: 10;
}

.lightbox-prev { left: 20px; }
.lightbox-next { right: 20px; }

.lightbox-prev:hover,
.lightbox-next:hover {
  background: var(--primary);
}

.lightbox-content {
  max-width: 800px;
  width: 90%;
  padding: 40px;
  text-align: center;
}

.lightbox-content h3 {
  font-size: 1.8rem;
  color: var(--text-primary);
  margin-bottom: 15px;
}

.lightbox-content p {
  color: var(--text-secondary);
  line-height: 1.8;
}
```

- [ ] **Step 3: Lightbox JS**

追加到 `js/main.js`:
```js
// ============================================
// Case Lightbox
// ============================================
const caseData = [
  { title: '某电子制造企业全球供应链项目', desc: '为国内Top3电子制造企业提供全球供应链解决方案，年运输量50万TEU，覆盖欧美亚30+目的港。提供门到门全程物流服务，含报关、保险、仓储一站式管理。项目实施后客户物流成本降低18%，运输时效提升25%。' },
  { title: '汽车零部件紧急空运方案', desc: '为某德系汽车品牌提供零部件全球紧急空运服务，48小时内从中国工厂直达全球生产线。全年365天×24小时响应，确保生产线零停工。已累计完成紧急运输任务3000+次，客户满意度100%。' },
  { title: '头部电商平台东南亚物流专线', desc: '为国内头部跨境电商平台提供东南亚六国专线物流服务，自建海外仓10万㎡+，系统对接API实现自动下单、轨迹追踪、异常预警。日均处理订单10万+，签收率高达99.5%，退货率低于行业平均60%。' },
  { title: '大型零售商全国仓储网络优化', desc: '为某上市零售企业重新设计全国仓储网络，设立5大区域中心仓、20个前置仓，部署WMS/TMS智能管理系统。库存周转率提升40%，配送时效从48小时缩短至12小时，仓配成本下降25%。' },
  { title: '大宗商品进口全链路服务', desc: '为多家大型贸易商提供铁矿石、煤炭、大豆等大宗商品进口全程物流服务，涵盖国际海运、港口卸货、报关报检、内陆运输。年进口量超200万吨，关务处理时效较行业平均水平快30%。' },
  { title: '中欧班列常态化运输项目', desc: '运营中欧班列专线，月发运50+班列，覆盖中亚五国、俄罗斯、波兰、德国等。提供整列/拼箱服务，运输时间仅为海运的1/3，成本仅为空运的1/5，为客户提供海运与空运之间的最佳选择。' },
];

let currentLightboxIndex = 0;

function openLightbox(index) {
  currentLightboxIndex = index;
  const data = caseData[index];
  document.getElementById('lightboxContent').innerHTML = `
    <span class="case-tag" style="--tag-color: var(--primary); margin: 0 auto 15px; display: inline-block;">案例详情</span>
    <h3>${data.title}</h3>
    <hr class="rainbow-divider" style="width: 60px; margin: 20px auto;">
    <p>${data.desc}</p>
  `;
  document.getElementById('lightbox').classList.add('active');
  document.body.style.overflow = 'hidden';
}

function closeLightbox() {
  document.getElementById('lightbox').classList.remove('active');
  document.body.style.overflow = '';
}

function changeLightbox(direction) {
  currentLightboxIndex = (currentLightboxIndex + direction + caseData.length) % caseData.length;
  openLightbox(currentLightboxIndex);
}

document.getElementById('lightbox').addEventListener('click', function(e) {
  if (e.target === this) closeLightbox();
});

document.addEventListener('keydown', function(e) {
  if (!document.getElementById('lightbox').classList.contains('active')) return;
  if (e.key === 'Escape') closeLightbox();
  if (e.key === 'ArrowLeft') changeLightbox(-1);
  if (e.key === 'ArrowRight') changeLightbox(1);
});
```

- [ ] **Step 4: 提交**

```bash
git add -A && git commit -m "feat: add case studies section with lightbox"
```

---

### Task 8: 新闻资讯 Section

**文件:**
- Modify: `index.html` (news section)
- Modify: `css/style.css` (news 样式)

- [ ] **Step 1: News HTML**

```html
<section id="news" class="section-padding bg-secondary-dark">
  <div class="container-custom">
    <h2 class="section-title" data-aos="fade-up">新闻资讯</h2>
    <p class="section-subtitle" data-aos="fade-up" data-aos-delay="100">NEWS & UPDATES</p>

    <div class="row g-4">
      <div class="col-lg-4 col-md-6" data-aos="fade-up" data-aos-delay="0">
        <div class="news-card">
          <div class="news-date"><span>18</span>2026.06</div>
          <div class="news-body">
            <span class="news-tag">企业动态</span>
            <h4>孙氏集团与中远海运签署战略合作协议</h4>
            <p>双方将在国际海运、港口物流等领域深度合作...</p>
          </div>
        </div>
      </div>
      <div class="col-lg-4 col-md-6" data-aos="fade-up" data-aos-delay="100">
        <div class="news-card">
          <div class="news-date"><span>12</span>2026.06</div>
          <div class="news-body">
            <span class="news-tag">行业资讯</span>
            <h4>2026全球物流行业趋势：数字化与绿色转型</h4>
            <p>AI调度、无人仓、新能源运输车成行业热点...</p>
          </div>
        </div>
      </div>
      <div class="col-lg-4 col-md-6" data-aos="fade-up" data-aos-delay="200">
        <div class="news-card">
          <div class="news-date"><span>05</span>2026.06</div>
          <div class="news-body">
            <span class="news-tag">公告通知</span>
            <h4>孙氏集团华南区域仓储中心正式投入运营</h4>
            <p>华南仓占地15万㎡，配备全自动化分拣系统...</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 2: News CSS**

追加到 `css/style.css`:
```css
/* ============================================
   News Section
   ============================================ */
.news-card {
  background: var(--bg-glass);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: var(--radius-lg);
  display: flex;
  overflow: hidden;
  transition: var(--transition-smooth);
}

.news-card:hover {
  transform: translateY(-4px);
  border-color: rgba(255, 255, 255, 0.12);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
}

.news-date {
  flex: 0 0 85px;
  background: var(--bg-tertiary);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 20px 10px;
  font-size: 0.7rem;
  color: var(--text-muted);
  letter-spacing: 1px;
}

.news-date span {
  font-size: 1.8rem;
  font-weight: 700;
  color: var(--primary);
  line-height: 1;
  margin-bottom: 4px;
}

.news-body {
  padding: 20px;
  flex: 1;
}

.news-tag {
  font-size: 0.7rem;
  padding: 3px 10px;
  border-radius: 50px;
  background: rgba(255, 107, 53, 0.1);
  color: var(--primary);
  letter-spacing: 1px;
  margin-bottom: 10px;
  display: inline-block;
}

.news-body h4 {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text-primary);
  margin: 10px 0;
  line-height: 1.5;
}

.news-body p {
  font-size: 0.85rem;
  color: var(--text-muted);
  margin-bottom: 0;
}
```

- [ ] **Step 3: 提交**

```bash
git add -A && git commit -m "feat: add news section with date cards"
```

---

### Task 9: 荣誉资质 + 灯箱图片预览

**文件:**
- Modify: `index.html` (honor section)
- Modify: `css/style.css` (honor 样式)
- Modify: `js/main.js` (honor lightbox 逻辑)

- [ ] **Step 1: Honor HTML**

```html
<section id="honor" class="section-padding bg-primary-dark">
  <div class="container-custom">
    <h2 class="section-title" data-aos="fade-up">荣誉资质</h2>
    <p class="section-subtitle" data-aos="fade-up" data-aos-delay="100">HONORS & CERTIFICATES</p>

    <div class="honor-grid">
      <div class="honor-item" data-aos="zoom-in" data-aos-delay="0" onclick="openHonorLightbox(0)">
        <div class="honor-thumb">
          <i class="fas fa-certificate"></i>
          <span>营业执照</span>
        </div>
      </div>
      <div class="honor-item" data-aos="zoom-in" data-aos-delay="50" onclick="openHonorLightbox(1)">
        <div class="honor-thumb">
          <i class="fas fa-award"></i>
          <span>ISO 9001认证</span>
        </div>
      </div>
      <div class="honor-item" data-aos="zoom-in" data-aos-delay="100" onclick="openHonorLightbox(2)">
        <div class="honor-thumb">
          <i class="fas fa-medal"></i>
          <span>国家A级物流企业</span>
        </div>
      </div>
      <div class="honor-item" data-aos="zoom-in" data-aos-delay="150" onclick="openHonorLightbox(3)">
        <div class="honor-thumb">
          <i class="fas fa-trophy"></i>
          <span>最佳物流服务商</span>
        </div>
      </div>
      <div class="honor-item" data-aos="zoom-in" data-aos-delay="200" onclick="openHonorLightbox(4)">
        <div class="honor-thumb">
          <i class="fas fa-shield-halved"></i>
          <span>海关AEO认证</span>
        </div>
      </div>
      <div class="honor-item" data-aos="zoom-in" data-aos-delay="250" onclick="openHonorLightbox(5)">
        <div class="honor-thumb">
          <i class="fas fa-star"></i>
          <span>5A级诚信企业</span>
        </div>
      </div>
      <div class="honor-item" data-aos="zoom-in" data-aos-delay="300" onclick="openHonorLightbox(6)">
        <div class="honor-thumb">
          <i class="fas fa-leaf"></i>
          <span>绿色物流认证</span>
        </div>
      </div>
      <div class="honor-item" data-aos="zoom-in" data-aos-delay="350" onclick="openHonorLightbox(7)">
        <div class="honor-thumb">
          <i class="fas fa-file-contract"></i>
          <span>国际货运代理资质</span>
        </div>
      </div>
    </div>
  </div>

  <!-- Honor Lightbox -->
  <div id="honorLightbox" class="lightbox">
    <span class="lightbox-close" onclick="closeHonorLightbox()">&times;</span>
    <button class="lightbox-prev" onclick="changeHonorLightbox(-1)"><i class="fas fa-chevron-left"></i></button>
    <button class="lightbox-next" onclick="changeHonorLightbox(1)"><i class="fas fa-chevron-right"></i></button>
    <div class="lightbox-content" id="honorLightboxContent"></div>
  </div>
</section>
```

- [ ] **Step 2: Honor CSS**

追加到 `css/style.css`:
```css
/* ============================================
   Honor Section
   ============================================ */
.honor-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
}

.honor-item {
  cursor: pointer;
  transition: var(--transition-smooth);
}

.honor-item:hover {
  transform: translateY(-6px);
}

.honor-thumb {
  background: var(--bg-glass);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: var(--radius-md);
  padding: 30px 20px;
  text-align: center;
  transition: var(--transition-smooth);
  aspect-ratio: 3/4;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
}

.honor-thumb i {
  font-size: 2.5rem;
  background: var(--gradient-rainbow);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  opacity: 0.7;
}

.honor-item:hover .honor-thumb {
  border-color: rgba(255, 255, 255, 0.15);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3),
              0 0 0 1px var(--primary) inset;
  background: rgba(255, 255, 255, 0.06);
}

.honor-item:hover .honor-thumb i {
  opacity: 1;
}

.honor-thumb span {
  font-size: 0.85rem;
  color: var(--text-secondary);
  letter-spacing: 1px;
}
```

- [ ] **Step 3: Honor Lightbox JS**

追加到 `js/main.js`:
```js
// ============================================
// Honor Lightbox
// ============================================
const honorData = [
  { title: '营业执照', icon: 'fa-certificate', color: 'var(--primary)' },
  { title: 'ISO 9001质量管理体系认证', icon: 'fa-award', color: 'var(--secondary)' },
  { title: '国家AAAAA级物流企业', icon: 'fa-medal', color: 'var(--accent-green)' },
  { title: '年度最佳物流服务商', icon: 'fa-trophy', color: 'var(--accent-blue)' },
  { title: '海关AEO高级认证企业', icon: 'fa-shield-halved', color: 'var(--accent-purple)' },
  { title: '5A级诚信经营示范企业', icon: 'fa-star', color: 'var(--accent-rose)' },
  { title: '绿色物流示范企业认证', icon: 'fa-leaf', color: 'var(--accent-green)' },
  { title: '国际货运代理企业资质', icon: 'fa-file-contract', color: 'var(--primary)' },
];

let currentHonorIndex = 0;

function openHonorLightbox(index) {
  currentHonorIndex = index;
  const data = honorData[index];
  document.getElementById('honorLightboxContent').innerHTML = `
    <i class="fas ${data.icon}" style="font-size: 5rem; color: ${data.color}; opacity: 0.4; margin-bottom: 20px;"></i>
    <h3 style="color: var(--text-primary);">${data.title}</h3>
    <p style="color: var(--text-muted);">孙氏集团荣誉资质</p>
    <hr class="rainbow-divider" style="width: 60px; margin: 20px auto;">
    <p style="color: var(--text-secondary);">此证书为孙氏集团依法取得的相关经营资质与行业荣誉，体现了集团在行业内的专业实力和良好信誉。</p>
  `;
  document.getElementById('honorLightbox').classList.add('active');
  document.body.style.overflow = 'hidden';
}

function closeHonorLightbox() {
  document.getElementById('honorLightbox').classList.remove('active');
  document.body.style.overflow = '';
}

function changeHonorLightbox(direction) {
  currentHonorIndex = (currentHonorIndex + direction + honorData.length) % honorData.length;
  openHonorLightbox(currentHonorIndex);
}

document.getElementById('honorLightbox').addEventListener('click', function(e) {
  if (e.target === this) closeHonorLightbox();
});

document.addEventListener('keydown', function(e) {
  if (!document.getElementById('honorLightbox').classList.contains('active')) return;
  if (e.key === 'Escape') closeHonorLightbox();
  if (e.key === 'ArrowLeft') changeHonorLightbox(-1);
  if (e.key === 'ArrowRight') changeHonorLightbox(1);
});
```

- [ ] **Step 4: 提交**

```bash
git add -A && git commit -m "feat: add honor/certificates section with gallery lightbox"
```

---

### Task 10: 人才招聘 + 客户评价 + 联系我们（含表单+地图）+ 页脚 + 悬浮工具栏

**文件:**
- Modify: `index.html`
- Modify: `css/style.css`
- Modify: `js/main.js`

（由于内容较多，此行以下合并为一个任务，包含 Recruitment、Reviews、Contact、Footer、Floating Toolbar 五个模块）

- [ ] **Step 1: HTML - 人才招聘**

```html
<section id="recruit" class="section-padding bg-secondary-dark">
  <div class="container-custom">
    <h2 class="section-title" data-aos="fade-up">人才招聘</h2>
    <p class="section-subtitle" data-aos="fade-up" data-aos-delay="100">JOIN OUR TEAM</p>
    <div class="row g-4">
      <div class="col-lg-4 col-md-6" data-aos="fade-up" data-aos-delay="0">
        <div class="job-card">
          <span class="job-type" style="--tag-color: var(--primary)">急聘</span>
          <h4>国际物流销售经理</h4>
          <p class="job-loc"><i class="fas fa-map-marker-alt"></i> 上海 · 浦东</p>
          <p class="job-salary"><i class="fas fa-coins"></i> 15K-25K + 提成</p>
          <a href="#contact" class="btn btn-primary-custom btn-sm">投递简历</a>
        </div>
      </div>
      <div class="col-lg-4 col-md-6" data-aos="fade-up" data-aos-delay="100">
        <div class="job-card">
          <span class="job-type" style="--tag-color: var(--accent-blue)">技术</span>
          <h4>供应链解决方案专家</h4>
          <p class="job-loc"><i class="fas fa-map-marker-alt"></i> 深圳 · 南山</p>
          <p class="job-salary"><i class="fas fa-coins"></i> 20K-30K</p>
          <a href="#contact" class="btn btn-primary-custom btn-sm">投递简历</a>
        </div>
      </div>
      <div class="col-lg-4 col-md-6" data-aos="fade-up" data-aos-delay="200">
        <div class="job-card">
          <span class="job-type" style="--tag-color: var(--accent-green)">运营</span>
          <h4>海外仓运营主管</h4>
          <p class="job-loc"><i class="fas fa-map-marker-alt"></i> 广州 · 天河</p>
          <p class="job-salary"><i class="fas fa-coins"></i> 18K-28K</p>
          <a href="#contact" class="btn btn-primary-custom btn-sm">投递简历</a>
        </div>
      </div>
    </div>
    <div class="text-center mt-4" data-aos="fade-up">
      <p class="text-muted mb-0">更多岗位请投递简历至 <span style="color: var(--primary);">hr@sungroup.com</span></p>
    </div>
  </div>
</section>
```

- [ ] **Step 2: HTML - 客户评价**

```html
<section id="reviews" class="section-padding bg-primary-dark">
  <div class="container-custom">
    <h2 class="section-title" data-aos="fade-up">客户评价</h2>
    <p class="section-subtitle" data-aos="fade-up" data-aos-delay="100">CLIENT TESTIMONIALS</p>
    <div class="row g-4 mb-5">
      <div class="col-md-4" data-aos="fade-up" data-aos-delay="0">
        <div class="review-card">
          <div class="review-stars">★★★★★</div>
          <p class="review-text">"与孙氏合作5年，从海运到仓储一站式服务，专业高效，是我们最信赖的物流伙伴。"</p>
          <div class="review-author">
            <strong>王建国</strong>
            <span>某电子科技集团 · 供应链总监</span>
          </div>
        </div>
      </div>
      <div class="col-md-4" data-aos="fade-up" data-aos-delay="100">
        <div class="review-card">
          <div class="review-stars">★★★★★</div>
          <p class="review-text">"跨境电商物流找孙氏就对了，系统对接顺畅，异常处理快，签收率远超同行。"</p>
          <div class="review-author">
            <strong>陈美玲</strong>
            <span>某头部电商平台 · 物流经理</span>
          </div>
        </div>
      </div>
      <div class="col-md-4" data-aos="fade-up" data-aos-delay="200">
        <div class="review-card">
          <div class="review-stars">★★★★★</div>
          <p class="review-text">"大宗商品进口交给孙氏很放心，关务团队专业，时效比预期还快，强烈推荐。"</p>
          <div class="review-author">
            <strong>张伟</strong>
            <span>某大型贸易公司 · 总经理</span>
          </div>
        </div>
      </div>
    </div>
    <!-- Logo墙 -->
    <div class="client-logos" data-aos="fade-up">
      <p class="text-muted text-center mb-4">合作企业</p>
      <div class="logo-wall">
        <div class="logo-item">TECHTRON</div>
        <div class="logo-item">GLOBALTRADE</div>
        <div class="logo-item">ASIAMART</div>
        <div class="logo-item">EUROLINK</div>
        <div class="logo-item">PACIFIC</div>
        <div class="logo-item">NEXUS</div>
        <div class="logo-item">METALPRO</div>
        <div class="logo-item">FASHIONFORWARD</div>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 3: HTML - 联系我们**

```html
<section id="contact" class="section-padding bg-secondary-dark">
  <div class="container-custom">
    <h2 class="section-title" data-aos="fade-up">联系我们</h2>
    <p class="section-subtitle" data-aos="fade-up" data-aos-delay="100">CONTACT US</p>
    <div class="row g-4">
      <div class="col-lg-6" data-aos="fade-right">
        <form id="contactForm" class="contact-form" onsubmit="handleSubmit(event)">
          <div class="row g-3">
            <div class="col-md-6">
              <label class="form-label">姓名 *</label>
              <input type="text" class="form-control-custom" placeholder="请输入姓名" required>
            </div>
            <div class="col-md-6">
              <label class="form-label">电话 *</label>
              <input type="tel" class="form-control-custom" placeholder="请输入电话" required pattern="[\d\-+\s]{7,15}">
            </div>
            <div class="col-12">
              <label class="form-label">需求内容</label>
              <textarea class="form-control-custom" rows="4" placeholder="请描述您的物流需求，我们将尽快与您联系"></textarea>
            </div>
            <div class="col-12">
              <button type="submit" class="btn btn-primary-custom btn-lg w-100">
                提交留言 <i class="fas fa-paper-plane"></i>
              </button>
            </div>
          </div>
        </form>
      </div>
      <div class="col-lg-6" data-aos="fade-left">
        <div class="contact-info-card">
          <h4>孙氏集团 · 总部</h4>
          <div class="contact-info-list">
            <div class="contact-info-item">
              <div class="ci-icon"><i class="fas fa-map-marker-alt"></i></div>
              <div><strong>地址</strong><br>上海市浦东新区陆家嘴金融区世纪大道100号</div>
            </div>
            <div class="contact-info-item">
              <div class="ci-icon"><i class="fas fa-phone"></i></div>
              <div><strong>电话</strong><br>400-888-6688</div>
            </div>
            <div class="contact-info-item">
              <div class="ci-icon"><i class="fas fa-envelope"></i></div>
              <div><strong>邮箱</strong><br>info@sungroup.com</div>
            </div>
            <div class="contact-info-item">
              <div class="ci-icon"><i class="fas fa-clock"></i></div>
              <div><strong>营业时间</strong><br>周一至周五 9:00-18:00</div>
            </div>
          </div>
        </div>
        <div class="map-container">
          <div class="map-placeholder">
            <i class="fas fa-map"></i>
            <span>高德地图定位</span>
            <small>上海市浦东新区陆家嘴金融区</small>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 4: HTML - 页脚**

```html
<footer id="footer">
  <div class="footer-rainbow-line"></div>
  <div class="container-custom">
    <div class="row g-4">
      <div class="col-lg-4">
        <h5 class="footer-brand">SUN GROUP <span>孙氏集团</span></h5>
        <p class="footer-about">链接全球 · 物流天下<br>国际物流与贸易综合服务商</p>
        <div class="footer-social">
          <a href="#"><i class="fab fa-weixin"></i></a>
          <a href="#"><i class="fab fa-weibo"></i></a>
          <a href="#"><i class="fab fa-linkedin-in"></i></a>
        </div>
      </div>
      <div class="col-lg-2 col-md-4">
        <h6>快捷导航</h6>
        <ul>
          <li><a href="#about">关于我们</a></li>
          <li><a href="#products">业务中心</a></li>
          <li><a href="#cases">案例展示</a></li>
          <li><a href="#news">新闻资讯</a></li>
        </ul>
      </div>
      <div class="col-lg-3 col-md-4">
        <h6>业务板块</h6>
        <ul>
          <li><a href="#products">国际海运</a></li>
          <li><a href="#products">航空货运</a></li>
          <li><a href="#products">陆运物流</a></li>
          <li><a href="#products">仓储配送</a></li>
          <li><a href="#products">跨境电商物流</a></li>
        </ul>
      </div>
      <div class="col-lg-3 col-md-4">
        <h6>联系方式</h6>
        <ul class="footer-contact">
          <li><i class="fas fa-phone"></i> 400-888-6688</li>
          <li><i class="fas fa-envelope"></i> info@sungroup.com</li>
          <li><i class="fas fa-map-marker-alt"></i> 上海市浦东新区陆家嘴</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 孙氏集团 Sun Group. All Rights Reserved.</p>
      <p><a href="#">沪ICP备XXXXXXXX号</a> | <a href="#">隐私政策</a></p>
    </div>
  </div>
</footer>
```

- [ ] **Step 5: HTML - 悬浮工具栏**

```html
<div id="floating-toolbar">
  <a href="tel:400-888-6688" class="float-btn" title="一键拨号">
    <i class="fas fa-phone"></i>
    <span class="float-tip">400-888-6688</span>
  </a>
  <a href="#" class="float-btn wechat-btn" title="微信咨询">
    <i class="fab fa-weixin"></i>
    <span class="float-tip wechat-qr">
      <span style="font-size:12px;line-height:1.4;">扫码添加<br>企业微信</span>
    </span>
  </a>
  <a href="#" class="float-btn" id="backToTop" title="返回顶部">
    <i class="fas fa-arrow-up"></i>
  </a>
  <a href="#contact" class="float-btn" title="在线咨询">
    <i class="fas fa-headset"></i>
  </a>
</div>

<!-- Toast -->
<div id="toast" class="toast-notification">
  <i class="fas fa-check-circle"></i> 提交成功，我们将尽快与您联系！
</div>
```

- [ ] **Step 6: CSS - 所有上述模块的样式**

追加到 `css/style.css`:
```css
/* ============================================
   Job Cards
   ============================================ */
.job-card {
  background: var(--bg-glass);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: var(--radius-lg);
  padding: 30px;
  transition: var(--transition-smooth);
}

.job-card:hover {
  transform: translateY(-4px);
  border-color: rgba(255, 255, 255, 0.12);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
}

.job-type {
  display: inline-block;
  font-size: 0.7rem;
  padding: 3px 10px;
  border-radius: 50px;
  background: rgba(255, 107, 53, 0.1);
  color: var(--tag-color, var(--primary));
  letter-spacing: 1px;
  margin-bottom: 12px;
}

.job-card h4 {
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 12px;
}

.job-loc, .job-salary {
  font-size: 0.85rem;
  color: var(--text-muted);
  margin-bottom: 6px;
}

.job-loc i, .job-salary i {
  margin-right: 6px;
  color: var(--primary);
  width: 16px;
}

.btn-sm {
  padding: 8px 20px !important;
  font-size: 0.85rem !important;
  margin-top: 10px;
}

/* ============================================
   Reviews Section
   ============================================ */
.review-card {
  background: var(--bg-glass);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: var(--radius-lg);
  padding: 30px;
  transition: var(--transition-smooth);
  position: relative;
}

.review-card::before {
  content: '\201C';
  font-size: 5rem;
  color: rgba(255, 255, 255, 0.03);
  position: absolute;
  top: -10px;
  left: 20px;
  font-family: serif;
  line-height: 1;
}

.review-card:hover {
  border-color: rgba(255, 255, 255, 0.12);
  transform: translateY(-4px);
}

.review-stars {
  color: var(--secondary);
  font-size: 1rem;
  margin-bottom: 15px;
  letter-spacing: 2px;
}

.review-text {
  color: var(--text-secondary);
  font-size: 0.95rem;
  line-height: 1.8;
  margin-bottom: 20px;
  font-style: italic;
}

.review-author strong {
  display: block;
  color: var(--text-primary);
  font-size: 0.9rem;
}

.review-author span {
  font-size: 0.8rem;
  color: var(--text-muted);
}

/* Logo Wall */
.client-logos {
  margin-top: 40px;
}

.logo-wall {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 30px;
}

.logo-item {
  padding: 15px 25px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: var(--radius-sm);
  color: var(--text-muted);
  font-family: "Roboto", sans-serif;
  font-size: 0.85rem;
  letter-spacing: 2px;
  transition: var(--transition-fast);
}

.logo-item:hover {
  border-color: rgba(255, 255, 255, 0.2);
  color: var(--text-primary);
  background: rgba(255, 255, 255, 0.06);
}

/* ============================================
   Contact Form
   ============================================ */
.contact-form {
  background: var(--bg-glass);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: var(--radius-lg);
  padding: 35px;
}

.form-label {
  color: var(--text-secondary);
  font-size: 0.85rem;
  margin-bottom: 6px;
}

.form-control-custom {
  width: 100%;
  padding: 12px 16px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: var(--radius-sm);
  color: var(--text-primary);
  font-size: 0.95rem;
  transition: var(--transition-fast);
  outline: none;
}

.form-control-custom:focus {
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(255, 107, 53, 0.1);
}

.form-control-custom::placeholder {
  color: var(--text-muted);
}

.contact-info-card {
  background: var(--bg-glass);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: var(--radius-lg);
  padding: 30px;
  margin-bottom: 20px;
}

.contact-info-card h4 {
  font-size: 1.2rem;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 20px;
}

.contact-info-item {
  display: flex;
  gap: 15px;
  margin-bottom: 18px;
}

.ci-icon {
  width: 42px;
  height: 42px;
  flex-shrink: 0;
  border-radius: 50%;
  background: rgba(255, 107, 53, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--primary);
  font-size: 0.9rem;
}

.contact-info-item strong {
  display: block;
  color: var(--text-primary);
  font-size: 0.85rem;
  margin-bottom: 2px;
}

.contact-info-item div:last-child {
  color: var(--text-secondary);
  font-size: 0.9rem;
  line-height: 1.6;
}

/* Map */
.map-container {
  border-radius: var(--radius-lg);
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.06);
}

.map-placeholder {
  height: 220px;
  background: linear-gradient(135deg, #1a2535, #1a2a40);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 8px;
  color: var(--text-muted);
}

.map-placeholder i {
  font-size: 2rem;
  opacity: 0.3;
}

.map-placeholder span {
  font-size: 1rem;
  color: var(--text-secondary);
}

/* ============================================
   Footer
   ============================================ */
#footer {
  background: var(--bg-primary);
  padding: 60px 0 0;
}

.footer-rainbow-line {
  height: 2px;
  background: var(--gradient-rainbow);
}

.footer-brand {
  font-family: "Roboto", sans-serif;
  font-size: 1.3rem;
  font-weight: 700;
  letter-spacing: 3px;
  background: var(--gradient-rainbow);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 15px;
}

.footer-brand span {
  font-size: 0.8rem;
  font-weight: 400;
  letter-spacing: 4px;
}

.footer-about {
  color: var(--text-muted);
  font-size: 0.9rem;
  line-height: 1.8;
  margin-bottom: 20px;
}

.footer-social {
  display: flex;
  gap: 12px;
}

.footer-social a {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  border: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-muted);
  font-size: 0.9rem;
  text-decoration: none;
  transition: var(--transition-fast);
}

.footer-social a:hover {
  border-color: var(--primary);
  color: var(--primary);
  background: rgba(255, 107, 53, 0.1);
}

#footer h6 {
  color: var(--text-primary);
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 20px;
}

#footer ul {
  list-style: none;
  padding: 0;
}

#footer ul li {
  margin-bottom: 10px;
}

#footer ul li a {
  color: var(--text-muted);
  text-decoration: none;
  font-size: 0.85rem;
  transition: var(--transition-fast);
}

#footer ul li a:hover {
  color: var(--primary);
  padding-left: 5px;
}

.footer-contact li {
  color: var(--text-muted);
  font-size: 0.85rem;
}

.footer-contact li i {
  color: var(--primary);
  margin-right: 8px;
  width: 16px;
}

.footer-bottom {
  margin-top: 40px;
  padding: 20px 0;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 10px;
}

.footer-bottom p {
  font-size: 0.8rem;
  color: var(--text-muted);
  margin: 0;
}

.footer-bottom a {
  color: var(--text-muted);
  text-decoration: none;
}

.footer-bottom a:hover {
  color: var(--primary);
}

/* ============================================
   Floating Toolbar
   ============================================ */
#floating-toolbar {
  position: fixed;
  right: 20px;
  top: 50%;
  transform: translateY(-50%);
  z-index: 999;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.float-btn {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: rgba(10, 14, 23, 0.85);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-secondary);
  font-size: 1.1rem;
  text-decoration: none;
  position: relative;
  transition: var(--transition-fast);
}

.float-btn:hover {
  color: var(--primary);
  border-color: var(--primary);
  background: rgba(255, 107, 53, 0.1);
  transform: scale(1.1);
}

.float-tip {
  position: absolute;
  right: 60px;
  background: var(--bg-tertiary);
  color: var(--text-primary);
  padding: 8px 16px;
  border-radius: var(--radius-sm);
  font-size: 0.8rem;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: var(--transition-fast);
}

.float-btn:hover .float-tip {
  opacity: 1;
}

.wechat-qr {
  width: 120px;
  height: 120px;
  background: #fff;
  color: #333;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius-sm);
}

#backToTop {
  opacity: 0;
  pointer-events: none;
  transition: var(--transition-fast);
}

#backToTop.visible {
  opacity: 1;
  pointer-events: auto;
}

/* ============================================
   Toast Notification
   ============================================ */
.toast-notification {
  position: fixed;
  top: 20px;
  right: 20px;
  background: var(--accent-green);
  color: #fff;
  padding: 16px 24px;
  border-radius: var(--radius-md);
  font-size: 0.95rem;
  display: flex;
  align-items: center;
  gap: 10px;
  z-index: 9999;
  opacity: 0;
  transform: translateX(100%);
  transition: var(--transition-smooth);
}

.toast-notification.show {
  opacity: 1;
  transform: translateX(0);
}
```

- [ ] **Step 7: JS - 表单提交 + 返回顶部 + Toast**

追加到 `js/main.js`:
```js
// ============================================
// Contact Form
// ============================================
function handleSubmit(e) {
  e.preventDefault();
  const toast = document.getElementById('toast');
  toast.classList.add('show');
  setTimeout(() => {
    toast.classList.remove('show');
  }, 3000);
  e.target.reset();
}

// ============================================
// Back to Top
// ============================================
const backToTop = document.getElementById('backToTop');
window.addEventListener('scroll', function() {
  if (window.scrollY > 300) {
    backToTop.classList.add('visible');
  } else {
    backToTop.classList.remove('visible');
  }
});

backToTop.addEventListener('click', function(e) {
  e.preventDefault();
  window.scrollTo({ top: 0, behavior: 'smooth' });
});
```

- [ ] **Step 8: 提交**

```bash
git add -A && git commit -m "feat: add recruitment, reviews, contact form, footer, and floating toolbar"
```

---

### Task 11: 响应式 CSS

**文件:**
- Modify: `css/responsive.css`

- [ ] **Step 1: 完整响应式样式**

写入 `css/responsive.css`:
```css
/* ============================================
   响应式适配 - 孙氏集团企业官网
   ============================================ */

/* --- XXL (≥1400px) --- */
@media (min-width: 1400px) {
  .container-custom { max-width: 1320px; }
}

/* --- LG (992px-1199px) --- */
@media (max-width: 1199.98px) {
  .hero-title { font-size: 2.8rem; }
  .stat-number { font-size: 2.8rem; }
  .honor-grid { grid-template-columns: repeat(3, 1fr); }
  .about-image-placeholder { height: 350px; }
}

/* --- MD / Tablet (768px-991px) --- */
@media (max-width: 991.98px) {
  :root { --section-padding: 70px 0; }

  .hero-title { font-size: 2.2rem; }
  .hero-desc { font-size: 0.95rem; }
  .hero-section { min-height: 500px; }

  .section-title { font-size: 1.8rem; }
  .about-stats-mini { gap: 25px; }
  .stat-mini-num { font-size: 1.5rem; }
  .honor-grid { grid-template-columns: repeat(2, 1fr); }

  /* Mobile nav */
  .navbar-collapse {
    position: fixed;
    top: 0;
    right: -100%;
    width: 280px;
    height: 100vh;
    background: rgba(10, 14, 23, 0.98);
    backdrop-filter: blur(20px);
    padding: 80px 30px;
    transition: right 0.4s ease;
    display: block !important;
    z-index: 999;
  }

  .navbar-collapse.show { right: 0; }

  .navbar-nav {
    flex-direction: column;
    gap: 5px;
  }

  .nav-link {
    font-size: 1.1rem;
    padding: 12px 0 !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  }

  .dropdown-menu {
    background: transparent;
    border: none;
    padding-left: 15px;
  }

  .dropdown-item {
    color: var(--text-muted);
    padding: 8px 0;
  }

  .logo-wall { gap: 15px; }
  .logo-item { padding: 10px 15px; font-size: 0.75rem; }

  #floating-toolbar {
    right: 10px;
    gap: 8px;
  }

  .float-btn {
    width: 40px;
    height: 40px;
    font-size: 0.9rem;
  }
}

/* --- SM / Mobile (<768px) --- */
@media (max-width: 767.98px) {
  :root { --section-padding: 50px 0; }

  .hero-title { font-size: 1.8rem; }
  .hero-tagline { font-size: 0.7rem; letter-spacing: 4px; }
  .hero-desc { font-size: 0.85rem; }
  .hero-section { height: 70vh; min-height: 400px; }
  .hero-btns { flex-direction: column; align-items: center; }

  .section-title { font-size: 1.5rem; }
  .section-subtitle { font-size: 0.8rem; margin-bottom: 30px; }

  .about-image-placeholder { height: 250px; }
  .about-heading { font-size: 1.4rem; }
  .about-stats-mini { gap: 20px; flex-wrap: wrap; }
  .stat-mini-num { font-size: 1.3rem; }

  .stat-number { font-size: 2.2rem; }
  .stat-card { padding: 25px 10px; }

  .honor-grid { grid-template-columns: repeat(2, 1fr); gap: 12px; }
  .honor-thumb { padding: 20px 15px; }
  .honor-thumb i { font-size: 1.8rem; }
  .honor-thumb span { font-size: 0.75rem; }

  .news-card { flex-direction: column; }
  .news-date { flex: 0 0 auto; flex-direction: row; gap: 8px; padding: 12px 20px; }
  .news-date span { font-size: 1.2rem; margin-bottom: 0; }

  .logo-wall { gap: 10px; }
  .logo-item { padding: 8px 12px; font-size: 0.7rem; letter-spacing: 1px; }

  .contact-form { padding: 20px; }
  .map-placeholder { height: 180px; }

  #floating-toolbar {
    right: 0;
    bottom: 0;
    top: auto;
    flex-direction: row;
    transform: none;
    width: 100%;
    justify-content: space-around;
    background: rgba(10, 14, 23, 0.95);
    backdrop-filter: blur(10px);
    padding: 8px 0;
    border-top: 1px solid rgba(255, 255, 255, 0.06);
  }

  .float-btn {
    width: 40px;
    height: 40px;
    background: transparent;
    border: none;
  }

  .float-tip { display: none; }

  .footer-bottom {
    flex-direction: column;
    text-align: center;
  }

  .hero-swiper .swiper-button-prev,
  .hero-swiper .swiper-button-next {
    display: none;
  }

  .lightbox-content { padding: 20px; }
  .lightbox-content h3 { font-size: 1.3rem; }
}
```

- [ ] **Step 2: 提交**

```bash
git add -A && git commit -m "feat: add responsive CSS for all breakpoints"
```

---

### Task 12: 最终验证 & README 完善

- [ ] **Step 1: 验证所有文件存在**

```bash
ls -la index.html css/style.css css/responsive.css js/main.js README.md
```

- [ ] **Step 2: 测试：用浏览器打开 index.html，滚动检查所有模块、灯箱、表单**

- [ ] **Step 3: 检查控制台无 JS 错误**

- [ ] **Step 4: 提交最终版本**

```bash
git add -A && git commit -m "feat: complete Sun Group corporate website v1.0"
```

---

## 实施说明

每个 Task 中的代码是**完整可直接替换**的内容。实施时从 Task 1 到 Task 12 顺序执行：
1. 创建好 `index.html` 骨架后，后续每个 Task 只需替换对应的 `...` 占位符或追加内容
2. CSS 全部追加到 `css/style.css` 末尾
3. JS 全部追加到 `js/main.js` 末尾
4. 每个 Task 可独立提交和验证

完成后在浏览器打开 `index.html` 即可看到完整效果。
