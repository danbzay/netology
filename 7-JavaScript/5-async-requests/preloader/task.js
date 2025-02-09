const url = 'https://students.netoservices.ru/nestjs-backend/slow-get-courses';
const xhr = new XMLHttpRequest();
let order = 0;

if (localStorage.length > 0) {
  const courses = {...localStorage};
  showCourses(courses);
} else { 
  xhr.open('GET', url);
  xhr.send();
  xhr.addEventListener('load', () => {
    const courses = JSON.parse(xhr.response).response.Valute;
    showCourses(courses);
  });
}

function showCourses(courses) {
  document.querySelector('#loader').classList.remove('loader_active');
  const items = document.querySelector('#items');
  for (const c in courses) {
    const codeValue = {};
    codeValue[c] = {Value: courses[c].Value};
    const item =document.createElement('div');
    item.classList.add('item');
    const code = document.createElement('div');
    code.classList.add('item__code');
    code.textContent = c;
    const value = document.createElement('div');
    value.classList.add('item__value');
    value.textContent = 
      typeof courses[c].Value != 'undefined' ? courses[c].Value : courses[c];
    const currency = document.createElement('div');
    currency.classList.add('item__currency');
    currency.textContent = 'руб';
    item.append(code, value, currency);
    items.append(item);
    //let str = {String(c):{'Value': courses[c].Value}}));
    localStorage.setItem(order++, JSON.stringify(codeValue));
  }
  order = 0;
}
