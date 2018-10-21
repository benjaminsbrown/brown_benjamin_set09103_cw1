from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
	return render_template('home.html'), 200


@app.route('/greeks/')
def greeks():
	return render_template('greeks.html')
@app.route('/greeks/pantheon/')
def pantheon():
	return render_template('pantheon.html')
@app.route('/romans/')
def romans():
	return render_template('romans.html')
@app.route('/romans/romans/')
def romans2():
	return render_template('romans.html')
@app.route('/romans.html')
def romanshtml():
	return render_template('romans.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
