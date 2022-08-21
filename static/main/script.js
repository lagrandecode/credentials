

let menu = document.querySelector('#bars');
let nav  = document.querySelector('.navbar');

menu.onclick = () => {
    menu.classList.toggle('fa-times');
    nav.classList.toggle('open'); 
}