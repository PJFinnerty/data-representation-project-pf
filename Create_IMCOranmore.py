import mysql.connector
import json
import dbconfigCinemas as cfg


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
    sql = "CREATE TABLE IMCOranmore (id int PRIMARY KEY AUTO_INCREMENT, Item varchar(255), Type Varchar(255), Quantity int, TotPrice int);"
    cursor.execute(sql)
    db.commit()
    db.close()
    cursor.close()

# Call the create table command - this should only be called once - No need to create database as it was already Created 
#createCinemasDatabase()
createDeliveryTable() 
   

#def create(values):
db2 = mysql.connector.connect(
    host=cfg.mysql['host'],
    user=cfg.mysql['user'],
    password=cfg.mysql['password'],
    database="CinemaDelivery"
)
# Insert new values for Oranmore table, commit and print to confirm
cursor = db2.cursor()
sql="insert into IMCOranmore (Item, Type, Quantity, TotPrice) values (%s,%s,%s,%s)"
create1= ("Coca Cola", "Soft-drinks", 50, 30)
create2= ("Bin bags", "Cleaning Products", 30, 14)
create3= ("Tea bags", "Food", 40, 32)
create4= ("Cadbury Caramel", "Food", 40, 32)
create5= ("Uniform", "Staffing", 40, 32)
cursor.execute(sql, create1)
db2.commit()
print("1 record inserted , ID: ", cursor.lastrowid)

cursor.execute(sql, create2)
print("1 record inserted , ID: ", cursor.lastrowid)
db2.commit()

cursor.execute(sql, create3)
print("1 record inserted , ID: ", cursor.lastrowid)
db2.commit()
    
cursor.execute(sql, create4)
print("1 record inserted , ID: ", cursor.lastrowid)
db2.commit()
    
cursor.execute(sql, create5)
print("1 record inserted , ID: ", cursor.lastrowid)
db2.commit()
    


