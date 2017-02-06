# 'import gal' means take everything from Gal.py and use it in this program.
# That is why we are calling gal.main instead of main
# 'main in fact is not a required term you can run your program from any function name

import gal

# import flask -> 
from flask import Flask, render_template

#  before any webpage you use the @ decorator
app = Flask(__name__)

# This is the main webpage
@app.route("/")
def hello():
	myvars= gal.main
# 	render_template calls the html document
	return render_template('template.html', vars=myvars())
	
# This is an extra page that returns hello
@app.route("/gal")
def testsite():
	return "hello"

# app is the flask application. run sais turn on the webserver, get it online. 
#  debug gives you the traceback of error when error occurs. 
#  without debug you get generic 'internal server error'

app.run(debug=True)

# to get on web change to:
# app.run(host='0.0.0.0', port=80,debug=True)
