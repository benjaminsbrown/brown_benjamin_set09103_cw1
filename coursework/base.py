from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/')
def root():
	return render_template('home.html'), 200


@app.route('/greeks')
def greeks():
	return render_template('greeks.html'), 200
@app.route('/greeks/pantheon/')
def pantheon():
	return render_template('pantheon.html'), 200

@app.route('/<string:page_name>/')
def static_page(page_name):
    return render_template('%s.html' % page_name)

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
