const counter = document.getElementById("timer");
const timeCounter = document.createElement("span"); 
counter.insertAdjacentElement('afterend', timeCounter);
timeEnd = Date.now() + Number(counter.textContent) * 1000;
const downloader = document.createElement("a");
downloader.href = "task.js";
downloader.setAttribute("download", "");
downloader.setAttribute("target", "_blank");

function msToHMS( seconds ) {
    let hours = (seconds - seconds % 3600) / 3600; // 3,600 seconds in 1 hour
    seconds = seconds % 3600; // seconds remaining after extracting hours
    let minutes = (seconds - seconds % 60) / 60; // 60 seconds in 1 minute
    seconds = seconds % 60;
    return ("00" + hours).slice(-2) + ":" 
         + ("00" + minutes).slice(-2) + ":"
         + ("00" + seconds).slice(-2);
}

const timerID = setInterval(() => {
  let count = Number(counter.textContent) - 1;
  if (count < 0) {
    clearInterval(timerID);
    alert("Вы победили в конкурсе");
    downloader.click();

  } else {
    counter.textContent = count;
    timeCounter.innerHTML = "<br/>" + 
      msToHMS(Math.floor((timeEnd - Date.now())/1000)); 
  }
}, 1000);

