from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///tasks.db'
app.config['SECRET_KEY']='zx6471bvn2f981bv3498001c'
app.config['SQLALCHEMY_TRACE_MODIFICATIONS']=False

db = SQLAlchemy(app)

migrate = Migrate(app,db)

api = Api(app)

from application import views