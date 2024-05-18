import facture
import abonnement


def menu():
    while True :
        print("\nBienvenue chez Sénégal-Connect!")
        print("1- Facturer un abonnement")
        print("2- Afficher le nombre d’abonnés par forfait")
        print("3- Quitter le programme")
        choix = input('faite votre choix')

        listChoix = ["1", "2", "3"]

        while choix not in listChoix:
            print("veuilllbnhndf,hj ")
            choix = input('faite votre choix')

        if choix == '1':
            # Facturer un abonnement
            facture.saisir_donnees()
        elif choix == '2':
            # Afficher le nombre d'abonnés par forfait
            abonnement.afficher_nombre_abonnes()
        elif choix == '3':
            # Quitter le programme
            print("Merci d'utiliser Sénégal-Connect. Au revoir!")
            break



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
