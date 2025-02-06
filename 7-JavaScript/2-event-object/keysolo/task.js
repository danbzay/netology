class Game {
  constructor(container) {
    this.container = container;
    this.statusBar = container.querySelector('.status');
    this.statusBar.innerHTML += 
        '<p>Времени осталось: <span id = "timer"></span>';
    this.wordElement = container.querySelector('.word');
    this.winsElement = container.querySelector('.status__wins');
    this.lossElement = container.querySelector('.status__loss');
    this.timer = this.statusBar.querySelector("#timer");
    this.timerInterval = null;
    this.reset();

    this.registerEvents();
  }

  reset() {
    this.setNewWord();
    this.winsElement.textContent = 0;
    this.lossElement.textContent = 0;
  }

  registerEvents() {
    /*
      TODO:
      Написать обработчик события, который откликается
      на каждый введённый символ.
      В случае правильного ввода символа вызываем this.success()
      При неправильном вводе символа - this.fail();
      DOM-элемент текущего символа находится в свойстве this.currentSymbol.
     */

     addEventListener('keydown', (e) => {
       console.log(e.key, this.currentSymbol.innerText);
     if (!e.ctrlKey) {
       if (e.key.toLowerCase() == this.currentSymbol.innerText.toLowerCase()) {
         this.success();
       } else { 
         this.fail();
       }
     }
       
     });
       
  }

  success() {
    if (this.currentSymbol.classList.contains("symbol_current")) 
      this.currentSymbol.classList.remove("symbol_current");
    this.currentSymbol.classList.add('symbol_correct');
    this.currentSymbol = this.currentSymbol.nextElementSibling;

    if (this.currentSymbol !== null) {
      this.currentSymbol.classList.add('symbol_current');
      return;
    }

    if (++this.winsElement.textContent === 10) {
      alert('Победа!');
      this.reset();
    } else {
      this.setNewWord();
    }
  }

  fail() {
    if (++this.lossElement.textContent === 5) {
      alert('Вы проиграли!');
      this.reset();
    } else {
      this.setNewWord();
    }
  }

  setNewWord() {
    const word = this.getWord();
    this.renderWord(word);
    this.timer.textContent = word.length;
    this.timerInterval = setInterval(() => {
        if(--this.timer.textContent < 0) {
          clearInterval(this.timerInterval);
          this.timerInterval = null;
          this.fail();
        }
      }, 1000);
  }


  getWord() {
    const words = [
        'кот bob',
        'awesome кот',
        'котology',
        'hello э',
        'kitty кэт',
        'rock',
        'youtube',
        'popcorn',
        'cinema',
        'love',
        'javascript'
      ],
      index = Math.floor(Math.random() * words.length);

    return words[index];
  }

  renderWord(word) {
    const html = [...word]
      .map(
        (s, i) =>
          `<span class="symbol ${i === 0 ? 'symbol_current': ''}">${s}</span>`
      )
      .join('');
    this.wordElement.innerHTML = html;

    this.currentSymbol = this.wordElement.querySelector('.symbol_current');
  }
}

new Game(document.getElementById('game'))

