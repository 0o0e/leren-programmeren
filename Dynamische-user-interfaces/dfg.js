console.log('hello world');



function button_click(event){
    console.log('button is clicked');
    var name = prompt('Whats your name? ');
    var difelement = document.getElementById('result');
    difelement.innerHTML = 'good afternoon ' + name;
}

button = document.getElementById('start');


button.onclick = button_click

console.dir(button)


