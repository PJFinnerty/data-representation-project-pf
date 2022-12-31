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
    sql = "CREATE TABLE EyeCinema (id int PRIMARY KEY AUTO_INCREMENT, Item varchar(255), Type Varchar(255), Quantity int, TotPrice int);"
    cursor.execute(sql)
    db.commit()
    db.close()
    cursor.close()
    
#createCinemasDatabase()
createDeliveryTable() 
   

def create(values):
db2 = mysql.connector.connect(
    host=cfg.mysql['host'],
    user=cfg.mysql['user'],
    password=cfg.mysql['password'],
    database="CinemaDelivery"
)
cursor = db2.cursor()
sql="insert into EyeCinema (Item, Type, Quantity, TotPrice) values (%s,%s,%s,%s)"
create1= ("Popcorn", "Food", 50, 30)
create2= ("Coca Cola", "Soft-drinks", 30, 14)
create3= ("Minstrels", "Food", 40, 32)
create4= ("Tayto", "Food", 20, 22)
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
    
def createCinemasDatabase(self):
    self.db = mysql.connector.connect(
        host=cfg.mysql['host'],
        user=cfg.mysql['user'],
        password=cfg.mysql['password']    
    )
    self.cursor = self.connection.cursor()
    sql = "create database delivery"
    self.cursor.execute(sql)
    self.connection.commit()
    self.closeAll()
    
def populateCinemasTable(self):
    self.db = mysql.connector.connect(
        host=cfg.mysql['host'],
        user=cfg.mysql['user'],
        password=cfg.mysql['password']    
    ) 
    
def createCinemas(self, values):
        cursor = self.db.cursor()
        sql="insert into cinemas (Cinema_Name, Location, NumberOfScreens, Member_Status) values (%s,%s,%s,%s)"
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid
    
def __init__(self): 
    self.db = mysql.connector.connect(
    host=cfg.mysql['host'],
    user=cfg.mysql['user'],
    password=cfg.mysql['password'],
    database=cfg.mysql['database']
    )



