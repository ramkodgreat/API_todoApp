from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from flask_marshmallow import Marshmallow

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todoapidb.sqlite3'
app.config['SECRET_KEY'] = "random string"

db=SQLAlchemy(app)
ma = Marshmallow(app)

if __name__ == "__main__":
    app.run(debug=True)