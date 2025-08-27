document.addEventListener("DomcontentLoaded", () => {
  const board = document.querySelector(".board");
  for (let i = 0; i < 16; i++) {
    let hole = document.createElement("div");
    hole.classList.add("hole");
    hole.setAttribute("data-index", i);
    board.appendChild(hole);
  }
  const head = document.createElement("img");
  head.setAttribute("src","img/goblin.png");

  board.querySelector('[data-index=1]')//Math.floor(Math.random()*15)])
  .appendChild(head);
});
