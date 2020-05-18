function validate()
{
    console.log('validate called');
    var allclear = true;
    var name = document.getElementById('name').value;
    var username = document.getElementById('username').value;
    var phone = document.getElementById('phone').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var confirm_password = document.getElementById('con_password').value;
    
    var name_regx = /^[a-zA-Z' ']+$/
    var email_regx = /^[a-zA-Z0-9.-]+@[a-zA-Z0-9]+.[a-z]+(.[a-z]+)?$/
    var phone_regx = /^[1-9][0-9]{9}$/
    var username_regx = /^[a-zA-Z0-9_$.@]+$/
    var password_regx = /^(?=.*\d).{4,12}$/
 
    if (!(name_regx.test(name)))
    {
        document.getElementById("label").innerHTML = "invalid inputs for some fields";
        document.getElementById("label").style = "visibilty : visible";
        allclear = false;
        console.log('inside name', allclear);
    }
    
    if (!(email_regx.test(email)))
    {
        document.getElementById("label").innerHTML = "invalid inputs for some fields";
        document.getElementById("label").style = "visibility : visible";
        allclear = false;
        console.log('inside email', allclear);
    }

    if (!(phone_regx.test(phone)))
    {
        document.getElementById("label").innerHTML = "invalid inputs for some fields";
        document.getElementById("label").style = "visibility : visible";
        allclear = false;
        console.log('inside phone', allclear);
    }

    if (!(username_regx.test(username)))
    {
        document.getElementById("label").innerHTML = "invalid inputs for some fields";
        document.getElementById("label").style = "visibility : visible";
        allclear = false;
        console.log('inside user name', allclear);
    }

    if (!(password_regx.test(password)))
    {
        document.getElementById("label").innerHTML = "invalid inputs for some fields";
        document.getElementById("label").style = "visibility : visible";
        allclear = false;
        console.log('inside password', allclear);
    }

    if (password != confirm_password)
    {
        document.getElementById("label").innerHTML = "invalid inputs for some fields";
        document.getElementById("label").style = "visibility : visible";
        allclear = false;
        console.log('inside confirm password', allclear);
    }

    return allclear;
}

