"""
Script principal dans lequel sont lancées les lignes complètes, SERBER,PRET...
"""
import menu_arborescence
import time
from timeit import default_timer as timer

Lunch_Menu = menu_arborescence.MainExtraction()


def main_lunch_function():
    start = timer()
    list_possibilities = [
        "PRÊT",
        "SERBER",
        "Métro A",
        "Métro B",
        "Métro C",
        "Métro D",
        "METRO communs",
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
    list_choices = []
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
    print(f"Vous avez donc choisit d'extraire {list_choices}")
    time.sleep(10)
    try:
        if "PRÊT" in list_choices:
            # -------- PRÊT --------
            Lunch_Menu.main(
                DIRNAME=f"""F:\Tcl\Prêt Plans""",
                name_file_arbo="output_datas/arborescence_tcl_pret_complet.csv",
                name_file_success="output_datas/listes des succes Prêt Complet.csv",
                name_file_failed="output_datas/listes des echecs Prêt Complet.csv",
                input_user=9,
            )
        if "SERBER" in list_choices:
            # -------- SERBER --------
            Lunch_Menu.main(
                DIRNAME=f"""G:""",
                name_file_arbo="output_datas/arborescence_tcl_serber_complet.csv",
                name_file_success="output_datas/listes des succes Serber Complet.csv",
                name_file_failed="output_datas/listes des echecs Serber Complet.csv",
                input_user=8,
            )

        if "Métro A" in list_choices:
            # # -------- Métro A --------

            Lunch_Menu.main(
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

        if "Métro B" in list_choices:
            # -------- Métro B --------

            Lunch_Menu.main(
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
        if "Métro C" in list_choices:
            # -------- Métro C --------
            Lunch_Menu.main(
                DIRNAME=f"""F:\Tcl\{str(210)} à {str(213)} - Métro C - stations""",
                name_file_arbo="output_datas/arborescence_metro_ligne_c.csv",
                name_file_success="output_datas/listes des succes Métro C complet TEST.csv",
                name_file_failed="output_datas/listes des echecs Métro C première passe TEST.csv",
                name_file_failed_rattrapage="output_datas/listes des echecs Métro C après seconde passe TEST.csv",
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
        if "Métro D" in list_choices:

            # -------- Métro D --------

            Lunch_Menu.main(
                DIRNAME=f"""F:\Tcl\{str(210)} à {str(213)} - Métro C - stations""",
                name_file_arbo="output_datas/arborescence_metro_ligne_c.csv",
                name_file_success="output_datas/listes des succes Métro C complet.csv",
                name_file_failed="output_datas/listes des echecs Métro C première passe.csv",
                name_file_failed_rattrapage="output_datas/listes des echecs Métro C après seconde passe.csv",
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
        if "METRO communs" in list_choices:
            # -------- Métro Communs --------
            Lunch_Menu.main(
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

        if "METRO ABC,AB,A,B,C,D COMMUNS" in list_choices:
            # -------- METRO ABC,AB,A,B,C,D COMMUNS --------
            Lunch_Menu.main(
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

        if "T1" in list_choices:
            # -------- T1 --------
            Lunch_Menu.main(
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
        if "T2" in list_choices:
            # -------- T2 --------
            Lunch_Menu.main(
                DIRNAME=f"""F:\Tcl\{str(501)} - Tramway T2 - stations""",
                name_file_arbo="output_datas/arborescence_tram_ligne_t2.csv",
                name_file_success="output_datas/listes des succes Tram Ligne T2 complet.csv",
                name_file_failed="output_datas/listes des echecs Tram Ligne T2 première passe.csv",
                name_file_failed_rattrapage="output_datas/listes des echecs Tram Ligne T2 après seconde passe.csv",
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

        if "T3" in list_choices:
            # -------- T3 --------
            Lunch_Menu.main(
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

        if "T4" in list_choices:
            # -------- T4 --------
            Lunch_Menu.main(
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
        if "T5" in list_choices:
            # -------- T5 --------
            Lunch_Menu.main(
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

        if "T6" in list_choices:
            # -------- T6 --------
            Lunch_Menu.main(
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

        if "TRAM COMMUNS" in list_choices:
            # -------- TRAM COMMUNS --------
            Lunch_Menu.main(
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
        if "TRAM T1 T2 T3 T4 T5 T6 COMMUNS" in list_choices:
            # -------- TRAM T1 T2 T3 T4 T5 T6 COMMUNS --------
            Lunch_Menu.main(
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

        if "RHONE EXPRESS COMMUNS" in list_choices:
            # -------- RHONE EXPRESS COMMUNS --------
            Lunch_Menu.main(
                DIRNAME=f"""F:\Tcl\{str(500)} - Tramway Rhone Express - communs""",
                name_file_arbo="output_datas/arborescence_rhone_express_communs.csv",
                name_file_success="output_datas/listes des succes Rhone express communs complet.csv",
                name_file_failed="output_datas/listes des echecs Rhone express communs première passe.csv",
                name_file_failed_rattrapage="output_datas/listes des echecs Rhone express communs après seconde passe.csv",
                input_user=1,
                list_a_traiter=["RHONEXPRESS"],
            )

        if "FUNI COMMUNS + STATIONS" in list_choices:
            # -------- FUNI COMMUNS + STATIONS --------
            Lunch_Menu.main(
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

        if "Lignes Fortes - C1 C2 C3 C13" in list_choices:
            # -------- Lignes Fortes - C1 C2 C3 C13 --------
            Lunch_Menu.main(
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
        if "Surface" in list_choices:
            # -------- Surface --------
            Lunch_Menu.main(
                DIRNAME=f"""F:\Tcl\{str(800)} à {str(843)} - Surface""",
                name_file_arbo="output_datas/arborescence_dossier_surface.csv",
                name_file_success="output_datas/listes des succes Dossier Surface complet.csv",
                name_file_failed="output_datas/listes des echecs Dossier Surface première passe.csv",
                name_file_failed_rattrapage="output_datas/listes des echecs Dossier Surface après seconde passe.csv",
                input_user=1,
                list_a_traiter=[
                    "ALSACE UTN 1 ET UMS",
                    "ALSACE UTN 2",
                    "ARCHIVES S/STATIONS",
                    "CENTRE S/STATION",
                    "COMMUNS BUS",
                    "COMMUNS S/STATION",
                    "COMMUNS SURFACE",
                    "CROIX ROUSSE S/STATION",
                    "DAUPHINE S/STATION",
                    "DIVERS SURFACE",
                    "DUCHERE PARC RELAIS",
                    "DUCHERE S/STATION",
                    "DUCHERE SITE PROPRE",
                    "GRANDCLEMENT S/STATION",
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
    except Exception as e:
        print(e.args)
    end = timer()
    print(end - start)


main_lunch_function()
