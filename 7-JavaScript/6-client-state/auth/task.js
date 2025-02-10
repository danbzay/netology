if (localStorage.getItem('id') != null) {
  showGreeting(localStorage.getItem("id"));
}

const url = 'https://students.netoservices.ru/nestjs-backend/auth';

const form = document.querySelector('#signin__form');

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const formData = new FormData(form);
  const response = await fetch(url, {method: 'POST', body: formData});
  const json = await response.json();
  if (json.success == true) {
    showGreeting(json.user_id);
    localStorage.setItem("id", json.user_id);
  }
  if (json.success == false) {
    form.append('Неверный логин/пароль');
  }
});

function showGreeting(id) {
  document.querySelector('#signin').classList.remove('signin_active');
  const divWelcome = document.querySelector('#welcome');
  divWelcome.classList.add('welcome_active');
  divWelcome.textContent = 'Добро пожаловать, пользователь #';
  const span = document.createElement('span');
  span.id = id;
  span.textContent = id;
  divWelcome.append(span);
}
