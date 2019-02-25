# -*- coding: utf-8 -*
import datas_manager
import database_manager


def main():
    """Main function"""

    # Categories put into the database
    """datas_extraction = datas_manager.categories_extract()
    list_tuples = datas_manager.convert_list_tuples(datas_extraction)
    database_manager.categories_to_database(list_tuples)"""

    # Products put into the database NE MARCHE PAS
    """test = datas_manager.category_to_url("Aliments et boissons à base de végétaux")
    products_extraction = datas_manager.products_extract("Aliments et boissons à base de végétaux", test)
    database_manager.products_to_database(products_extraction)""" # Problème au niveau des colonnes


    """Application loop"""

    # ACCUEIL
    print(
        "Bienvenue sur l'application Pur BEURRE !\n"
        "Choisissez un produit que vous souhaitez remplacer par un substitut plus sain...\n ")

    # QUESTION 1

    categories_list = database_manager.categories_show()

    category_choice = input("\nA quelle catégorie appartient votre produit ? insérez le numéro :")

    for element in categories_list:
        for key, value in element:
            if category_choice == key:
                print(value)


    # QUESTION 2
    # Choice of the product
    product_choice = input("Quel est votre produit ? insérez le numéro :")
    # vérifier si la variable est bien un int
    # si le produit correspond à celles affichées on sort de la boucle

    question_3 = True
    while question_3 is True:
        # Choice of allergies
        allergies_choice = input(
            "Êtes-vous allergique à un produit ? insérez le numéro (insérez 0 si vous n'êtes pas allergique):")
        # vérifier si la variable est bien un int
        # si le produit correspond à celles affichées on sort de la boucle

    # Affichage des résultats
    # Voir les produits avec leur nutrition_grade_score, description, magasins.


if __name__ == "__main__":
    main()
