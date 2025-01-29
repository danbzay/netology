const holes = document.getElementsByClassName("hole");
var winCounter = 0, loseCounter = 0;
const dead = document.getElementById("dead");
const lost = document.getElementById("lost");
for (const hole of holes) {
  hole.addEventListener("click", (e) => {
    if (e.target.className.includes("hole_has-mole")) {
      winCounter += 1;
      if (winCounter >= 10) {
        alert("Победа")
        winCounter = 0;
        loseCounter = 0;
        lost.textContent = loseCounter;
      }
      dead.textContent = winCounter;
    } else {
      loseCounter += 1;
      if (loseCounter >= 5) {
        alert("Поражение")
        winCounter = 0;
        dead.textContent = winCounter;
        loseCounter = 0;
      }
      lost.textContent = loseCounter;
    }
  });
}

