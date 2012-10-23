# -*- coding: utf-8 -*-
from mongoengine import *

from flask.ext.mongoengine.wtf import model_form
from datetime import datetime


# PROFILE OBJECT 

# class Profile(Document):
# 	name = StringField()
# 	nickname = StringField()
# 	pic = URLField()
# 	fav = EmbeddedDocumentField()
# 	sandwiches = ListField( EmbeddedDocumentField() )
# 	reviews = ListField( EmbeddedDocumentField() )
# 	likes = IntField()

	  
# SANDWICH OBJECT 

class Sandwich(EmbeddedDocument):
	title = StringField()
	author = StringField()
	# author_prof = EmbeddedDocumentField()
	descrip = StringField()
	bread_brand = StringField()
	bread_type = StringField()
	butter_brand = StringField() 
	butter_type = StringField()
	qty1 = StringField()
	ingred1 = StringField()
	qty2 = StringField()
	ingred2 = StringField()
	instructions = StringField()
	# rating = DecimalField()
	# likes = IntField()
	# pic = URLField()	

SandwichForm = model_form(Sandwich)	


# REVIEW OBJECT 
# class Review (object):
# 	# author = EmbeddedDocumentField()
# 	rating = IntField()
# 	text = StringField()


# BREAD OBJECT  
# class Bread (Document):
# 	brand = StringField()
# 	category = StringField()
# 	names = ListField( StringField() )


# # BUTTER OBJECT
# class Butter (Document):
# 	brand = StringField()
# 	types = ListField( StringField() )


# # ADDON OBJECT
# class Addon (Document):
# 	name = StringField()
# 	category = StringField()
# 	types = ListField( StringField() )
	



