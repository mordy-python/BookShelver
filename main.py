from deta import Deta
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()
app = Flask(__name__)
deta = Deta()
users = deta.Base('users')
bookshelves = deta.Base('bookshelves')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    return render_template('login_signup.html', verb='Log In')

@app.route('/signup', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

    return render_template('login_signup.html', verb='Sign Up')

if __name__ == '__main__':
    app.run(debug=True)