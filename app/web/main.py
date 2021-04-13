from flask_login import login_user
from sqlalchemy import desc

from app.web import web
from flask import render_template, request

from models.base import db
from models.table import User


@web.route('/')
def hello_world():
    return render_template('home.html')


@web.route('/test')
def test():
    print(request)
    return 'test'
