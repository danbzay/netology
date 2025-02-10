const form = document.querySelector('#form');
const progress = document.getElementById('progress');

const xhr = new XMLHttpRequest();
const url = 'https://students.netoservices.ru/nestjs-backend/upload'
const fileData = new FormData(form);
xhr.open("POST", url);

form.addEventListener('submit', (e) => {
  e.preventDefault();
  xhr.send(fileData);
});

xhr.upload.addEventListener("loadstart", (event) => {
  progress.value = 0;
  progress.max = event.total;
});

xhr.upload.addEventListener("progress", (event) => {
  progress.value = event.loaded;
});



