function shuffle(array) {
  return array.sort(() => Math.random() - 0.5);
}

const imagelist = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']; // nummers van buttons
let flippedCardRow1 = null;
let flippedCardRow2 = null;

const buttonsContainer = document.getElementById('buttons');
const firstCards = document.createElement('div');
const secondCards = document.createElement('div');

shuffle(imagelist).forEach((image) => {
  const button = createCardButton(image);
  firstCards.appendChild(button);
});

shuffle([...imagelist]).forEach((image) => {
  const button = createCardButton(image);
  secondCards.appendChild(button);
});


buttonsContainer.append(firstCards, secondCards);

function createCardButton(cardId) {
  const button = document.createElement('button');
  button.id = cardId;
  const image = document.createElement('img');
  image.src = 'images/background.png';

  button.addEventListener('click', function () {
    if (flippedCardRow1 === button || flippedCardRow2 === button) {
      return;
    }

    image.src = `images/${cardId}.jpg`;

    if (flippedCardRow1 === null) {
      flippedCardRow1 = button;
      return;
    }

    flippedCardRow2 = button;

    if (flippedCardRow1 !== null && flippedCardRow2 !== null) {
      if (flippedCardRow1.id === flippedCardRow2.id) {
        flippedCardRow1 = null;
        flippedCardRow2 = null;
      } else {
        setTimeout(() => {
          flippedCardRow1.querySelector('img').src = 'images/background.png';
          flippedCardRow2.querySelector('img').src = 'images/background.png';
          flippedCardRow1 = null;
          flippedCardRow2 = null;
        }, 1000);
      }
    }
  });

  button.appendChild(image);
  return button;
}
