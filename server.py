from flask import Flask, jsonify, request, abort
from DAO import DAO

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/cinema')
def findAll():
    #print("in findAll")
    results = DAO.findAll()
    return jsonify(results)
    
@app.route('/cinema/<int:id>')
def findItem(id):
    foundItem = DAO.findItem(id)
    return jsonify(foundItem)
    
@app.route('/cinema', methods=['POST'])
def create():

    delivery = {
            "Film": request.json['Film'],
            "Director": request.json['Director'],
            "Screen": request.json['Screen'],
            "Minutes": request.json['Minutes'],
        }
        
@app.route('/cinema/<int:id>' , methods=['DELETE'])
def delete(id):
    DAO.delete(id)
    return jsonify({"done":True})
    
@app.route('/cinema/<int:id>', methods=['PUT'])
def update(id):
    
if __name__ == '__main__' :
    app.run(debug= True)