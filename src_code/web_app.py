#. venv/bin/activate

from flask import Flask, render_template,url_for,redirect,request,session,jsonify,Response
from forms import *
import json,requests

app = Flask(__name__)
app.config["SECRET_KEY"] = "a-key-that-is-secret"


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',title="Web App - Home")

@app.route("/formtest",methods=["GET","POST"])
def formtest():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        # session["username"] = username
        return redirect(url_for("name",username=username))
    return render_template('formtest.html',title="Web App - Form",form=form)

@app.route("/name")
def name():
    username = request.args["username"]
    # username = session["username"]
    return render_template('name.html',title="Web App - Name",username=username)

@app.route("/allegiances",methods=["GET","POST"])
def allegiances():

    #handle file
    with open("allegiance.json","r") as jsonFile:
        data = json.load(jsonFile)
        return jsonify(data)     #Response(jsonFile.read(),mimetype="text/json")

@app.route("/allegiancedashboard")
def allegiancedashboard():
    return render_template("allegiancedashboard.html",title="Web App - Allegiance Dashboard")

if __name__ == '__main__':
    app.run(debug=True)
