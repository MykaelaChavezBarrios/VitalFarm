from flask import Flask
from config import config
from flask_cors import CORS
from database.db import initialize_db, init_app
from flask_restful import Api
from database.db_maker import create_db, drop_db
from resources.routes import initialize_routes

app = Flask(__name__)
config(app=app)
CORS(app=app)
api = Api(app)
initialize_db(app=app)
init_app(app=app)
drop_db(app=app)
create_db(app=app)
initialize_routes(api=api)

@app.route("/")
@app.route("/api")
def index():
    return {
        "Author": "Mykaela",
        "message": "Welcome to the API REST from VitalFarm",
        "routes": [
            "/",
        ],
    }

if __name__ == "__main__":
    app.run(debug=True)