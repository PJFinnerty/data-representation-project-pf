import mysql.connector
import json
import dbconfigCinemas as cfg2

# Create CinemasDAO class
class CinemasDAO:
    db=""
   
    def createDatabase(self):
        self.db = mysql.connector.connect(
            host=cfg2.mysql['host'],
            user=cfg2.mysql['user'],
            password=cfg2.mysql['password']    
        )
        self.cursor = self.connection.cursor()
        sql = "create database " + self.database
        self.cursor.execute(sql)
        self.connection.commit()
        self.closeAll()
    
    def __init__(self): 
        self.db = mysql.connector.connect(
        host=cfg2.mysql['host'],
        user=cfg2.mysql['user'],
        password=cfg2.mysql['password'],
        database=cfg2.mysql['database']
        )
  # Create findAllCinemas Functions, with SQL command and execute
    def findAllCinemas(self):
        cursor = self.db.cursor()
        sql="select * from cinemas"
        cursor.execute(sql)
        # Call fetchall and initialise an empty list
        results = cursor.fetchall()
        returnArray = []
        print(results)
        # Iterate through the list and call the convertToDictionaryCinemas() function to convert to correct format
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionaryCinemas(result))
        return returnArray
      
# Create findCinema_Name() function to return based on cinema ID      
    def findCinema_Name(self, id):
        cursor = self.db.cursor()
        sql="select * from cinemas where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionaryCinemas(result)
     
       # Create Cinema, Update, and delete will not be used through the html cinemas page, but the functions listed in the Delivery DAO pages will be used
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
    # Convert to dict return items as dictionary pairs - it is used by a number of the function above 
    def convertToDictionaryCinemas(self, result):
        colnames=['id','Cinema_Name','Location', 'NumberOfScreens',"Member_Status"]
        item = {}      
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value        
        return item
   # Initialise a new class instance     
cinemasDAO = CinemasDAO()


