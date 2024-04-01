import sqlite3

def add_sql_commands():
    conn = sqlite3.connect("luidlinkcareer.db")
    cursor = conn.cursor()
    enter_data = f'INSERT INTO jobs VALUES (8,"Game Developer", "Mumbai, India", 7000, "dollars", "You have to create games on unity", "Unity, C++")'
    cursor.execute(enter_data)  
    conn.commit()
    conn.close()

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
    
    
