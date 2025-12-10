// SIMPLE WORKING SLIDER - GUARANTEED TO WORK
console.log('=================================');
console.log('🎬 SLIDER LOADING...');
console.log('=================================');

// Wait for page to load
window.addEventListener('load', function() {
    console.log('✅ Page loaded, starting slider...');
    
    // Get all elements
    const slides = document.querySelectorAll('.hero-slide');
    const dots = document.querySelectorAll('.dot');
    const labels = document.querySelectorAll('.label-text');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');
    
    // Check if slides exist
    if (!slides || slides.length === 0) {
        console.error('❌ ERROR: No slides found!');
        console.log('Looking for elements with class: .hero-slide');
        return;
    }
    
    console.log('✅ Found ' + slides.length + ' slides');
    console.log('✅ Found ' + dots.length + ' dots');
    console.log('✅ Found ' + labels.length + ' labels');
    
    let currentSlide = 0;
    let autoplayInterval;
    
    // Function to change slide
    function changeSlide(newIndex) {
        console.log('📸 Changing to slide ' + (newIndex + 1) + ' of ' + slides.length);
        
        // Remove active from all
        for (let i = 0; i < slides.length; i++) {
            slides[i].classList.remove('active');
        }
        for (let i = 0; i < dots.length; i++) {
            dots[i].classList.remove('active');
        }
        for (let i = 0; i < labels.length; i++) {
            labels[i].classList.remove('active');
        }
        
        // Add active to current
        slides[newIndex].classList.add('active');
        if (dots[newIndex]) dots[newIndex].classList.add('active');
        if (labels[newIndex]) labels[newIndex].classList.add('active');
        
        currentSlide = newIndex;
    }
    
    // Next slide
    function nextSlide() {
        let next = (currentSlide + 1) % slides.length;
        changeSlide(next);
    }
    
    // Previous slide
    function prevSlide() {
        let prev = (currentSlide - 1 + slides.length) % slides.length;
        changeSlide(prev);
    }
    
    // Start autoplay
    function startAutoplay() {
        if (autoplayInterval) {
            clearInterval(autoplayInterval);
        }
        autoplayInterval = setInterval(function() {
            nextSlide();
        }, 3000); // 3 seconds
        console.log('▶️ Autoplay started (3 second interval)');
    }
    
    // Stop autoplay
    function stopAutoplay() {
        if (autoplayInterval) {
            clearInterval(autoplayInterval);
            console.log('⏸️ Autoplay paused');
        }
    }
    
    // Add button listeners
    if (nextBtn) {
        nextBtn.addEventListener('click', function() {
            console.log('➡️ Next button clicked');
            nextSlide();
            stopAutoplay();
            startAutoplay();
        });
    }
    
    if (prevBtn) {
        prevBtn.addEventListener('click', function() {
            console.log('⬅️ Previous button clicked');
            prevSlide();
            stopAutoplay();
            startAutoplay();
        });
    }
    
    // Add dot listeners
    for (let i = 0; i < dots.length; i++) {
        dots[i].addEventListener('click', function() {
            console.log('🔵 Dot ' + (i + 1) + ' clicked');
            changeSlide(i);
            stopAutoplay();
            startAutoplay();
        });
    }
    
    // Add label listeners
    for (let i = 0; i < labels.length; i++) {
        labels[i].addEventListener('click', function() {
            console.log('🏷️ Label ' + (i + 1) + ' clicked');
            changeSlide(i);
            stopAutoplay();
            startAutoplay();
        });
    }
    
    // Initialize
    console.log('🎬 Initializing slider...');
    changeSlide(0);
    startAutoplay();
    
    console.log('=================================');
    console.log('✅ SLIDER READY!');
    console.log('⏱️ Images will change every 3 seconds');
    console.log('=================================');
});
