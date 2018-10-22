from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
	return render_template('home.html'), 200
@app.route('/demigods/')
def demigods():
	return render_template('demigods.html'), 200
@app.route('/demigods.html')
def demigodshtml():
	return render_template('demigods.html'), 200
@app.route('/greeks/')
def greeks():
	return render_template('greeks.html'), 200
@app.route('/greeks.html')
def greekshtml():
	return render_template('greeks.html'), 200
@app.route('/pantheon.html')
def pantheonshtml():
	return render_template('pantheon.html'), 200
@app.route('/greeks/pantheon/')
def pantheon():
	return render_template('pantheon.html'), 200
@app.route('/romans/')
def romans():
	return render_template('romans.html'), 200
@app.route('/romans.html')
def romanshtml():
	return render_template('romans.html'), 200
@app.route('/romans-gods.html')
def romanshtml():
	return render_template('romans.html'), 200

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
