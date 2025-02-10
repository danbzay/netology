const xhr = new XMLHttpRequest();
const url = "https://students.netoservices.ru/nestjs-backend/poll";
xhr.open('GET', url);
xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
xhr.send();
xhr.addEventListener('load', () => {
  renderQuestion(JSON.parse(xhr.response));
});

function renderQuestion(response) {
  document.querySelector('#poll__title').textContent = response.data.title;
  const divAnswers  = document.querySelector('#poll__answers');
  for (let i = 0; i < response.data.answers.length; i++) {
    const button = document.createElement('button');
    button.textContent = response.data.answers[i];
    button.addEventListener('click', () => {
      alert('Спасибо, ваш голос засчитан');
      showResults(response.id, i);
    });
    divAnswers.append(button);
  }
}

function showResults(vote, answer) {
  const xhr1 = new XMLHttpRequest();
  xhr1.open('POST', url);
  xhr1.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
  xhr1.send(`vote=${vote}&answer=${answer}`);
  xhr1.addEventListener('load', () => {
    const stat = JSON.parse(xhr1.response).stat;
    let summ = stat.reduce( (pv, cv) => pv + cv.votes, 0);
    const divPoll = document.querySelector('.poll'); 
    document.querySelector('#poll__answers').remove();
    for(const line of stat) {
      const divLine = document.createElement('div');
      divLine.textContent = 
        `${line.answer}: ${Number(line.votes*100/summ).toFixed(2)}%`;
      divPoll.append(divLine);
    }
  });
}



