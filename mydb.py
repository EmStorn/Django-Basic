import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Pako1991!'
)

#prepare cursor object
cursorObject = dataBase.cursor()

#create DB
cursorObject.execute("CREATE DATABASE IF NOT EXISTS exerciseDB")

cursorObject.execute("USE exerciseDB")

print("DB created")