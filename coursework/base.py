from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def root():
	return render_template('home.html'), 200
@app.route('/romans.html')
def roman():
	return render_template('romans.html'), 200
@app.route('/greeks.html')
def greek():
	return render_template('greeks.html'), 200



if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
