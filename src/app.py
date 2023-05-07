from flask import Flask
from src.config import config
from flask_cors import CORS
from src.config import config

app = Flask(__name__)
config(app=app)
CORS(app=app)