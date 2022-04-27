from deta import Deta
from dotenv import load_dotenv
from flask import Flask, request

load_dotenv()
app = Flask(__name__)
deta = Deta()
users = deta.Base('users')

@app.route('/')
def index():
    return f'{("bob", "bob@gmail.com", "1234")}'

