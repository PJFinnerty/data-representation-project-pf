import mysql.connector
import json
#import dbconfig as cfg2
import dbconfigCinemas as cfg2

class DeliveryDAOOranmore:
    db=""
    
#    def createDatabase(self):
#        self.db = mysql.connector.connect(
#            host=cfg2.mysql['host'],
#            user=cfg2.mysql['user'],
#            password=cfg2.mysql['password']    
#        )
#        self.cursor = self.connection.cursor()
#        sql = "create database " + self.database
#        self.cursor.execute(sql)
#        self.connection.commit()
#        self.closeAll()
#        
#    def createDeliveryTable(self):
#        self.db = mysql.connector.connect(
#            host=cfg2.mysql['host'],
#            user=cfg2.mysql['user'],
#            password=cfg2.mysql['password']    
#        )
#        self.cursor = self.connection.cursor()
#        sql = "CREATE TABLE CinemaDelivery (id int PRIMARY KEY AUTO_INCREMENT, Item varchar(255), Type Varchar(255), Quantity int, TotPrice int);"
#        self.cursor.execute(sql)
#        self.connection.commit()
#        self.closeAll()
        
    def __init__(self): 
        self.db = mysql.connector.connect(
        host=cfg2.mysql['host'],
        user=cfg2.mysql['user'],
        password=cfg2.mysql['password'],
        database=cfg2.mysql['database']
        )
  
    def findAllOranmore(self):
        cursor = self.db.cursor()
        sql="select * from IMCOranmore"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        return returnArray
        
    def findItemOranmore(self, id):
        cursor = self.db.cursor()
        sql="select * from IMCOranmore where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)
            
    def createOranmore(self, values):
        cursor = self.db.cursor()
        sql="insert into IMCOranmore (Item, Type, Quantity, TotPrice) values (%s,%s,%s,%s)"
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def updateOranmore(self, values):
        cursor = self.db.cursor()
        sql="update IMCOranmore set Item=%s, Type=%s, Quantity=%s, TotPrice=%s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()

    def deleteOranmore(self, id):
        cursor = self.db.cursor()
        sql="delete from IMCOranmore where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.db.commit()
        print("delete done")

    def convertToDictionary(self, result):
        colnames=['id','Item','Type', 'Quantity',"TotPrice"]
        item = {}      
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value        
        return item
        
deliveryDAOOranmore = DeliveryDAOOranmore()


