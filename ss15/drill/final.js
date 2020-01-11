console.log('1.', '\n')
var songs = document.getElementsByClassName("song");
for(var i = 0; i < songs.length; i++) {
    console.log(songs[i])
}

var titles = document.getElementsByClassName("title");
var artists = document.getElementsByClassName("artist");
console.log('2.', '\n')
for(var k = 0; k < songs.length; k++) {
    console.log(titles[k].innerHTML,'\n', artists[k].innerHTML)
}

console.log('3.', '\n')
var delButtons = document.getElementsByClassName("btn_del")
for(var i = 0; i < delButtons.length; i++) {
    var delButton = delButtons[i];
    delButton.addEventListener('click', function(e) {
        var btnDel = e.target; 
        var div = btnDel.parentNode;
        div.remove();
    })
}

console.log('4.', '\n')
var edit = document.getElementsByClassName("edit");

for(var i = 0; i < edit.length; i++) {
    var editBtn = edit[i];
    //console.log(editBtn);
    editBtn.addEventListener('click', function(e) {
        var btnEdit = e.target;
        var div = btnEdit.parentNode;
        console.log(div);
    })
}

console.log('5.', '\n');
function changeID1() {
    document.getElementById("id1").innerText = "song_id=78ab12";
}
function changeID2() {
    document.getElementById("id2").innerText = "song_id=ab762";
}
function changeID3() {
    document.getElementById("id3").innerText = "song_id=12354";
}