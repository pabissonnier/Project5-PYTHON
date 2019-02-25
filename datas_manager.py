# -*- coding: utf-8 -*
import urllib.request
import json
import database_manager


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


def category_to_url(categories_name_list):
    """ Converting category name to url """
    category_name_url_list = []
    for category_name in categories_name_list:
        category_url_dict = {}
        category_name_url = category_name.lower()
        category_name_url = category_name_url.replace(' ', '-')
        category_name_url = category_name_url.replace('é', 'e')
        category_name_url = category_name_url.replace('è', 'e')
        category_name_url = category_name_url.replace('à', 'a')
        category_name_url = category_name_url.replace('ç', 'c')
        category_name_url = category_name_url.replace('ù', 'u')
        category_name_url = category_name_url.replace("'", '-')
        category_url_dict[category_name] = category_name_url
        category_name_url_list.append(category_url_dict)
    return category_name_url_list


def products_extract(category_name_url_list):
    """ Extracting JSON products values and converting into list """
    for element in category_name_url_list:
        for key_list, value_list in element:
            while i <= 2:
                category_url = "https://fr.openfoodfacts.org/categorie/{0}/{1}.json".format(value_list, i)
                return category_url
                products_json = urllib.request.urlopen(category_url)
                products_read = products_json.read()
                products_data = json.loads(products_read.decode("utf-8"))

                for content in products_data["products"]:
                    products_dict = {}
                    for key, value in content.items():
                        products_dict["nom_category"] = key_list
                        if key == "product_name":
                            products_dict["name"] = value
                        elif key == "url":
                            products_dict["link"] = value
                        elif key == "stores_tags":
                            products_dict["shops"] = value
                        elif key == "ingredients_text_fr":
                            products_dict["ingredients"] = value
                        elif key == "nutrition_grades":
                            products_dict["nutriscore"] = value
                    products_in_category_list.append(products_dict)
                i += 1
            products_list.append(products_in_category_list)
    return products_list


def convert_list_tuples(list_name):
    """ Convert list into list of tuples"""
    tuples_list = []
    for x in list_name:
        tuples_list.append((x,))
    return tuples_list


categories_names = database_manager.category_name_extract()
categories_names_url = category_to_url(categories_names)
#product_url = products_extract(categories_names, categories_names_url)
print(categories_names_url)
