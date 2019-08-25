from flask import Flask, escape, request
from hashlib import sha384
import re


def login(app, db_conn):
    username = request.form["username"]
    password = request.form["password"]
    db_cursor = db_conn.cursor()
    db_cursor.execute(f'SELECT passhash, salt FROM users WHERE name = {db_conn.escape(username).decode()} LIMIT 1')
    res = db_cursor.fetchone()
    if not res:
        return {
            'code': -1,
            'err_msg': 'User not exist'
        }
    passhash, salt = res
    passhash_req = sha384((salt + password + salt).encode('utf-8')).digest()
    if passhash == passhash_req:
        resp = app.make_response({
            'code': 0,
            'msg': 'Login successful'
        })
        resp.set_cookie('rv_auth', passhash.hex())
        return resp
    else:
        return {
            'code': -2,
            'msg': 'Incorrect password'
        }


def cookie_auth(db_conn):
    passhash = request.cookies['rv_auth']
    pattern = re.compile("^[0-9a-f]{96}$")
    if not pattern.match(passhash):
        return False
    db_cursor = db_conn.cursor()
    db_cursor.execute(f'SELECT id FROM users WHERE passhash = 0x{passhash} LIMIT 1')
    res = db_cursor.fetchone()
    if not res:
        return False
    return res


