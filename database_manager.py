import mysql.connector
import mysql
from difflib import SequenceMatcher
from datas_manager import DatasManager

# Database connection
cnx = mysql.connector.connect(user="root", password="458127",
                                                host="localhost", database="purbeurre",
                                                auth_plugin='caching_sha2_password')


class DatabaseManager:
    """ Class for the management of the database and its datas """
    def __init__(self):
        pass

    def connection_to_database(self):
        """ Connection to the databse"""
        cursor = cnx.cursor()
        return cursor

    def categories_to_database(self, category_list):
        """ Puts categories in categories table """
        cursor = DatabaseManager.connection_to_database(self)

        for element in category_list:
            query = "INSERT INTO category (name) VALUES (%s)"
            cursor.execute(query, element)

        cnx.commit()

        print("Names inserted successfully into category table")

    def category_name_extract(self):
        """ Takes category name from the database to use products url from the API """

        cursor = DatabaseManager.connection_to_database(self)

        categories_list = []
        cursor.execute("SELECT * FROM category")
        my_results = cursor.fetchall()
        for element in my_results:
            for product_name in element:
                categories_list.append(product_name)
        return categories_list

    def products_to_database(self, products_lists):
        """ Puts products into the database """

        cursor = DatabaseManager.connection_to_database(self)

        for category_products_list in products_lists:
            for products_dicts in category_products_list:
                cursor.execute("INSERT INTO product (name, nom_category, ingredients, shops, "
                               "link, nutriscore) VALUES (%(name)s, %(nom_category)s, %(ingredients)s, "
                               "%(shops)s, %(link)s, %(nutriscore)s)", products_dicts)
                cnx.commit()

        print("Names inserted successfully into product table")

    def categories_show(self):
        """ Showing categories from DB to console """

        cursor = DatabaseManager.connection_to_database(self)

        cursor.execute("SELECT * FROM category")

        my_results = cursor.fetchall()

        i = 1
        cat_list = []
        for cat_tuples in my_results:
            for cat_str in cat_tuples:
                cat_list2 = []
                cat_list2.append(i)
                cat_list2.append(cat_str)
                i += 1
            cat_list.append(cat_list2)

        for cat_list2 in cat_list:
            print(cat_list2)

    def category_from_database(self):
        """ Extract categories from database to get products """
        cursor = DatabaseManager.connection_to_database(self)

        cursor.execute("SELECT * FROM category")

        my_results = cursor.fetchall()

        categories_list = []
        for cat_tuples in my_results:
            for value in cat_tuples:
                categories_list.append(value)
        return categories_list

    def str_to_tuple(self, str_to_transform):
        """ Converts string to tuple to extract from DB"""
        tuple_with_str = (str_to_transform, )
        return tuple_with_str

    def category_name_chosen(self, category_number):
        """ The user selects the number of the category and this returns the name of the category"""

        category_list = DatabaseManager.category_from_database(self)

        category_position = category_number-1

        category_name = category_list[category_position]
        return category_name

    def products_show(self, category_number):
        """The user selects the category and the products are shown"""

        cursor = DatabaseManager.connection_to_database(self)

        category_name = DatabaseManager.category_name_chosen(self, category_number)

        category_name_tuple = DatabaseManager.str_to_tuple(self, category_name)

        query_name_in_db = """SELECT name FROM product WHERE nom_category = %s"""
        cursor.execute(query_name_in_db, category_name_tuple)
        my_results = cursor.fetchall()

        i = 1
        cat_list = []
        for prod_tuples in my_results:
            for prod_str in prod_tuples:
                prod_list2 = []
                prod_list2.append(i)
                prod_list2.append(prod_str)
                i += 1
            cat_list.append(prod_list2)

        for cat_list2 in cat_list:
            print(cat_list2)

    def products_from_database(self):
        """ Extract categories from database to get products """
        cursor = DatabaseManager.connection_to_database(self)

        cursor.execute("SELECT name FROM product")

        my_results = cursor.fetchall()

        products_list = []
        for prod_tuples in my_results:
            for value in prod_tuples:
                products_list.append(value)
        return products_list

    def product_choice(self, product_number, category_chosen):
        """ Choice of the product to replace"""
        cursor = DatabaseManager.connection_to_database(self)

        query = "SELECT name, nutriscore FROM product WHERE nom_category = %s"
        cursor.execute(query, (category_chosen, ))

        my_results = cursor.fetchall()

        products_list = []
        product_position = product_number-1
        for prod_tuples in my_results:
            prod_tuples = prod_tuples + (product_position,)
            products_list.append(prod_tuples)
        product_name_ns_pos = products_list[product_position]

        return product_name_ns_pos

    def get_product_name(self, product_choice):
        """ Extract nutriscore for a list of products """
        product_name = product_choice[0]
        return product_name

    def get_product_nutriscore(self, product_choice):
        """ Extract nutriscore for a list of products """
        product_nutriscore = product_choice[1]
        return product_nutriscore

    def get_product_index(self, product_choice):
        """ Extract nutriscore for a list of products """
        product_index = product_choice[2]
        return product_index

    def better_nutriscore(self, nutriscore):
        """ Find products in the same category with better nutriscore """
        nutriscore_list = ['A', 'B', 'C', 'D', 'E']
        better_nutriscores = []
        nutriscore_product = nutriscore.upper()
        if nutriscore_product in nutriscore_list[4:]:
            nutriscore_position = nutriscore_list.index(nutriscore_product)
            nutriscores_wanted = nutriscore_list[:nutriscore_position]
            better_nutriscores.append(nutriscores_wanted)
        elif nutriscore_product == nutriscore_list[0]:
            nutriscores_wanted = nutriscore_list[0]
            better_nutriscores.append(nutriscores_wanted)
        return better_nutriscores

    def extract_products_for_replace(self, category_number, product_nutriscore):
        """ Takes products with same category and higer nutriscore"""
        cursor = DatabaseManager.connection_to_database(self)

        category_name = DatabaseManager.category_name_chosen(self, category_number)

        nutriscores_wanted = DatabaseManager.better_nutriscore(self, product_nutriscore)

        data = (category_name, nutriscores_wanted)

        query = "SELECT name FROM product WHERE nom_category = %s AND nutriscore = %s"
        cursor.execute(query, data)

        products_with_better_nutriscore = cursor.fetchall()

        return products_with_better_nutriscore

    def check_name_ratio(self, product_name, products_with_better_nutriscore):
        """ Checks similar name to repalce a product """
        products_ratio_list = []
        for value in products_with_better_nutriscore:
            product_name = product_name[0]
            value = value[0]
            product_ratio = []
            product_ratio.append(value)
            product_score = SequenceMatcher(None, product_name, value).ratio()
            product_ratio.append(product_score)
            products_ratio_list.append(product_ratio)
        print(products_ratio_list)
