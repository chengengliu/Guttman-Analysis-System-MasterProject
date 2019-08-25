from flask import Flask, escape, request

import MySQLdb
from . import config
from .models import auth

app = Flask("rv")

conf = config.get_config()
db_conf = conf['db']
db_conn = MySQLdb.connect(
    host=db_conf['host'],
    user=db_conf['user'],
    passwd=db_conf['passwd'],
    db=db_conf['db'],
    port=db_conf['port'],
)


@app.route('/auth', methods=['POST'])
def login():
    return auth.login(
        app=app,
        db_conn=db_conn
    )




