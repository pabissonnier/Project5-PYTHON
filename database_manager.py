import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


def catgories_display(category_number, category_name):
    """ Connection to the database and put categories in categories table """

    datas_connect = mysql.connector.connect(user="root", password = "458127", host = "localhost", database = "purbeurre")
    cursor = datas_connect.cursor()

    sql_insertion = "INSERT INTO 'categories' ('id', 'name') VALUES (%s, %s)",  (category_number, category_name)
    result = cursor.execute(sql_insertion)
    datas_connect.commit()
    print("Datas intégrées")

    datas_connect.close()

