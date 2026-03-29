const revealEls = document.querySelectorAll('.reveal');

const pageOverlay = document.createElement('div');
pageOverlay.className = 'page-transition-overlay';
document.body.appendChild(pageOverlay);

requestAnimationFrame(() => {
  document.body.classList.add('page-ready');
});

const transitionLinks = document.querySelectorAll('.nav-links a, .brand-mark, .footer-brand');
transitionLinks.forEach((link) => {
  link.addEventListener('click', (event) => {
    const href = link.getAttribute('href');
    if (!href) return;
    if (href.startsWith('#')) return;
    if (href.startsWith('http')) return;
    if (!href.endsWith('.html')) return;
    if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;

    event.preventDefault();
    document.body.classList.add('is-transitioning');
    pageOverlay.classList.add('active');

    setTimeout(() => {
      window.location.href = href;
    }, 380);
  });
});

if (revealEls.length > 0) {
  const revealObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('show');
          revealObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.14 }
  );

  revealEls.forEach((el) => revealObserver.observe(el));
}

const contactForm = document.getElementById('contact-form');
if (contactForm) {
  contactForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const status = document.getElementById('contact-status');
    if (status) {
      status.textContent = 'Thanks. Your message has been queued for review.';
    }
    contactForm.reset();
  });
}

const filterButtons = document.querySelectorAll('[data-filter]');
const postCards = document.querySelectorAll('[data-post-card]');

function applyFilter(category) {
  postCards.forEach((card) => {
    const categories = (card.dataset.category || '').toLowerCase().split(/\s+/).filter(Boolean);
    const show = category === 'all' || categories.includes(category);

    if (show) {
      card.classList.remove('is-hidden');
      requestAnimationFrame(() => {
        card.classList.remove('filtered-out');
      });
    } else {
      card.classList.add('filtered-out');
      setTimeout(() => {
        if (card.classList.contains('filtered-out')) {
          card.classList.add('is-hidden');
        }
      }, 320);
    }
  });
}

if (filterButtons.length > 0 && postCards.length > 0) {
  filterButtons.forEach((button) => {
    button.addEventListener('click', () => {
      filterButtons.forEach((chip) => chip.classList.remove('active'));
      button.classList.add('active');
      applyFilter((button.dataset.filter || 'all').toLowerCase());
    });
  });
}
