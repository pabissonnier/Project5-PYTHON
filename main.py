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

    categories_list = DatabaseManager.categories_show(initialization_database.category_table)
    print(categories_list)

    category_number = input("\nA quelle catégorie appartient votre produit ? insérez le numéro :")
    category_number = int(category_number)

    categories_list_for_products = DatabaseManager.category_from_database(initialization_database.category_table)
    DatabaseManager.products_show(initialization_database.products_table, category_number, categories_list_for_products)


if __name__ == "__main__":
    main()
