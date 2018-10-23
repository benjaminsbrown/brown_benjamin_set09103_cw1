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

@app.route('/greeks/greekgods.html')
def greekgods():
	return render_template('greekgods.html'), 200

@app.route('/greeks/greekgods/zues.html')
def zues():
	return render_template('zues.html'), 200
@app.route('/greeks/greekgods/hera.html')
def hera():
	return render_template('hera.html'), 200
@app.route('/greeks/greekgods/ares.html')
def ares():
	return render_template('ares.html'), 200
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

@app.route('/romans/romansgods.html')
def romangods():
	return render_template('romangods.html'), 200

@app.route('/romans/romansgods/jupiter.html')
def jupiter():
	return render_template('jupiter.html'), 200

@app.route('/romans/romansgods/juno.html')
def juno():
	return render_template('juno.html'), 200

@app.route('/romans/romansgods/mars.html')
def mars():
	return render_template('mars.html'), 200
@app.errorhandler(404)
def page_not_found(error):
return render_template("youfool.html"), 404

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
