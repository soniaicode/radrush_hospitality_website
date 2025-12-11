// ============================================
// MOBILE MENU TOGGLE - FIXED VERSION
// ============================================
console.log('🍔 Initializing Mobile Menu...');

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    const body = document.body;

    console.log('Hamburger found:', hamburger);
    console.log('Nav menu found:', navMenu);

    if (hamburger && navMenu) {
        // Hamburger click event
        hamburger.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            console.log('🍔 Hamburger clicked!');
            
            const isActive = navMenu.classList.contains('active');
            
            if (isActive) {
                navMenu.classList.remove('active');
                hamburger.classList.remove('active');
                hamburger.setAttribute('aria-expanded', 'false');
                body.style.overflow = '';
                console.log('❌ Menu closed');
            } else {
                navMenu.classList.add('active');
                hamburger.classList.add('active');
                hamburger.setAttribute('aria-expanded', 'true');
                body.style.overflow = 'hidden';
                console.log('✅ Menu opened');
            }
        });

        // Touch event for mobile
        hamburger.addEventListener('touchstart', function(e) {
            e.preventDefault();
            console.log('👆 Touch detected on hamburger');
            hamburger.click();
        }, { passive: false });

        // Close menu when clicking on a link
        const navLinks = document.querySelectorAll('.nav-menu a');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                console.log('🔗 Nav link clicked, closing menu');
                navMenu.classList.remove('active');
                hamburger.classList.remove('active');
                hamburger.setAttribute('aria-expanded', 'false');
                body.style.overflow = '';
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!hamburger.contains(e.target) && !navMenu.contains(e.target)) {
                if (navMenu.classList.contains('active')) {
                    console.log('🚪 Clicked outside, closing menu');
                    navMenu.classList.remove('active');
                    hamburger.classList.remove('active');
                    hamburger.setAttribute('aria-expanded', 'false');
                    body.style.overflow = '';
                }
            }
        });

        console.log('✅ Mobile menu initialized successfully!');
    } else {
        console.error('❌ Hamburger or nav menu not found!');
    }
});

// Simple Navbar scroll effect
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.pageYOffset > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Intersection Observer for fade-in animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe service cards and feature items
document.addEventListener('DOMContentLoaded', () => {
    const animatedElements = document.querySelectorAll('.service-card, .feature-item');
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
});

// Scroll to Top Button
document.addEventListener('DOMContentLoaded', () => {
    // Create scroll to top button
    const scrollBtn = document.createElement('div');
    scrollBtn.className = 'scroll-to-top';
    scrollBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
    document.body.appendChild(scrollBtn);

    // Show/hide button on scroll
    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            scrollBtn.classList.add('visible');
        } else {
            scrollBtn.classList.remove('visible');
        }
    });

    // Scroll to top on click
    scrollBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
});

// Add loading animation to images
document.addEventListener('DOMContentLoaded', () => {
    const images = document.querySelectorAll('img');
    images.forEach(img => {
        img.addEventListener('load', function() {
            this.style.opacity = '1';
        });
    });
});

// Enhanced form validation
const contactForm = document.querySelector('form');
if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        const email = this.querySelector('input[type="email"]');
        const name = this.querySelector('input[name="name"]');
        const message = this.querySelector('textarea[name="message"]');
        
        let isValid = true;
        
        // Simple validation
        if (name && name.value.trim().length < 2) {
            alert('Please enter a valid name');
            isValid = false;
        }
        
        if (email && !email.value.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)) {
            alert('Please enter a valid email address');
            isValid = false;
        }
        
        if (message && message.value.trim().length < 10) {
            alert('Please enter a message with at least 10 characters');
            isValid = false;
        }
        
        if (!isValid) {
            e.preventDefault();
        }
    });
}

// Parallax effect for hero section
window.addEventListener('scroll', () => {
    const hero = document.querySelector('.hero');
    if (hero) {
        const scrolled = window.pageYOffset;
        hero.style.transform = `translateY(${scrolled * 0.5}px)`;
    }
});

// Add animation on scroll for elements
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const fadeInObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe all cards and sections
document.addEventListener('DOMContentLoaded', () => {
    const elementsToAnimate = document.querySelectorAll('.service-card, .feature-item, .stat-item, .contact-item');
    elementsToAnimate.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        fadeInObserver.observe(el);
    });
});


