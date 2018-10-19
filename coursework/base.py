from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
	return render_template('home.html'), 200
@app.route('/romans.html')
def display():
	return render_template('romans.html'), 200

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
