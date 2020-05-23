import mysql.connector
from essential import credential
db = mysql.connector.connect(user=credential['db_user'], password=credential['password'], database=credential['using_db'], host='localhost')

sql = db.cursor()
busid = ['SEABIRD6300', 'SRS7300', 'VRL7266', 'SRL3200', 'SRIDURGA3401','SUGUNA2302', 'KAMATA8303', 'AIRAVATA7304', 'RAJAHAMSA7605', 'VRL5606', 'SRS3407', 'SRL6508', 'SEABIRD7809', 'AIRAVATACC4510', 'RAJAHAMSA0911',
         'AMBAARI8912', 'KAMATA6513', 'SUGUNA5414', 'AIRAVATA6515', 'SRS2416','VRL7617', 'AIRAVATA6518', 'RAJAHAMSA7619', 'SRS0920', 'SUGUNA9821', 'SRL9822', 'SEABIRD8723',
         'SRS8824', 'VRL0925', 'SEABIRS8926', 'AMBAARI7827', 'AIRAVATACC6528', 'SUGUNA6729', 'KAMATA8730', 'RAJAHAMSA6731', 'SRL9832', 'VRL4333',
         'SUGUNA7634', 'SRS6535', 'VRL1236', 'SRL2337', 'SEABIRD9038', 'RAJAHAMSA7639', 'AMBAAR33I40', 'AIRAVATA9841',
         'AIRAVATACC8842', 'RAJAHAMSA7643', 'AMBAAI0044', 'SRS3245', 'SRL8746', 'VRL7747',
         'SRS4348', 'VRL1149', 'SRL7350', 'AIRAVATACC5551',
         'AMBAARI0552', 'SUGUNA6653']


departure_time =['10:00 PM', '09:00 PM', '08:30 PM', '04:30 AM', '08:30 PM', '08:00 PM', '09:00 PM', '08:30 PM', '09:30 PM', '06:00 PM', '11:00 PM', '11:00 PM', '07:00 PM', '06:30 PM', '06:00 PM',
                 '10:00 PM', '04:00 AM', '10:00 PM', '09:00 PM', '07:00 PM', '08:00 PM', '07:30 PM', '06:00 PM', '09:00 PM', '08:00 PM', '04:30 AM', '10:00 PM'
                 '07:00 PM', '10:00 PM', '06:00 PM', '07:00 PM', '08:00 PM', '09:00 PM', '01:00 AM', '10:00 PM', '11:00 PM', '10:00 PM',
                 '07:00 PM', '09:00 PM', '06:00 PM', '07:00 PM', '06:00 PM', '07:30 PM', '09:00 PM', '10:30 PM',
                 '09:00 PM', '08:00 PM', '11:00 PM', '11:45 PM', '10:00 PM', '09:00 PM',
                 '08:00 PM', '07:00 PM', '04:00 PM', '05:00 PM',
                 '03:00 PM', '05:00 PM']


arrival_time = ['07:30 AM', '07:00 AM', '06:30 AM', '08:00 AM', '01:00 AM', '07:30 AM', '07:00 AM', '06:30 AM', '06:00 AM', '11:00 AM', '04:00 PM', '11:30 PM', '08:00 PM', '07:00 AM', '06:30 AM',
                '07:00 AM', '06:30 AM', '01:30 AM', '10:00 AM', '08:00 PM', '08:30 PM', '11:45 PM', '10:30 PM', '10:00 AM', '08:30 AM', '07:00 AM', '01:00 AM'
                '07:00 AM', '10:00 AM', '11:00 AM', '12:00 PM', '09:00 PM', '10:00 PM', '07:00 AM', '05:00 AM', '06:00 AM', '05:30 AM',
                '06:00 AM', '08:00 AM', '10:00 AM', '11:00 AM', '10:00 PM', '11:00 PM', '07:00 AM', '08;00 AM',
                '08:00 AM', '06:30 AM', '06:30 AM', '07:00 AM', '11:30 PM', '10:00 PM',
                '07:00 AM', '06:30 AM', '09:00 AM', '09:30 AM',
                '11:00 PM', '01:00 AM']


bus_description = ['NON AC seater(1+1)', 'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)', 'NON AC seater(1+1)', 'NON AC sleaper(1+1)',
                   'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)', 'NON AC seater(2+1)', 'NON AC sleaper(2+1)',
                   'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)', 'NON AC seater(1+1)', 'NON AC sleaper(1+1)',
                   'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)',
                   'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)',
                   'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)',
                   'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)',
                   'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)',
                   'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)',
                   'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)',
                   'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)',
                   'NON AC sleaper(2+1)', 'NON AC sleaper(2+1)']


price = [750, 1200, 900, 350, 800, 2000, 1950, 1450, 1000, 3000, 3200, 4000, 4250, 2500, 2900,
         1200, 1300, 2550, 2400, 3000, 2900, 3500, 3400, 2000, 1950, 800, 750,
         2500, 2350, 2900, 2750, 3500, 3400, 1100, 1000, 1500, 1450,
         2300, 2200, 2700, 2650, 3300, 3250, 1200, 1200,
         1300, 1200, 2000, 2100, 2800, 2750,
         2000, 2100, 2500, 2550,
         3700, 3750]


source = ['banglore', 'coorg', 'banglore','banglore', 'mysore', 'banglore', 'hampi', 'banglore', 'ooty', 'banglore', 'goa', 'banglore', 'mumbai', 'banglore', 'kanyakumari',
          'mysore', 'coorg', 'mysore', 'hampi', 'mysore', 'goa', 'mysore', 'mumbai', 'mysore', 'kanyakumari', 'mysore', 'ooty'
          'ooty', 'hampi', 'ooty', 'goa', 'ooty', 'mumbai', 'ooty', 'coorg', 'ooty', 'kanyakumari',
          'coorg', 'hampi', 'coorg', 'goa', 'coorg', 'mumbai', 'coorg', 'kanyakumari',
          'goa', 'hampi', 'goa', 'mumbai', 'goa', 'kanyakumari',
          'hampi', 'mumbai', 'hampi', 'kanyakumari',
          'kanyakumari', 'mumbai']


destination = ['coorg', 'banglore', 'coorg', 'mysore', 'banglore', 'hampi', 'banglore', 'ooty', 'banglore', 'goa', 'banglore', 'mumbai', 'banglore', 'kanyakumari', 'banglore',
               'coorg', 'mysore', 'hampi', 'mysore', 'goa', 'mysore', 'mumbai', 'mysore', 'kanyakumari', 'mysore', 'ooty', 'mysore'
               'hampi', 'ooty', 'goa', 'ooty', 'mumbai', 'ooty', 'coorg', 'ooty', 'kanyakumari', 'ooty',
               'hampi', 'coorg', 'goa', 'coorg', 'mumbai', 'coorg', 'kanyakumari', 'coorg',
               'hampi', 'goa', 'mumbai', 'goa', 'kanyakumari', 'goa',
               'mumbai', 'hampi', 'kanyakumari', 'hampi',
               'mumbai', 'kanyakumari']

for i in range(0, len(price)):
    try:
        query = f'insert into bus value("{busid[i]}", "{departure_time[i]}", "{arrival_time[i]}", "{bus_description[i]}", "{price[i]}", "{source[i]}", "{destination[i]}")'
        sql.execute(query)
        db.commit()
    except Exception as e:
        print(e)
        pass