import dht12
import mysql.connector
mydb = mysql.connector.connect(
        host="10.0.1.33",
        user="username",
        password="password",
        database="main"
)
mycursor = mydb.cursor()
sql= "INSERT INTO main.mycomon (generation, temperaturef, humidity) VALUES(%s, %s, %s)"
generation = 2
temperaturef = dht12.temperature
humidity = dht12.humidity


try:
        mycursor.execute(sql, (generation, temperaturef, humidity))
        print(sql, (generation, temperaturef, humidity))
        mydb.commit()
        print(mycursor.rowcount, 'inserted')

except:
        mydb.rollback()
        print(mycursor.rowcount, 'failed to insert')
mydb.close()
