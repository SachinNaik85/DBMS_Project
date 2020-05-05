from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector
db = mysql.connector.connect(user='root', passwd='An@lien@85', database='travel', host='localhost')
sql = db.cursor()


def home(request):
    return render(request, 'index.html')


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
                return render(request, 'index.html')
            else:
                message = 'Invalid credentials'
                return render(request, 'login.html', {'message' : message})
        except Exception as e:
            print(e)


def signup(request):
    return render(request, 'signin.html')


def signed_up(request):
    return render(request, 'index.html')