// Simple Working Image Slider
(function() {
    const slides = document.querySelectorAll('.hero-slide');
    const dots = document.querySelectorAll('.dot');
    const labels = document.querySelectorAll('.label-text');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');
    
    if (!slides || slides.length === 0) return;
    
    let currentIndex = 0;
    let autoSlideInterval;
    
    // Show specific slide
    function showSlide(index) {
        // Remove active from all
        slides.forEach(s => s.classList.remove('active'));
        dots.forEach(d => d.classList.remove('active'));
        labels.forEach(l => l.classList.remove('active'));
        
        // Add active to current
        slides[index].classList.add('active');
        if (dots[index]) dots[index].classList.add('active');
        if (labels[index]) labels[index].classList.add('active');
        
        currentIndex = index;
    }
    
    // Next slide
    function nextSlide() {
        let next = (currentIndex + 1) % slides.length;
        showSlide(next);
    }
    
    // Previous slide
    function prevSlide() {
        let prev = (currentIndex - 1 + slides.length) % slides.length;
        showSlide(prev);
    }
    
    // Start auto slide
    function startAutoSlide() {
        stopAutoSlide();
        autoSlideInterval = setInterval(nextSlide, 4000); // Change every 4 seconds
    }
    
    // Stop auto slide
    function stopAutoSlide() {
        if (autoSlideInterval) {
            clearInterval(autoSlideInterval);
        }
    }
    
    // Button clicks
    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
            nextSlide();
            stopAutoSlide();
            startAutoSlide();
        });
    }
    
    if (prevBtn) {
        prevBtn.addEventListener('click', () => {
            prevSlide();
            stopAutoSlide();
            startAutoSlide();
        });
    }
    
    // Dot clicks
    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
            showSlide(index);
            stopAutoSlide();
            startAutoSlide();
        });
    });
    
    // Label clicks
    labels.forEach((label, index) => {
        label.addEventListener('click', () => {
            showSlide(index);
            stopAutoSlide();
            startAutoSlide();
        });
    });
    
    // Initialize
    showSlide(0);
    startAutoSlide();
    
    console.log('Slider started with', slides.length, 'images');
})();


// ============================================
// IMAGE SLIDER - AUTO CHANGE EVERY 3 SECONDS
// ============================================
(function() {
    console.log('🎬 Initializing Image Slider...');
    
    const slides = document.querySelectorAll('.hero-slide');
    const dots = document.querySelectorAll('.dot');
    const labels = document.querySelectorAll('.label-text');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');
    
    if (!slides || slides.length === 0) {
        console.log('❌ No slides found!');
        return;
    }
    
    console.log('✅ Found', slides.length, 'slides');
    
    let currentIndex = 0;
    let autoSlideInterval;
    
    // Show specific slide
    function showSlide(index) {
        console.log('📸 Showing slide:', index + 1, 'of', slides.length);
        
        // Remove active from all
        slides.forEach((s, i) => {
            s.classList.remove('active');
        });
        
        dots.forEach((d, i) => {
            d.classList.remove('active');
        });
        
        labels.forEach((l, i) => {
            l.classList.remove('active');
        });
        
        // Add active to current
        slides[index].classList.add('active');
        if (dots[index]) dots[index].classList.add('active');
        if (labels[index]) labels[index].classList.add('active');
        
        currentIndex = index;
    }
    
    // Next slide
    function nextSlide() {
        let next = (currentIndex + 1) % slides.length;
        showSlide(next);
    }
    
    // Previous slide
    function prevSlide() {
        let prev = (currentIndex - 1 + slides.length) % slides.length;
        showSlide(prev);
    }
    
    // Start auto slide - CHANGE EVERY 3 SECONDS
    function startAutoSlide() {
        stopAutoSlide();
        console.log('▶️ Auto-slide started (3 seconds interval)');
        autoSlideInterval = setInterval(() => {
            nextSlide();
        }, 3000); // 3 seconds = 3000 milliseconds
    }
    
    // Stop auto slide
    function stopAutoSlide() {
        if (autoSlideInterval) {
            clearInterval(autoSlideInterval);
            console.log('⏸️ Auto-slide paused');
        }
    }
    
    // Button clicks
    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
            console.log('➡️ Next button clicked');
            nextSlide();
            stopAutoSlide();
            startAutoSlide();
        });
    }
    
    if (prevBtn) {
        prevBtn.addEventListener('click', () => {
            console.log('⬅️ Previous button clicked');
            prevSlide();
            stopAutoSlide();
            startAutoSlide();
        });
    }
    
    // Dot clicks
    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
            console.log('🔵 Dot', index + 1, 'clicked');
            showSlide(index);
            stopAutoSlide();
            startAutoSlide();
        });
    });
    
    // Label clicks
    labels.forEach((label, index) => {
        label.addEventListener('click', () => {
            console.log('🏷️ Label', index + 1, 'clicked');
            showSlide(index);
            stopAutoSlide();
            startAutoSlide();
        });
    });
    
    // Pause on hover
    const hero = document.querySelector('.hero');
    if (hero) {
        hero.addEventListener('mouseenter', () => {
            stopAutoSlide();
        });
        
        hero.addEventListener('mouseleave', () => {
            startAutoSlide();
        });
    }
    
    // Initialize - Show first slide and start auto-play
    console.log('🎬 Starting slider...');
    showSlide(0);
    startAutoSlide();
    
    console.log('✅ Slider initialized successfully!');
    console.log('⏱️ Images will change every 3 seconds');
})();
