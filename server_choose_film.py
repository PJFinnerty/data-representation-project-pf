from flask import Flask, jsonify, request, abort, session, url_for, redirect
from cinemasDAO import cinemasDAO
from deliveryDAO import deliveryDAO

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
       # User is authorised
    #return '{"data":"all here"}'
    return redirect('web_cinemas5.html')
#==============================================

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
    
      