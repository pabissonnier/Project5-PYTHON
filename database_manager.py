import mysql.connector
import mysql
from difflib import SequenceMatcher


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
        prod_list = []
        for prod_tuples in my_results:
            for prod_str in prod_tuples:
                prod_list2 = []
                prod_list2.append(i)
                prod_list2.append(prod_str)
                i += 1
            prod_list.append(prod_list2)

        return prod_list

    def get_number_products(self, products_whole_list):
        """ Get maximum number of products in list """
        for product in products_whole_list[-1]:
            return product

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

        query = "SELECT name, nutriscore, link FROM product WHERE nom_category = %s"
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
        better_nutriscores_list = []
        nutriscore_product = nutriscore.upper()
        if nutriscore_product in nutriscore_list[1:]:
            nutriscore_position = nutriscore_list.index(nutriscore_product)
            nutriscores_wanted = nutriscore_list[:nutriscore_position]
            for elements in nutriscores_wanted:
                better_nutriscores_list.append(elements)
        elif nutriscore_product == nutriscore_list[0]:
            nutriscores_wanted = nutriscore_list[0]
            better_nutriscores_list.append(nutriscores_wanted)
        return better_nutriscores_list

    def extract_products_for_replace(self, category_chosen, better_nutriscores_list):
        """ Takes products with same category and higer nutriscore"""
        cursor = DatabaseManager.connection_to_database(self)

        products_for_replace = []

        for nutriscore in better_nutriscores_list:

            data = (category_chosen, nutriscore)
            query = "SELECT name, nutriscore, link FROM product WHERE nom_category = %s AND nutriscore = %s"
            cursor.execute(query, data)

            products_with_better_nutriscore = cursor.fetchall()
            products_for_replace.append(products_with_better_nutriscore)

        return products_for_replace

    def check_name_ratio(self, product_name, products_for_replace):
        """ Checks similar name to repalce a product """
        products_ratio_list = []
        for value in products_for_replace:
            for element in value:
                product_ratio = []
                product_for_replace = element[0]
                nutriscore = element[1]
                link = element[2]
                product_score = SequenceMatcher(None, product_name, product_for_replace).ratio()
                product_ratio_couple = product_for_replace, nutriscore, link, product_score
                if product_score > 0.25:
                    product_ratio.append(product_ratio_couple)

                products_ratio_list.append(product_ratio)
        return products_ratio_list

    def get_best_nutriscore(self, product_list):
        "Get best nutriscore possible "
        nutriscore_list = ['A', 'B', 'C', 'D', 'E']
        best_nutriscore_list = []
        for element in product_list:
            for product_tuple in element:
                best_nutriscore_list.append(product_tuple[1])

        best_nutriscore = min(best_nutriscore_list)
        return best_nutriscore

    def list_products_best_nutriscore(self, products_ratio_list, best_nutriscore):
        """ Update list with only """
        products_list_best_nutriscore = []
        for element in products_ratio_list:
            for values in element:
                if values[1] == best_nutriscore:
                    products_list_best_nutriscore.append(values)
        return products_list_best_nutriscore

    def get_best_ratio(self, products_list_best_nutriscore):
        """ Get best ratio """
        ratio_list = []
        for element in products_list_best_nutriscore:
            ratio_list.append(element[2])
        best_ratio = max(ratio_list)
        return best_ratio

    def get_products_for_replace(self, products_list_best_nutriscore, best_ratio):
        """ Get product with same name with higher nutriscore"""
        for element in products_list_best_nutriscore:
            if element[2] == best_ratio:
                return element

    def get_result(self, product_for_replace):
        """ Get product for replacement with infos """
        cursor = DatabaseManager.connection_to_database(self)

        name = product_for_replace[0]
        nutriscore = product_for_replace[1]
        link = product_for_replace[2]

        datas = (name, nutriscore, link)

        query = "SELECT name, ingredients, nutriscore, shops, link FROM product WHERE name = %s AND nutriscore = %s AND link = %s"
        cursor.execute(query, datas)

        my_results = cursor.fetchall()

        return my_results

    def show_result(self, my_results):
        """ Show results """
        for element in my_results:
            name_results = element[0]
            ingredients_results = element[1]
            nutriscore_results = element[2]
            shops_results = element[3]
            link_results = element[4]

            results = "\nVoici le produit se rapprochant le plus du vôtre avec de meilleures qualités nutritionnelles :\n\n" \
                      "Nom : {0}\nIngrédients : {1}\nNutriscore :{2}\nShops : {3}\nLink : {4}".format(name_results, ingredients_results, nutriscore_results, shops_results, link_results)

            return results

    def save_product_database(self, my_result):
        """ User can save product to the database """
        try:
            cursor = DatabaseManager.connection_to_database(self)

            for element in my_result:
                name_results = element[0]
                ingredients_results = element[1]
                nutriscore_results = element[2]
                shops_results = element[3]
                link_results = element[4]

            answer = input("\nVoulez-vous sauvegarder ce produit ? Tapez 1 pour oui et 0 pour non :")
            answer = int(answer)
            if answer == 1:
                query = """INSERT INTO usertable (name, ingredients, nutriscore, shops, link) VALUES (%s, %s, %s, %s, %s)"""
                cursor.execute(query, (name_results, ingredients_results, nutriscore_results, shops_results, link_results))

                cnx.commit()

                print("Produit enregistré !")

        except mysql.connector.Error:
            cnx.rollback()
            print("Import du produit impossible")

        finally:
            if cnx.is_connected():
                cursor.close()

    def show_products_history(self):
        """ Show products from the user database """
        cursor = DatabaseManager.connection_to_database(self)

        answer = input("\nTapez 1 pour voir l'historique de vos produits (sinon tapez autre chose) :")

        if answer == 1:
            cursor.execute("SELECT * FROM usertable")

            my_results = cursor.fetchall()

            for element in my_results:
                name_results = element[0]
                ingredients_results = element[1]
                shops_results = element[2]
                link_results = element[3]
                nutriscore_results = element[4]

                results = "\nNom : {0}\nIngrédients : {1}\nNutriscore :{2}\nShops : {3}" \
                          "\nLink : {4}\n".format(name_results, ingredients_results, nutriscore_results, shops_results, link_results)

                print(results)

        else:
            pass
