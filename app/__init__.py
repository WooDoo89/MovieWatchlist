import os
import urllib
from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient
from app.routes import pages

load_dotenv()


def create_app():
    app = Flask(__name__)
    username = urllib.parse.quote_plus(os.environ.get("UNAME"))
    password = urllib.parse.quote_plus(os.environ.get("PASSWORD"))
    app.config["MONGODB_URI"] = os.environ.get("MONGODB_URI") % (username, password)
    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY", "pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw"
    )
    app.db = MongoClient(app.config["MONGODB_URI"]).movies

    app.register_blueprint(pages)
    return app
