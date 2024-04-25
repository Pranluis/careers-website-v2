import sqlite3

def add_sql_commands():
    conn = sqlite3.connect("luidlinkcareer.db")
    cursor = conn.cursor()
    enter_data = f'INSERT INTO jobs VALUES (8,"Game Developer", "Mumbai, India", 7000, "dollars", "You have to create games on unity", "Unity, C++")'
    cursor.execute(enter_data)  
    conn.commit()
    conn.close()

def load_application():
    conn = sqlite3.connect("luidlinkcareer.db")
    cursor = conn.cursor()
    get_data = f"SELECT * FROM application"
    cursor.execute(get_data)
    rows = cursor.fetchall()

    def tuples_to_dict(keys, values):
        return dict(zip(keys, values))
    
    keys = [description[0] for description in cursor.description]
    applications = [tuples_to_dict(keys, row) for row in rows]
    conn.close()
    return applications

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

def load_job_from_db(id):
    conn = sqlite3.connect("luidlinkcareer.db")
    cursor = conn.cursor()
    get_data = f"SELECT * FROM jobs WHERE id = '{id}'"
    cursor.execute(get_data)
    vals = cursor.fetchall()
    if len(vals) == 0:
        return None
    else:
        def tuples_to_dict(keys, values):
            return dict(zip(keys, values))
        keys = [description[0] for description in cursor.description]
        jobs = [tuples_to_dict(keys, val) for val in vals]
        return jobs[0]
    


def add_data_db(job_id, data):
    all_app = load_application()
    id_person = len(all_app) + 1
    conn = sqlite3.connect("luidlinkcareer.db")
    cursor = conn.cursor()
    add_data_table = '''CREATE TABLE IF NOT EXISTS application 
    (id INT NOT NULL PRIMARY KEY, job_id INT NOT NULL, full_name VARCHAR(250) NOT NULL, email VARCHAR(250) NOT NULL, linkedin_url VARCHAR(250), work_exp VARCHAR(2000), resume_url VARCHAR(500))'''
    cursor.execute(add_data_table)
    insert_data = f"INSERT INTO application (id, job_id, full_name, email, linkedin_url, work_exp, resume_url) VALUES (?, ?, ?, ?, ?, ?, ?)"
    insert_value = (id_person, job_id, data['full_name'], data['email'], data['linkin'], data['work'], data['resume'])
    cursor.execute(insert_data, insert_value)
    conn.commit()
    conn.close()



