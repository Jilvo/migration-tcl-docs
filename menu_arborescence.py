import os
import sys
import pandas as pd
import re
from timeit import default_timer as timer
import time
import arborescence_tcl
import arborescence_tcl_tout_darfeuille
import arborescence_tcl_pret
import arborescence_tcl_reprise_echecs
import arborescence_serber
from pprint import pprint


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
        # print(df)
        list_ligne = []
        list_arret = []
        list_provisoire = []
        list_extraction = []
        for index, row in df.iterrows():
            list_ligne.append(row["Ligne"])
            list_arret.append(row["Site"])
        new_ligne_list = list(dict.fromkeys(list_ligne))
        while input_user != 4:
            print("------------------------")
            if input_user == 1:
                print("Vous avez choisi ", input_user)
                pprint(new_ligne_list)
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
                pprint(list_arret)
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
                        ("Vous voulez supprimer une station ? : (O ou N) : ")
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
                f"""1 - Ajouter une ligne complete\n2 - Ajouter une station\n3 - Supprimer une station\n4 - Pour lancer la recherche"""
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
        dict_df = {}
        # NOUVELLE METHODE PAR LIGNE VIA DICT DE DATAFAME
        for station in list_a_traiter:
            list_station = []
            print("station actuelle : ", station)
            for index, row in df.iterrows():
                if row["LIBSITE"] in station:
                    list_station.append(
                        [
                            row["NUMERO_REF_FOURN"],
                            row["REFFIC"],
                            row["LIBSITE"],
                        ],
                    )
            df_extraction = pd.DataFrame(
                list_station,
                columns=["Référence fournisseur", "Référence fiche", "Station"],
            )
            dict_df[station] = df_extraction

        # ANCIENNE METHODE FILTRE PAR LIGNE
        # for index, row in df.iterrows():
        #     if row["LIBSITE"] in list_a_traiter:
        #         list_extaction.append(
        #             [
        #                 row["NUMERO_REF_FOURN"],
        #                 row["REFFIC"],
        #                 row["LIBSITE"],
        #             ],
        #         )
        # print(list_extaction)
        # df_extraction = pd.DataFrame(
        #     list_extaction,
        #     columns=["Référence fournisseur", "Référence fiche", "Station"],
        # )
        # return df_extraction
        print(dict_df)
        return dict_df

    def extraction_tcl_doc_rattrapage_echecs(self, list_a_traiter):
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
        df_extraction_rattrapage = pd.DataFrame(
            list_extaction,
            columns=["Référence fournisseur", "Référence fiche", "Station"],
        )
        return df_extraction_rattrapage

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
        df_extraction_pret = pd.DataFrame(
            list_extaction,
            columns=["Référence fournisseur", "Référence fiche", "Station"],
        )
        return df_extraction_pret

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
            # try:
            #     list_extaction.append(
            #         [
            #             row["NUMERO_REF_FOURN"],
            #             row["REFFIC"],
            #             row["ARMOIRE"],
            #         ],
            #     )
            # except Exception as e:
            #     pass
        # print(list_extaction)
        df_extraction = pd.DataFrame(
            list_extaction,
            columns=["Référence fournisseur", "Référence fiche", "Armoire"],
        )
        print("df_extraction dans la fonction", df_extraction)
        return df_extraction

    def extraction_serber_reprise(self):
        df = pd.read_csv(
            "input_datas/Extraction Serber juste AA et non serber.csv",
            encoding="cp1252",
            sep=";",
        )
        list_extaction = []

        for index, row in df.iterrows():
            try:
                list_extaction.append(
                    [
                        row["NUMERO_REF_FOURN"],
                        row["REFFIC"],
                        row["ARMOIRE"],
                    ],
                )
            except Exception as e:
                pass
            # try:
            #     list_extaction.append(
            #         [
            #             row["NUMERO_REF_FOURN"],
            #             row["REFFIC"],
            #             row["ARMOIRE"],
            #         ],
            #     )
            # except Exception as e:
            #     pass
        # print(list_extaction)
        df_extraction = pd.DataFrame(
            list_extaction,
            columns=["Référence fournisseur", "Référence fiche", "Armoire"],
        )
        print("df_extraction dans la fonction", df_extraction)
        return df_extraction

    def extraction_tout_tcl_doc(self):
        df = pd.read_csv(
            "input_datas/20221010_ExtratTCLDoc complete modifié.csv",
            encoding="cp1252",
            sep=";",
        )
        list_extaction = []

        for index, row in df.iterrows():
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
        print(df_extraction)
        return df_extraction

    def main(
        self,
        DIRNAME,
        name_file_arbo,
        name_file_success,
        name_file_failed,
        name_file_failed_rattrapage,
        input_user,
        list_a_traiter,
    ):
        ### A DECOMMENTER DIRNAME,name_file_arbo,name_file_success,name_file_failed,input_user
        start = timer()
        print("********************************")
        if input_user == None:
            print(
                f"""1 - Choisir d'extraire une ligne complete \n2 - Choisir une station\n3 - Comparer le dossier à l'extraction complète de DARFEUILLE \n4 - Ne rien extraire\n8 - Réaliser une extraction de SERBER\n9 - Réaliser une extraction des prêts """
            )

            input_user = int(input("Que voulez vous extraire ? (1 ou 2 ou 8 ou 9) :  "))

        # list_a_traiter = None
        df_extraction = None
        # ---------- MODIFIER ICI ----------
        # DIRNAME = f"""F:\Tcl\{str(900)} - Lignes Fortes - C1 C2 C3 C13"""
        if (
            name_file_arbo == None
            and name_file_success == None
            and name_file_failed == None
            and name_file_failed_rattrapage == None
            and DIRNAME == None
        ):
            name_file_arbo = "output_datas/arbo tram commun.csv"
            name_file_success = "output_datas/listes des succes tram commun.csv"
            name_file_failed = "output_datas/listes des echecs tram commun.csv"
            name_file_failed_rattrapage = (
                "output_datas/listes des echecs tram commun rattrapage.csv"
            )
            DIRNAME = f"""F:\Tcl\{str(500)} - Tramway - communs"""

        if input_user != 8:
            if input_user == 9:
                # name_file_arbo = "output_datas/arborescence_tcl_pret_total.csv"
                # name_file_success = "output_datas/listes des succes Prêt Total.csv"
                # name_file_failed = "output_datas/listes des echecs Prêt Total.csv"
                df_extraction_pret = self.extraction_pret_tcl()
                arborescence_tcl_pret.create_arbo(DIRNAME, name_file_arbo)
                arborescence_tcl_pret.compare_list_arbo_csv_bi_pret(
                    name_file_arbo,
                    df_extraction_pret,
                    name_file_success,
                    name_file_failed,
                )
                print("Nombre de références dans l'extraction", df_extraction_pret)
            else:
                if input_user == 3:
                    df_extraction = self.extraction_tout_tcl_doc()
                    # arborescence_tcl.create_arbo(DIRNAME, name_file_arbo)
                    arborescence_tcl_tout_darfeuille.compare_list_arbo_csv_bi(
                        name_file_arbo,
                        df_extraction,
                        name_file_success,
                        name_file_failed,
                    )
                else:
                    if list_a_traiter == None:
                        list_a_traiter = self.create_list_station(input_user)
                        print(list_a_traiter)
                    else:
                        pass
                    df_extraction = self.extraction_tcl_doc_file(list_a_traiter)
                    arborescence_tcl.create_arbo(DIRNAME, name_file_arbo)
                    arborescence_tcl.compare_list_arbo_csv_bi(
                        name_file_arbo,
                        df_extraction,
                        name_file_success,
                        name_file_failed,
                    )
                    print("La listes des arrêt à traiter est ", list_a_traiter)
                    print("Nombre de références dans l'extraction", df_extraction)
                    print("PREMIER SCAN TERMINE")
                    print("PASSAGE A LA REPRISE DES ECHECS SUR LA LIGNE COMPLETE")
                    df_extraction_rattrapage = (
                        self.extraction_tcl_doc_rattrapage_echecs(list_a_traiter)
                    )
                    # time.sleep(5)
                    # Comparaison echecs avec la ligne complete
                    arborescence_tcl_reprise_echecs.compare_list_arbo_csv_bi_rattrapage(
                        name_file_failed,
                        df_extraction_rattrapage,
                        name_file_success,
                        name_file_failed_rattrapage,
                    )
                    print("SECOND SCAN TERMINE")
            print("DIRNAME", DIRNAME)

        else:
            DIRNAME = f"""G:\{str(1)}00000"""
            # DIRNAME = f"""G:"""
            name_file_arbo = "output_datas/arborescence_serber_10000_version.csv"
            # name_file_arbo = "output_datas/listes des echecs serber complet.csv"
            name_file_success = (
                "output_datas/listes des succes serber 10000_version.csv"
            )
            name_file_failed = "output_datas/listes des echecs serber 10000_version.csv"
            name_file_failed_rattrapage = (
                "output_datas/listes des echecs serber 10000_version rattrapage.csv"
            )
            df_extraction = self.extraction_serber()
            arborescence_serber.create_arbo(DIRNAME, name_file_arbo)
            arborescence_serber.compare_list_arbo_csv_bi(
                name_file_arbo,
                df_extraction,
                name_file_success,
                name_file_failed,
                nb_passage=1,
            )
            print("La listes des arrêt à traiter est ", list_a_traiter)
            print("Nombre de références dans l'extraction", df_extraction)
            print("PREMIER SCAN TERMINE")
            print("PASSAGE A LA REPRISE DES ECHECS SUR LE FICHIER FILTRÉ")
            df_extraction_rattrapage = self.extraction_serber_reprise()
            print(df_extraction_rattrapage)
            # arborescence_serber.create_arbo(DIRNAME, name_file_arbo)
            arborescence_serber.compare_list_arbo_csv_bi(
                name_file_failed,
                df_extraction_rattrapage,
                name_file_success,
                name_file_failed_rattrapage,
                nb_passage=2,
            )
            print("SECOND SCAN TERMINE")
            print("DIRNAME", DIRNAME)
        end = timer()
        print(end - start)
        # print("Voulez-vous repriser les echecs avec la ligne complete ")


# Extraction = MainExtraction()
# Extraction.main(
#     DIRNAME=None,
#     name_file_arbo=None,
#     name_file_success=None,
#     name_file_failed=None,
#     name_file_failed_rattrapage=None,
#     input_user=None,
#     list_a_traiter=None,
# )
# Extraction.extraction_tcl_doc_file()
