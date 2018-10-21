from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def root():
	return render_template('home.html'), 200
@app.route('/romans')
def roman():
	return render_template('romans.html'), 200
@app.route('/greeks')
def greek():
	return render_template('greeks.html'), 200
@app.route('/greeks/pantheon/')
def pantheon():
	return render_template('pantheon.html'), 200



if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
