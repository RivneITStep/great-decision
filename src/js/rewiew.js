let caro = document.getElementById('carousel')
let left_btn = document.getElementById('carou_left')
let right_btn = document.getElementById('carou_right')
let text_p = document.querySelectorAll('.text_rew')
let root = document.getElementById('root')
let index = 0
let text_slide = [];

for (let i = 0; i < text_p.length; i ++){
    text_slide[i] = text_p[i];
}

root.innerHTML = text_p[0].innerHTML
root.style.textAlign="center";
root.style.marginTop="25px";

left_btn.addEventListener('click', function(){
    index -- ;
        if(index < 0){
            index = (text_slide.length - 1);
        }
        root.innerHTML = text_p[index].innerHTML;
})
right_btn.addEventListener('click', function(){
    index ++ ;
        if(index == text_slide.length){
            index = 0;
        }
        root.innerHTML = text_p[index].innerHTML;
})