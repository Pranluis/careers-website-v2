# Importing important modules in the app
from flask import Flask, redirect, render_template, request, json, jsonify, url_for
import sqlite3

from sendmail import send_mail
from database import load_jobs, load_job_from_db, add_data_db, load_application, add_sql_commands, del_job_db, edit_sql_commands, del_applicant_db
app = Flask(__name__)
  


######################################### JOB SECTION (MAIN WEBSITE PART) ########################################################################
@app.route("/")
def home():
    JOBS = load_jobs()
    return render_template('home.html', jobs=JOBS)

@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Not found", 404
    
    return render_template('jobpage.html', job=job)

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
    data = request.form
    emailid = request.form['email']
    name = request.form['full_name']
    job = load_job_from_db(id)
    job_name = job['title']

    add_data_db(id, data)

    send_mail(emailid, name, job_name)
    print(data)
    print(type(data))
    return render_template('application_form_sub.html', application=data, job=job)

#################################################### ADMIN SECTION ##################################################################################


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

######################################## ADMIN EDIT JOB SECTION #######################################################################################

@app.route("/adminlogin/editjobs")
def editjobs():
    JOBS = load_jobs()
    return render_template('edit_jobs.html' , data = JOBS)

@app.route("/adminlogin/editjobs/addjob", methods=["GET", "POST"])
def add_transaction():
    
    return render_template("form.html")

###################### Operation only links #############################

@app.route("/adminlogin/editjobs/addjob/added", methods=["GET","POST"])
def add_job():
    job_data = request.form
    add_sql_commands(job_data)
    return redirect(url_for("editjobs"))

@app.route("/adminlogin/editjobs/addjob/<id>/delete", methods=['GET'])
def del_job(id):
    del_job_db(id)
    return redirect(url_for("editjobs"))

@app.route("/adminlogin/editjobs/addjob/<id>/edit", methods=['GET','POST'])
def edit_job_val(id):
    data = load_job_from_db(id)
    return render_template('edit_form.html', data=data)

@app.route("/adminlogin/editjobs/addjob/<id>/edit/edited", methods=["GET","POST"])
def edit_job(id):
    job_data = request.form
    edit_sql_commands(job_data, id)
    return redirect(url_for("editjobs"))



################################################ ADMIN EDIT APPLICANT SECTION ############################################################################

@app.route("/adminlogin/editapplicants")
def editapplicants():
    application = load_application()
    return render_template('edit_applicant.html' , data = application)


@app.route("/adminlogin/editapplicants/<id>/delete", methods=['GET'])
def del_application(id):
    del_applicant_db(id)
    return redirect(url_for("editapplicants"))


################################################ API FOR THE SERVER #####################################################################################
# All applicants api.
@app.route("/dashboard")
def admin_application():
    application = load_application()
    return jsonify(application)

# All jobs api.
@app.route("/api/jobs")
def list_jobs():
    JOBS = load_jobs()
    return jsonify(JOBS)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)