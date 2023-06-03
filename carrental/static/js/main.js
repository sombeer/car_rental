// JavaScript code
window.addEventListener("DOMContentLoaded", function() {
  const slides = document.querySelectorAll(".home__image .slide");
  let currentSlide = 0;

  setInterval(function() {
    slides[currentSlide].classList.remove("active");
    currentSlide = (currentSlide + 1) % slides.length;
    slides[currentSlide].classList.add("active");
  }, 5000);
});

// Slideshow functionality
const slides = document.querySelectorAll('.slide');
let currentSlide = 0;

function showSlide(n) {
  // Hide all slides
  slides.forEach(slide => {
    slide.classList.remove('active');
  });

  // Show the desired slide
  slides[n].classList.add('active');
}

function changeSlide() {
  currentSlide++;

  // Wrap around to the first slide if reached the end
  if (currentSlide >= slides.length) {
    currentSlide = 0;
  }

  showSlide(currentSlide);
}

// Automatic slideshow
setInterval(changeSlide, 5000);

$(document).ready(function() {
  // Add animations to elements
  $('.animate__animated').addClass('animate__fadeIn');

  // Initialize the slider
  $('.slideshow').slick({
    dots: true,
    autoplay: true,
    autoplaySpeed: 5000,
    arrows: false,
  });
});

document.addEventListener('DOMContentLoaded', function() {
  // Set minimum booking time to 12 hours
  var minBookingTime = moment().add(12, 'hours');
  
  // Set maximum booking time to 30 days
  var maxBookingTime = moment().add(30, 'days');
  
  // Initialize the DateTimePicker with the specified options
  $('input[name="datetimes"]').daterangepicker({
    timePicker: true,
    startDate: moment().startOf('hour'),
    minDate: minBookingTime,
    maxDate: maxBookingTime,
    locale: {
      format: 'YYYY-MM-DD hh:mm A'
    }
  });
  
  // Set the default date and time to today
  $('input[name="datetimes"]').val(moment().format('YYYY-MM-DD hh:mm A'));
  
  // Handle form submission
  $('form.home__search').on('submit', function(event) {
    var selectedDate = $('input[name="datetimes"]').val();
    var startDateTime = moment(selectedDate, 'YYYY-MM-DD hh:mm A');
    var endDateTime = moment(selectedDate, 'YYYY-MM-DD hh:mm A').add(12, 'hours');
    var currentDateTime = moment();
  
    if (endDateTime.isBefore(startDateTime) || currentDateTime.isAfter(endDateTime)) {
      event.preventDefault(); // Prevent form submission
  
      // Show the popup
      $('#popup').show();
  
      // Hide the popup after 3 seconds
      setTimeout(function() {
        $('#popup').hide();
      }, 3000);
    }
  });
});



    document.getElementById("loginForm").addEventListener("submit", function(event) {
      event.preventDefault(); // Prevent form submission

      var username = document.getElementById("username").value;
      var password = document.getElementById("password").value;

      // Send a request to the server to check if the credentials are valid
      // Replace the serverRequest() function with your actual server-side logic
      serverRequest(username, password);
    });

   
   document.write(new Date().getFullYear()); 