# -*- coding: utf-8 -*
import urllib.request
import json


def categories_extract():
    """ Extracting JSON categories values and converting into list """

    categories_json = urllib.request.urlopen('https://fr.openfoodfacts.org/categories.json')
    categories_read = categories_json.read()
    categories_data = json.loads(categories_read.decode("utf-8"))

    categories_list = []
    for value in categories_data["tags"]:
        if value["products"] >= 4017:
            categories_values = value["name"]
            categories_list.append(categories_values)
    return categories_list

def products_extract():
    """ Extracting JSON categories values and converting into list """
    

def convert_list_tuples(list_name):
    """ Convert list into list of tuples"""
    tuples_list = []
    for x in list_name:
        tuples_list.append((x,))
    return tuples_list


