# Add to this file for the sample app lab
from flask import Flask
from flask import request
from flask import render_template

sample = Flask(__name__)

@sample.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    #Port 5050 because Jenkins will be using this app which is already using the port 8080
    sample.run(host="0.0.0.0", port=5050)
    
