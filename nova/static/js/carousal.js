new Glide('.hero__glide', {
    type: 'carousel',
    perView: 1,
    autoplay: 3000, // Set the autoplay interval in milliseconds (e.g., 3000 = 3 seconds)
    hoverpause: true // Pause autoplay when hovering over the carousel
  }).mount();

  // tetimonial carousal 
  new Glide('.testimonial-carousel', { // Use the unique class name "testimonial-carousel"
    type: 'carousel',
    perView: 3, // Display two reviews at a time
    focusAt: 'center', // Center the focused slide
    autoplay: 3000, // Transition every 3 seconds (adjust as needed)
    breakpoints: {
      640: {
        perView: 1 // Display one review at a time on smaller screens
      }
    }
  }).mount();