"""
Script principal dans lequel sont lancées les lignes complètes, SERBER,PRET...
"""
import menu_arborescence

import time
import os
from timeit import default_timer as timer
import pandas as pd
from fichiers_et_constantes import *

Lunch_Menu = menu_arborescence.MainExtraction()


def main_lunch_function(list_choices):
    start = timer()
    list_possibilities = [
        "PRÊT",
        "SERBER",
        "Métro A",
        "Métro B",
        "Métro C",
        "Métro D",
        "METRO communs",
        "MetroABCD interstations",
        "Liaison B/D",
        "METRO ABC,AB,A,B,C,D COMMUNS",
        "T1",
        "T2",
        "T3",
        "T4",
        "T5",
        "T6",
        "TRAM COMMUNS",
        "TRAM T1 T2 T3 T4 T5 T6 COMMUNS",
        "RHONE EXPRESS COMMUNS",
        "FUNI COMMUNS + STATIONS",
        "Lignes Fortes - C1 C2 C3 C13",
        "Surface",
    ]
    if len(list_choices) == 0:
        for choice in list_possibilities:
            flag = False
            while not flag:
                print(f"Voulez vous traiter et extraire le dossier {choice}")
                input_yes_no = input("O / N : ")
                if input_yes_no.upper() == "O":
                    list_choices.append(choice)
                    flag = True
                elif input_yes_no.upper() == "N":
                    print(f"Le dossier {choice} ne sera pas ajouté")
                    flag = True
                else:
                    print("Je ne comprend pas votre réponse, réessayez ")
                    pass
    print(f"Vous avez donc choisi d'extraire {list_choices}")
    flag_re = False
    input_retraiter_tous_echecs = ""
    while not flag_re:
        print(
            f"Voulez vous retraiter tous les echecs en comparant à toute l'extraction de Darfeuille ? (O / N ) "
        )
        input_retraiter_tous_echecs = input("O / N : ")
        input_retraiter_tous_echecs = input_retraiter_tous_echecs.upper()
        if input_retraiter_tous_echecs == "O":
            print("Les erreurs seront retraitées")
            flag_re = True
        elif input_retraiter_tous_echecs == "N":
            print(f"Les erreurs ne seront pas retraitées")
            flag_re = True
        else:
            print("Je ne comprend pas votre réponse, réessayez ")
            pass

    time.sleep(3)
    concatenation_succes_path = "output_datas\concatenation des succes tcl.csv"
    concatenation_echecs_path = "output_datas\concatenation des echecs tcl.csv"
    while len(list_choices) > 0:
        if len(list_choices) == 0:
            break
        if "PRÊT" in list_choices:
            # -------- PRÊT --------
            name_file_success, name_file_failed_rattrapage = Lunch_Menu.main(
                DIRNAME=f"""F:\Tcl\Prêt Plans""",
                # DIRNAME=[
                #     f"""F:\Tcl\Prêt Plans\Prêt 2017\Bordereau 17-141""",
                # f"""F:\Tcl\Prêt Plans\Prêt 2016""",
                #         f"""F:\Tcl\Prêt Plans\Prêt 2017""",
                #         f"""F:\Tcl\Prêt Plans\Prêt 2018""",
                #         f"""F:\Tcl\Prêt Plans\Prêt 2019""",
                # ],
                name_file_arbo="output_datas/arborescence_tcl_pret_complet.csv",
                name_file_success="output_datas/listes des succes Prêt complet.csv",
                name_file_failed="output_datas/listes des echecs Prêt complet.csv",
                input_user=9,
                list_a_traiter=None,
                name_file_failed_rattrapage=None,
            )
            name_file_failed_rattrapage = (
                "output_datas/listes des echecs Prêt complet.csv"
            )
            list_choices.remove("PRÊT")
        elif "SERBER" in list_choices:
            # -------- SERBER --------
            name_file_success, name_file_failed_rattrapage = Lunch_Menu.main(
                # DIRNAME=f"""G:\{str(5)}00000""",
                DIRNAME=f"""G:""",
                name_file_arbo="output_datas/arborescence_tcl_serber_complet.csv",
                name_file_success="output_datas/listes des succes Serber Complet.csv",
                name_file_failed="output_datas/listes des echecs Serber Complet.csv",
                input_user=8,
                list_a_traiter=None,
                name_file_failed_rattrapage=None,
            )
            name_file_failed_rattrapage = (
                "output_datas/listes des echecs Serber Complet.csv"
            )
            list_choices.remove("SERBER")

        elif "Métro A" in list_choices:
            # # -------- Métro A --------

            name_file_success, name_file_failed_rattrapage = Lunch_Menu.main(
                DIRNAME=f"""F:\Tcl\{str(105)} à {str(122)} - Métro A - stations""",
                name_file_arbo="output_datas/arborescence_metro_ligne_a.csv",
                name_file_success="output_datas/listes des succes Métro A complet.csv",
                name_file_failed="output_datas/listes des echecs Métro A première passe.csv",
                name_file_failed_rattrapage="output_datas/listes des echecs Métro A après seconde passe.csv",
                input_user=1,
                list_a_traiter=[
                    "AMPERE",
                    "ARCHIVES USVB",
                    "ARCHIVES UTMA",
                    "BELLECOUR A & D",
                    "BONNEVAY",
                    "CHARPENNES A & B",
                    "COMMUNS  A",
                    "COMMUNS  A & B",
                    "COMMUNS  A , B & C",
                    "COMMUNS METRO",
                    "CORDELIERS",
                    "CUSSET",
                    "FLACHET",
                    "FOCH",
                    "GRATTE CIEL",
                    "HOTEL DE VILLE A & C",
                    "HOTEL DE VILLE LIGNE A",
                    "INTERSTATIONS  A",
                    "LA SOIE",
                    "MASSENA",
                    "PERRACHE",
                    "POUDRETTE",
                    "REPUBLIQUE",
                    "UTMA POUDRETTE",
                ],
            )
            list_choices.remove("Métro A")

        elif "Métro B" in list_choices:
            # -------- Métro B --------

            name_file_success, name_file_failed_rattrapage = Lunch_Menu.main(
                DIRNAME=f"""F:\Tcl\{str(130)} à {str(137)} - Métro B - stations""",
                name_file_arbo="output_datas/arborescence_metro_ligne_b.csv",
                name_file_success="output_datas/listes des succes Métro B complet.csv",
                name_file_failed="output_datas/listes des echecs Métro B première passe.csv",
                name_file_failed_rattrapage="output_datas/listes des echecs Métro B après seconde passe.csv",
                input_user=1,
                list_a_traiter=[
                    "ARCHIVES USVB",
                    "ARCHIVES UTMA",
                    "BROTTEAUX",
                    "CHARPENNES A & B",
                    "COMMUNS  A & B",
                    "COMMUNS  A , B & C",
                    "COMMUNS  B",
                    "COMMUNS METRO",
                    "DEBOURG",
                    "GARE OULLINS",
                    "GERLAND",
                    "GUICHARD",
                    "INTERSTATIONS  B",
                    "JEAN MACE",
                    "LIAISON B/D",
                    "PART DIEU",
                    "PLACE JEAN JAURES",
                    "PLAINE DES JEUX",
                    "SAXE GAMBETTA  B & D",
                    "SAXE GAMBETTA B",
                ],
            )
            list_choices.remove("Métro B")
        elif "Métro C" in list_choices:
            # -------- Métro C --------
            name_file_success, name_file_failed_rattrapage = Lunch_Menu.main(
                DIRNAME=f"""F:\Tcl\{str(210)} à {str(213)} - Métro C - stations""",
                name_file_arbo="output_datas/arborescence_metro_ligne_c_2.csv",
                name_file_success="output_datas/listes des succes Métro C complet.csv",
                name_file_failed="output_datas/listes des echecs Métro C première passe.csv",
                name_file_failed_rattrapage="output_datas/listes des echecs Métro C après seconde passe.csv",
                input_user=1,
                list_a_traiter=[
                    "ARCHIVES USVB",
                    "ARCHIVES UTMA",
                    "COMMUNS  A , B & C",
                    "COMMUNS  C",
                    "COMMUNS METRO",
                    "CROIX PAQUET",
                    "CROIX ROUSSE",
                    "CUIRE",
                    "HENON ATELIERS",
                    "HENON STATION",
                    "HOTEL DE VILLE A & C",
                    "HOTEL DE VILLE C",
                    "INTERSTATIONS  C",
                ],
            )
            list_choices.remove("Métro C")
        elif "Métro D" in list_choices:

            # -------- Métro D --------

            name_file_success, name_file_failed_rattrapage = Lunch_Menu.main(
                DIRNAME=f"""F:\Tcl\{str(305)} à {str(322)} - Métro D - stations""",
                name_file_arbo="output_datas/arborescence_metro_ligne_d.csv",
                name_file_success="output_datas/listes des succes Métro D complet.csv",
                name_file_failed="output_datas/listes des echecs Métro D première passe.csv",
                name_file_failed_rattrapage="output_datas/listes des echecs Métro D après seconde passe.csv",
                input_user=1,
                list_a_traiter=[
                    "ARCHIVES USEQ",
                    "BELLECOUR A & D",
                    "COMMUNS  D",
                    "COMMUNS METRO",
                    "GARE DE VAISE",
                    "GARE DE VENISSIEUX",
                    "GARIBALDI",
                    "GORGE DE LOUP",
                    "GRANGE BLANCHE",
                    "GUILLOTIERE",
                    "INTERSTATIONS  D",
                    "LAENNEC",
                    "LIAISON B/D",
                    "MERMOZ PINEL",
                    "MONPLAISIR LUMIERE",
                    "PARILLY",
                    "SANS SOUCI",
                    "SAXE GAMBETTA  B & D",
                    "THIOLEY",
                    "VALMY",
                    "VIEUX LYON",
                ],
            )
            list_choices.remove("Métro D")
        elif "METRO communs" in list_choices:
            # -------- Métro Communs --------
            name_file_success, name_file_failed_rattrapage = Lunch_Menu.main(
                DIRNAME=f"""F:\Tcl\{str(0)}01 - Métro - communs""",
                name_file_arbo="output_datas/arborescence_metro_communs.csv",
                name_file_success="output_datas/listes des succes Métro Communs complet.csv",
                name_file_failed="output_datas/listes des echecs Métro Communs première passe.csv",
                name_file_failed_rattrapage="output_datas/listes des echecs Métro Communs après seconde passe.csv",
                input_user=1,
                list_a_traiter=[
                    "COMMUNS METRO",
                ],
            )
            list_choices.remove("METRO communs")
        elif "METRO ABC,AB,A,B,C,D COMMUNS" in list_choices:
            # -------- METRO ABC,AB,A,B,C,D COMMUNS --------
            name_file_success, name_file_failed_rattrapage = Lunch_Menu.main(
                DIRNAME=[
                    f"""F:\Tcl\{str(0)}02 - Métro ABC - communs""",
                    f"""F:\Tcl\{str(0)}03 - Métro AB - communs""",
                    f"""F:\Tcl\{str(100)} - Métro A - communs""",
                    f"""F:\Tcl\{str(102)} - Métro B - communs""",
                    f"""F:\Tcl\{str(200)} - Métro C - communs""",
                    f"""F:\Tcl\{str(300)} - Métro D - communs""",
                ],
                name_file_arbo="output_datas/arborescence_metro_abc_ab_a_b_c_d_communs.csv",
                name_file_success="output_datas/listes des succes METRO ABC,AB,A,B,C,D COMMUNS complet.csv",
                name_file_failed="output_datas/listes des echecs METRO ABC,AB,A,B,C,D COMMUNS première passe.csv",
                name_file_failed_rattrapage="output_datas/listes des echecs METRO ABC,AB,A,B,C,D COMMUNS après seconde passe.csv",
                input_user=1,
                list_a_traiter=[
                    "COMMUNS  A , B & C",
                    "COMMUNS  A & B",
                    "COMMUNS  A",
                    "COMMUNS  B",
                    "COMMUNS  C",
                    "COMMUNS  D",
                ],
            )
            list_choices.remove("METRO ABC,AB,A,B,C,D COMMUNS")
        elif "MetroABCD interstations" in list_choices:
            # -------- MetroABCD interstations --------
            name_file_success, name_file_failed_rattrapage = Lunch_Menu.main(
                DIRNAME=[
                    f"""F:\Tcl\{str(101)} - Métro A - interstations""",
                    f"""F:\Tcl\{str(103)} - Métro B - interstations""",
                    f"""F:\Tcl\{str(201)} - Métro C - interstations""",
                    f"""F:\Tcl\{str(301)} - Métro D - interstations""",
                ],
                name_file_arbo="output_datas/arborescence_metro_abc_ab_a_b_c_d_interstations.csv",
                name_file_success="output_datas/listes des succes MetroABCD interstations complet.csv",
                name_file_failed="output_datas/listes des echecs MetroABCD interstations première passe.csv",
                name_file_failed_rattrapage="output_datas/listes des echecs MetroABCD interstations après seconde passe.csv",
                input_user=1,
                list_a_traiter=[
                    "INTERSTATIONS  A",
                    "INTERSTATIONS  B",
                    "INTERSTATIONS  C",
                    "INTERSTATIONS  D",
                ],
            )
            list_choices.remove("MetroABCD interstations")
        elif "Liaison B/D" in list_choices:
            # -------- Liaison B/D --------
            name_file_success, name_file_failed_rattrapage = Lunch_Menu.main(
                DIRNAME=[
                    f"""F:\Tcl\{str(303)} - Liaison BD""",
                ],
                name_file_arbo="output_datas/arborescence_liaison_b_d.csv",
                name_file_success="output_datas/listes des succes Liaison b_d complet.csv",
                name_file_failed="output_datas/listes des echecs Liaison b_d première passe.csv",
                name_file_failed_rattrapage="output_datas/listes des echecs Liaison b_d après seconde passe.csv",
                input_user=1,
                list_a_traiter=[
                    "LIAISON B/D",
                ],
            )
            list_choices.remove("Liaison B/D")
        elif "T1" in list_choices:
            # -------- T1 --------
            name_file_success, name_file_failed_rattrapage = Lunch_Menu.main(
                DIRNAME=f"""F:\Tcl\{str(501)} - Tramway T1 - stations""",
                name_file_arbo="output_datas/arborescence_tram_ligne_t1.csv",
                name_file_success="output_datas/listes des succes Tram Ligne T1 complet.csv",
                name_file_failed="output_datas/listes des echecs Tram Ligne T1 première passe.csv",
                name_file_failed_rattrapage="output_datas/listes des echecs Tram Ligne T1 après seconde passe.csv",
                input_user=1,
                list_a_traiter=[
                    "C.HERNU A IUT FEYSSINE",
                    "CHARPENNES - CHARLES HERNU",
                    "COLLEGE BELLECOMBE",
                    "COMMUN TRAMWAY EXT. MONTROCHET",
                    "COMMUNS TRAMWAY",
                    "COMMUNS TRAMWAY T1",
                    "CONDORCET",
                    "CROIX LUIZET",
                    "DEBOURG",
                    "DEBOURG S/STATION",
                    "DEBRANCHEMENT L1/L2",
                    "ENS LYON",
                    "GARIBALDI SERVIENT",
                    "GUILLOTIERE",
                    "HALLE TONY GARNIER",
                    "INSA EINSTEIN",
                    "IUT - FEYSSINE",
                    "LA DOUA GASTON BERGER",
                    "LE TONKIN",
                    "LIBERTE",
                    "MONCEY MAIRIE DU 3EME",
                    "MONTROCHET",
                    "MUSEE DES CONFLUENCES",
                    "PART DIEU",
                    "PART DIEU",
                    "PART DIEU - SERVIENT",
                    "PART DIEU - VIVIER MERLE",
                    "PERRACHE à CHARPENNES C. HERNU",
                    "PLANCHES T1 ",
                    "QUAI CLAUDE BERNARD",
                    "QUAIS DE STATION T1/T2",
                    "RETOUR. CHARPEN. - CRX LUIZET",
                    "RUE DE L UNIVERSITE",
                    "SAINT ANDRE",
                    "SAINTE BLANDINE",
                    "SAXE - PREFECTURE",
                    "SST - LTS - TRAMWAY T1/T2",
                    "SUCHET",
                    "TERMINUS FEYSSINE",
                    "THIERS LAFAYETTE",
                    "UNIVERSITE LYON 1",
                    "VOUTE DE PERRACHE",
                ],
            )
            list_choices.remove("T1")
        elif "T2" in list_choices:
            # -------- T2 --------
            name_file_success, name_file_failed_rattrapage = Lunch_Menu.main(
                DIRNAME=f"""F:\Tcl\{str(501)} - Tramway T2 - stations""",
                name_file_arbo="output_datas/arborescence_tram_ligne_t2_test.csv",
                name_file_success="output_datas/listes des succes Tram Ligne T2 Test complet.csv",
                name_file_failed="output_datas/listes des echecs Tram Ligne T2 Test première passe.csv",
                name_file_failed_rattrapage="output_datas/listes des echecs Tram Ligne T2 Test après seconde passe.csv",
                input_user=1,
                list_a_traiter=[
                    "ALFRED DE VIGNY",
                    "AMBROISE PARE",
                    "BACHUT - MAIRIE DU 8EME",
                    "BERTHELOT A AMBROISE PARE",
                    "BOUTASSE - C.ROUSSET",
                    "CENTRE BERTHELOT",
                    "COMMUN TRAMWAY EXT. ST PRIEST",
                    "COMMUNS TRAMWAY",
                    "COMMUNS TRAMWAY T2",
                    "CORDIERE",
                    "DEBRANCHEMENT L1/L2",
                    "ESPLANADE DES ARTS",
                    "ESSARTS - IRIS",
                    "EUROPE UNIVERSITE",
                    "GARIBALDI BERTHELOT",
                    "GRANGE BLANCHE",
                    "HAUTS DE FEUILLY",
                    "HOTEL DE VILLE BRON",
                    "JEAN MACE",
                    "JEAN XXIII - MARYSE BASTIE",
                    "JULES FERRY",
                    "LA COTIERE",
                    "LES ALIZES",
                    "MUR DU VINATIER",
                    "PARC RELAIS BEL AIR",
                    "PARC TECHNOLOGIQUE",
                    "PARILLY UNIVERSITE",
                    "PLACE JET D EAU",
                    "PLANCHES T2",
                    "PONT DES TCHECOSLOVAQUES",
                    "PORTE DES ALPES",
                    "QUAIS DE STATION T1/T2",
                    "REBUFFER",
                    "ROUTE DE VIENNE",
                    "SALVADOR ALLENDE",
                    "SST - LTS - T2 EXT. ST PRIEST",
                    "SST - LTS - TRAMWAY T1/T2",
                    "ST PRIEST  C D M",
                    "ST PRIEST BEL AIR",
                    "ST PRIEST HOTEL DE VILLE",
                    "VILLON",
                    "VINATIER",
                ],
            )
            list_choices.remove("T2")

        elif "T3" in list_choices:
            # -------- T3 --------
            name_file_success, name_file_failed_rattrapage = Lunch_Menu.main(
                DIRNAME=f"""F:\Tcl\{str(501)} - Tramway T3 - stations""",
                name_file_arbo="output_datas/arborescence_tram_ligne_t3.csv",
                name_file_success="output_datas/listes des succes Tram Ligne T3 complet.csv",
                name_file_failed="output_datas/listes des echecs Tram Ligne T3 première passe.csv",
                name_file_failed_rattrapage="output_datas/listes des echecs Tram Ligne T3 après seconde passe.csv",
                input_user=1,
                list_a_traiter=[
                    "BUE Boulevard Urbain Est",
                    "CARREAU SOUS STATION",
                    "COMMUNS TRAMWAY",
                    "COMMUNS TRAMWAY T3",
                    "DAUPHINE",
                    "GARE DE DECINES",
                    "GARE DE MEYZIEU",
                    "GARE DE VILLEURBANNE",
                    "GARE DE VILLEURBANNE S/STATION",
                    "GODARD SOUS STATION",
                    "GRAND LARGE",
                    "GRAND STADE",
                    "MEYZIEU CDM",
                    "MEYZIEU LES PANETTES",
                    "MEYZIEU Z.I.",
                    "PART DIEU",
                    "PART DIEU LEA",
                    "PART DIEU SUD",
                    "PLANCHES T3",
                    "RECONNAISSANCE",
                    "SALENGRO SOUS STATION",
                    "VAULX EN VELIN LA SOIE",
                    "VILLEURBANNE BEL AIR",
                    "VILLEURBANNE LA SOIE",
                ],
            )
            list_choices.remove("T3")

        elif "T4" in list_choices:
            # -------- T4 --------
            name_file_success, name_file_failed_rattrapage = Lunch_Menu.main(
                DIRNAME=f"""F:\Tcl\{str(501)} - Tramway T4 - stations""",
                name_file_arbo="output_datas/arborescence_tram_ligne_t4.csv",
                name_file_success="output_datas/listes des succes Tram Ligne T4 complet.csv",
                name_file_failed="output_datas/listes des echecs Tram Ligne T4 première passe.csv",
                name_file_failed_rattrapage="output_datas/listes des echecs Tram Ligne T4 après seconde passe.csv",
                input_user=1,
                list_a_traiter=[
                    "CAGNE - HERRIOT",
                    "CLINIQUE FEYZIN",
                    "COMMUNS TRAMWAY",
                    "COMMUNS TRAMWAY T4",
                    "CROIZAT - PAUL BERT",
                    "DARNAISE",
                    "DIVISION LECLERC/SST CERISIER",
                    "ETATS-UNIS TONY GARNIER",
                    "ETATS-UNIS VIVIANI",
                    "FELIX FAURE DAUPHINE",
                    "GARE DE VENISSIEUX",
                    "JET D EAU - MENDES FRANCE",
                    "JOLIOT CURIE - MARCEL SEMBAT",
                    "LA BORELLE",
                    "LENINE - CORSIERE",
                    "LYCEE COLBERT",
                    "LYCEE JACQUES BREL",
                    "LYCEE LUMIERE",
                    "MANUFACTURE DES TABACS",
                    "MANUFACTURE SOUS STATION",
                    "MARCEL HOUEL - HOTEL DE VILLE",
                    "MAURICE THOREZ",
                    "PART DIEU",
                    "PART DIEU",
                    "PART DIEU T4",
                    "PLANCHES T4",
                    "PROFESSEUR BEAUVISAGE",
                    "SST FELIX FAURE DAUPHINE",
                    "THIERS LAFAYETTE",
                    "VENISSY",
                    "ZAC BERTHELOT",
                ],
            )
            list_choices.remove("T4")

        elif "T5" in list_choices:
            # -------- T5 --------
            name_file_success, name_file_failed_rattrapage = Lunch_Menu.main(
                DIRNAME=f"""F:\Tcl\{str(501)} - Tramway T5 - stations""",
                name_file_arbo="output_datas/arborescence_tram_ligne_t5.csv",
                name_file_success="output_datas/listes des succes Tram Ligne T5 complet.csv",
                name_file_failed="output_datas/listes des echecs Tram Ligne T5 première passe.csv",
                name_file_failed_rattrapage="output_datas/listes des echecs Tram Ligne T5 après seconde passe.csv",
                input_user=1,
                list_a_traiter=[
                    "COMMUNS TRAMWAY",
                    "COMMUNS TRAMWAY T5",
                    "CURIAL",
                    "EUREXPO",
                    "GRANGE BLANCHE",
                    "LYCEE JEAN PAUL SARTRE",
                    "PARC DU CHENE",
                    "PLANCHES T5",
                ],
            )
            list_choices.remove("T5")

        elif "T6" in list_choices:
            # -------- T6 --------
            name_file_success, name_file_failed_rattrapage = Lunch_Menu.main(
                DIRNAME=f"""F:\Tcl\{str(501)} - Tramway T6 - stations""",
                name_file_arbo="output_datas/arborescence_tram_ligne_t6.csv",
                name_file_success="output_datas/listes des succes Tram Ligne T6 complet.csv",
                name_file_failed="output_datas/listes des echecs Tram Ligne T6 première passe.csv",
                name_file_failed_rattrapage="output_datas/listes des echecs Tram Ligne T6 après seconde passe.csv",
                input_user=1,
                list_a_traiter=[
                    "BEAUVISAGE CISL",
                    "BEAUVISAGE PRESSENSE",
                    "CHALLEMEL-LACOUR ARTILLERIE",
                    "COMMUNS TRAMWAY",
                    "COMMUNS TRAMWAY T6",
                    "DESGENETTES",
                    "ESSARTS - LAENNEC",
                    "GRANGE ROUGE - SANTY",
                    "HOPITAUX EST - PINEL",
                    "MERMOZ - MOSELLE",
                    "MERMOZ CALIFORNIE",
                    "MERMOZ PINEL",
                    "MERMOZ PINEL + QUAI DE SECOURS",
                    "MOULIN A VENT",
                    "PETITE GUILLE",
                    "PLANCHES T6",
                    "VINATIER",
                    "VINATIER T6",
                ],
            )
            list_choices.remove("T6")

        elif "TRAM COMMUNS" in list_choices:
            # -------- TRAM COMMUNS --------
            name_file_success, name_file_failed_rattrapage = Lunch_Menu.main(
                DIRNAME=f"""F:\Tcl\{str(500)} - Tramway - communs""",
                name_file_arbo="output_datas/arborescence_tram_communs.csv",
                name_file_success="output_datas/listes des succes Tram communs complet.csv",
                name_file_failed="output_datas/listes des echecs Tram communs première passe.csv",
                name_file_failed_rattrapage="output_datas/listes des echecs Tram communs après seconde passe.csv",
                input_user=1,
                list_a_traiter=[
                    "COMMUNS TRAMWAY",
                    "COMMUNS TRAMWAY T1",
                    "COMMUNS TRAMWAY T2",
                    "COMMUNS TRAMWAY T3",
                    "COMMUNS TRAMWAY T4",
                    "COMMUNS TRAMWAY T5",
                    "COMMUNS TRAMWAY T6",
                ],
            )
            list_choices.remove("TRAM COMMUNS")

        elif "TRAM T1 T2 T3 T4 T5 T6 COMMUNS" in list_choices:
            # -------- TRAM T1 T2 T3 T4 T5 T6 COMMUNS --------
            name_file_success, name_file_failed_rattrapage = Lunch_Menu.main(
                DIRNAME=[
                    f"""F:\Tcl\{str(500)} - Tramway T1 - communs""",
                    f"""F:\Tcl\{str(500)} - Tramway T2 - communs""",
                    f"""F:\Tcl\{str(500)} - Tramway T3 - communs""",
                    f"""F:\Tcl\{str(500)} - Tramway T4 - communs""",
                    f"""F:\Tcl\{str(500)} - Tramway T5 - communs""",
                    f"""F:\Tcl\{str(500)} - Tramway T6 - communs""",
                ],
                name_file_arbo="output_datas/arborescence_tram_communs.csv",
                name_file_success="output_datas/listes des succes Tram communs complet.csv",
                name_file_failed="output_datas/listes des echecs Tram communs première passe.csv",
                name_file_failed_rattrapage="output_datas/listes des echecs Tram communs après seconde passe.csv",
                input_user=1,
                list_a_traiter=[
                    "COMMUNS TRAMWAY",
                    "COMMUNS TRAMWAY T1",
                    "COMMUNS TRAMWAY T2",
                    "COMMUNS TRAMWAY T3",
                    "COMMUNS TRAMWAY T4",
                    "COMMUNS TRAMWAY T5",
                    "COMMUNS TRAMWAY T6",
                ],
            )
            list_choices.remove("TRAM T1 T2 T3 T4 T5 T6 COMMUNS")

        elif "RHONE EXPRESS COMMUNS" in list_choices:
            # -------- RHONE EXPRESS COMMUNS --------
            name_file_success, name_file_failed_rattrapage = Lunch_Menu.main(
                DIRNAME=f"""F:\Tcl\{str(500)} - Tramway Rhone Express - communs""",
                name_file_arbo="output_datas/arborescence_rhone_express_communs.csv",
                name_file_success="output_datas/listes des succes Rhone express communs complet.csv",
                name_file_failed="output_datas/listes des echecs Rhone express communs première passe.csv",
                name_file_failed_rattrapage="output_datas/listes des echecs Rhone express communs après seconde passe.csv",
                input_user=1,
                list_a_traiter=["RHONEXPRESS"],
            )
            list_choices.remove("RHONE EXPRESS COMMUNS")
        elif "FUNI COMMUNS + STATIONS" in list_choices:
            # -------- FUNI COMMUNS + STATIONS --------
            name_file_success, name_file_failed_rattrapage = Lunch_Menu.main(
                DIRNAME=[
                    f"""F:\Tcl\{str(302)} - Funiculaires - communs""",
                    f"""F:\Tcl\{str(330)} à {str(332)} - Funiculaires - stations""",
                ],
                name_file_arbo="output_datas/arborescence_funi_communs_stations.csv",
                name_file_success="output_datas/listes des succes Funi Communs et Stations complet.csv",
                name_file_failed="output_datas/listes des echecs Funi Communs et Stations première passe.csv",
                name_file_failed_rattrapage="output_datas/listes des echecs Funi Communs et Stations après seconde passe.csv",
                input_user=1,
                list_a_traiter=[
                    "COMMUNS FUN",
                    "COMMUNS METRO",
                    "FOURVIERE",
                    "MINIMES",
                    "SAINT JUST",
                    "VIEUX LYON",
                ],
            )
            list_choices.remove("FUNI COMMUNS + STATIONS")
        elif "Lignes Fortes - C1 C2 C3 C13" in list_choices:
            # -------- Lignes Fortes - C1 C2 C3 C13 --------
            name_file_success, name_file_failed_rattrapage = Lunch_Menu.main(
                DIRNAME=f"""F:\Tcl\{str(900)} - Lignes Fortes - C1 C2 C3 C13""",
                name_file_arbo="output_datas/arborescence_dossier_lignes_fortes.csv",
                name_file_success="output_datas/listes des succes Lignes Fortes C1 C2 C3 C13 complet.csv",
                name_file_failed="output_datas/listes des echecs Lignes Fortes C1 C2 C3 C13 première passe.csv",
                name_file_failed_rattrapage="output_datas/listes des echecs Lignes Fortes C1 C2 C3 C13 après seconde passe.csv",
                input_user=1,
                list_a_traiter=[
                    "LIGNE FORTE C13",
                    "LIGNES FORTES C1/C2",
                    "LIGNE FORTE C3",
                ],
            )
            list_choices.remove("Lignes Fortes - C1 C2 C3 C13")
        elif "Surface" in list_choices:
            # -------- Surface --------
            name_file_success, name_file_failed_rattrapage = Lunch_Menu.main(
                DIRNAME=[
                    f"""F:\Tcl\{str(750)} - Agences""",
                    f"""F:\Tcl\{str(800)} à {str(843)} - Surface""",
                    f"""F:\Tcl\{str(808)} à {str(819)} - Unités de Transport""",
                    f"""F:\Tcl\{str(826)} - Duchère""",
                    f"""F:\Tcl\{str(830)} - {str(832)} à {str(857)} - Sous Stations""",
                ],
                # DIRNAME=f"""F:\Tcl\{str(800)} à {str(843)} - Surface""",
                # DIRNAME=f"""F:\Tcl\{str(800)} à {str(843)} - Surface\{str(820)} - Siège Social B12\{str(0)}0 Bâtiment\B12 001""",
                # DIRNAME=f"""F:\Tcl\{str(800)} à {str(843)} - Surface\{str(820)} - Siège Social B12""",
                name_file_arbo="output_datas/arborescence_dossier_surface.csv",
                name_file_success="output_datas/listes des succes Dossier Surface complet.csv",
                name_file_failed="output_datas/listes des echecs Dossier Surface première passe.csv",
                name_file_failed_rattrapage="output_datas/listes des echecs Dossier Surface après seconde passe.csv",
                input_user=1,
                list_a_traiter=[
                    "ALSACE UTN 1 ET UMS",
                    "ALSACE UTN 2",
                    "ARCHIVES S/STATIONS",
                    "BELLECOUR AGENCE",
                    "CENTRE S/STATION",
                    "COMMUNS BUS",
                    "COMMUN TCL",
                    "COMMUNS RESEAU",
                    "COMMUNS S/STATION",
                    "COMMUNS SURFACE",
                    "CROIX ROUSSE S/STATION",
                    "DAUPHINE S/STATION",
                    "DIR SERVICES TECHNIQUES",
                    "DIVERS SURFACE",
                    "DUCHERE PARC RELAIS",
                    "DUCHERE S/STATION",
                    "DUCHERE SITE PROPRE",
                    "FOCH",
                    "GRANDCLEMENT S/STATION",
                    "PART DIEU",
                    "PART DIEU  AGENCE",
                    "SIEGE SOCIAL",
                    "SST ACHILLE LIGNON",
                    "SST BAUMER GRAPPINIERE",
                    "SST CALUIRE",
                    "SST DREVET",
                    "SST FOCH",
                    "SST MICHELET",
                    "SST MOBILE",
                    "SST TERME",
                    "SST THOREZ",
                    "SST TONKIN",
                    "SST VAISE",
                    "SST VENDOME",
                    "SURFACE",
                    "SURFACE L.A.",
                    "USEL ARCHIVES",
                    "UT AUDIBERT",
                    "UT CALUIRE",
                    "UT GIVORS",
                    "UT LA SOIE",
                    "UT LES PINS",
                    "UT OULLINS",
                    "UT PARMENTIER",
                    "UT PERRACHE",
                    "UT PERRACHE CONFLUENCE",
                    "UT VAISE",
                ],
            )
            list_choices.remove("Surface")
        print(
            "******************************** ON A FINI UNE LIGNE ********************************"
        )
        time.sleep(1)
        df_succes_concatenation = pd.read_csv(
            name_file_success,
            header=None,
            sep=";",
            encoding="utf-8-sig",
        )
        df_name_file_failed_rattrapage_concatenation = pd.read_csv(
            name_file_failed_rattrapage,
            header=None,
            sep=";",
            encoding="utf-8-sig",
        )
        if os.path.exists("output_datas\concatenation des succes tcl.csv"):
            mode = "a"
            df_succes_concatenation = df_succes_concatenation.iloc[1:, :]
            df_name_file_failed_rattrapage_concatenation = (
                df_name_file_failed_rattrapage_concatenation.iloc[1:, :]
            )
        else:
            mode = "w"
        print("df_succes_concatenation", df_succes_concatenation)
        print(
            "df_name_file_failed_rattrapage_concatenation",
            df_name_file_failed_rattrapage_concatenation,
        )
        print("*")

        df_succes_concatenation.to_csv(
            concatenation_succes_path,
            mode=mode,
            index=None,
            header=None,
            sep=";",
            encoding="utf-8-sig",
        )
        df_name_file_failed_rattrapage_concatenation.to_csv(
            concatenation_echecs_path,
            mode=mode,
            index=None,
            header=None,
            sep=";",
            encoding="utf-8-sig",
            # encoding="cp1252",
        )
    print("input_retraiter_tous_echecs", input_retraiter_tous_echecs)
    if input_retraiter_tous_echecs == "O":
        name_file_success, name_file_failed_rattrapage = Lunch_Menu.main(
            DIRNAME=None,
            name_file_arbo=concatenation_echecs_path,
            name_file_success=concatenation_succes_path,
            name_file_failed="output_datas\erreurs restantes apres comparaison complete darfeuille.csv",
            name_file_failed_rattrapage=None,
            input_user=3,
            list_a_traiter=None,
        )
    end = timer()
    print(end - start)


main_lunch_function(list_choices=[])
# main_lunch_function(list_choices=["Liaison B/D"])
# main_lunch_function(list_choices=["Surface"])
# main_lunch_function(list_choices=["PRÊT"])
