const form = document.querySelector('form');
const tasks = document.querySelector('#tasks');
let taskId = 0;

if (localStorage.length > 0) {
  for (const id in {...localStorage}) {
    taskId = Number(id);
    addTask(localStorage.getItem(id), taskId);
  } 
}

function addTask(taskTitle, taskId) {
  const task = document.createElement('div');
  task.classList.add('task');
  const title = document.createElement('div');
  title.classList.add('task__title');
  title.textContent = taskTitle;
  localStorage.setItem(taskId, taskTitle);
  const remover = document.createElement('a');
  remover.href = '#';
  remover.classList.add('task__remove');
  remover.innerHTML = '&times;';
  remover.addEventListener('click', () => {
    task.remove();
    localStorage.removeItem(taskId);
  });
  task.append(title, remover);
  tasks.append(task);
  form.reset();
}

form.addEventListener('submit', (e) => {
  e.preventDefault();
  addTask(form.querySelector('#task__input').value, ++taskId);
});

