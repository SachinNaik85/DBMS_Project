import mysql.connector
import mysql.connector.errorcode
from django.shortcuts import render
from essential import credential


def home(request):
    return render(request, 'index.html', {'authenticate' : False})


def login(request):
    if request.method == 'GET':
        message = ''
        return render(request, 'login.html', {'message': message})

    elif request.method == 'POST':
        try:
            db = mysql.connector.connect(user=credential['db_user'], passwd=credential['password'],
                                         database=credential['using_db'], host='localhost')
            sql = db.cursor()
            username = request.POST['username']
            password = request.POST['password']
            query = f'SELECT EXISTS (select * from user where username="{username}" and password=MD5("{password}"))'
            sql.execute(query)
            authenticated = sql.fetchall()
            if authenticated[0][0]:
                return render(request, 'index.html', {'authenticate' : True, 'username' : username})
            else:
                message = 'Invalid credentials'
                return render(request, 'login.html', {'message' : message})
        except Exception as e:
            print(e)

        finally:
            sql.close()


def signup(request):
    if request.method == 'GET':
        return render(request, 'signin.html')

    elif request.method == 'POST':
        try:
            db = mysql.connector.connect(user=credential['db_user'], passwd=credential['password'],
                                         database=credential['using_db'], host='localhost')
            sql = db.cursor()
            new_username = request.POST['username']
            query = f'select exists(select * from user where username = "{new_username}")'
            sql.execute(query)
            not_valid_username = sql.fetchall()

            if not not_valid_username[0][0]:
                name = request.POST['name']
                username = request.POST['username']
                email = request.POST['email']
                phone = request.POST['phone']
                password = request.POST['password']
                try:
                    query = f'insert into user values ("{username}", "{name}", "{email}", {phone}, MD5("{password}"));'
                    sql.execute(query)
                    db.commit()
                except mysql.connector.IntegrityError as e:
                    print(e)
                return render(request, 'index.html')
            elif not_valid_username[0][0]:
                message = 'Username already taken'
                return render(request, 'signin.html', {'error_message': message})

        except mysql.connector.Error as e:
            print(e)

        finally:
            sql.close()


def logout(request):
    return home(request)
