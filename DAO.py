import mysql.connector
import json
import dbconfig as cfg

class CinemasDAO:
    db=""
    
    def createDatabase(self):
        self.db = mysql.connector.connect(
            host=cfg.mysql['host'],
            user=cfg.mysql['user'],
            password=cfg.mysql['password']    
        )
        self.cursor = self.connection.cursor()
        sql = "create database " + self.database
        self.cursor.execute(sql)
        self.connection.commit()
        self.closeAll()
    
    def __init__(self): 
        self.db = mysql.connector.connect(
        host=cfg.mysql['host'],
        user=cfg.mysql['user'],
        password=cfg.mysql['password'],
        database=cfg.mysql['database']
        )
  
    def findAllCinemas(self):
        cursor = self.db.cursor()
        sql="select * from cinemas"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionaryCinemas(result))
        return returnArray
        
    def findCinema_Name(self, id):
        cursor = self.db.cursor()
        sql="select * from cinemas where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionaryCinemas(result)
            
    def createCinemas(self, values):
        cursor = self.db.cursor()
        sql="insert into cinemas (Cinema_Name, Location, NumberOfScreens, Member_Status) values (%s,%s,%s,%s)"
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def updateCinemas(self, values):
        cursor = self.db.cursor()
        sql="updateCinemas cinemas set Cinema_Name=%s, Location=%s, NumberOfScreens=%s, Member_Status=%s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()

    def deleteCinemas(self, id):
        cursor = self.db.cursor()
        sql="deleteCinemas from cinemas where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.db.commit()
        print("deleteCinemas done")

    def convertToDictionaryCinemas(self, result):
        colnames=['id','Cinema_Name','Location', 'NumberOfScreens',"Member_Status"]
        item = {}      
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value        
        return item
        
cinemasDAO = CinemasDAO()


import mysql.connector
import json

class DAO

def findAll(self):
        cursor = self.db.cursor()
        sql="SELECT * FROM cinema"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            
def findItem(self, id):
        cursor = self.db.cursor()
        
def findItem(self, id):
    cursor = self.db.cursor()
    sql="select * from cinema where id = %s"
    values = (id,)
    cursor.execute(sql, values)
    result = cursor.fetchone()
    print(result)
        
def update(self, values):
        cursor = self.db.cursor()
        sql="update cinema set Film=%s, Director=%s, Screen=%s, Minutes=%s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
        
def delete(self, id):
        cursor = self.db.cursor()
        
        
# findItem()
## findAll()