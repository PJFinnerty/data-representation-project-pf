import mysql.connector
import json
import dbconfig as cfg

# This program will create the CinemasDelivery database and Cinemas table
db=""
def createCinemasDatabase():
    # Set dep = Mysql connector object
    db = mysql.connector.connect(
    # Set parameters = dbconfig file values
        host=cfg.mysql['host'],
        user=cfg.mysql['user'],
        password=cfg.mysql['password']    
    )
    # Call the cursor object and pass in sql command
    cursor = db.cursor()
    sql = "create database CinemaDelivery"
    cursor.execute(sql)
    # Commit changes and close db and cursor
    db.commit()
    db.close()
    cursor.close()
  
# Function to create Cinemas table with 4 cols: Cinema_Name, Location, NumberOfScreens and Member_Status  
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
 
 
# Call the create database and create table command - these should only be called 1
createCinemasDatabase()
createDeliveryTable() 
   

#def create(values):

# Now create db2 variable and pass in the 3 insert command below for the 3 cinemas - print statement to the screen to confirm successful insert and commit()
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
