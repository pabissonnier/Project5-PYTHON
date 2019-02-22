import mysql.connector
import mysql


def connection_to_database ():
    """ Connection to the databse"""
    pass


def categories_to_database(category_name):
    """ Puts categories in categories table """

    cnx = mysql.connector.connect(user="root", password="458127",
                                            host="localhost", database="purbeurre",
                                            auth_plugin='caching_sha2_password')

    cursor = cnx.cursor()

    for element in category_name:
        query = "INSERT INTO category(name) VALUES (%s)"
        cursor.execute(query, element)

        cnx.commit()

    print("Names inserted successfully into category table")


def products_to_database(category_list):
    """ Puts products into the catabase """

    cnx = mysql.connector.connect(user="root", password="458127",
                                            host="localhost", database="purbeurre",
                                            auth_plugin='caching_sha2_password')

    cursor = cnx.cursor()

    for dict in category_list:
        columns = ', '.join("'" + str(x).replace('/', '_') + "'" for x in dict.keys())
        values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in dict.values())

        cursor.execute("INSERT INTO %s(%s) VALUES (%s);" % ('product', columns, values))
        cnx.commit()

    print("Names inserted successfully into category table")


def categories_show():
    """ Showing categories from DB to console """

    connection = mysql.connector.connect(user="root", password="458127",
                                            host="localhost", database="purbeurre",
                                            auth_plugin='caching_sha2_password')

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM test")

    my_results = cursor.fetchall()

    for x in my_results:
        print(x)

