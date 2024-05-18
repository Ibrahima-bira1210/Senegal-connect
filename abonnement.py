# Les données des forfaits internet
forfaits_internet = {
    50: {"description": "internet fibre hybride 50", "prix": 12500},
    150: {"description": "internet fibre hybride 150", "prix": 15250},
    500: {"description": "internet fibre hybride 500", "prix": 20500}
}

# Les données des forfaits télé
forfaits_tele = {
    'B': {"description": "forfait bien", "prix": 4900},
    'T': {"description": "forfait tres bien", "prix": 8400},
    'E': {"description": "forfait excellent", "prix": 12500}
}

# Initialisation des variables globales pour le nombre d'abonnés
nombre_abonnes_par_forfait = {
    50: 0,
    150: 0,
    500: 0,
    'B': 0,
    'T': 0,
    'E': 0
}

# Fonction pour afficher le nombre d'abonnés par forfait
def afficher_nombre_abonnes():
    print("\n--- Nombre d'abonnés par forfait ---")
    for key, value in forfaits_internet.items():
        print(f"Forfait {value['description']}: {nombre_abonnes_par_forfait[key]} abonnés")
    for key, value in forfaits_tele.items():
        print(f"Forfait {value['description']}: {nombre_abonnes_par_forfait[key]} abonnés")

