# Importing important modules in the app
from flask import Flask, redirect, render_template, request, json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)