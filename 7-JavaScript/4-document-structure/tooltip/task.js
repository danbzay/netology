let active = null;
const hasTooltips = document.querySelectorAll('.has-tooltip');
for (let i = 0; i < hasTooltips.length; i++) {
  let t = document.createElement('div');
  t.append(hasTooltips[i].title);
  hasTooltips[i].removeAttribute('title');
  t.classList.add('tooltip');
  hasTooltips[i].after(t);
  hasTooltips[i].addEventListener('click', (e) => {
    e.preventDefault();
    let position = hasTooltips[i].getBoundingClientRect();
    if (active != null) {
      tooltips[active].classList.remove('tooltip_active');
    }
    if (active != i) {
      tooltips[i].classList.add('tooltip_active');
      let tooltipRectangle = tooltips[i].getBoundingClientRect();
      if (window.innerWidth - position.left > tooltipRectangle.width) {
        tooltips[i].style.left = position.left + 'px';
      } else {
        tooltips[i].style.left = (position.right - tooltipRectangle.width) 
          + 'px';
      }
      if (window.innerHeight - position.bottom > tooltipRectangle.height) {
        tooltips[i].style.top = position.bottom + 'px';
        tooltips[i].dataset.position = 'bottom';
      } else {
        tooltips[i].style.top = (position.top - tooltipRectangle.height) + 'px';
        tooltips[i].dataset.position = 'top';
      }
      active = i;
    } else {
      active = null;
    }
  });
}
const tooltips = document.querySelectorAll('.tooltip');

