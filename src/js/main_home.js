// Збільшення блока з картинкою з плавною анімацією

let house_level = document.querySelectorAll('.house_level div');
let house_level_buttons = document.querySelectorAll('.house_level button')
for (let i = 0; i<house_level.length; i++){
    house_level[i].addEventListener('mouseenter', function(){
        house_level_buttons[i].style.marginTop="47px";
        house_level_buttons[i].style.transition="all 0.2s linear";
        house_level[i].style.width="395px";
        house_level[i].style.height="390px";
        house_level[i].style.zIndex="2";
        house_level[i].style.transition="all linear 0.2s";
    })
    house_level[i].addEventListener('mouseleave', function(){
        house_level_buttons[i].style.marginTop="33px";
        house_level_buttons[i].style.transition="all 0.2s linear";
        house_level[i].style.width="370px";
        house_level[i].style.height="375px";
        house_level[i].style.zIndex="1";
        house_level[i].style.transition="all linear 0.2s";
        
    })
}

// Зміна кольору кнопок при наведенні і відведенні курсора з плавною анімацією

let buttons = document.querySelectorAll('.btn--orange');
for(let i = 0; i<buttons.length; i++){
    buttons[i].addEventListener('mouseenter', function(){ // для більшості кнопок
        buttons[i].style.backgroundColor='#f7941e';
        buttons[i].style.border='solid 1px #f7941e';
        buttons[i].style.color='#fff';
    })
    buttons[i].addEventListener('mouseleave', function(){
        buttons[i].style.backgroundColor='#f3d43d';
        buttons[i].style.border='solid 1px #f3d43d';
        buttons[i].style.color='#4e4751';
    })
    buttons[i].style.transition='all 0.4s linear';
}

let showAllBtn = document.querySelector('.btn--grey');

showAllBtn.addEventListener('mouseenter', function(){ // для однієї кнопки "Показати все"
    showAllBtn.style.backgroundColor='#fff';
    showAllBtn.style.border='solid 1px #4b434f';
    showAllBtn.style.color='#4b434f';
})
showAllBtn.addEventListener('mouseleave', function(){
    showAllBtn.style.backgroundColor='#4b434f';
    showAllBtn.style.border='solid 1px #4b434f';
    showAllBtn.style.color='#fff';
})
showAllBtn.style.transition='all 0.4s linear';