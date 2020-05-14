import mysql.connector
from essential import credential
db = mysql.connector.connect(user=credential['db_user'], passwd=credential['password'],
                             database=credential['using_db'], host='localhost')
sql = db.cursor()

hotel_names = ['Sea_view', 'Machali', 'Makara', "Park_hotel", 'Signature_Inn']
hotel_type = ['AC delux', 'AC luxury', 'World class', 'Mid range', 'world class']
hotel_location = ['New Market Kolkatta', 'Lindsay street kolkatta', 'Esplande kolkatta', 'Park street kolkatta', 'Market street kolkatta']
hotel_price = [1200, 2000, 1800, 1500, 2200]

for i in range(5):
    query = f'insert into hotel values ("{hotel_names[i]}" , "{hotel_type[i]}", "{hotel_location[i]}", "{hotel_price[i]}")'
    sql.execute(query)
    db.commit()

