const tabs = document.querySelectorAll('.tab');
const tabsContent = document.querySelectorAll('.tab__content'); 
let active = 0;
for (let i=0; i<3; i++) {
  tabs[i].addEventListener('click', (e) => {
    tabs[i].classList.add('tab_active');
    tabs[active].classList.remove('tab_active');
    tabsContent[i].classList.add('tab__content_active');
    tabsContent[active].classList.remove('tab__content_active');
    active = i;
  });
}


