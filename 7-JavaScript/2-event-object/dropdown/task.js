document.querySelector('.card').style.setProperty('text-align','left');
const value = document.querySelector('.dropdown__value');
const list = document.querySelector('.dropdown__list');
list.style.setProperty('left','0px');
value.addEventListener('click', (e) => {
  list.classList.add('dropdown__list_active');
});
list.querySelectorAll('a').forEach((item) => {
  item.href = "#";
  item.addEventListener('click', (e) => {
    value.textContent = item.textContent; 
    list.classList.remove('dropdown__list_active');

  });
});

