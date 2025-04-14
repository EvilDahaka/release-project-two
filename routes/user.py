import re
import bcrypt
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import sqlite3
from models import get_db_connection

user_bp = Blueprint('user', __name__)

def validate_registration_data(username, email, password, confirm_password):
    if not username or not email or not password or not confirm_password:
        return "Всі поля є обов'язковими."
    if len(username) < 3:
        return "Ім'я користувача повинно бути не менше 3 символів."
    if not re.match(r'^[a-zA-Z0-9_.-]+$', username):
        return "Ім'я користувача може містити тільки букви, цифри, _, . або -."
    if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
        return "Некоректний формат email."
    if len(password) < 4:
        return "Пароль повинен бути не менше 4 символів."
    if not re.search(r'\d', password):
        return "Пароль повинен містити букви та цифри."
    if password != confirm_password:
        return "Паролі не співпадають."
    return None

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        validation_error = validate_registration_data(username, email, password, confirm_password)
        print(validation_error)
        if validation_error:
            return redirect(url_for('user.register'))

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        conn = get_db_connection()  # Отримати нове з'єднання
        try:
            existing_user = conn.execute('SELECT * FROM users WHERE username = ? OR email = ?', (username, email)).fetchone()
            if existing_user:
                print("Користувач із таким ім'ям або email вже існує.") #перевірка на існуючий ім'я чи email
                return redirect(url_for('user.register'))

            conn.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', 
                         (username, email, hashed_password))
            conn.commit()
            print('записанна в базу даних')
        finally:
            conn.close()  # Закрити з'єднання

        #print("Реєстрація успішна! Ви можете увійти в систему.")
        #return redirect(url_for('user.login'))

    return render_template('register.html')
