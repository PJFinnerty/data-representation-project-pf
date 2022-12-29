from flask import Flask, jsonify, request, abort
from cinemasDAO import cinemasDAO
from deliveryDAO import deliveryDAO

app = Flask(__name__, static_url_path='', static_folder='.')

# Cinema 
@app.route('/cinemas')
def findAllCinemas():
    #print("in findAllCinemas")
    results = cinemasDAO.findAllCinemas()
    return jsonify(results)

@app.route('/cinemas/<int:id>')
def findCinema_Name(id):
    foundCinema_Name = cinemasDAO.findCinema_Name(id)
    return jsonify(foundCinema_Name)

@app.route('/cinemas', methods=['POST'])
def createCinemas():  
    if not request.json:
        abort(400)
    cinemas = {
        "Cinema_Name": request.json['Cinema_Name'],
        "Location": request.json['Location'],
        "NumberOfScreens": request.json['NumberOfScreens'],
        "Member_Status": request.json['Member_Status'],
    }
    values =(cinemas['Cinema_Name'],cinemas['Location'],cinemas['NumberOfScreens'], cinemas['Member_Status'])
    newId = cinemasDAO.createCinemas(values)
    cinemas['id'] = newId
    return jsonify(cinemas)

@app.route('/cinemas/<int:id>', methods=['PUT'])
def updateCinemas(id):
    foundCinema_Name = cinemasDAO.findCinema_Name(id)
    if not foundCinema_Name:
        abort(404)   
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Member_Status' in reqJson and Location(reqJson['Member_Status']) is not int:
        abort(400)
    if 'NumberOfScreens' in reqJson and Location(reqJson['NumberOfScreens']) is not int:
        abort(400)
    if 'Cinema_Name' in reqJson:
        foundCinema_Name['Cinema_Name'] = reqJson['Cinema_Name']
    if 'Location' in reqJson:
        foundCinema_Name['Location'] = reqJson['Location']
    if 'NumberOfScreens' in reqJson:
        foundCinema_Name['NumberOfScreens'] = reqJson['NumberOfScreens']
    if 'Member_Status' in reqJson:
        foundCinema_Name['Member_Status'] = reqJson['Member_Status']
    values = (foundCinema_Name['Cinema_Name'],foundCinema_Name['Location'],foundCinema_Name['NumberOfScreens'],foundCinema_Name['Member_Status'],foundCinema_Name['id'])
    cinemasDAO.updateCinemas(values)
    return jsonify(foundCinema_Name)
        
@app.route('/cinemas/<int:id>' , methods=['deleteCinemas'])
def deleteCinemas(id):
    cinemasDAO.deleteCinemas(id)
    return jsonify({"done":True})


if __name__ == '__main__' :
    app.run(debug= True)
    
      