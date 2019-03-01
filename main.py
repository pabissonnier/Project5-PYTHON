# -*- coding: utf-8 -*
from datas_manager import DatasManager
from database_manager import DatabaseManager
import initialization_database


def main():
    """Main function"""

    # ACCUEIL
    print(
        "Bienvenue sur l'application Pur BEURRE !\n"
        "Choisissez un produit que vous souhaitez remplacer par un substitut plus sain...\n ")

    # QUESTION 1

    # Showing list of categories
    categories_list = DatabaseManager.categories_show(initialization_database.category_table)
    print(categories_list)

    # Getting number for the category
    category_number = input("\nA quelle catégorie appartient votre produit ? insérez le numéro :")
    category_number = int(category_number)

    # The category chosen by the user
    category_chosen = DatabaseManager.category_name_chosen(initialization_database.category_table, category_number)

    # QUESTION 2

    # From category chosen in the category list, showing the list of products
    DatabaseManager.products_show(initialization_database.products_table, category_number)

    product_choice_number = input("\nQuel produit souhaitez-vous remplacer ? Insérez le numéro :")
    product_choice_number = int(product_choice_number)

    # Product chosen elements
    product_name_ns = DatabaseManager.product_choice(initialization_database.products_table, product_choice_number, category_chosen)
    product_name = DatabaseManager.get_product_name(initialization_database.products_table, product_name_ns)
    product_ns = DatabaseManager.get_product_nutriscore(initialization_database.products_table, product_name_ns)

    # Get list with better nutriscore or equivalent if A
    better_nutriscore_list = DatabaseManager.better_nutriscore(initialization_database.products_table, product_ns)

    # Getting the list of products in the category chosen where nutriscore is higher
    #products_list_A = DatabaseManager.extract_products_for_replace(initialization_database.products_table, category_number)

    #product_list = DatabaseManager.products_from_database(initialization_database.products_table)

    #products_ratio_list = DatabaseManager.check_name_ratio(initialization_database.products_table, product_name, products_list_A)

    print(product_ns)
    print(product_name)
    print(better_nutriscore_list)


if __name__ == "__main__":
    main()
