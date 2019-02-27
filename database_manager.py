import mysql.connector
import mysql
import product_list_test

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
                """placeholders = ', '.join(['?'] * len(products_dicts.values()))
                columns = ', '.join(products_dicts.keys())
                query = "INSERT INTO product (%s) VALUES (%s)" % (columns, placeholders)
                cursor.execute(query, products_dicts.keys(), products_dicts.values())
                cnx.commit()"""

                """placeholder = ', '.join(["%s"] * len(products_dicts))
                query = "INSERT INTO product ({columns}) VALUES ({values});".format(columns=",".join(products_dicts.keys()), values = placeholder)
                cursor.execute(query, list(products_dicts.values()))
                cnx.commit()"""

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

    def category_choice(self, category_number, category_list):
        """The user selects the category"""

        cursor = DatabaseManager.connection_to_database(self)

        category_row = category_list[category_number-1]

        category_name = category_row[1]

        query_name_in_db = """SELECT "name" FROM 'product' WHERE 'nom_category' = %s"""
        cursor.execute(query_name_in_db, category_name)
        record = cursor.fetchall()

        print(record)
