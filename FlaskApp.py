from flask import *

app  = Flask(__name__)

@app.route("/")

def Hello():

    return "Hello, This is my first application in Flask"


@app.route("/careers") 

def careers():

    return "This is my first career page"

@app.route("/team")

def team():

    return "This is my team for flask App"



if __name__ == "__main__":

    app.run(debug=True)