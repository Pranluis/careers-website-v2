# Importing important modules in the app
from flask import Flask, redirect, render_template, request, json, jsonify
app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'

    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary': 'Rs. 15,00,000'

    },
    {
        'id': 3,
        'title': 'Frontend Developer',
        'location': 'Vadodara, India',
        'salary': 'Rs. 8,00,000'

    },
    {
        'id': 4,
        'title': 'Backend Developer',
        'location': 'Pune, India',
        'salary': 'Rs. 8,00,000'

    },
    {
        'id': 5,
        'title': 'Backend Developer',
        'location': 'Chennai, India',
        'salary': 'Rs. 7,00,000'

    },
]

@app.route("/")
def home():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)