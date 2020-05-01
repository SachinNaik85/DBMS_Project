function validate()
{
    console.log('validate called');
    var name = document.getElementById('name').value;
    var username = document.getElementById('username').value;
    var phone = document.getElementById('phone').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var confirm_password = document.getElementById('con_password').value;
    console.log(name, username, phone, email, password, confirm_password);
    
    var name_regx = /^[a-zA-Z]+$/
    var email_regx = /^[a-zA-Z0-9.-]+@[a-zA-Z0-9]+.[a-z]+(.[a-z]+)?$/

    if (!(name_regx.test(name)))
    {
        document.getElementById('name').style = "border : 2px solid red";
    }
    
    if (!(email_regx.test(email)))
    {
        console.log('invalid id');
    }
    return false;
}