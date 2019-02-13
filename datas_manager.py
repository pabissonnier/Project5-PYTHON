# -*- coding: utf-8 -*
import urllib.request
import json
import mysql.connector
import mysql


def categories_extract():
    """ Parse JSON into a list """

    categories_json = urllib.request.urlopen('https://fr.openfoodfacts.org/categories.json')
    categories_read = categories_json.read()
    categories_data = json.loads(categories_read.decode("utf-8"))

    for value in categories_data["tags"]:
        if value["products"] >= 4017:
            categories_values = value["name"]

            connection = mysql.connector.connect(user="root", password="458127",
                                            host="localhost", database="purbeurre",
                                            auth_plugin='caching_sha2_password')

            cursor = connection.cursor()
            sql_query = "INSERT INTO category 'nom' VALUES %s"
            cursor.execute(sql_query, categories_values)
            connection.commit()
            print("Names inserted successfully into category table")

            """except mysql.connector.Error as error:
                connection.rollback()
                print("Failed to insert record")

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
                    print("MySQL connection is closed")"""




categories_extract()

