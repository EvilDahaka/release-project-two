from flask import Flask, render_template, session
from models import init_db
from routes.feedback import feedback_bp
from routes.user import user_bp

app = Flask(__name__)
app.secret_key = 'super secret key'

app.register_blueprint(feedback_bp)

app.register_blueprint(user_bp)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(debug=True)