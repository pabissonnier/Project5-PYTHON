import mysql.connector
import mysql


def categories_to_database(category_name):
    """ Connection to the database and put categories in categories table """

    connection = mysql.connector.connect(user="root", password="458127",
                                            host="localhost", database="purbeurre",
                                            auth_plugin='caching_sha2_password')

    cursor = connection.cursor()
    query = "INSERT INTO category(nom) VALUES (%s)"
    cursor.execute(query, category_name)
    #cursor.execute("INSERT INTO category (nom) VALUES ('test')")
    connection.commit()
    print("Names inserted successfully into category table")
    cursor.close()
    connection.close()

    """except mysql.connector.Error as error:
        connection.rollback()
        print("Failed to insert record")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")"""


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

categories_show()
