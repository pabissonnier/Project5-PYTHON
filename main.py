# -*- coding: utf-8 -*
import application
from database_manager import DatabaseManager
import initialization_database


def main():
    """Main function"""

    continue_application = True

    while continue_application:

        # ACCUEIL
        print(
            "Bienvenue sur l'application Pur BEURRE !\n"
            "Choisissez un produit que vous souhaitez remplacer par un substitut plus sain...\n ")

        while True:
            start_or_history = input("Tapez 1 pour commencer ou 0 pour voir votre historique :")
            try:
                start_or_history = int(start_or_history)
            except TypeError:
                print("Insérez un nombre !")
            if start_or_history == 0:
                DatabaseManager.show_products_history_begin(initialization_database.products_table, start_or_history)
                break
            elif start_or_history == 1:
                break
            else:
                print("La valeur ne correspond pas !")

        # QUESTION 1

        # Showing list of categories
        DatabaseManager.categories_show(initialization_database.category_table)

        # Getting number for the category
        while True:
            category_number = input("\nA quelle catégorie appartient votre produit ? insérez le numéro :")
            try:
                category_number = int(category_number)
            except TypeError:
                print("Insérez un nombre !")
            if 0 < category_number < 53:
                break
            else:
                print("La valeur ne correspond à aucune catégorie !")

        # The category chosen by the user
        category_chosen = DatabaseManager.category_name_chosen(initialization_database.category_table, category_number)

        # QUESTION 2

        # From category chosen in the category list, showing the list of products
        products_whole_list = DatabaseManager.products_show(initialization_database.products_table, category_number)
        for element in products_whole_list:
            print(element)

        # Get number of indexes in the product list
        last_product_number = DatabaseManager.get_number_products(initialization_database.products_table, products_whole_list)

        while True:
            product_choice_number = input("\nQuel produit souhaitez-vous remplacer ? Insérez le numéro :")
            try:
                product_choice_number = int(product_choice_number)
            except TypeError:
                print("Insérez un nombre !")

            if 0 < product_choice_number < last_product_number:
                break
            else:
                print("La valeur ne correspond à aucun produit !")

        # Product chosen elements
        product_name_ns = DatabaseManager.product_choice(initialization_database.products_table, product_choice_number, category_chosen)
        product_name = DatabaseManager.get_product_name(initialization_database.products_table, product_name_ns)
        product_ns = DatabaseManager.get_product_nutriscore(initialization_database.products_table, product_name_ns)
        product_index = DatabaseManager.get_product_index(initialization_database.products_table, product_name_ns)

        # Get list with better nutriscore or equivalent if A
        better_nutriscore_list = DatabaseManager.better_nutriscore(initialization_database.products_table, product_ns)

        # Getting the list of products in the category chosen where nutriscore is higher
        products_list_better_nutriscore = DatabaseManager.extract_products_for_replace(initialization_database.products_table, category_chosen, better_nutriscore_list)

        # Getting list with name, nutriscore and name.ratio
        products_ratio_list = DatabaseManager.check_name_ratio(initialization_database.products_table, product_name, products_list_better_nutriscore)

        # Get 1 to 3 products with description with best ratio
        best_nutriscore_of_category = DatabaseManager.get_best_nutriscore(initialization_database.products_table, products_ratio_list)
        products_list_best_nutriscore = DatabaseManager.list_products_best_nutriscore(initialization_database.products_table, products_ratio_list, best_nutriscore_of_category)
        best_ratio = DatabaseManager.get_best_ratio(initialization_database.products_table, products_list_best_nutriscore)
        results_list = DatabaseManager.get_products_for_replace(initialization_database.products_table, products_list_best_nutriscore, best_ratio)
        result = DatabaseManager.get_result(initialization_database.products_table, results_list)
        show_result = DatabaseManager.show_result(initialization_database.products_table, result)

        """print(product_name_ns)
        print(product_name)
        print(product_ns)
        print(product_index)
        print(better_nutriscore_list)
        print(products_ratio_list)
        print(best_nutriscore_of_category)
        print(best_ratio)
        print(products_list_best_nutriscore)
        print(results_list)"""
        print(show_result)

        DatabaseManager.save_product_database(initialization_database.products_table, result)
        DatabaseManager.show_products_history_end(initialization_database.products_table)

        continue_application = application.continue_application()


if __name__ == "__main__":
    main()
