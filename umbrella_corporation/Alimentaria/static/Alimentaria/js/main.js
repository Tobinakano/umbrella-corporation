const menuToggle = document.querySelector('.menu-toggle');
const menu = document.querySelector('.menu');
const cur = document.getElementById('cur');
const curRing = document.getElementById('cur-r');
const transparentPixel = 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///ywAAAAAAQABAAACAUwAOw==';

const allImages = document.querySelectorAll('img');
allImages.forEach((img) => {
    img.addEventListener('error', () => {
        if (img.dataset.fallbackApplied === '1') {
            img.src = transparentPixel;
            return;
        }

        img.dataset.fallbackApplied = '1';
        img.src = '/static/Alimentaria/img/placeholder.jpg';
    });
});

if (cur && curRing && window.matchMedia('(min-width: 769px)').matches) {
    const moveCursor = (event) => {
        const { clientX, clientY } = event;
        cur.style.left = `${clientX}px`;
        cur.style.top = `${clientY}px`;
        curRing.style.left = `${clientX}px`;
        curRing.style.top = `${clientY}px`;
    };

    window.addEventListener('mousemove', moveCursor);

    const interactiveElements = document.querySelectorAll('a, button, .card, .op-card');
    interactiveElements.forEach((element) => {
        element.addEventListener('mouseenter', () => {
            curRing.style.width = '34px';
            curRing.style.height = '34px';
            curRing.style.borderColor = 'rgba(200, 16, 46, 0.75)';
        });

        element.addEventListener('mouseleave', () => {
            curRing.style.width = '24px';
            curRing.style.height = '24px';
            curRing.style.borderColor = 'rgba(200, 16, 46, 0.45)';
        });
    });
}

if (menuToggle && menu) {
    menuToggle.addEventListener('click', () => {
        const isOpen = menu.classList.toggle('is-open');
        menuToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    menu.querySelectorAll('a').forEach((link) => {
        link.addEventListener('click', () => {
            menu.classList.remove('is-open');
            menuToggle.setAttribute('aria-expanded', 'false');
        });
    });
}

const revealElements = document.querySelectorAll('.reveal');

if (revealElements.length) {
    const revealObserver = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                }
            });
        },
        {
            threshold: 0.15,
        }
    );

    revealElements.forEach((element) => revealObserver.observe(element));
}

const counters = document.querySelectorAll('.counter');

const formatCounterValue = (value, isDecimal) => {
    if (isDecimal) {
        return value.toFixed(1);
    }

    return Math.floor(value).toLocaleString('es-ES');
};

const animateCounter = (counter) => {
    const target = Number(counter.dataset.target || 0);
    const suffix = counter.dataset.suffix || '';
    const isDecimal = String(target).includes('.');
    const duration = 1800;
    const startTime = performance.now();

    const step = (currentTime) => {
        const progress = Math.min((currentTime - startTime) / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3);
        const currentValue = target * eased;
        counter.textContent = `${formatCounterValue(currentValue, isDecimal)}${suffix}`;

        if (progress < 1) {
            requestAnimationFrame(step);
        } else {
            counter.textContent = `${formatCounterValue(target, isDecimal)}${suffix}`;
        }
    };

    requestAnimationFrame(step);
};

if (counters.length) {
    const counterObserver = new IntersectionObserver(
        (entries, observer) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    animateCounter(entry.target);
                    observer.unobserve(entry.target);
                }
            });
        },
        {
            threshold: 0.5,
        }
    );

    counters.forEach((counter) => counterObserver.observe(counter));
}
