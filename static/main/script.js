

let x = document.getElementById('bars');
let y  = document.getElementById('navid');

x.onclick = () => {
    x.classList.toggle('fa-times');
    y.classList.toggle('open'); 
}


//Oluwaseun Ogunmolu//

var swiper = new Swiper(".home-container", {
    spaceBetween: 30,
    centeredSlides: true,
    autoplay: {
      delay: 7500,
      disableOnInteraction: false,
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    loop:true,
  });


  var swiper = new Swiper(".review-container", {
    spaceBetween: 30,
    centeredSlides: true,
    autoplay: {
      delay: 7500,
      disableOnInteraction: false,
    },
    loop:true,
  });