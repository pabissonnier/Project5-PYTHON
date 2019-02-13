# -*- coding: utf-8 -*
import json
from datas_mgmt import *
from database_mgmt import *


def main():
    """Main function"""



    continue_app = True

    while continue_app is True:
        """Application loop"""

        print("Bienvenue sur l'application Pur BEURRE !\nChoisissez un produit que vous souhaitez remplacer par un substitut plus sain...\n ")
        question_1_over = 0
        while question_1_over == 0:
            categoy_choice = input("A quelle catégorie appartient votre produit ? insérez le numéro :")
            try: categoy_choice = int(categoy_choice)
            except: print("Insérez un chiffre")
            if type(categoy_choice) is int:
                question_1_over = 1

        question_2 = True
        while question_2 is True:
            # Choice of the product
            product_choice = input("Quel est votre produit ? insérez le numéro :")
            # vérifier si la variable est bien un int
            # si le produit correspond à celles affichées on sort de la boucle

        question_3 = True
        while question_3 is True:
            # Choice of allergies
            allergies_choice = input("Êtes-vous allergique à un produit ? insérez le numéro (insérez 0 si vous n'êtes pas allergique):")
            # vérifier si la variable est bien un int
            # si le produit correspond à celles affichées on sort de la boucle

        # Affichage des résultats
        # Voir les produits avec leur nutrition_grade_score, description, magasins.


if __name__ == "__main__":
    main()
