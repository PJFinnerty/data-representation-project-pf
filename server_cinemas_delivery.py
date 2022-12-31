# Import Flas modules
from flask import Flask, jsonify, request, abort, session, url_for, redirect

# Import MySQL Config Files
import dbconfig as cfg
import dbconfigCinemas as cfg2

# Import DAO Classes for Cinema Delivery Tables
from cinemasDAO import cinemasDAO
from DAOEyeCinema import deliveryDAO
from DAOIMCHeadfordRoad import deliveryDAOHeadfordRoad
from DAOIMCOranmore import deliveryDAOOranmore

app = Flask(__name__, static_url_path='', static_folder='.')

app.secret_key = 'SomeSecretKey'

# Autheticate on opening the Server
# If Username is not in config file, redirect to login
@app.route('/')
def home():
    if not 'username' in session:
        return redirect(url_for('login'))
    # return redirect('web_delivery.html')
   # Else proceed to url of getToOrder() function
    return 'welcome '+ session['username'] +\
        '<br><a href="'+url_for('logout')+'">logout</a>'+\
        '<br><br><a href="'+url_for('getToOrder')+'">Go to order</a>'

# login button
@app.route('/login')
def login():
    return '<h1> login</h1> '+\
        '<button>'+\
            '<a href="'+url_for('process_login')+'">' +\
                'login' +\
            '</a>' +\
        '</button>'  
                
#"<a href="url_for('process_login')+"'>" +\    
  
# Process login url  
@app.route('/processlogin')
def process_login():
    # Check cred - if wrong redirect to login page
    
    # else
    session['username']=cfg.mysql['username']
    return redirect(url_for('home'))
    
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))
 
@app.route('/data')
def getToOrder():
    if not 'username' in session:
        abort(401)
       # User is authorised - redirect to Cinemas Homepage
    return redirect('Cinemas_Homepage.html')
#==============================================
# Main Cinema Page

# Create routes to Cinema table functions - stored in 'cinemasDAO.py'
@app.route('/cinemas')
def findAllCinemas():
    #print("in findAllCinemas")
    results = cinemasDAO.findAllCinemas()
    return jsonify(results)

# Function to return Cinema_Name by ID
@app.route('/cinemas/<int:id>')
def findCinema_Name(id):
    foundCinema_Name = cinemasDAO.findCinema_Name(id)
    return jsonify(foundType)

# Function to create new cinema (not necessary for Cinema table - but is relevant for the 3 DAO files routed below
@app.route('/cinemas', methods=['POST'])
def createCinemas():  
    if not request.json:
        abort(400)
    cinemas = {
        "Type": request.json['Type'],
        "Location": request.json['Location'],
        "NumberOfScreens": request.json['NumberOfScreens'],
        "Member_Status": request.json['Member_Status'],
    }
    values =(cinemas['Type'],cinemas['Location'],cinemas['NumberOfScreens'], cinemas['Member_Status'])
    newId = cinemasDAO.createCinemas(values)
    cinemas['id'] = newId
    return jsonify(cinemas)

# Once again updateCinemas is not relevant for the Cinemas table, as the user will not be asked to update the cinema list on the Cinema Homepage, this function is used by the EyeCinema, IMC Headford Road and IMC Oranmore DAO files that are connected to below
@app.route('/cinemas/<int:id>', methods=['PUT'])
def updateCinemas(id):
    foundType = cinemasDAO.findCinema_Name(id)
    if not foundType:
        abort(404)   
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Member_Status' in reqJson and Location(reqJson['Member_Status']) is not int:
        abort(400)
    if 'NumberOfScreens' in reqJson and Location(reqJson['NumberOfScreens']) is not int:
        abort(400)
    if 'Type' in reqJson:
        foundType['Type'] = reqJson['Type']
    if 'Location' in reqJson:
        foundType['Location'] = reqJson['Location']
    if 'NumberOfScreens' in reqJson:
        foundType['NumberOfScreens'] = reqJson['NumberOfScreens']
    if 'Member_Status' in reqJson:
        foundType['Member_Status'] = reqJson['Member_Status']
    values = (foundType['Type'],foundType['Location'],foundType['NumberOfScreens'],foundType['Member_Status'],foundType['id'])
    cinemasDAO.updateCinemas(values)
    return jsonify(foundType)
        
@app.route('/cinemas/<int:id>' , methods=['deleteCinemas'])
def deleteCinemas(id):
    cinemasDAO.deleteCinemas(id)
    return jsonify({"done":True})
 
#=============================================== 
 
# Eye Cinema Connections

@app.route('/EyeCinema')
def findAll():
    #print("in findAll")
    results = deliveryDAO.findAll()
    return jsonify(results)

@app.route('/EyeCinema/<int:id>')
def findItem(id):
    foundItem = deliveryDAO.findItem(id)
    return jsonify(foundItem)

@app.route('/EyeCinema', methods=['POST'])
def create():  
    if not request.json:
        abort(400)
    delivery = {
        "Item": request.json['Item'],
        "Type": request.json['Type'],
        "Quantity": request.json['Quantity'],
        "TotPrice": request.json['TotPrice'],
    }
    values =(delivery['Item'],delivery['Type'],delivery['Quantity'], delivery['TotPrice'])
    newId = deliveryDAO.create(values)
    delivery['id'] = newId
    return jsonify(delivery)

