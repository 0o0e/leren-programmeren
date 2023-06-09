let imagelist = ['1','2','3','4','5','6','7','8','9','10']

imagelist = shuffle(imagelist);

// shuffelen 
function shuffle(array) {
  let currentIndex = array.length, randomIndex;

  while (currentIndex != 0) {
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;

    [array[currentIndex], array[randomIndex]] = [array[randomIndex], array[currentIndex]];
  }

  return array;
}
console.log(shuffle(imagelist))