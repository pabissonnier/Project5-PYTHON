# -*- coding: utf-8 -*
from datas_manager import DatasManager
from database_manager import DatabaseManager


# Creation of the instances
categories_list = DatasManager()
products_lists = DatasManager()
category_table = DatabaseManager()


def categories_to_database():
    """ Categories are sent to the databse, to do ONCE """
    """categories_extraction = DatasManager.categories_extract(categories_list)
    categories_tuples_in_list = DatasManager.convert_list_tuples(categories_list, categories_extraction)
    DatabaseManager.categories_to_database(category_table, categories_tuples_in_list)"""

# Products put into the database NE MARCHE PAS
    """test = datas_manager.category_to_url("Aliments et boissons à base de végétaux")
    products_extraction = datas_manager.products_extract("Aliments et boissons à base de végétaux", test)
    database_manager.products_to_database(products_extraction)"""

print(DatabaseManager.category_from_database(category_table))
"""DatasManager.category_to_url(categories_list, )
DatasManager.products_extract(products_lists, )"""
