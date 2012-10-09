import os, datetime

from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def mainpage():

    featured = {
        'pic' : '/static/img/featured.png',
        'name' : 'The Tasty Tower',
        'descrip' : 'A double-decker grilled veggie and proscuitto taste explosion on toasted home-made sourdough.',
        'author' : 'Matthew Epler'
    }


    return render_template('index.html', **featured)


# start the webserver
if __name__ == "__main__":
	app.debug = True
	
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)
