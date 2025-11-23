// PSIOP Landing Page - JavaScript Interactions

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    
    // Smooth scroll for anchor links
    initSmoothScroll();
    
    // Animate sections on scroll
    initScrollAnimations();
    
    // Interactive brain map state change
    initBrainStateAnimation();
    
    // Mode cards modal functionality
    initModeModals();
    
    // Form validation
    initFormValidation();
    
});

/**
 * Smooth scroll for navigation links
 */
function initSmoothScroll() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            // Skip if href is just "#"
            if (href === '#') {
                e.preventDefault();
                return;
            }
            
            const target = document.querySelector(href);
            
            if (target) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

/**
 * Animate sections when they come into view
 */
function initScrollAnimations() {
    const fadeElements = document.querySelectorAll('.fade-in');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });
    
    fadeElements.forEach(element => {
        observer.observe(element);
    });
}

/**
 * Animate brain state text changes
 */
function initBrainStateAnimation() {
    const brainState = document.getElementById('brainState');
    
    if (!brainState) return;
    
    const states = ['Фокус', 'Спокойствие', 'Стресс', 'Усталость'];
    let currentIndex = 0;
    
    // Change state every 3 seconds
    setInterval(() => {
        currentIndex = (currentIndex + 1) % states.length;
        
        // Fade out
        brainState.style.opacity = '0';
        
        // Change text and fade in
        setTimeout(() => {
            brainState.textContent = states[currentIndex];
            brainState.style.opacity = '1';
        }, 300);
        
    }, 3000);
    
    // Add hover effect to brain map
    const brainMap = document.getElementById('brainMap');
    if (brainMap) {
        brainMap.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.05)';
        });
        
        brainMap.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    }
}

/**
 * Mode cards modal functionality
 */
function initModeModals() {
    const modeCards = document.querySelectorAll('.mode-card');
    const modal = document.getElementById('modeModal');
    const modalBody = document.getElementById('modalBody');
    const modalClose = document.getElementById('modalClose');
    
    if (!modal || !modalBody) return;
    
    // Mode details content
    const modeDetails = {
        meditation: {
            title: 'Медитация',
            content: `
                <h3>Режим медитации</h3>
                <p>Погружайтесь в глубокие медитативные состояния с помощью персонализированной обратной связи от PSIOP.</p>
                <ul>
                    <li>Интерактивный круг «вдох/выдох» синхронизирован с вашим дыханием</li>
                    <li>Адаптивная музыка автоматически подстраивается под ваш ЭЭГ-сигнал</li>
                    <li>Дыхательные подсказки для достижения более глубоких состояний</li>
                    <li>Детальный разбор сессии: динамика альфа/тета ритмов, моменты максимального спокойствия</li>
                    <li>Рекомендации по оптимальной длительности и времени практики</li>
                </ul>
            `
        },
        focus: {
            title: 'Фокус и продуктивность',
            content: `
                <h3>Фокус и продуктивность</h3>
                <p>Управляйте своей когнитивной нагрузкой и работайте в оптимальном режиме без выгорания.</p>
                <ul>
                    <li>Непрерывный мониторинг уровня фокуса, усталости и стресса</li>
                    <li>Умные уведомления о необходимости перерыва до наступления усталости</li>
                    <li>Рекомендации по оптимальному времени возвращения к работе</li>
                    <li>Определение ваших «часов максимальной продуктивности»</li>
                    <li>Аналитика паттернов работы за день/неделю/месяц</li>
                    <li>Предложения по оптимизации рабочего графика</li>
                </ul>
            `
        },
        communication: {
            title: 'EQ-коуч',
            content: `
                <h3>EQ-коуч (коммуникации)</h3>
                <p>Снижайте конфликтность в диалогах и выстраивайте более осознанные коммуникации.</p>
                <ul>
                    <li>Анализ ЭЭГ-сигналов и речи в реальном времени (в разработке)</li>
                    <li>Мягкие уведомления при обнаружении признаков эскалации</li>
                    <li>Предложение сделать паузу и выполнить дыхательный протокол</li>
                    <li>Подсказки для возвращения к конструктивному диалогу</li>
                    <li>Аналитика паттернов стресса в коммуникациях</li>
                    <li>Рекомендации по времени для важных разговоров</li>
                </ul>
            `
        }
    };
    
    // Open modal on mode card click
    modeCards.forEach(card => {
        const modeBtn = card.querySelector('.mode-btn');
        const mode = card.getAttribute('data-mode');
        
        if (modeBtn && mode && modeDetails[mode]) {
            modeBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                modalBody.innerHTML = modeDetails[mode].content;
                modal.classList.add('active');
            });
        }
        
        // Also allow clicking on the card itself
        card.addEventListener('click', () => {
            if (mode && modeDetails[mode]) {
                modalBody.innerHTML = modeDetails[mode].content;
                modal.classList.add('active');
            }
        });
    });
    
    // Close modal
    if (modalClose) {
        modalClose.addEventListener('click', () => {
            modal.classList.remove('active');
        });
    }
    
    // Close modal when clicking outside
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.classList.remove('active');
        }
    });
    
    // Close modal on Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('active')) {
            modal.classList.remove('active');
        }
    });
}

/**
 * Client-side form validation
 */
function initFormValidation() {
    const form = document.getElementById('leadForm');
    
    if (!form) return;
    
    form.addEventListener('submit', function(e) {
        let isValid = true;
        const errors = [];
        
        // Get form fields
        const nameInput = document.getElementById('name');
        const emailInput = document.getElementById('email');
        
        // Remove previous error states
        document.querySelectorAll('.form-input').forEach(input => {
            input.classList.remove('error');
        });
        
        // Validate name
        if (!nameInput.value.trim()) {
            isValid = false;
            nameInput.classList.add('error');
            errors.push('Пожалуйста, укажите ваше имя');
        }
        
        // Validate email
        const emailValue = emailInput.value.trim();
        if (!emailValue) {
            isValid = false;
            emailInput.classList.add('error');
            errors.push('Пожалуйста, укажите ваш email');
        } else if (!isValidEmail(emailValue)) {
            isValid = false;
            emailInput.classList.add('error');
            errors.push('Пожалуйста, укажите корректный email адрес');
        }
        
        // If validation fails, prevent form submission and show errors
        if (!isValid) {
            e.preventDefault();
            
            // Show first error (in a real app you might want to show all errors)
            if (errors.length > 0) {
                alert(errors[0]);
            }
            
            // Focus on first error field
            const firstError = form.querySelector('.form-input.error');
            if (firstError) {
                firstError.focus();
            }
        }
    });
    
    // Real-time validation feedback
    const nameInput = document.getElementById('name');
    const emailInput = document.getElementById('email');
    
    if (nameInput) {
        nameInput.addEventListener('blur', function() {
            if (!this.value.trim()) {
                this.classList.add('error');
            } else {
                this.classList.remove('error');
            }
        });
    }
    
    if (emailInput) {
        emailInput.addEventListener('blur', function() {
            const emailValue = this.value.trim();
            if (!emailValue || !isValidEmail(emailValue)) {
                this.classList.add('error');
            } else {
                this.classList.remove('error');
            }
        });
    }
}

/**
 * Email validation helper
 */
function isValidEmail(email) {
    // Basic email validation
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

/**
 * Add transition styles to brain state
 */
const brainState = document.getElementById('brainState');
if (brainState) {
    brainState.style.transition = 'opacity 0.3s ease-in-out';
}

/**
 * Add transition to brain map
 */
const brainMap = document.getElementById('brainMap');
if (brainMap) {
    brainMap.style.transition = 'transform 0.3s ease-in-out';
}

