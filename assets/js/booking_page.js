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

function hotel_open_model() {
    console.log('modal called');
    var modalpopup = document.getElementsByClassName('book-hotel');
    for (var i = 0; i < modalpopup.length; i++) {
        modalpopup[i].style = "visibility : visible ; filter : blur(0px)";
    }
}

function hotel_close_model() {
    var modalpopup = document.getElementsByClassName('book-hotel');
    for (var i = 0; i < modalpopup.length; i++) {
        modalpopup[i].style = "visibility: hidden ; filter : blur(0px)";
    }
}

var busform = document.getElementById('busform');
function handle_bus_form()
{
busform.onsubmit =  function (c)
{
    var date = document.getElementById("departure_date").value;
    var username = document.getElementById("username").value;
    var seats = document.getElementById("seats").value;
    var password = document.getElementById("password").value;
    var date_regx = /^(19|20)\d\d([- /.])(0[1-9]|1[012])\2(0[1-9]|[12][0-9]|3[01])$/
    var username_regx = /^[a-zA-Z0-9_$.@]+$/
    var password_regx = /^(?=.*\d).{4,12}$/
    var seats_regx = /[1-6]{1}/
    var valid = true
    console.log(date, username, seats, password);
    if (! date_regx.test(date))
    {
        console.log(! date_regx.test(date))
        valid = false;
    }

    if (! username_regx.test(username))
    {
        valid = false;
    }

    if (! seats_regx.test(seats))
    {
        valid = false;
    }

    if(! password_regx.test(password))
    {
        valid = false;
    }

    if (!valid)
    {
        var error = document.getElementById("error_message").innerHTML = "invalid input";
    }
    console.log(valid)
    return valid;
};
};
handle_bus_form();

function close_booking_modal()
{
    var modal = document.getElementsByClassName("booking_confirmed")
    for (var i=0; i<modal.length; i++)
    {
        modal[i].style = "visibility : hidden";
    }
}