var delButtons = document.getElementsByClassName("btn_del")
for(var i = 0; i < delButtons.length; i++) {
    var delButton = delButtons[i];
    delButton.addEventListener('click', function(e) {
        var btnDel = e.target; 
        var div = btnDel.parentNode;
        div.remove();
    })
}