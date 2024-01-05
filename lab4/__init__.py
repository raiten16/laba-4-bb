from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://avnadmin:AVNS_8BMAPwZEqrNbkW5N9Sq@pg-3662c8ac-raiten16-868f.a.aivencloud.com:27883/defaultdb?sslmode=require"
app.config['JWT_SECRET_KEY'] = "allah"
app.config['JWT_ALGORITHM'] = "HS256"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

import lab4.views
import lab4.models
