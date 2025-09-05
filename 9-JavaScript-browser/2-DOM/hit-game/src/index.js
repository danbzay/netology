import "./css/style.css";

document.addEventListener("DOMContentLoaded", () => {
  const board = document.querySelector(".board");
  for (let i = 0; i < 16; i++) {
    let hole = document.createElement("div");
    hole.classList.add("hole");
    hole.setAttribute("data-index", i);
    board.appendChild(hole);
  }
  const head = document.createElement("img");
  head.classList.add("goblin");
  head.setAttribute("src","img/goblin.png");
  head.setAttribute("alt","G");
  setInterval( () => {
    let goblinHoleIndex = Math.floor(Math.random()*15);
    board.querySelector(`[data-index="${ goblinHoleIndex }"]`)
    .appendChild(head);
  }, 1000);
});
