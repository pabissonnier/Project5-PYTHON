# -*- coding: utf-8 -*
from datas_manager import DatasManager
from database_manager import DatabaseManager
from product_list_test import *


# Creation of the instances
categories_list = DatasManager()
products_lists = DatasManager()
category_table = DatabaseManager()
products_table = DatabaseManager()


def categories_to_database():
    """ Categories are sent to the databse, to do ONCE, DONE """
    categories_extraction = DatasManager.categories_extract(categories_list)
    categories_tuples_in_list = DatasManager.convert_list_tuples(categories_list, categories_extraction)
    DatabaseManager.categories_to_database(category_table, categories_tuples_in_list)

# Products put into the database NE MARCHE PAS
    """test = datas_manager.category_to_url("Aliments et boissons à base de végétaux")
    products_extraction = datas_manager.products_extract("Aliments et boissons à base de végétaux", test)
    database_manager.products_to_database(products_extraction)"""


"""category_name = DatabaseManager.category_from_database(category_table)
category_url_list = DatasManager.category_to_url(categories_list, category_name)
products_datas = DatasManager.products_extract(products_lists, category_url_list)
DatabaseManager.products_to_database(products_table, products_datas)"""

list_test = [
    [{'nom_category': 'Aliments à base de fruits et de légumes', 'shops': "leclercl",
      'nutriscore': 'c', 'ingredients': '_ noix de cajou _ 25%, _ noix _ 25%, _ noisettes _ 25%, _ amandes _ 25%',
      'link': 'https://fr.openfoodfacts.org/',
      'name': 'Noix de cajou & cranberries'},
     {'nom_category': 'Aliments à base de fruits et de légumes',
      'ingredients': "conserver frais h de f9gricufture biologiqu Poids Nef A de préférence avan(ié' 25%9/2021 04 76 95 56 70",
      'link': 'https://fr.openfoodfacts.org/',
      'name': 'Confiture de framboise', 'nutriscore': 'c', 'shops': "leclerc"},
     {'nom_category': 'Aliments à base de fruits et de légumes',
      'link': 'https://fr.openfoodfacts.org/produit/',
      'name': 'Asperges blanches pelées',
      'shops': 'leclerc','nutriscore': 'a', 'ingredients': '_ noix de cajou _ 25%, _ noix _ 25%, _ noisettes _ 25%, _ amandes _ 25%'},
     {'nom_category': 'Aliments à base de fruits et de légumes',
      'link': 'https://fr.openfoodfacts.org/produit/26042473/',
      'name': 'Poires Williams au sirop léger', 'ingredients': 'Poires, eau, sucre, acidifiant : acide citrique, antioxydant : acide ascorbique',
      'shops': 'leclercl', 'nutriscore': 'a'}]
    ]

DatabaseManager.products_to_database(products_table, list_test)
