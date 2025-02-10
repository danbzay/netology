const textarea = document.querySelector('#editor');

if (localStorage.length > 0) {
  textarea.value = localStorage[0];
}

textarea.addEventListener('input', () => {
  setTimeout(() => localStorage[0] = textarea.value, 1000);
});

const resetBtn = document.createElement('button');
resetBtn.textContent = 'reset';
resetBtn.addEventListener('click', () => {
  localStorage.clear();
  textarea.value = '';
});

textarea.after(resetBtn);
