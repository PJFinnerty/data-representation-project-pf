import mysql.connector
import json

class TestDAO

def findAll(self):
        cursor = self.db.cursor()
        sql=""
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            
def findItem(self, id):
        cursor = self.db.cursor()
        
def update(self, values):
        cursor = self.db.cursor()
        
def delete(self, id):
        cursor = self.db.cursor()