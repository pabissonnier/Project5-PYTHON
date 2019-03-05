# -*- coding: utf-8 -*


def continue_game():
    """ Continue game or not """
    once_again = input("Voulez-vous continuer ? Tapez 1 pour oui et 0 pour non :")
    once_again = int(once_again)

    if once_again == 1:
        return True

    elif once_again == 0:
        print("\nMerci pour votre visite et à bientôt !")
        return False
