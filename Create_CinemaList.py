import mysql.connector
import json
import dbconfig as cfg


db=""
def createCinemasDatabase():
    db = mysql.connector.connect(
        host=cfg.mysql['host'],
        user=cfg.mysql['user'],
        password=cfg.mysql['password']    
    )
    cursor = db.cursor()
    sql = "create database CinemaDelivery"
    cursor.execute(sql)
    db.commit()
    db.close()
    cursor.close()
    
def createDeliveryTable():
    db = mysql.connector.connect(
        host=cfg.mysql['host'],
        user=cfg.mysql['user'],
        password=cfg.mysql['password'], 
        database="CinemaDelivery"
    )
    cursor = db.cursor()
    sql = "CREATE TABLE Cinemas (id int PRIMARY KEY AUTO_INCREMENT, Cinema_Name varchar(255), Location Varchar(255), NumberOfScreens int, Member_Status int);"
    cursor.execute(sql)
    db.commit()
    db.close()
    cursor.close()
    
#createCinemasDatabase()
createDeliveryTable() 
   

#def create(values):
db2 = mysql.connector.connect(
    host=cfg.mysql['host'],
    user=cfg.mysql['user'],
    password=cfg.mysql['password'],
    database="CinemaDelivery"
)
cursor = db2.cursor()
sql="insert into Cinemas (Cinema_Name, Location, NumberOfScreens, Member_Status) values (%s,%s,%s,%s)"
create1= ("IMC Oranmore", "Oranmore", 5, 1)
create2= ("IMC Headford Road", "Headfor Road", 9, 1)
create3= ("The Eye Cinema", "Wellpark Retail Park", 8, 0)
cursor.execute(sql, create1)
db2.commit()
print("1 record inserted , ID: ", cursor.lastrowid)

cursor.execute(sql, create2)
print("1 record inserted , ID: ", cursor.lastrowid)
db2.commit()

cursor.execute(sql, create3)
print("1 record inserted , ID: ", cursor.lastrowid)
db2.commit()
