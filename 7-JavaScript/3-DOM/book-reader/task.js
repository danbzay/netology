document.querySelectorAll('a').forEach((a) => {
  if (a.getAttribute('href') == '') {
    a.setAttribute('href', '#');
  }
});
const fonts = document.querySelectorAll('.book__control_font-size .font-size');
const colors = document.querySelectorAll('.book__control_color .color');
const bgColors = document.querySelectorAll('.book__control_background .color');
const book = document.querySelector('#book');

fonts.forEach((element) => {
  element.addEventListener('click', (e) => {
    fonts.forEach((el) => el.classList.remove('font-size_active'));
    element.classList.add('font-size_active');
    book.classList.remove('book_fs-big', 'book_fs-small');
    book.classList.add(
      element.dataset.size ? 'book_fs-' + element.dataset.size : '');
  });
});
colors.forEach((element) => {
  element.addEventListener('click', (e) => {
    colors.forEach((el) => el.classList.remove('color_active'));
    element.classList.add('color_active');
    book.classList.remove('book_color-gray', 'book_color-whitesmoke', 
      'book_color-black');
    book.classList.add('book_color-' + element.dataset.textColor);
  });
});
bgColors.forEach((element) => {
  element.addEventListener('click', (e) => {
    bgColors.forEach((el) => el.classList.remove('color_active'));
    element.classList.add('color_active');
    book.classList.remove('book_bg-gray', 'book_bg-black', 'book_bg-white');
    book.classList.add('book_bg-' + element.dataset.bgColor);
  });
});
