import smtplib
from essential import gmail, credential
import random
import mysql.connector
from travel.models import package, booked_package


def shorten_mail(email):
    lst = email.split('@')
    email = lst[0][:3]
    for i in range(3, len(lst[0])):
        email += '*'
    email += lst[1]
    return email


def send_email(reciever):
    # creates SMTP session
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(gmail['sender'], gmail['password'])

        # message to be sent
        secret_key = random.randint(100000, 999999)
        subject = "YES TRAVELS password reset code"
        text = f"Hello Sir/Madam \n use this code for resetting your password\n {secret_key}"
        message = 'Subject: {}\n\n{}'.format(subject, text)

        # sending the mail
        s.sendmail(gmail['sender'], reciever, message)

        # terminating the session
        s.quit()
        return secret_key
    except Exception as e:
        print('error in sending mail')


def read_status():
    file = open('travel/login_status.txt', 'r')
    file_data = file.read()
    file_data = file_data.split()
    status = bool(int(file_data[0]))
    file.close()
    return status


def write_status(status, name):
    file = open('travel/login_status.txt', 'w')
    line = int(status)
    file.writelines(str(line))
    file.writelines('\n')
    file.writelines(str(name))
    file.close()
    return


def read_name():
    file = open('travel/login_status.txt', 'r')
    try:
        file_data = file.read()
        file_data = file_data.split()
        name = str(file_data[1])
        return name
    except IndexError as e:
        pass
    finally:
        file.close()


def execute_query(query):
    try:
        db = mysql.connector.connect(user=credential['db_user'], passwd=credential['password'],
                                     database=credential['using_db'], host='localhost')
        sql = db.cursor()
        try:
            sql.execute(query)
            data = sql.fetchall()
            return data
        except mysql.connector.ProgrammingError:
            print(f'error in executing {query}')

    except mysql.connector.Error as e:
        print(e)

    finally:
        sql.close()


def packages():
    query = f'select * from package limit 6'
    data = execute_query(query)
    packags = []
    for i in data:
        obj = package()
        obj.id = i[0]
        obj.name = i[1]
        obj.image = i[2]
        obj.bus = i[3]
        obj.hotel = i[4]
        obj.price = i[5]
        packags.append(obj)
    return packags


def booked_packages():
    data = execute_query(f'select * from package_booking where username = "{read_name()}"')
    packages_booked = []
    for i in data:
        obj = booked_package()
        obj.pid = i[0]
        obj.booking_date = i[2]
        obj.booking_time = i[3]
        obj.journey_date = i[4]
        obj.bus = i[5]
        obj.hotel = i[6]
        obj.guests = i[7]
        obj.amount_paid = i[8]
        packages_booked.append(obj)
    return packages_booked
