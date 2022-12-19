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