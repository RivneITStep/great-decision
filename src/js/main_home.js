let house_level = document.querySelectorAll('.house_level div');
let house_level_buttons = document.querySelectorAll('.house_level button')
for (let i = 0; i<house_level.length; i++){
    house_level[i].addEventListener('mouseenter', function(){
        house_level_buttons[i].style.marginTop="42px";
        house_level[i].style.width="395px";
        house_level[i].style.height="390px";
        house_level[i].style.zIndex="2";
        house_level[i].style.transition="all linear 0.2s";
    })
    house_level[i].addEventListener('mouseleave', function(){
        house_level_buttons[i].style.marginTop="30px";
        house_level[i].style.width="370px";
        house_level[i].style.height="375px";
        house_level[i].style.zIndex="1";
        house_level[i].style.transition="all linear 0.2s";
        
    })
}
let buttons = document.querySelectorAll('button');
for(let i = 0; i<buttons.length; i++){
    buttons[i].addEventListener('mouseenter', function(){
        buttons[i].style.backgroundColor='#f7941e';
        buttons[i].style.border='solid 1px #f7941e';
        buttons[i].style.color='#fff';
        buttons[i].style.transition='all .4s linear';
    })
    buttons[i].addEventListener('mouseleave', function(){
        buttons[i].style.backgroundColor='#f3d43d';
        buttons[i].style.border='solid 1px #f3d43d';
        buttons[i].style.color='#4e4751';
        buttons[i].style.transition='all .4s linear';
    })
}