// ============================================
// MOBILE MENU - STANDALONE SCRIPT
// ============================================

(function() {
    'use strict';
    
    console.log('🍔 Mobile Menu Script Loading...');
    
    function initMobileMenu() {
        const hamburger = document.querySelector('.hamburger');
        const navMenu = document.querySelector('.nav-menu');
        const body = document.body;
        
        console.log('Hamburger element:', hamburger);
        console.log('Nav menu element:', navMenu);
        
        if (!hamburger || !navMenu) {
            console.error('❌ Required elements not found!');
            return;
        }
        
        // Toggle menu function
        function toggleMenu() {
            const isActive = navMenu.classList.contains('active');
            console.log('Toggle menu - Currently active:', isActive);
            
            if (isActive) {
                // Close menu
                navMenu.classList.remove('active');
                hamburger.classList.remove('active');
                hamburger.setAttribute('aria-expanded', 'false');
                body.style.overflow = '';
                console.log('✅ Menu CLOSED');
            } else {
                // Open menu
                navMenu.classList.add('active');
                hamburger.classList.add('active');
                hamburger.setAttribute('aria-expanded', 'true');
                body.style.overflow = 'hidden';
                console.log('✅ Menu OPENED');
            }
        }
        
        // Click event
        hamburger.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            console.log('🍔 HAMBURGER CLICKED!');
            toggleMenu();
        });
        
        // Touch event for mobile devices
        hamburger.addEventListener('touchend', function(e) {
            e.preventDefault();
            e.stopPropagation();
            console.log('👆 HAMBURGER TOUCHED!');
            toggleMenu();
        }, { passive: false });
        
        // Close menu when clicking nav links
        const navLinks = navMenu.querySelectorAll('a');
        navLinks.forEach(function(link) {
            link.addEventListener('click', function() {
                console.log('🔗 Nav link clicked');
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
                    console.log('🚪 Clicked outside - closing menu');
                    navMenu.classList.remove('active');
                    hamburger.classList.remove('active');
                    hamburger.setAttribute('aria-expanded', 'false');
                    body.style.overflow = '';
                }
            }
        });
        
        console.log('✅ Mobile menu initialized successfully!');
    }
    
    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initMobileMenu);
    } else {
        initMobileMenu();
    }
})();
