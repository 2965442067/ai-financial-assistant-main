# extensions.py
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# 这里只实例化，不传入 app
db = SQLAlchemy()
jwt = JWTManager()