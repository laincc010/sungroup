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
  document.getElementById('navMenu').classList.toggle('show');
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

        bars.forEach(bar => bar.classList.add('animated'));
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(counter => observer.observe(counter));
}

document.addEventListener('DOMContentLoaded', animateCounters);

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
  document.getElementById('lightboxContent').innerHTML =
    '<span class="case-tag" style="--tag-color: var(--primary); margin: 0 auto 15px; display: inline-block;">案例详情</span>' +
    '<h3>' + data.title + '</h3>' +
    '<hr class="rainbow-divider" style="width: 60px; margin: 20px auto;">' +
    '<p>' + data.desc + '</p>';
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
  document.getElementById('honorLightboxContent').innerHTML =
    '<i class="fas ' + data.icon + '" style="font-size: 5rem; color: ' + data.color + '; opacity: 0.4; margin-bottom: 20px;"></i>' +
    '<h3 style="color: var(--text-primary);">' + data.title + '</h3>' +
    '<p style="color: var(--text-muted);">孙氏集团荣誉资质</p>' +
    '<hr class="rainbow-divider" style="width: 60px; margin: 20px auto;">' +
    '<p style="color: var(--text-secondary);">此证书为孙氏集团依法取得的相关经营资质与行业荣誉，体现了集团在行业内的专业实力和良好信誉。</p>';
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

// ============================================
// Contact Form
// ============================================
function handleSubmit(e) {
  e.preventDefault();
  const toast = document.getElementById('toast');
  toast.classList.add('show');
  setTimeout(function() {
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
