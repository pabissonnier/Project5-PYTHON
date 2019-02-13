# -*- coding: utf-8 -*
import urllib.request
import json


def categories_extract():
    """ Parse JSON into a list """

    categories_json = urllib.request.urlopen('https://fr.openfoodfacts.org/categories.json')
    categories_read = categories_json.read()
    categories_data= json.loads(categories_read.decode("utf-8"))

    categories_list = []
    for value in categories_data["tags"]:
        if value["products"] >= 4017:
            categories_list.append(value["name"])
            categories_list.sort()
            for category_name in enumerate(categories_list):
                print(category_name)



categories_extract()
