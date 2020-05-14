function validate()
{
    var username_regx = /^[a-zA-Z0-9_$.@]+$/
    var password_regx = /^(?=.*\d).{4,12}$/
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    var allclear = true;
    if (! (username_regx.test(username)))
    {
        allclear = false;
        document.getElementById('warning').style = "visibility : visible";
        document.getElementById('warning').innerHTML = "invalid username";
    }

    if (! (password_regx.test(password)))
    {
        allclear = false;
        document.getElementById('warning').style = "visibility : visible";
        document.getElementById('warning').innerHTML = "invalid password";
    }
    return allclear;
}

