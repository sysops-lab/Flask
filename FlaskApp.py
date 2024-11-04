from flask import *

app  = Flask(__name__)

@app.route("/")

def Hello():

    return "Hello, This is my first application in Flask"

if __name__ == "__main__":

    app.run(debug=True)