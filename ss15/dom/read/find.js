var div_x = document.getElementById("song_container");
console.log(div_x);

var size = document.getElementById("custom");
console.log("width :", size.clientWidth);
console.log("height :", size.clientHeight);

var words = document.getElementById("box_with_words");
console.log(words.innerText);

var boxes = document.getElementsByClassName("box");
for(var i = 0; i < boxes.length; i++) {
    console.log(boxes[i]);
}