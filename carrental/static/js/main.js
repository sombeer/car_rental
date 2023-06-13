/*=============== SHOW MENU ===============*/
const navMenu = document.getElementById('nav-menu'),
      navToggle = document.getElementById('nav-toggle'),
      navClose = document.getElementById('nav-close')

/*===== MENU SHOW =====*/
/* Validate if constant exists */
if(navToggle){
    navToggle.addEventListener('click', () =>{
        navMenu.classList.add('show-menu')
    })
}

/*===== MENU HIDDEN =====*/
/* Validate if constant exists */
if(navClose){
    navClose.addEventListener('click', () =>{
        navMenu.classList.remove('show-menu')
    })
}

/*=============== REMOVE MENU MOBILE ===============*/
const navLink = document.querySelectorAll('.nav__link')

function linkAction(){
    const navMenu = document.getElementById('nav-menu')
    // When we click on each nav__link, we remove the show-menu class
    navMenu.classList.remove('show-menu')
}
navLink.forEach(n => n.addEventListener('click', linkAction))

/*=============== CHANGE BACKGROUND HEADER ===============*/
function scrollHeader(){
    const header = document.getElementById('header')
    // When the scroll is greater than 50 viewport height, add the scroll-header class to the header tag
    if(this.scrollY >= 50) header.classList.add('scroll-header'); else header.classList.remove('scroll-header')
}
window.addEventListener('scroll', scrollHeader)

/*=============== POPULAR SWIPER ===============*/
let swiperPopular = new Swiper('.popular__container', {
    loop: true,
    spaceBetween: 24,
    slidesPerView: "auto",
    grabCursor: true,

    pagination: {
      el: ".swiper-pagination",
      dynamicBullets: true,
    },
    breakpoints: {
        768: {
          slidesPerView: 3,
        },
        1024: {
          spaceBetween: 48,
        },
      },
});

/*=============== MIXITUP FILTER FEATURED ===============*/
let mixerFeatured = mixitup('.featured__content', {
    selectors: {
        target: '.featured__card'
    },
    animation: {
        duration: 300
    }
});

/* Link active featured */ 
const linkFeatured = document.querySelectorAll('.featured__item')

function activeFeatured(){
    linkFeatured.forEach(l=> l.classList.remove('active-featured'))
    this.classList.add('active-featured')
}
linkFeatured.forEach(l=> l.addEventListener('click', activeFeatured))

/*=============== SHOW SCROLL UP ===============*/ 
function scrollUp(){
    const scrollUp = document.getElementById('scroll-up');
    // When the scroll is higher than 350 viewport height, add the show-scroll class to the a tag with the scroll-top class
    if(this.scrollY >= 350) scrollUp.classList.add('show-scroll'); else scrollUp.classList.remove('show-scroll')
  }
  window.addEventListener('scroll', scrollUp)

/*=============== SCROLL SECTIONS ACTIVE LINK ===============*/
const sections = document.querySelectorAll('section[id]')

function scrollActive(){
    const scrollY = window.pageYOffset
    
    sections.forEach(current =>{
        const sectionHeight = current.offsetHeight,
        sectionTop = current.offsetTop - 58,
        sectionId = current.getAttribute('id')
        
        if(scrollY > sectionTop && scrollY <= sectionTop + sectionHeight){
            document.querySelector('.nav__menu a[href*=' + sectionId + ']').classList.add('active-link')
        }else{
            document.querySelector('.nav__menu a[href*=' + sectionId + ']').classList.remove('active-link')
        }
    })
}
window.addEventListener('scroll', scrollActive)

/*=============== SCROLL REVEAL ANIMATION ===============*/
const sr = ScrollReveal({
    origin: 'top',
    distance: '60px',
    duration: 2500,
    delay: 400,
    // reset: true
})
  
  sr.reveal(`.home__title, .popular__container, .features__img, .featured__filters`)
  sr.reveal(`.home__subtitle`,{delay: 100})
  sr.reveal(`.home__elec`, {delay: 400})
  sr.reveal(`.home__img`, {delay: 600})
  sr.reveal(`.home__car-data`, {delay: 700, interval: 100, origin: 'bottom'})
  sr.reveal(`.home__button`, {delay: 900, origin: 'bottom'})
  sr.reveal(`.about__group, .offer__data`,{origin: 'left'})
  sr.reveal(`.about__data, .offer__img`,{origin: 'right'})
  sr.reveal(`.features__map`,{delay: 500, origin: 'bottom'})
  sr.reveal(`.features__card`,{interval: 200})
  sr.reveal(`.featured__card, .logos__content, .footer__content`,{interval: 100})


  /*=============== booking form ===============*/
  
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
  ('input[name="datetimes"]').daterangepicker({
    timePicker: true,
    startDate: moment(),
    minDate: minBookingTime,
    maxDate: maxBookingTime,
    locale: {
      format: 'YYYY-MM-DD hh:mm A'
    }
  });
  // Handle form submission
  $('form.home__search').on('submit', function(event) {
    var selectedDate = $('input[name="datetimes"]').val();
    var startDateTime = moment(selectedDate, 'YYYY-MM-DD hh:mm A');
    var endDateTime = startDateTime.clone().add(12, 'hours');
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



    