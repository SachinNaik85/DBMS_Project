import smtplib
from essential import gmail, credential
import random
import mysql.connector
from travel.models import package, booked_package
from django.shortcuts import redirect


def shorten_mail(email):
    lst = email.split('@')
    email = lst[0][:3]
    for i in range(3, len(lst[0])):
        email += '*'
    email += lst[1]
    return email


def send_email(receiver, message):
    # creates SMTP session
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(gmail['sender'], gmail['password'])

        # message to be sent

        # sending the mail
        s.sendmail(gmail['sender'], receiver, message)

        # terminating the session
        s.quit()
        return
    except Exception as e:
        print('error in sending mail', e)
        return redirect(to='LoginPage')


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
            print(data)
            return data
        except mysql.connector.ProgrammingError:
            print(f'error in executing {query}')

    except mysql.connector.Error as e:
        print(e)

    finally:
        sql.close()


def packages():
    query = f'select * from package'
    data = execute_query(query)
    select = []
    for i in range(6):
        ele = random.randint(0, len(data)-1)
        while ele in select:
            ele = random.randint(0, len(data)-1)
        select.append(ele)
    packags = []
    for _ in select:
        i = data[_]
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


def reset_mail(name, email):
    secret_key = random.randint(100000, 999999)
    subject = "YES TRAVELS PASSWORD RESET WIZARD"
    text = f"Dear {name} \n\n Sorry to hear you're having trouble logging into YES TRAVELS\n" \
           f"For any support you can reach us through contacts given in the 'HAVE SOME QUESTIONS?' section\n" \
           f"\n\nFor resetting your password use this security key {secret_key}" \
           f"\n\nIf you have not requested password reset please ignore this mail" \
           f"Thanks and Regards," \
           f"YES TRAVELS"
    message = 'Subject: {}\n\n{}'.format(subject, text)
    send_email(email, message)
    return secret_key


def confirmation_mail(name, email, **dix):
    name1 = name
    tdix = dix
    subject = "YES TRAVELS, BOOKING CONFIRMED"
    text = f"Dear {name1} \n\nYour booking has been confirmed for {tdix['topic']} \n\nThanks and regards,\nYES TRAVELS"
    message = 'Subject: {}\n\n{}'.format(subject, text)
    send_email(email, message)
