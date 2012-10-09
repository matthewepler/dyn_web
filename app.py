import os, datetime

from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def mainpage():

    featured = {
        'pic' : '/static/img/featured.png',
        'name' : 'Electric Elvis',
        'descrip' : 'Almond butter, bananas, and guava paste slices on toasted home-made wheat bread. "An Elvis man should love it."',
        'author' : 'Matthew Epler'
    }

    return render_template('index.html', **featured)


@app.route("/share.html")
def share():
    return render_template('share.html')

# start the webserver
if __name__ == "__main__":
	app.debug = True
	
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)
