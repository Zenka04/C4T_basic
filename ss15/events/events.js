function clicked() {
    alert("clicked!");
}
function change() {
    document.getElementById("text").style.color = "blue";
    document.getElementById("text").innerText = "Tadaaa. Chữ sau khi được thẩm mĩ!";
}
function box_color() {
    document.getElementById("changed").style.backgroundColor = "blue";
}
function hide() {
    document.getElementById("box2").style.display = 'none';
}
var score = 0;
console.log(score)
function plus(score) {
    score += 1;
    console.log(score)
}
function minus(score) {
    score -= 1;
    console.log(score)
}