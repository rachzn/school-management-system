import sqlite3
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR,"school.db")

def get_connection():
    return sqlite3.connect(DATABASE_PATH)

def create_tables():
    connection= get_connection()
    cursor = connection.cursor()

    cursor.execute("""
     CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_number TEXT UNIQUE NOT NULL,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        date_of_birth TEXT,
        gender TEXT,
        grade TEXT,
        enrollment_date TEXT,
        status TEXT DEFAULT "Active"
     )
     """)
    cursor.execute("""
         CREATE TABLE IF NOT EXISTS teachers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            teacher_id TEXT UNIQUE NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone TEXT,
            email TEXT,
            subject_class TEXT,
            status TEXT DEFAULT "Active"
         )
         """)
    cursor.execute("""
         CREATE TABLE IF NOT EXISTS attendance(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         student_number TEXT NOT NULL,
         attendance_date TEXT NOT NULL,
         status TEXT NOT NULL,
         UNIQUE(student_number, attendance_date)
         )

        """
    )
    cursor.execute("""
         SELECT name FROM sqlite_master
         WHERE type="table"
         """
    )

    tables= cursor.fetchall()
    print("DATABASE TABLES:", tables)


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS payments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_number TEXT NOT NULL,
        amount REAL NOT NULL,
        payment_date TEXT NOT NULL,
        payment_method TEXT,
        description TEXT  
        )
    
    """ )

    

    connection.commit()
    connection.close()
        
    
if __name__ == "__main__":
    create_tables()
    print("Database ready!")

connection= sqlite3.connect(DATABASE_PATH)
cursor= connection.cursor()

cursor.execute
("SELECT * FROM teachers")

teachers=cursor.fetchall()
print("Teachers:")
print(teachers)
connection.close()
    
