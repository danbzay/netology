const rotator = document.querySelectorAll('.rotator__case'); 
let current = 0;

const rotate = function() {
  rotator[current].classList.remove('rotator__case_active');
  if (++current == rotator.length) {
    current = 0;
  } 
  rotator[current].classList.add('rotator__case_active');
  rotator[current].style.color = rotator[current].dataset.color;
  setTimeout(rotate, rotator[current].dataset.speed);
}

setTimeout(rotate, rotator[current].dataset.speed);
