from distutils.log import debug
from flask import Flask, render_template, redirect, url_for, request
import sqlite3
import random
import string

app = Flask(__name__)

def validate(username, password):
    con = sqlite3.connect('loginpage/db.db')
    #with sqlite3.connect('static/db.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Users")
    rows = cur.fetchall()
    for row in rows:
        dbUser = row[0]
        dbPass = row[1]
        if dbUser==username and dbPass == password:
            return True
    
    return False

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        completion = validate(username, password)
        if completion ==False:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('secret'))
    return render_template('login.html', error=error)



@app.route('/secret')
def secret():
    return "This is a secret page!"


app.run(debug=True)