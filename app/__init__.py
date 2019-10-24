from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = \
    "mysql+pymysql://root:Blbj123456@rm-bp16nmlmn159wru4reo.mysql.rds.aliyuncs.com/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_COMMIT_TEARDOWN"] = True
app.config["SECRET_KEY"] = "887771752dac4713b2c4fdbe8a06d5c2"
app.debug = True
db = SQLAlchemy(app)

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404