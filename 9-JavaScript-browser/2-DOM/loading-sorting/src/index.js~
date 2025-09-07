import movies from './movies.json';

const moviesTable = document.createElement('table');

for (const movie of movies) {
  const tr = document.createElement('tr');
  tr.dataset.id = movie.id;
  tr.dataset.title = movie.title;
  tr.dataset.imdb = movie.imdb;
  tr.dataset.year = movie.year;
  let td = document.createElement('td');
  td.textContent = '#' + movie.id;
  tr.appendChild(td);
  td = document.createElement('td');
  td.textContent = movie.title;
  tr.appendChild(td);
  td = document.createElement('td');
  td.textContent = '(' + movie.year + ')';
  tr.appendChild(td);
  td = document.createElement('td');
  td.textContent = 'imdb' + movie.imdb;
  tr.appendChild(td);
  moviesTable.appendChild(tr);
}
document.body.appendChild(moviesTable);


let sortCounter = 0;
const rows = [...moviesTable.querySelectorAll('tr')];
const dataKeys = Object.keys(rows[0].dataset);
let p = document.createElement('p');

const sortIntervalID = setInterval( () => {
  sortCounter %= 8;
  rows.sort(compareRows);  
  for ( const row in rows ) {
    moviesTable.appendChild(rows[row]);
  }
  p.textContent = ('Sorting field: ' + dataKeys[Math.floor(sortCounter/2)] + 
    ' order: ' + ((sortCounter % 2 == 0) ? 'ascending' : 'descending'));
  document.body.appendChild(p);
  sortCounter++;
}, 5000)

function compareRows(a, b) {
  const aString = a.dataset[dataKeys[Math.floor(sortCounter/2)]];    
  const bString = b.dataset[dataKeys[Math.floor(sortCounter/2)]];
  //compare strings with removed numbers
  let result = aString.replace(/[\d\.]/g, '')
    .localeCompare(bString.replace(/[\d\.]/g, ''));
  //compare numbers if equal
  if (result == 0) {
    result = Number(aString) - Number(bString);
  }
  return (1 - 2*(sortCounter%2)) * result;
}

