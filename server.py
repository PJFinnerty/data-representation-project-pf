from flask import Flask, jsonify, request, abort
from DAO import TestDAO

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/cinema')
def findAll():
    #print("in findAll")
    results = TestDAO.findAll()
    return jsonify(results)
    
@app.route('/cinema/<int:id>')
def findItem(id):
    foundItem = TestDAO.findItem(id)
    return jsonify(foundItem)
    
@app.route('/delivery', methods=['POST'])
def create():

    delivery = {
            "Film": request.json['Film'],
            "Director": request.json['Director'],
            "Screen": request.json['Screen'],
            "Minutes": request.json['Minutes'],
        }