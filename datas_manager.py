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


def category_to_url(category_name):
    """ Converting category name to url """
    category_name_url = category_name.lower()
    category_name_url = category_name_url.replace(' ', '-')
    category_name_url = category_name_url.replace('é', 'e')
    category_name_url = category_name_url.replace('è', 'e')
    category_name_url = category_name_url.replace('à', 'a')
    category_name_url = category_name_url.replace('ç', 'c')
    category_name_url = category_name_url.replace('ù', 'u')
    category_name_url = category_name_url.replace("'", '-')
    return category_name_url


def products_extract(category_name_url):
    """ Extracting JSON products values and converting into list """
    category_url = "https://fr.openfoodfacts.org/categorie/{0}.json".format(category_name_url)
    products_json = urllib.request.urlopen(category_url)
    products_read = products_json.read()
    products_data = json.loads(products_read.decode("utf-8"))

    key_list = ["product_name", "ingredients_text", "url", "categories" \
                , "stores_tags" , "nutrition_grades"]
    products_list = []
    for content in products_data["products"]:
        products_list_2 = []
        for key, value in content.items():
            if key in key_list:
                products_list_2.append(value)
                products_list.append(products_list_2)
            elif key not in key_list:
                pass
    print(products_list)


def convert_list_tuples(list_name):
    """ Convert list into list of tuples"""
    tuples_list = []
    for x in list_name:
        tuples_list.append((x,))
    return tuples_list


test = category_to_url("Aliments et boissons à base de végétaux")
print(test)
products_extract(test)
