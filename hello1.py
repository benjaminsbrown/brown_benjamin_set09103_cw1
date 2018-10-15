from flask import Flask, redirect, url_for
app = Flask(__name__)
@app.route('/')
def hello_world():
	return 'Hello Napier'
@app.route("/hello/")
def hello():
	return "Hello Napier!!! :D"
@app.route("/goodbye/")
def goodbye():
	return "Goodbye cruel world :(" 
@app.route("/private") 
def private():
# Test for user logged in failed 
# so redirect to login URL
	return redirect(url_for('login'))
@app.route("/login") 
def login():
	return "Now we would get username & password"
@app.errorhandler(404)
def page_not_found(error):
	return "couldn't find the page you requested.", 404
