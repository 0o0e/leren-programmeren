// let imagelist = ['1','2','3','4','5','6','7','8','9','10']

// imagelist = shuffle(imagelist);

// const myImage = document.getElementById(img);
// document.getElementById('button_0').style.backgroundColor='#911';

// const button = document.getElementById("buttons");

// function shuffle(array) {
//   let currentIndex = array.length, randomIndex;

//   while (currentIndex != 0) {
//     randomIndex = Math.floor(Math.random() * currentIndex);
//     currentIndex--;

//     [array[currentIndex], array[randomIndex]] = [array[randomIndex], array[currentIndex]];
//   }

//   return array;
// }

// console.log(shuffle(imagelist))
// console.log(imagelist)


//////////////////////////////////////////////////////////////////////////////////////

// function shuffle(array) {
//   return array.sort(() => Math.random() - 0.5);
// }

// const imagelist = ['1','2','3','4','5','6','7','8','9','10']
// let firstCard, secondCard;
// let flippedCardRow1 = null;
// let flippedCardRow2 = null;

// const buttonsContainer = document.getElementById('buttons');
// const firstCards = document.createElement('div');
// const secondCards = document.createElement('div');


// shuffle(imagelist).forEach((imagee) => {
//   const button = document.createElement('button');
//   button.id = imagee;
//   const image = document.createElement('img');
//   image.src = 'images/background.png';

//   button.addEventListener('click', function () {
//     if (flippedCardRow1 === button || flippedCardRow2 === button) {

//       return;
//     }

//     image.src = `images/${imagee}.jpg`;

//     if (flippedCardRow1 === null) {
//       flippedCardRow1 = button;
//       return;
//     }

//     flippedCardRow2 = button;

//     if (flippedCardRow1 !== null && flippedCardRow2 !== null) {
//       if (flippedCardRow1.id === flippedCardRow2.id) {

//         flippedCardRow1 = null;
//         flippedCardRow2 = null;
//       } else {

//         setTimeout(() => {
//           flippedCardRow1.querySelector('img').src = 'images/background.png';
//           flippedCardRow2.querySelector('img').src = 'images/background.png';
//           flippedCardRow1 = null;
//           flippedCardRow2 = null;
//         }, 1000);
//       }
//     }
//   });

//   button.appendChild(image);
//   firstCards.appendChild(button);
// });



// shuffle([...imagelist]).forEach((animal) => {
//   const button = document.createElement('button');
//   button.id = animal;
//   const image = document.createElement('img');
//   image.src = 'images/background.png';

//   button.addEventListener('click', function () {
//     if (flippedCardRow1 === button || flippedCardRow2 === button) {
      
      
//       return;
//     }

//     image.src = `images/${animal}.jpg`;

//     if (flippedCardRow1 === null) {
//       flippedCardRow1 = button;
//       return;
//     }

//     flippedCardRow2 = button;

//     if (flippedCardRow1 !== null && flippedCardRow2 !== null) {
//       if (flippedCardRow1.id === flippedCardRow2.id) {
       
        
//         flippedCardRow1 = null;
//         flippedCardRow2 = null;
//       } else {

//         setTimeout(() => {
//           flippedCardRow1.querySelector('img').src = 'images/background.png';
//           flippedCardRow2.querySelector('img').src = 'images/background.png';
//           flippedCardRow1 = null;
//           flippedCardRow2 = null;
//         }, 1000);
//       }
//     }
//   });

//   button.appendChild(image);
//   secondCards.appendChild(button);
// });

// buttonsContainer.append(firstCards, secondCards);




