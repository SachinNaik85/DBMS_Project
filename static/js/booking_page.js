function open_modal() {
    console.log('modal called');
    var modalpopup = document.getElementsByClassName('book-bus');
    for (var i = 0; i < modalpopup.length; i++) {
        modalpopup[i].style = "visibility : visible ; filter : blur(0px)";
    }
}

function close_modal() {
    var modalpopup = document.getElementsByClassName('book-bus');
    for (var i = 0; i < modalpopup.length; i++) {
        modalpopup[i].style = "visibility: hidden ; filter : blur(0px)";
    }
}

function open_model() {
    console.log('modal called');
    var modalpopup = document.getElementsByClassName('book-hotel');
    for (var i = 0; i < modalpopup.length; i++) {
        modalpopup[i].style = "visibility : visible ; filter : blur(0px)";
    }
}

function close_model() {
    var modalpopup = document.getElementsByClassName('book-hotel');
    for (var i = 0; i < modalpopup.length; i++) {
        modalpopup[i].style = "visibility: hidden ; filter : blur(0px)";
    }
}