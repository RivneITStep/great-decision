//Variable
var glavna = document.getElementById('glav');
var slike = document.getElementsByClassName('slk');
var box = document.getElementsByClassName('slike')[0];
var left = document.getElementsByClassName('left')[0];
var right = document.getElementsByClassName('rightt')[0];

for (var i = 0; i < slike.length; i++) {
  slike[i].addEventListener('click', run);
}

function run() { 
  var displ = this.getAttribute("src");
  glavna.setAttribute("src", displ);
}

left.addEventListener("click", lft);
right.addEventListener("click", rght);
var pos = 0;

function lft() { 
  if (pos != null) {
    if (pos == 0) { 
      console.log(pos + 'if');
    } else {
      pos += 150;
      box.style.marginLeft = pos + 'px';
      box.style.transition = 'all 1s';
      console.log(pos + 'left');
    }
  }
}

function rght() { 
  if (pos != null) {
    pos -= 150;
    box.style.marginLeft = pos + 'px';
    box.style.transition = 'all 1s';
    console.log(pos + 'rght');
    if (pos == -2400) { 
      pos = 150;
    }
  }
}
