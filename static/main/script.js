

let x = document.getElementById('bars');
let y  = document.getElementById('navid');

x.onclick = () => {
    x.classList.toggle('fa-times');
    y.classList.toggle('.open'); 
}