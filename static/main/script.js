

let x = document.querySelector('#bars');
let y  = document.querySelector('#navid');

x.onclick = () => {
    x.classList.toggle('fa-times');
    y.classList.toggle('.navbar .open'); 
}