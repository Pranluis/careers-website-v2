import sqlite3

def add_sql_commands():
    conn = sqlite3.connect("luidlinkcareer.db")
    cursor = conn.cursor()
    enter_data = f'INSERT INTO jobs VALUES (8,"Game Developer", "Mumbai, India", 7000, "dollars", "You have to create games on unity", "Unity, C++")'
    cursor.execute(enter_data)  
    conn.commit()
    conn.close()

if __name__ == '__main__':
    add_sql_commands()