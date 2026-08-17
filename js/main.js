/* ==========================================================================
   XPERT CONSULTANCY — Main JavaScript
   Lightweight vanilla JS — no jQuery, no bloat.
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  initHeader();
  initMobileNav();
  initScrollReveal();
  initCounters();
  initTestimonials();
  initMarquee();
  initSmoothScroll();
  initKBExpansion();
  initParallaxCards();
});


/* ---------- Sticky Header ---------- */
function initHeader() {
  const header = document.querySelector('.site-header');
  if (!header) return;

  const threshold = 60;

  function update() {
    if (window.scrollY > threshold) {
      header.classList.remove('site-header--transparent');
      header.classList.add('site-header--solid');
    } else {
      header.classList.remove('site-header--solid');
      header.classList.add('site-header--transparent');
    }
  }

  // Check if page has a hero (homepage) — if not, start solid
  const hasHero = document.querySelector('.hero');
  if (!hasHero) {
    header.classList.remove('site-header--transparent');
    header.classList.add('site-header--solid');
    return;
  }

  update();
  window.addEventListener('scroll', update, { passive: true });
}


/* ---------- Mobile Navigation ---------- */
function initMobileNav() {
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.nav');

  if (!toggle || !nav) return;

  toggle.addEventListener('click', () => {
    toggle.classList.toggle('active');
    nav.classList.toggle('open');
    document.body.style.overflow = nav.classList.contains('open') ? 'hidden' : '';
  });

  // Close when clicking a nav link
  nav.querySelectorAll('.nav__link, .nav__dropdown-link, .nav__cta').forEach(link => {
    link.addEventListener('click', () => {
      toggle.classList.remove('active');
      nav.classList.remove('open');
      document.body.style.overflow = '';
    });
  });
}


/* ---------- Scroll Reveal ---------- */
function initScrollReveal() {
  const reveals = document.querySelectorAll('.reveal, .reveal-scale');
  if (!reveals.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        if (entry.target.classList.contains('reveal')) {
          entry.target.classList.add('reveal--visible');
        }
        if (entry.target.classList.contains('reveal-scale')) {
          entry.target.classList.add('reveal-scale--visible');
        }
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.12,
    rootMargin: '0px 0px -40px 0px'
  });

  reveals.forEach(el => observer.observe(el));
}


/* ---------- Animated Counters ---------- */
function initCounters() {
  const counters = document.querySelectorAll('[data-count]');
  if (!counters.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.4 });

  counters.forEach(el => observer.observe(el));
}

function animateCounter(el) {
  const target = parseInt(el.getAttribute('data-count'), 10);
  const duration = 2000;
  const start = performance.now();

  function step(now) {
    const elapsed = now - start;
    const progress = Math.min(elapsed / duration, 1);
    // Ease out cubic
    const eased = 1 - Math.pow(1 - progress, 3);
    const current = Math.floor(eased * target);
    el.textContent = current;

    if (progress < 1) {
      requestAnimationFrame(step);
    } else {
      el.textContent = target;
    }
  }

  requestAnimationFrame(step);
}


/* ---------- Testimonial Slider ---------- */
function initTestimonials() {
  const slider = document.querySelector('.testimonial-slider');
  if (!slider) return;

  const track = slider.querySelector('.testimonial-track');
  const slides = slider.querySelectorAll('.testimonial-slide');
  const prevBtn = document.getElementById('testimonial-prev');
  const nextBtn = document.getElementById('testimonial-next');
  const dotsContainer = document.querySelector('.testimonial-dots');

  if (!track || slides.length === 0) return;

  let current = 0;
  let autoplayTimer;
  const total = slides.length;

  // Build dots
  if (dotsContainer) {
    slides.forEach((_, i) => {
      const dot = document.createElement('button');
      dot.classList.add('testimonial-dot');
      dot.setAttribute('aria-label', `Go to testimonial ${i + 1}`);
      if (i === 0) dot.classList.add('testimonial-dot--active');
      dot.addEventListener('click', () => goTo(i));
      dotsContainer.appendChild(dot);
    });
  }

  function goTo(index) {
    current = index;
    track.style.transform = `translateX(-${current * 100}%)`;
    updateDots();
    resetAutoplay();
  }

  function next() {
    goTo((current + 1) % total);
  }

  function prev() {
    goTo((current - 1 + total) % total);
  }

  function updateDots() {
    if (!dotsContainer) return;
    const dots = dotsContainer.querySelectorAll('.testimonial-dot');
    dots.forEach((dot, i) => {
      dot.classList.toggle('testimonial-dot--active', i === current);
    });
  }

  function resetAutoplay() {
    clearInterval(autoplayTimer);
    autoplayTimer = setInterval(next, 6000);
  }

  if (prevBtn) prevBtn.addEventListener('click', prev);
  if (nextBtn) nextBtn.addEventListener('click', next);

  // Touch / swipe support
  let touchStartX = 0;
  let touchEndX = 0;

  track.addEventListener('touchstart', e => {
    touchStartX = e.changedTouches[0].screenX;
  }, { passive: true });

  track.addEventListener('touchend', e => {
    touchEndX = e.changedTouches[0].screenX;
    const diff = touchStartX - touchEndX;
    if (Math.abs(diff) > 50) {
      if (diff > 0) next();
      else prev();
    }
  }, { passive: true });

  // Start autoplay
  resetAutoplay();
}


/* ---------- Partner Logo Marquee ---------- */
function initMarquee() {
  const marquee = document.querySelector('.marquee');
  if (!marquee) return;

  // Clone children to create seamless loop
  const items = Array.from(marquee.children);
  items.forEach(item => {
    const clone = item.cloneNode(true);
    clone.setAttribute('aria-hidden', 'true');
    marquee.appendChild(clone);
  });
}


/* ---------- Smooth Scroll Anchor Links ---------- */
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      
      const targetEl = document.querySelector(targetId);
      if (targetEl) {
        e.preventDefault();
        const headerOffset = 80;
        const elementPosition = targetEl.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.scrollY - headerOffset;

        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth'
        });
      }
    });
  });
}


/* ---------- Knowledge Base Expansion ---------- */
function initKBExpansion() {
  const kbButtons = document.querySelectorAll('.kb-read-more');
  if (!kbButtons.length) return;

  kbButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      const article = e.target.closest('.kb-article');
      if (!article) return;
      const content = article.querySelector('.kb-article__content');
      if (!content) return;

      if (content.style.maxHeight === '0px' || !content.style.maxHeight) {
        // Expand
        content.style.maxHeight = content.scrollHeight + 'px';
        e.target.textContent = 'Close Guide';
      } else {
        // Collapse
        content.style.maxHeight = '0';
        e.target.textContent = 'Read Guide';
      }
    });
  });
}


/* ---------- Elegant Parallax & Tilt Effect ---------- */
function initParallaxCards() {
  const tiltElements = document.querySelectorAll('.partner-logo-card, .feature-list__item, .hero__title');
  if (!tiltElements.length || window.matchMedia("(hover: none)").matches) return;

  tiltElements.forEach(el => {
    el.addEventListener('mousemove', (e) => {
      const rect = el.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      
      // Extremely subtle rotation for organic feel
      const rotateX = ((y - centerY) / centerY) * -3; 
      const rotateY = ((x - centerX) / centerX) * 3;
      
      el.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-2px)`;
      el.style.transition = 'none';
    });
    
    el.addEventListener('mouseleave', () => {
      el.style.transform = '';
      el.style.transition = 'all 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
    });
  });
}
