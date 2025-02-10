const url = 'https://students.netoservices.ru/nestjs-backend/slow-get-courses';
const xhr = new XMLHttpRequest();
let order = 0;

if (localStorage.length > 0) {
  showCourses(getCoursesFromStorage());
} else { 
  xhr.open('GET', url);
  xhr.send();
  xhr.addEventListener('load', () => {
    const responseData = JSON.parse(xhr.response).response.Valute;
    showCourses(saveCourses(responseData));
  });
}

//courses: {order: [code, value]}
function getCoursesFromStorage() {
  const storage = {...localStorage};
  const courses = {};
  for (let order = 0; order < localStorage.length; order++) {
    courses[order] = JSON.parse(storage[order]);
  }
  return courses;
}

function showCourses(courses) {
  document.querySelector('#loader').classList.remove('loader_active');
  for (let order = 0; order < Object.keys(courses).length; order++) {
    const divItem =document.createElement('div');
    divItem.classList.add('item');
    const divCode = document.createElement('div');
    divCode.classList.add('item__code');
    divCode.textContent = courses[order][0];
    const divValue = document.createElement('div');
    divValue.classList.add('item__value');
    divValue.textContent = courses[order][1];
    const divCurrency = document.createElement('div');
    divCurrency.classList.add('item__currency');
    divCurrency.textContent = 'руб';
    divItem.append(divCode, divValue, divCurrency);
    document.querySelector('#items').append(divItem);
  }
}

function saveCourses(responseData) {
  let order = 0;
  const courses = {};
  for (item in responseData) {
    localStorage.setItem(order, `["${item}", ${responseData[item].Value}]`);
    courses[order] = [item, responseData[item].Value];
    order++;
  }
  return courses;
}

