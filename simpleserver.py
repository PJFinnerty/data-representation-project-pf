from flask import Flask
import dbconfig as cfg
import dbconfigCinemas as cfg2

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/', methods=['GET'])
def printHello():
    return "Hello, are ya well?"

if __name__ == '__main__' :
    app.run(debug= True)
    
