from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote

app = Flask(__name__)
db = SQLAlchemy()
username = "postgres"
password = "JackBauer@24"
password_encoded = quote(password)
hostname = "localhost"
dbname = "postgres"

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{username}:{password_encoded}@{hostname}/{dbname}"
)

db.init_app(app)
