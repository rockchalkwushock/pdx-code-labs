const button = document.getElementById('button')
const numDice = document.getElementById('input').valueAsNumber
const area = document.getElementById('area')
const totalDiv = document.getElementById('total')
let total = 0
const faces = {
  1: './images/one.png',
  2: './images/two.png',
  3: './images/three.png',
  4: './images/four.png',
  5: './images/five.png',
  6: './images/six.png'
}

button.onclick = function(event) {
  event.preventDefault()
  area.innerHTML = ''
  total = 0
  for (let i = 0; i < numDice; i++) {
    const dice = document.createElement('img')
    const random = Math.floor(Math.random() * 6) + 1
    dice.value = random
    dice.src = faces[random]
    total += random
    totalDiv.innerHTML = total
    dice.addEventListener('click', event => {
      event.preventDefault()
      const random2 = Math.floor(Math.random() * 6) + 1
      event.target.value = random2
      event.target.src = faces[random2]
    })
    area.appendChild(dice)
  }
}
