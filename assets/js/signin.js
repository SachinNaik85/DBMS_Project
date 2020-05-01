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
    return 0;
}