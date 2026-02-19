// SStech Hub - JavaScript Otimizado

// Throttle helper para performance
function throttle(func, delay) {
    let lastCall = 0;
    return function(...args) {
        const now = new Date().getTime();
        if (now - lastCall < delay) return;
        lastCall = now;
        return func(...args);
    };
}

// Mobile Menu Toggle
const mobileMenuBtn = document.getElementById('mobileMenuBtn');
const mobileMenu = document.getElementById('mobileMenu');
const mobileMenuClose = document.getElementById('mobileMenuClose');
const mobileNavLinks = document.querySelectorAll('.mobile-nav-link');

function toggleMobileMenu() {
    mobileMenuBtn.classList.toggle('active');
    mobileMenu.classList.toggle('active');
    document.body.style.overflow = mobileMenu.classList.contains('active') ? 'hidden' : '';
}

if (mobileMenuBtn) mobileMenuBtn.addEventListener('click', toggleMobileMenu);
if (mobileMenuClose) mobileMenuClose.addEventListener('click', toggleMobileMenu);

mobileNavLinks.forEach(link => {
    link.addEventListener('click', toggleMobileMenu);
});

// Scroll Reveal Animation - Otimizado
const observerOptions = {
    threshold: 0.15,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('revealed');
            observer.unobserve(entry.target); // Para de observar após revelar
        }
    });
}, observerOptions);

// Observe sections com requestIdleCallback para melhor performance
if ('requestIdleCallback' in window) {
    requestIdleCallback(() => {
        document.querySelectorAll('section').forEach(section => {
            section.classList.add('scroll-reveal');
            observer.observe(section);
        });
    });
} else {
    document.querySelectorAll('section').forEach(section => {
        section.classList.add('scroll-reveal');
        observer.observe(section);
    });
}

// Stagger animation for project cards
const projectCards = document.querySelectorAll('.project-card');
projectCards.forEach((card, index) => {
    if (index < 10) { // Limita delay apenas aos primeiros 10
        card.classList.add('stagger-item');
        card.style.animationDelay = `${index * 0.1}s`;
    }
});

// Smooth scroll for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            const headerOffset = 80;
            const elementPosition = target.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
            
            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });
        }
    });
});

// Consolidated Scroll Handler - Throttled para performance
const header = document.querySelector('.header');

const handleScroll = throttle(() => {
    const currentScroll = window.pageYOffset;
    
    // Header effect
    if (header) {
        if (currentScroll > 100) {
            header.style.background = 'rgba(10, 10, 15, 0.95)';
            header.style.boxShadow = '0 5px 30px rgba(0, 247, 255, 0.3)';
        } else {
            header.style.background = 'rgba(10, 10, 15, 0.8)';
            header.style.boxShadow = '0 0 30px rgba(0, 247, 255, 0.2)';
        }
    }
}, 100); // Executa no máximo a cada 100ms

window.addEventListener('scroll', handleScroll, { passive: true });

// Form submission via WhatsApp
const contactForm = document.getElementById('contactForm');
if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        // Capturar dados do formulário
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const subject = document.getElementById('subject').value || 'Contato pelo site';
        const message = document.getElementById('message').value;
        
        // Validar campos obrigatórios
        if (!name || !email || !message) {
            alert('Por favor, preencha todos os campos obrigatórios.');
            return;
        }
        
        // Montar mensagem para WhatsApp
        const whatsappMessage = `🚀 *Novo Contato - SStech Hub*\n\n` +
            `👤 *Nome:* ${name}\n` +
            `📧 *Email:* ${email}\n` +
            `📋 *Assunto:* ${subject}\n\n` +
            `💬 *Mensagem:*\n${message}\n\n` +
            `---\n_Enviado pelo site SStech Hub_`;
        
        // Codificar mensagem para URL
        const encodedMessage = encodeURIComponent(whatsappMessage);
        
        // Número do WhatsApp (mesmo do site)
        const whatsappNumber = '5511984969596';
        
        // Abrir WhatsApp
        const whatsappURL = `https://wa.me/${whatsappNumber}?text=${encodedMessage}`;
        window.open(whatsappURL, '_blank');
        
        // Limpar formulário
        contactForm.reset();
        
        // Feedback visual
        const submitBtn = document.querySelector('.submit-btn');
        const originalText = submitBtn.textContent;
        submitBtn.textContent = 'ENVIADO! ✓';
        submitBtn.style.background = 'linear-gradient(135deg, #22c55e, #16a34a)';
        
        setTimeout(() => {
            submitBtn.textContent = originalText;
            submitBtn.style.background = 'linear-gradient(135deg, var(--neon-cyan), var(--neon-pink))';
        }, 3000);
    });
}

// Console easter egg
console.log('%c🚀 SStech Hub', 'font-size: 20px; font-weight: bold; color: #00f7ff; text-shadow: 0 0 10px #00f7ff;');
console.log('%cSoluções Tecnológicas Integradas', 'font-size: 14px; color: #ff00e6;');
console.log('%cDesenvolvido com tecnologia de ponta', 'font-size: 12px; color: #94a3b8;');
