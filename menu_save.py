import os
import sys
import pandas as pd
import re
from timeit import default_timer as timer
import arborescence_tcl


class MainExtraction:
    def __init__(self):
        self.found_station = False

    def create_list_station(self, input_user):
        # with open("input_datas/Listes des arrets en fonction de la ligne.xlsx") as f:
        #     print(f)
        df = pd.read_csv(
            "input_datas/listes_arrets_lignes.csv",
            encoding="cp1252",
            sep=";",
        )
        print(df)
        list_ligne = []
        list_arret = []
        list_provisoire = []
        list_extraction = []
        for index, row in df.iterrows():
            list_ligne.append(row["Ligne"])
            list_arret.append(row["Site"])
        new_ligne_list = list(dict.fromkeys(list_ligne))
        while input_user != 4:
            if input_user == 1:
                print(input_user)
                print(new_ligne_list)
                input_user_ligne = input("Quelle ligne voulez vous extraire :  ")
                for value in new_ligne_list:
                    if input_user_ligne in value:
                        print("Vous voulez bien la ligne : " + value)
                        print_add = value
                        break
                for index, row in df.iterrows():
                    if value == row["Ligne"]:
                        print(row["Site"])
                        list_extraction.append(row["Site"])

            elif input_user == 2:
                print(input_user)
                print(list_arret)
                # user_response = "O"
                # while user_response == "O":
                self.found_station = False
                input_user_ligne = input("Quel arrêt voulez vous extraire :  ")
                input_user_ligne = input_user_ligne.upper()
                for value in list_arret:
                    if input_user_ligne in value:
                        print("Vous voulez bien la station : " + value)
                        list_extraction.append(value)
                        self.found_station = True
                if self.found_station == False:
                    print("Station non trouvé")
                # user_response = input(
                #     "Voulez vous ajouter une autre station ? : (O ou N)"
                # )
                # user_response = user_response.upper()
            elif input_user == 3:
                flag_delete = True
                while flag_delete:
                    print("Liste des stations : ", list_extraction)
                    flag_delete_station = input(
                        ("Vous voulez supprimer une station ? : (O ou N) :")
                    )
                    flag_delete_station = flag_delete_station.upper()
                    if flag_delete_station == "O":
                        station_to_delete = input("Entrez le nom de la station : ")
                        if station_to_delete in list_extraction:
                            for i in list_extraction:
                                if station_to_delete in i:
                                    list_extraction.remove(i)
                        else:
                            print("Station non connu")
                    else:
                        break

            elif input_user == 4:
                break
            print("Liste actuelle : ", list_extraction)
            print(
                f"""1 - Ajouter une ligne complete\n2 - Ajouter une station\n3 - Supprimer une station\n4 - Pour quitter"""
            )
            input_user = int(input("Que voulez vous extraire ? (1 ou 2 ou 3) :  "))

        return list_extraction
        # if row["Ligne"] == "MA":
        #     print(row["Site"])

    def extraction_tcl_doc_file(self, list_a_traiter):
        df = pd.read_csv(
            "input_datas/20221010_ExtratTCLDoc complete modifié.csv",
            encoding="cp1252",
            sep=";",
        )
        # print(df["LIBSITE"].head())

        list_extaction = []

        for index, row in df.iterrows():
            if row["LIBSITE"] in list_a_traiter:
                list_extaction.append(
                    [
                        row["NUMERO_REF_FOURN"],
                        row["REFFIC"],
                        row["LIBSITE"],
                    ],
                )
        print(list_extaction)
        df_extraction = pd.DataFrame(
            list_extaction,
            columns=["Référence fournisseur", "Référence fiche", "Station"],
        )
        return df_extraction

    def extraction_pret_tcl(self):
        df = pd.read_csv(
            "input_datas/20221010_ExtratTCLDoc complete modifié.csv",
            encoding="cp1252",
            sep=";",
        )
        list_extaction = []

        for index, row in df.iterrows():
            if row["DEFINITIF"] == "P":
                list_extaction.append(
                    [
                        row["NUMERO_REF_FOURN"],
                        row["REFFIC"],
                        row["LIBSITE"],
                    ],
                )
        # print(list_extaction)
        df_extraction = pd.DataFrame(
            list_extaction,
            columns=["Référence fournisseur", "Référence fiche", "Station"],
        )
        return df_extraction

    def extraction_serber(self):
        df = pd.read_csv(
            "input_datas/20221010_ExtratTCLDoc complete modifié sans AR.csv",
            encoding="cp1252",
            sep=";",
        )
        list_extaction = []

        for index, row in df.iterrows():
            try:
                if "SERBER" in row["ARMOIRE"]:
                    list_extaction.append(
                        [
                            row["NUMERO_REF_FOURN"],
                            row["REFFIC"],
                            row["ARMOIRE"],
                        ],
                    )
            except Exception as e:
                pass
        # print(list_extaction)
        df_extraction = pd.DataFrame(
            list_extaction,
            columns=["Référence fournisseur", "Référence fiche", "Armoire"],
        )
        print("df_extraction dans la fonction", df_extraction)
        return df_extraction

    def main(self):
        start = timer()

        print("********************************")
        print(
            f"""1 - Choisir d'extraire une ligne complete \n2 - Choisir une station\n4 - Ne rien extraire\n8 - Réaliser une extraction de SERBER\n9 - Réaliser une extraction des prêts """
        )
        input_user = int(input("Que voulez vous extraire ? (1 ou 2) :  "))
        list_a_traiter = None
        df_extraction = None
        # ---------- MODIFIER ICI ----------
        DIRNAME = f"""F:\Tcl\{str(105)} à {str(122)} - Métro A - stations"""
        # DIRNAME = (
        #     f"""F:\Tcl\{str(210)} à {str(213)} - Métro C - stations\Croix-Paquet"""
        # )
        # DIRNAME_SERBER = f"""G:\{str(500000)}"""

        if input_user != 8:
            if input_user == 9:
                name_file_arbo = "output_datas/arborescence_tcl_pret.csv"
                name_file_success = (
                    "output_datas/listes des succes Prêt Complet test.csv"
                )
                name_file_failed = (
                    "output_datas/listes des echecs Prêt Complet test.csv"
                )
            else:
                name_file_arbo = "output_datas/arborescence_ligne_a.csv"
                name_file_success = (
                    "output_datas/listes des succes TCL LIGNE A test.csv"
                )
                name_file_failed = "output_datas/listes des echecs TCL LIGNE A test.csv"

            list_a_traiter = self.create_list_station(input_user)
            df_extraction = self.extraction_tcl_doc_file(list_a_traiter)
            arborescence_tcl.create_arbo(DIRNAME, name_file_arbo)
            arborescence_tcl.compare_list_arbo_csv_bi(
                name_file_arbo, df_extraction, name_file_success, name_file_failed
            )
        else:
            DIRNAME_SERBER = f"""G:\{str(1)}00000"""
            name_file_arbo = "output_datas/arborescence_serber 100000.csv"
            name_file_success = "output_datas/listes des succes serber 100000.csv"
            name_file_failed = "output_datas/listes des echecs serber 100000.csv"
            df_extraction = self.extraction_serber()
            arborescence_serber.create_arbo(DIRNAME_SERBER, name_file_arbo)
            arborescence_serber.compare_list_arbo_csv_bi(
                name_file_arbo, df_extraction, name_file_success, name_file_failed
            )
        print("La listes des arrêt à traiter est ", list_a_traiter)
        print("Nombre de références dans l'extraction", df_extraction)
        print(DIRNAME)
        # end = timer()
        # print(end - start)


Extraction = MainExtraction()
Extraction.main()
# Extraction.extraction_tcl_doc_file()
