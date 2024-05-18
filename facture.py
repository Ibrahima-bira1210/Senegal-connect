import datetime
import abonnement

# Initialisation du numéro de facture
numero_facture = 1

# Fonction pour saisir les données et facturer un abonnement
def saisir_donnees():
    global numero_facture

    # Saisie des informations de l'abonné
    nom = input("Nom: ")
    prenom = input("Prénom: ")
    telephone = input("Numéro de téléphone: ")
    adresse = input("Adresse: ")
    service = input("Type de service désiré (1 = Internet, 2 = Télé, 3 = Internet et Télé): ")

    # Validation du type de service
    if service not in ['1', '2', '3']:
        print("Service invalide.")
        return

    service = int(service)
    forfaits_choisis = []

    # Saisie et validation du forfait internet
    if service == 1:
        identifiant = int(input("Identifiant du forfait internet (50, 150, 500): "))
        if identifiant not in abonnement.forfaits_internet:
            print("Identifiant de forfait internet invalide.")
            return
        forfaits_choisis.append(abonnement.forfaits_internet[identifiant])
        abonnement.nombre_abonnes_par_forfait[identifiant] += 1

    # Saisie et validation du forfait télé
    elif service == 2:
        identifiant = input("Identifiant du forfait télé (B, T, E): ").upper()
        if identifiant not in abonnement.forfaits_tele:
            print("Identifiant de forfait télé invalide.")
            return
        forfaits_choisis.append(abonnement.forfaits_tele[identifiant])
        abonnement.nombre_abonnes_par_forfait[identifiant] += 1
    # Saisie et validation des forfaits internet et télé
    elif service == 3:
        identifiant_internet = int(input("Identifiant du forfait internet (50, 150, 500): "))
        identifiant_tele = input("Identifiant du forfait télé (B, T, E): ").upper()
        if identifiant_internet not in abonnement.forfaits_internet or identifiant_tele not in abonnement.forfaits_tele:
            print("Identifiant de forfait invalide.")
            return
        forfaits_choisis.append(abonnement.forfaits_internet[identifiant_internet])
        forfaits_choisis.append(abonnement.forfaits_tele[identifiant_tele])
        abonnement.nombre_abonnes_par_forfait[identifiant_internet] += 1
        abonnement.nombre_abonnes_par_forfait[identifiant_tele] += 1

    # Saisie et validation du mode de paiement
    mode_paiement = input("Mode de paiement (1 = Carte de crédit, 2 = PayPal, 3 = Virement bancaire): ")
    if mode_paiement not in ['1', '2', '3']:
        print("Mode de paiement invalide.")
        return

    # Calcul de la facture
    sous_total = sum(forfait["prix"] for forfait in forfaits_choisis)
    tva = sous_total * 0.18
    total = sous_total + tva

    # Génération de la facture
    date_facturation = datetime.datetime.now()
    print(f"\n--- Facture ---")
    print(f"Numéro de facture: {numero_facture}")
    print(f"Nom: {nom}")
    print(f"Prénom: {prenom}")
    print(f"Numéro de téléphone: {telephone}")
    print(f"Adresse: {adresse}")
    print(f"Date de facturation: {date_facturation}")
    for forfait in forfaits_choisis:
        print(f"Forfait: {forfait['description']} - Prix: {forfait['prix']} FCFA")
    print(f"Sous-total: {sous_total} FCFA")
    print(f"TVA (18%): {tva} FCFA")
    print(f"Total: {total} FCFA")
    print(f"Mode de paiement: {mode_paiement}")
    print(f"-----------------")

    # Incrémentation du numéro de facture
    numero_facture += 1