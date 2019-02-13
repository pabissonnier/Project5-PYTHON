# -*- coding: utf-8 -*
import urllib.request
import json
import mysql.connector
import mysql


def categories_extract():
    """ Extracting JSON categories values """

    categories_json = urllib.request.urlopen('https://fr.openfoodfacts.org/categories.json')
    categories_read = categories_json.read()
    categories_data = json.loads(categories_read.decode("utf-8"))

    for value in categories_data["tags"]:
        if value["products"] >= 4017:
            categories_values = value["name"]
            return categories_values



