import json
from flask import Flask
from flask import json
from flask import render_template
from flask import url_for
from flask import request
from jinja2 import Template
from getplaces import placeSearch


app = Flask("__main__")

@app.route("/")
def hello():
	return render_template("index.html")

@app.route("/query/",methods = ['POST'])
def query():
	loc = request.form["loc"]
	pfinal,add = placeSearch(loc)
	return render_template("results.html",name = pfinal, address = add)

if __name__ == "__main__":
    app.run(debug=True)