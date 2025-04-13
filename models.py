import sqlite3
from flask import session
from datetime import datetime
def init_db():
    conn = sqlite3.connect('db.sqlite')

    cursor = conn.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS feedback (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT,
                    message TEXT)
                   ''')
    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect('db.sqlite')
    conn.row_factory = sqlite3.Row
    return conn


def add_feedback(name, email, message):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO feedback (name, email, message) VALUES (?, ?, ?)', (name, email, message))
        conn.commit()
    finally:
        conn.close()
     
   



def add_feedback(name, email, message):
    """
    Функція для додавання нового відгуку в базу даних.
    Параметри:
    - name: ім'я користувача
    - email: email користувача
    - message: текст відгуку
    """
    conn = get_db_connection()
    try:
        conn.execute(
            'INSERT INTO feedback (name, email, message) VALUES (?, ?, ?)',
            (name, email, message)
        )
        conn.commit()
    finally:
        conn.close()

