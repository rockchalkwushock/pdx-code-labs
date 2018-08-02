const board = document.getElementById('board')
const scoreboard = document.getElementById('scoreboard')
let score = 0
const ROWS = 5
const COLUMNS = 4

for (let i = 0; i < ROWS; i++) {
  const row = document.createElement('div')
  board.appendChild(row)
  for (let j = 0; j < COLUMNS; j++) {
    const column = document.createElement('img')
    column.src = './images/hole.jpg'
    row.appendChild(column)
  }
}

let mole = setInterval(() => {
  const ran1 = Math.floor(Math.random() * 5)
  const ran2 = Math.floor(Math.random() * 4)
  board.childNodes[ran1].childNodes[ran2].src = './images/mole.jpg'
  board.childNodes[ran1].childNodes[ran2].addEventListener('click', () => {
    score++
    scoreboard.innerHTML = score
    board.childNodes[ran1].childNodes[ran2].src = './images/hole.jpg'
  })
}, 1000)
