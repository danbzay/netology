const cookie = document.getElementById("cookie");
var counter = 0;
const clickerCounter = document.getElementById("clicker__counter");
const clickFrequencyText = document.createElement("span");
const clickFrequency = document.createElement("span");
clickFrequencyText.innerHTML = "<br/>Скорость клика: "; 
clickerCounter.insertAdjacentElement("afterend", clickFrequencyText);
clickFrequencyText.insertAdjacentElement("afterend", clickFrequency);
var currentTime = Date.now(), lastTime;

cookie.onclick = () => {
  counter += 1;
  clickerCounter.textContent = counter;
  cookie.width *= 1 + (counter % 2 - 0.5) * 0.1;
  cookie.height *= 1 + (counter % 2 - 0.5) * 0.1;
  lastTime = currentTime;
  currentTime = Date.now();
  clickFrequency.textContent = Number(1000/(currentTime - lastTime)).toFixed(2);
};
  
