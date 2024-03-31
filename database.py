import sqlite3

def add_sql_commands():
    conn = sqlite3.connect("luidlinkcareer.db")
    cursor = conn.cursor()
    enter_data = f'INSERT INTO jobs VALUES (7,"Full Stack Developer", "Mumbai, India", 1500000, "rupees", "You have to set backend system and design website with database", "MERN")'
    cursor.execute(enter_data)  
    conn.commit()
    conn.close()

if __name__ == '__main__':
    add_sql_commands()