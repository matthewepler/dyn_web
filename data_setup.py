import csv
import sys
import os
import models

all_addons_categories = {}
all_bread_brands = {}
all_nuts = {}

def get_data():
    #------------------ ADDONS >>
    path = "/Users/matthewepler/Documents/ITP/class_documents/_dynamic_web/week5_databases1/my_app/static/data/addons/"

    category_dict = {}
    dirList = os.listdir(path)
    for fname in dirList:
        if(fname != ".DS_Store"):
            path_str = path + fname
            with open(path_str, 'rU') as f:

                try:
                    reader = csv.DictReader(f, dialect='excel', delimiter=',')
                    headers = reader.fieldnames 
                    for h in headers:
                        types = []
                        counter = 0;
                        for row in reader:  
                            if row[h] is not None:
                                types.append(row[h])
                                counter += 1
                        category_dict[h] = types        
                        f.seek(counter)
                finally:
                    f.close()
    keyname = fname.replace("_", " ")
    keyname = keyname.replace(".csv", "")
    all_addons_categories[keyname] = category_dict


    #------------------ BREADS >>
    path = "/Users/matthewepler/Documents/ITP/class_documents/_dynamic_web/week5_databases1/my_app/static/data/bread/"

    brand_dict = {}
    dirList = os.listdir(path)
    for fname in dirList:
        if(fname != ".DS_Store"):
            # print fname
            path_str = path + fname
            with open(path_str, 'rU') as f:
                f.seek(0)

                try:
                    reader = csv.DictReader(f, dialect='excel', delimiter=',')
                    headers = reader.fieldnames 
                    for h in headers:
                        # print h
                        types = []
                        for row in reader:  
                            if len(row[h]) is not 0:
                                # print row[h]
                                types.append(row[h])
                        brand_dict[h] = types   
                        # print types
                        # print ""
                        f.seek(0)

                finally:
                    f.close()
        keyname = fname.replace("_", " ")
    	keyname = keyname.replace(".csv", "")
        all_bread_brands[keyname] = brand_dict
        brand_dict={}
    all_bread_brands['Homemade'] = "Homemade"


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
	        all_nuts[keyname] = brand_dict



    # for a in all_addons_categories:
    #     for key, value in all_addons_categories[a].iteritems():
    #         new = models.Addon()
    #         new.name = key
    #         new.types = value
    #         new.category = a.replace(".csv", "")
    #         new.save()

    # for b in all_bread_brands:
    #     new = models.Bread()
    #     new.brand = b.replace(".csv", "")
    #     for key, value in all_bread_brands[b].iteritems():
    #         new.category = key
    #         new.names = value
    #         new.save()

    # for c in all_butter_brands:
    # 	types = {}
    #     new = models.Butter()
    #     new.brand = c.replace(".csv", "")
    #     for key, value in all_bread_brands[c].iteritems():
    #     	types[key] = value
    #    	new.types = types
    #     new.save()