@app.route('/EyeCinema/<int:id>', methods=['PUT'])
def update(id):
    foundItem = deliveryDAO.findItem(id)
    if not foundItem:
        abort(404)   
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'TotPrice' in reqJson and type(reqJson['TotPrice']) is not int:
        abort(400)
    if 'Quantity' in reqJson and type(reqJson['Quantity']) is not int:
        abort(400)
    if 'Item' in reqJson:
        foundItem['Item'] = reqJson['Item']
    if 'Type' in reqJson:
        foundItem['Type'] = reqJson['Type']
    if 'Quantity' in reqJson:
        foundItem['Quantity'] = reqJson['Quantity']
    if 'TotPrice' in reqJson:
        foundItem['TotPrice'] = reqJson['TotPrice']
    values = (foundItem['Item'],foundItem['Type'],foundItem['Quantity'],foundItem['TotPrice'],foundItem['id'])
    deliveryDAO.update(values)
    return jsonify(foundItem)
        
@app.route('/EyeCinema/<int:id>' , methods=['DELETE'])
def delete(id):
    deliveryDAO.delete(id)
    return jsonify({"done":True})

#=============================================== 
 # IMC Headford Road Connections

# IMC Headford Road Connections
@app.route('/IMCHeadfordRoad')
def findAllHeadford():
    #print("in findAll")
    results = deliveryDAOHeadfordRoad.findAllHeadford()
    return jsonify(results)

@app.route('/IMCHeadfordRoad/<int:id>')
def findItemHeadford(id):
    foundItem = deliveryDAOHeadfordRoad.findItemHeadford(id)
    return jsonify(foundItem)

@app.route('/IMCHeadfordRoad', methods=['POST'])
def createHeadford():  
    if not request.json:
        abort(400)
    delivery = {
        "Item": request.json['Item'],
        "Type": request.json['Type'],
        "Quantity": request.json['Quantity'],
        "TotPrice": request.json['TotPrice'],
    }
    values =(delivery['Item'],delivery['Type'],delivery['Quantity'], delivery['TotPrice'])
    newId = deliveryDAOHeadfordRoad.createHeadford(values)
    delivery['id'] = newId
    return jsonify(delivery)

@app.route('/IMCHeadfordRoad/<int:id>', methods=['PUT'])
def updateHeadford(id):
    foundItem = deliveryDAOHeadfordRoad.findItemHeadford(id)
    if not foundItem:
        abort(404)   
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'TotPrice' in reqJson and type(reqJson['TotPrice']) is not int:
        abort(400)
    if 'Quantity' in reqJson and type(reqJson['Quantity']) is not int:
        abort(400)
    if 'Item' in reqJson:
        foundItem['Item'] = reqJson['Item']
    if 'Type' in reqJson:
        foundItem['Type'] = reqJson['Type']
    if 'Quantity' in reqJson:
        foundItem['Quantity'] = reqJson['Quantity']
    if 'TotPrice' in reqJson:
        foundItem['TotPrice'] = reqJson['TotPrice']
    values = (foundItem['Item'],foundItem['Type'],foundItem['Quantity'],foundItem['TotPrice'],foundItem['id'])
    deliveryDAOHeadfordRoad.updateHeadford(values)
    return jsonify(foundItem)
        
@app.route('/IMCHeadfordRoad/<int:id>' , methods=['DELETE'])
def deleteHeadford(id):
    deliveryDAOHeadfordRoad.deleteHeadford(id)
    return jsonify({"done":True})
    
#=============================================== 
 # IMC Oranmore  Connections

# IMC Oranmore  Connections
@app.route('/IMCOranmore')
def findAllOranmore():
    #print("in findAll")
    results = deliveryDAOOranmore.findAllOranmore()
    return jsonify(results)

@app.route('/IMCOranmore/<int:id>')
def findItemOranmore(id):
    foundItem = deliveryDAOOranmore.findItemOranmore(id)
    return jsonify(foundItem)

@app.route('/IMCOranmore', methods=['POST'])
def createOranmore():  
    if not request.json:
        abort(400)
    delivery = {
        "Item": request.json['Item'],
        "Type": request.json['Type'],
        "Quantity": request.json['Quantity'],
        "TotPrice": request.json['TotPrice'],
    }
    values =(delivery['Item'],delivery['Type'],delivery['Quantity'], delivery['TotPrice'])
    newId = deliveryDAOOranmore.createOranmore(values)
    delivery['id'] = newId
    return jsonify(delivery)

@app.route('/IMCOranmore/<int:id>', methods=['PUT'])
def updateOranmore(id):
    foundItem = deliveryDAOOranmore.findItemOranmore(id)
    if not foundItem:
        abort(404)   
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'TotPrice' in reqJson and type(reqJson['TotPrice']) is not int:
        abort(400)
    if 'Quantity' in reqJson and type(reqJson['Quantity']) is not int:
        abort(400)
    if 'Item' in reqJson:
        foundItem['Item'] = reqJson['Item']
    if 'Type' in reqJson:
        foundItem['Type'] = reqJson['Type']
    if 'Quantity' in reqJson:
        foundItem['Quantity'] = reqJson['Quantity']
    if 'TotPrice' in reqJson:
        foundItem['TotPrice'] = reqJson['TotPrice']
    values = (foundItem['Item'],foundItem['Type'],foundItem['Quantity'],foundItem['TotPrice'],foundItem['id'])
    deliveryDAOOranmore.updateOranmore(values)
    return jsonify(foundItem)
        
@app.route('/IMCOranmore/<int:id>' , methods=['DELETE'])
def deleteOranmore(id):
    deliveryDAOOranmore.deleteOranmore(id)
    return jsonify({"done":True})
    

if __name__ == '__main__' :
    app.run(debug= True)
    
      