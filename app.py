# Importing important modules in the app
from flask import Flask, redirect, render_template, request, json, jsonify
import sqlite3
app = Flask(__name__)

def load_jobs():
    conn = sqlite3.connect("luidlinkcareer.db")
    cursor = conn.cursor()
    get_data = f"SELECT * FROM jobs"
    cursor.execute(get_data)
    rows = cursor.fetchall()

    def tuples_to_dict(keys, values):
        return dict(zip(keys, values))
    
    keys = [description[0] for description in cursor.description]
    jobs = [tuples_to_dict(keys, row) for row in rows]
    conn.close()
    return jobs

@app.route("/")
def home():
    JOBS = load_jobs()
    conn = sqlite3.connect("luidlinkcareer.db")
    cursor = conn.cursor()
    car_entry = '''CREATE TABLE IF NOT EXISTS jobs
            (id INT NOT NULL PRIMARY KEY, title VARCHAR(250) NOT NULL, location VARCHAR(250) NOT NULL, salary INT, currency VARCHAR(250), responsibilities VARCHAR(2000), requirements VARCHAR(2000))'''
    conn.execute(car_entry)
    conn.commit()
    conn.close()
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    JOBS = load_jobs()
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)