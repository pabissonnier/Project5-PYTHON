# -*- coding: utf-8 -*
from datas_manager import DatasManager
from database_manager import DatabaseManager


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


def products_to_database():
    """ Prodcuts are sent to the databse, to do ONCE, DONE """
    category_name = DatabaseManager.category_from_database(category_table)
    category_url_list = DatasManager.category_to_url(categories_list, category_name)
    products_datas = DatasManager.products_extract(products_lists, category_url_list)
    DatabaseManager.products_to_database(products_table, products_datas)

products_to_database()



