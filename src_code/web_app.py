#. venv/bin/activate

from flask import Flask, render_template,flash,url_for,redirect,request,session,jsonify
from forms import *
import pandas as pd

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
        # flash(f"Name entered: {form.username.data}")
        username = form.username.data
        session["username"] = username
        return redirect(url_for("name",username=username))
    return render_template('formtest.html',title="Web App - Form",form=form)

@app.route("/name")
def name():
    username = request.args["username"]
    username = session["username"]
    return render_template('name.html',title="Web App - Name",username=username)

@app.route("/allegiances")
def allegiances():
    json_ = request.json
    allegiance = pd.read_csv('allegiance.csv')
    json_vector = allegiance.transform(json_)
    query = pd.DataFrame(json_vector)
    prediction = regr.predict(query)
    return json.dumps({'allegiances': list({{allegiances}})})    

if __name__ == '__main__':
    app.run(debug=True)