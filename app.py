import os, datetime, sys, csv
import re
import models
import data_setup

from unidecode import unidecode
from flask import Flask, request, render_template, redirect, abort
from flask.ext.mongoengine import mongoengine

mongoengine.connect('mydata', host=os.environ.get('MONGOLAB_URI'))

# -------------------------------------- DATA 

data_setup.get_data()

# -------------------------------------- APP & "/" 

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


# -------------------------------------- "/SHARE.HTML"

@app.route("/share")
def share():
    all_data = {
        'Addons' : data_setup.all_addons_categories,
        'Breads' : data_setup.all_bread_brands,
        'Butters' : data_setup.all_nuts
    }
    
    return render_template('share.html', **all_data)

# -------------------------------------- "/RECORD"
@app.route("/save", methods=['GET','POST'])
def save():
    sandwich_form = models.SandwichForm(request.form)

    if request.method == "POST" :
        new = models.Sandwich()
        new.title = request.form.get('title', 'that \'which')
        new.author = request.form.get('author', 'anonymous')
        new.descip = request.form.get('descrip', 'it is what it is')
        new.bread_brand = request.form.get('bread_brand', 'none')
        new.bread_type = request.form.get('bread_type', 'none')
        new.butter_brand = request.form.get('butter_brand', 'none')
        new.butter_type = request.form.get('butter_type', 'none')
        new.qty1 = request.form.get('qty1', None)
        new.ingred1 = request.form.get('ingred1', None)
        new.qty2 = request.form.get('qty2', None)
        new.ingred2 = request.form.get('ingred2', None)
        new.instructions = request.form.get('instructions', 'figure it out yourself')
        new.save()

    return render_template("/success/%s"  % new.title)

# -------------------------------------- "/SUCCESS.HTML"

@app.route("/success/<title_string>", methods=['GET', 'POST'])
def success():
    try:
        title = title_string
    except:
        abort(404)

    # prepare template data
    templateData = {
        'title' : title_slug
    }

    return render_template('success.html', **templateData)




# -------------------------------------- (START WEBSERVER)

if __name__ == "__main__":
	app.debug = True
	
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)



