# Importing important modules in the app
from flask import Flask, redirect, render_template, request, json, jsonify
import sqlite3
from database import load_jobs, load_job_from_db, add_data_db, load_application
app = Flask(__name__)


@app.route("/")
def home():
    JOBS = load_jobs()
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    JOBS = load_jobs()
    return jsonify(JOBS)

@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Not found", 404
    
    return render_template('jobpage.html', job=job)


@app.route("/admin")
def admin():
     return render_template("admin.html")

@app.route("/adminlogin", methods=['get','post'])
def adminlogin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'pr1729' and password == '1729':
            application = load_application()
            return render_template('admindash.html', appdata=application)
    
    return render_template("admin.html")

@app.route("/adminlogin/dashboard")
def admin_application():
    application = load_application()
    return jsonify(application)


@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
    data = request.form
    job = load_job_from_db(id)
    
    add_data_db(id, data)

    return render_template('application_form_sub.html', application=data, job=job)




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)