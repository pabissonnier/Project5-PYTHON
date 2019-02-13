import mysql.connector


def categories_display(category_name):
    """ Connection to the database and put categories in categories table """

    datas_connect = mysql.connector.connect(user="root", password="458127",
                                            host="localhost", database="purbeurre",
                                            auth_plugin='caching_sha2_password')
    cursor = datas_connect.cursor()

    query = "INSERT INTO 'category' ('name') VALUES (%s)"
    cursor.execute(query, category_name)

    datas_connect.close()


