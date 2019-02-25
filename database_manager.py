import mysql.connector
import mysql


class DatabaseManager:
    """ Class for the management of the database and its datas """
    def __init__(self, table):
        self.table = table

    def connection_to_database(self):
        """ Connection to the databse"""
        cnx = mysql.connector.connect(user="root", password="458127",
                                                host="localhost", database="purbeurre",
                                                auth_plugin='caching_sha2_password')

        cursor = cnx.cursor()
        return cursor

    def categories_to_database(self, category_name):
        """ Puts categories in categories table """

        cursor = DatabaseManager.connection_to_database(self)

        for element in category_name:
            query = "INSERT INTO category(name) VALUES (%s)"
            cursor.execute(query, element)

            cursor.cnx.commit()

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

    def products_to_database(self, category_list):
        """ Puts products into the catabase """

        cursor = DatabaseManager.connection_to_database(self)

        for dict in category_list:
            columns = ', '.join("'" + str(x).replace('/', '_') + "'" for x in dict.keys())
            values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in dict.values())

            cursor.execute("INSERT INTO %s(%s) VALUES (%s);" % ('product', columns, values))
            cursor.cnx.commit()

        print("Names inserted successfully into category table")

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

    def category_choice(self, category_number, category_list):
        """The user selects the category"""

        cursor = DatabaseManager.connection_to_database(self)

        category_row = category_list[category_number-1]

        category_name = category_row[1]

        query_name_in_db = """SELECT "name" FROM 'product' WHERE 'nom_category' = %s"""
        cursor.execute(query_name_in_db, category_name)
        record = cursor.fetchall()

        print(record)
