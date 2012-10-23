import csv
import sys
import os

all_butters = {}

def get_data():
   #------------------ BUTTERS >>
    path = "/Users/matthewepler/Documents/ITP/class_documents/_dynamic_web/week5_databases1/my_app/static/data/butter/"
    butter_cats = ["almond/", "peanut/", "cashew/"]

    brand_dict = {}

    for cat in butter_cats:
    	pathStr = path + cat
    	dirList = os.listdir(pathStr)
    	for fname in dirList:
	        path_str = pathStr + fname
	        if( fname != ".DS_Store"):
	            f = open(path_str, 'rU')
	        else:
	            break

	        try:
	            reader = csv.DictReader(f, dialect='excel', delimiter=',')
	            headers = reader.fieldnames 
	            for h in headers:
	                types = []
	                for row in reader:  
	                    if len(row[h]) is not 0:
	                        types.append(row[h])
	                brand_dict[h] = types
	                f.seek(0)
	        finally:
	            f.close()
	        keyname = fname.replace("_", " ")
	        keyname = keyname.replace(".csv", "")
	        all_butters[keyname] = brand_dict


get_data()

for b in all_butters:
	print "***"
	print b
	for key, value in all_butters[b].iteritems():
		print key
		print value
		print ""
	










