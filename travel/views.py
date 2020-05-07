from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector
from essential import credential
db = mysql.connector.connect(user='root', passwd=credential, database='travel', host='localhost')
sql = db.cursor()


def home(request):
    return render(request, 'index.html', {'authenticate' : False})


def login(request):
    if request.method == 'GET':
        message = ''
        return render(request, 'login.html', {'message': message})

    elif request.method == 'POST':
        try:
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


def signup(request):
    if request.method == 'GET':
        return render(request, 'signin.html')

    elif request.method == 'POST':
        new_username = request.POST['username']
        query = f'select exists(select * from user where username = "{new_username}")'
        sql.execute(query)
        valid_username = sql.fetchall()
        if valid_username[0][0] == 0:
            return render(request, 'index.html')
        elif valid_username[0][0] == 1:
            message = 'Username already taken'
            return render(request, 'signin.html', {'error_message' : message})
