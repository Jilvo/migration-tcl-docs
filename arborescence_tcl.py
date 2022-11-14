"""
Ce Script crée l'arborescence d'un chemin et la retourne sous format CSV
Input : None
Output : output_datas/arborescence_tcl.csv
"""
import os
import sys
import pandas as pd
import re
from timeit import default_timer as timer
import time
from difflib import SequenceMatcher
import jellyfish

start = timer()

with open("input_datas\parse_filter.txt", encoding="utf-8") as f:
    LIST_PARSE_WORD = f.read().splitlines()


def create_arbo(DIRNAME, name_file_arbo):
    """On crée l'arborescence"""
    list_arbo = []
    if type(DIRNAME) == str:
        for path, subdirs, files in os.walk(DIRNAME):
            for name in files:
                try:
                    print(os.path.join(path, name))
                    list_arbo.append(os.path.join(path, name))
                except Exception as e:
                    print(e.args)
    else:
        for dir in DIRNAME:
            for path, subdirs, files in os.walk(dir):
                for name in files:
                    try:
                        print(os.path.join(path, name))
                        list_arbo.append(os.path.join(path, name))
                    except Exception as e:
                        print(e.args)
    df = pd.DataFrame(
        {
            "Chemin du fichier": list_arbo,
        }
    )
    df.to_csv(
        name_file_arbo,
        sep="\t",
        index=False,
        encoding="utf-8-sig",
    )


def split_arbo(
    path,
):
    """On formate le format du chemin"""
    return path.split("\\")


def find_ref_fournisseur(name_file_arbo):
    """
    Création d'une d'un dict des réfs fournisseurs
    keys = chemin d'un fichier
    values = liste des sous dossiers,nom de fichier affiné
    """
    # df = pd.read_csv("output_datas/arborescence_tcl.csv")
    # df = pd.read_csv("output_datas/arborescence_tcl_bellecour.csv")
    # df = pd.read_csv(
    #     "output_datas/arborescence_tcl_bellecour.csv",
    #     error_bad_lines=False,
    #     sep=";",
    #     encoding="utf-8-sig",
    # )
    df = pd.read_csv(
        name_file_arbo,
        sep=";",
        error_bad_lines=False,
        encoding="utf-8-sig",
        # encoding = "cp1252"
    )
    df_stations = pd.read_csv(
        "input_datas/listes_arrets_lignes.csv",
        encoding="cp1252",
        sep=";",
    )
    # df_stations = df_stations["Site"].values.tolist()
    dict_stations = {}
    for site, doss in zip(
        df_stations["Site"].values.tolist(), df_stations["Nom Dossier"].values.tolist()
    ):
        dict_stations[doss] = site
    dict_arbo = {}
    for index, row in df.iterrows():
        list_split_station = []
        list_split = split_arbo(row["Chemin du fichier"])
        list_split_station.append(list_split)
        if "communs" in list_split[2]:
            list_station_for_filter = []
            if "2 - Métro ABC - communs" in list_split[2]:
                list_station_for_filter.append("COMMUNS  A , B & C")
            elif "3 - Métro AB" in list_split[2]:
                list_station_for_filter.append("COMMUNS  A & B")
            elif "0 - Métro A" in list_split[2]:
                list_station_for_filter.append("COMMUNS  A")
            elif "102 - Métro B - communs" in list_split[2]:
                list_station_for_filter.append("COMMUNS  B")
            elif "200 - Métro C - communs" in list_split[2]:
                list_station_for_filter.append("COMMUNS  C")
            elif "300 - Métro D - communs" in list_split[2]:
                list_station_for_filter.append("COMMUNS  D")
            elif "1 - Métro -" in list_split[2]:
                list_station_for_filter.append("COMMUNS METRO")
            elif "302 - Funiculaires - communs" in list_split[2]:
                list_station_for_filter.append("COMMUNS FUN")
            elif "500 - Tramway T1 - communs" in list_split[2]:
                list_station_for_filter.append("COMMUNS TRAMWAY T1")
            elif "500 - Tramway T2 - communs" in list_split[2]:
                list_station_for_filter.append("COMMUNS TRAMWAY T2")
            elif "500 - Tramway T3 - communs" in list_split[2]:
                list_station_for_filter.append("COMMUNS TRAMWAY T3")
            elif "500 - Tramway T4 - communs" in list_split[2]:
                list_station_for_filter.append("COMMUNS TRAMWAY T4")
            elif "500 - Tramway T5 - communs" in list_split[2]:
                list_station_for_filter.append("COMMUNS TRAMWAY T5")
            elif "500 - Tramway T6 - communs" in list_split[2]:
                list_station_for_filter.append("COMMUNS TRAMWAY T6")
            elif "500 - Tramway - communs" in list_split[2]:
                list_station_for_filter.append("COMMUNS TRAMWAY")
            elif "500 - Tramway Rhone Express - communs" in list_split[2]:
                list_station_for_filter.append("RHONEXPRESS")

            list_split_station.append(list_station_for_filter)
        elif "interstations" in list_split[2]:
            list_station_for_filter = []
            if "101 - Métro A - interstations" in list_split[2]:
                list_station_for_filter.append("INTERSTATIONS  A")
            elif "103 - Métro B - interstations" in list_split[2]:
                list_station_for_filter.append("INTERSTATIONS  B")
            elif "201 - Métro C - interstations" in list_split[2]:
                list_station_for_filter.append("INTERSTATIONS  C")
            elif "301 - Métro D - interstations" in list_split[2]:
                list_station_for_filter.append("INTERSTATIONS  D")
            list_split_station.append(list_station_for_filter)
        elif "Liaison BD" in list_split[2]:
            list_station_for_filter = []
            if "303 - Liaison BD" in list_split[2]:
                list_station_for_filter.append("LIAISON B/D")
            list_split_station.append(list_station_for_filter)
        elif "900 - Lignes Fortes - C1 C2 C3 C13" in list_split[2]:
            list_station_for_filter = []
            if "C1 C2" in list_split[3]:
                list_station_for_filter.append("LIGNES FORTES C1/C2")
            elif "C3" in list_split[3]:
                list_station_for_filter.append("LIGNE FORTE C3")
            elif "C13" in list_split[3]:
                list_station_for_filter.append("LIGNE FORTE C13")
            list_split_station.append(list_station_for_filter)
        elif "Surface" in list_split[2]:
            list_station_for_filter = []
            if "00 Ligne Aérienne Trolleybus" in list_split[3]:
                list_station_for_filter.append("SURFACE L.A.")
            elif "Surface - communs" in list_split[3]:
                list_station_for_filter.append("COMMUNS SURFACE")
            else:
                list_station_for_filter.append("SURFACE")
            list_split_station.append(list_station_for_filter)
        elif "stations" in list_split[2]:
            list_station_for_filter = []
            for key, value in dict_stations.items():
                if list_split[3] == key:
                    list_station_for_filter.append(value)
                    continue
            list_split_station.append(list_station_for_filter)
        dict_arbo[row["Chemin du fichier"]] = list_split_station
    for i in dict_arbo.values():
        index_element = i[0]
        print("index_element", index_element)
        for item in index_element:
            if not re.match("(.*\d{1,}.*)", item):
                index_element.remove(item)
                continue
            if re.match("(.*\d{2,}\D{11,})", item):
                index_element.remove(item)
                continue
            for parse in LIST_PARSE_WORD:
                try:
                    if parse in item:
                        index_element.remove(item)
                        break
                except Exception as e:
                    pass

        try:
            for item in index_element:
                if not re.match("(.*\d{1,}.*)", item):
                    index_element.remove(item)
                    continue
                if re.match("(.*\d{2,}\D{11,})", item):
                    index_element.remove(item)
                    continue
                for parse in LIST_PARSE_WORD:
                    try:
                        if parse in item:
                            index_element.remove(item)
                            break
                    except Exception as e:
                        pass
        except Exception as e:
            pass

        try:
            if re.match("^(.+)\.", index_element[-1]):
                last_item_to_parse = re.findall("^(.+)\.", index_element[-1])
                index_element[-1] = last_item_to_parse[0]
            if len(index_element[0]) == 3:
                del index_element[0]
            if re.match("(.*\D{8,}.*)", index_element[0]):
                del index_element[0]
        except Exception as e:
            pass
    return dict_arbo


def compare_list_arbo_csv_bi(
    name_file_arbo,
    df_extraction,
    name_file_success,
    name_file_failed,
):
    """On itère les lists afin de trouver la référence fournisseur
    Input : input_datas/*.csv"""
    dict_arbo = find_ref_fournisseur(name_file_arbo)
    df = df_extraction
    list_success_path = []
    list_success_list = []
    list_success_values = []
    list_failed_path = []
    list_failed_list = []
    list_success_provenance = []
    list_failed_provenance = []
    print("df", df)
    for keys, values in dict_arbo.items():
        if "ST-100012-B.pdf" in keys:
            print("On entre dans un doublon")
            time.sleep(10)
        flag = False
        dict_jaro_distance = {}
        for value in values[0]:
            for ref_fourn, ref_fiche in zip(
                df[values[1][0]]["Référence fournisseur"],
                df[values[1][0]]["Référence fiche"],
            ):
                # print("ref_fourn", ref_fourn)
                ### Recherche basique
                if value == ref_fourn:
                    flag = True
                    list_success_path.append(keys)
                    list_success_list.append(ref_fiche)
                    list_success_values.append(values)
                    list_success_provenance.append("égalité")
                    break
                if value.replace(" ", "") == ref_fourn.replace(" ", ""):
                    flag = True
                    list_success_path.append(keys)
                    list_success_list.append(ref_fiche)
                    list_success_values.append(values)
                    list_success_provenance.append("égalité sans espaces")
                    break
                # try:
                if re.sub("[^A-Za-z0-9]+", "", value) in re.sub(
                    "[^A-Za-z0-9]+", "", ref_fourn
                ):
                    flag = True
                    list_success_path.append(keys)
                    list_success_list.append(ref_fiche)
                    list_success_values.append(values)
                    list_success_provenance.append("1 ")
                    break

                ### Recherche en enlevant 15 caractères si commence par AQ,AL,AY,AE,AL,BW,CC
                if value[:5] == "GMZ00":
                    value_zero_minus = value.replace("GMZ00", "GMZ0")
                    if value_zero_minus in ref_fourn:
                        flag = True
                        list_success_path.append(keys)
                        list_success_list.append(ref_fiche)
                        list_success_values.append(values)
                        list_success_provenance.append("2")
                        break
                if (
                    value[:2] == "AQ"
                    or value[:2] == "A0"
                    or value[:2] == "AA"
                    or value[:2] == "AD"
                    or value[:2] == "AE"
                    or value[:2] == "AF"
                    or value[:2] == "AK"
                    or value[:2] == "AL"
                    or value[:2] == "AN"
                    or value[:2] == "AO"
                    or value[:2] == "AS"
                    or value[:2] == "AT"
                    or value[:2] == "AV"
                    or value[:2] == "AY"
                    or value[:2] == "BD"
                    or value[:2] == "BG"
                    or value[:2] == "BH"
                    or value[:2] == "BO"
                    or value[:2] == "BS"
                    or value[:2] == "BU"
                    or value[:2] == "BV"
                    or value[:2] == "BW"
                    or value[:2] == "CC"
                    or value[:2] == "CG"
                    or value[:2] == "CI"
                    or value[:2] == "CM"
                    or value[:2] == "CN"
                    or value[:2] == "CP"
                    or value[:2] == "CT"
                    or value[:2] == "CZ"
                    or value[:2] == "DE"
                    or value[:2] == "DG"
                    or value[:2] == "DH"
                    or value[:2] == "EH"
                    or value[:2] == "EI"
                    or value[:2] == "EK"
                    or value[:2] == "EO"
                    or value[:2] == "EP"
                    or value[:2] == "ER"
                    or value[:2] == "EV"
                    or value[:2] == "FH"
                    or value[:2] == "FI"
                    or value[:2] == "FY"
                    or value[:2] == "FP"
                    or value[:2] == "FT"
                    or value[:2] == "HA"
                    or value[:2] == "HL"
                    or value[:2] == "IS"
                ):
                    value_last_eight = value[-8:]
                    # a[:2] + " " + a[2:]
                    if value[:2] == "AA" and len(value) < 9:
                        value_a = value.replace("AA", "AA-")
                        if value_a in ref_fourn:
                            flag = True
                            list_success_path.append(keys)
                            list_success_list.append(ref_fiche)
                            list_success_values.append(values)
                            list_success_provenance.append("3")
                            break
                    if value[:2] == "AQ":
                        # if (
                        #     value_last_eight.replace(
                        #         value_last_eight[1], value_last_eight[1] + " "
                        #     ).count(" ")
                        #     == 2
                        # ):
                        #     value_last_eight = (
                        #         value_last_eight[:2] + " " + value_last_eight[2:]
                        #     )
                        if value_last_eight[:2] == "TS" or value_last_eight[:2] == "TP":
                            if (
                                value_last_eight.replace(
                                    value_last_eight[1], value_last_eight[1] + " "
                                ).count(" ")
                                == 2
                            ):
                                value_last_eight = (
                                    value_last_eight[:2] + " " + value_last_eight[2:]
                                )
                            else:
                                value_last_eight = value_last_eight.replace(
                                    value_last_eight[1], value_last_eight[1] + " "
                                )
                        else:
                            if (
                                value_last_eight.replace(
                                    value_last_eight[1], value_last_eight[1] + "-"
                                ).count(" ")
                                == 2
                            ):
                                value_last_eight = (
                                    value_last_eight[:2] + "-" + value_last_eight[2:]
                                )
                            else:
                                value_last_eight = value_last_eight.replace(
                                    value_last_eight[1], value_last_eight[1] + "-"
                                )
                    # try:
                    if len(value) >= 8:
                        if value[-7] == value[-6]:
                            value_last_eight = value[-8:]
                            value_remove_double = (
                                value_last_eight[:1] + value_last_eight[2:]
                            )
                            if value_remove_double in ref_fourn:
                                flag = True
                                list_success_path.append(keys)
                                list_success_list.append(ref_fiche)
                                list_success_values.append(values)
                                list_success_provenance.append("4")
                                break
                            value_remove_double_space = (
                                value_last_eight[:1] + " " + value_last_eight[2:]
                            )
                            if not flag and value_remove_double_space in ref_fourn:
                                flag = True
                                list_success_path.append(keys)
                                list_success_list.append(ref_fiche)
                                list_success_values.append(values)
                                list_success_provenance.append("5")
                                break
                        else:
                            if (
                                value_last_eight.replace(
                                    value_last_eight[1], value_last_eight[1] + " "
                                ).count(" ")
                                == 2
                            ):
                                value_last_eight = (
                                    value_last_eight[:2] + " " + value_last_eight[2:]
                                )
                            else:
                                value_last_eight = value_last_eight.replace(
                                    value_last_eight[1], value_last_eight[1] + " "
                                )
                    if value_last_eight in ref_fourn:
                        flag = True
                        list_success_path.append(keys)
                        list_success_list.append(ref_fiche)
                        list_success_values.append(values)
                        list_success_provenance.append("6")
                        break
                    if flag == False:
                        value_no_spaces = value.replace(" ", "")
                        ref_fourn_no_spaces = ref_fourn.replace(" ", "")
                        if value_no_spaces[-8:] in ref_fourn_no_spaces[-8:]:
                            flag = True
                            list_success_path.append(keys)
                            list_success_list.append(ref_fiche)
                            list_success_values.append(values)
                            list_success_provenance.append("7")
                            break
                    # # list_duo = ["HF", "FA", "FB", "FC", "FD", "FE"]
                    # for duo in list_duo:
                    #     if duo in value:
                    #         value_no_spaces = value.replace(" ", "")
                    #         if value_no_spaces[15:] in ref_fourn:
                    #             flag = True
                    #             list_success_path.append(keys)
                    #             list_success_list.append(ref_fiche)
                    #             list_success_values.append(values) list_success_provenance.append(" ")

                    #             break
                ### Rajouter un tiret après ST,YA,SF,GL
                list_need_dash = [
                    "BA",
                    "BD",
                    "BL",
                    "BT",
                    "FA",
                    "FB",
                    "FD",
                    "FE",
                    "FN",
                    "GP",
                    "GL",
                    "HF",
                    "HL",
                    "MA",
                    "SE",
                    "SF",
                    "SM",
                    "ST",
                    "YA",
                ]
                for dash in list_need_dash:
                    if dash in value and re.match("\w{2}.?\d{5,}", value):
                        value = re.findall("\w{2}.?\d{5,}", value)
                        value = value[0]
                        value_dash = value.replace(dash, dash + "-")
                        value_dash_remove_space = value.replace(dash + " ", dash + "-")
                        value_dash_remove_space_add_zero = value.replace(
                            dash, dash + "-0"
                        )
                        value_dash_zero = value[:2] + "-0" + value[-2:]
                        value_only_tree_number = re.findall("(\w{2}.?\d{3})", value)
                        if (
                            value_only_tree_number[:2]
                            + "000"
                            + value_only_tree_number[2:]
                            in ref_fourn
                        ):
                            flag = True
                            list_success_path.append(keys)
                            list_success_list.append(ref_fiche)
                            list_success_values.append(value_only_tree_number)
                            list_test_number.append("10-1")
                            list_folder_doublon_succes.append(folder_for_doublon)
                            break
                        # if value_dash_zero.replace(" ", "") in ref_fourn.replace(
                        #     " ", ""
                        # ):
                        #     if "AQ" in ref_fourn:
                        #         flag = True
                        #         list_success_path.append(keys)
                        #         list_success_list.append(ref_fiche)
                        #         list_success_values.append(values)
                        #         list_success_provenance.append("8")
                        #         break
                        #     else:
                        #         pass
                        if value_dash in ref_fourn:
                            flag = True
                            list_success_path.append(keys)
                            list_success_list.append(ref_fiche)
                            list_success_values.append(values)
                            list_success_provenance.append("9")
                            break
                        elif value_dash_remove_space in ref_fourn:
                            flag = True
                            list_success_path.append(keys)
                            list_success_list.append(ref_fiche)
                            list_success_values.append(values)
                            list_success_provenance.append("10")
                            break
                        elif value_dash_remove_space_add_zero in ref_fourn:
                            flag = True
                            list_success_path.append(keys)
                            list_success_list.append(ref_fiche)
                            list_success_values.append(values)
                            list_success_provenance.append("11 ")
                            break
                        # if re.match("\w{2}.?\d{5}", value):
                        #     value_remove_post = re.findall("(\w{2}.?\d{5})", value)
                        #     value_remove_post = value_remove_post[0]
                        #     if value_remove_post in ref_fourn:
                        #         flag = True
                        #         list_success_path.append(keys)
                        #         list_success_list.append(ref_fiche)
                        #         list_success_values.append(values)
                        #         list_success_provenance.append("12 ")
                        #         break

                        if re.match("(ST\d{6})", value):
                            value_remove_post = re.findall("(ST\d{6})", value)
                            value_remove_post = value_remove_post[0]
                            value_remove_post = value_remove_post.replace("ST", "ST-")
                            if value_remove_post in ref_fourn:
                                flag = True
                                list_success_path.append(keys)
                                list_success_list.append(ref_fiche)
                                list_success_values.append(values)
                                list_success_provenance.append(" 13")
                                break
                        if not flag:
                            if value in ref_fourn:
                                flag = True
                                list_success_path.append(keys)
                                list_success_list.append(ref_fiche)
                                list_success_values.append(values)
                                list_success_provenance.append("14 ")
                                break
                        if not flag:
                            value_no_spaces = value.replace(" ", "")
                            if value_no_spaces in ref_fourn:
                                flag = True
                                list_success_path.append(keys)
                                list_success_list.append(ref_fiche)
                                list_success_values.append(values)
                                list_success_provenance.append("15 ")
                                break
                        if dash == "SF":
                            if not flag:
                                value_remove_zero = value[:2] + value[3:]
                                if value_remove_zero in ref_fourn:
                                    flag = True
                                    list_success_path.append(keys)
                                    list_success_list.append(ref_fiche)
                                    list_success_values.append(values)
                                    list_success_provenance.append("16 ")
                                    break
                        if dash == "FA":
                            if not flag:
                                try:
                                    value_add_zero = value.replace("FA-", "FA-0")
                                    if value_add_zero in ref_fourn:
                                        flag = True
                                        list_success_path.append(keys)
                                        list_success_list.append(ref_fiche)
                                        list_success_values.append(values)
                                        list_success_provenance.append("17 ")
                                        break
                                except Exception as e:
                                    value_add_zero = value.replace("FA", "FA-0")
                                    if value_add_zero in ref_fourn:
                                        flag = True
                                        list_success_path.append(keys)
                                        list_success_list.append(ref_fiche)
                                        list_success_values.append(values)
                                        list_success_provenance.append(" 18")
                                        break
                        if dash == "HF":
                            if not flag:
                                value_add_zero = value.replace("HF-", "HF-0")
                                if value_add_zero in ref_fourn:
                                    flag = True
                                    list_success_path.append(keys)
                                    list_success_list.append(ref_fiche)
                                    list_success_values.append(values)
                                    list_success_provenance.append("19 ")
                                    break
                                value_add_zero = value.replace("HF", "HF-0")
                                if value_add_zero in ref_fourn:
                                    flag = True
                                    list_success_path.append(keys)
                                    list_success_list.append(ref_fiche)
                                    list_success_values.append(values)
                                    list_success_provenance.append(" 20")
                                    break
                if value[:3] == "ETL":
                    ref_fourn_no_zero = ref_fourn.replace("0", "")
                    if value == ref_fourn_no_zero:
                        flag = True
                        list_success_path.append(keys)
                        list_success_list.append(ref_fiche)
                        list_success_values.append(values)
                        list_success_provenance.append(" 21")
                        break
                ### On recherche le pattern 800E263
                if not flag:
                    if re.match("^(\d{3}E\d{3})$", value):
                        value_e = value.replace("E", " E ")
                        if value_e == ref_fourn:
                            flag = True
                            list_success_path.append(keys)
                            list_success_list.append(ref_fiche)
                            list_success_values.append(values)
                            list_success_provenance.append("22 ")
                            break
                    if re.match("([A-Z]{2}.*)", value):
                        value_replace = re.findall("([A-Z]{2}.*)", value)
                        value_replace = value_replace[0]
                        ref_fourn_no_spaces = ref_fourn.replace(" ", "")
                        if value_replace == ref_fourn_no_spaces:
                            flag = True
                            list_success_path.append(keys)
                            list_success_list.append(ref_fiche)
                            list_success_values.append(values)
                            list_success_provenance.append("23 ")
                            break

                    if re.match("(\d{3,6}\W*\D{3,5}\W*\d{3,6})", value):
                        ref_fourn_no_spaces = ref_fourn.replace(" ", "")
                        value_no_spaces = value.replace(" ", "")
                        if value_no_spaces == ref_fourn_no_spaces:
                            flag = True
                            list_success_path.append(keys)
                            list_success_list.append(ref_fiche)
                            list_success_values.append(values)
                            list_success_provenance.append("24 ")
                            break

                if len(value) == 8:
                    if value[:2] == "AA":
                        value_a = value.replace("AA", "AA-")
                        if value_a in ref_fourn:
                            flag = True
                            list_success_path.append(keys)
                            list_success_list.append(ref_fiche)
                            list_success_values.append(values)
                            list_success_provenance.append("25 ")
                            break
                if re.match("([A-Z0-9]{5,})", value):
                    value_cut_point = re.findall("([A-Z0-9]{5,})", value)
                    value_cut_point = value_cut_point[0]
                    ref_fourn_no_spaces = ref_fourn.replace(" ", "")
                    value_cut_point = value_cut_point.replace(" ", "")
                    if value_cut_point in ref_fourn_no_spaces:
                        flag = True
                        list_success_path.append(keys)
                        list_success_list.append(ref_fiche)
                        list_success_values.append(values)
                        list_success_provenance.append(" 26")
                        break
                if value[:-1].replace(" ", "") == ref_fourn.replace(" ", ""):
                    flag = True
                    list_success_path.append(keys)
                    list_success_list.append(ref_fiche)
                    list_success_values.append(values)
                    list_success_provenance.append("27 ")
                    break

                jaro_stat = jellyfish.jaro_distance(
                    value.replace(" ", ""), ref_fourn.replace(" ", "")
                )
                jaro_distance = jellyfish.damerau_levenshtein_distance(
                    value.replace(" ", ""), ref_fourn.replace(" ", "")
                )
                dict_jaro_distance[jaro_stat] = {
                    "ref": ref_fourn,
                    "value": value,
                    "jaro_distance": jaro_distance,
                }
            if flag == True:
                print("DEJA AJOUTE")
                break
        if flag == False:
            sorted_dict_jaro_distance = {
                k: dict_jaro_distance[k]
                for k in sorted(dict_jaro_distance, reverse=True)
            }
            print(
                "***********sorted_dict_jaro_distance**********",
                sorted_dict_jaro_distance,
            )
            if len(dict_jaro_distance) > 0:
                stats_key = list(sorted_dict_jaro_distance)[0]
                if (
                    stats_key >= 0.90
                    and sorted_dict_jaro_distance[stats_key]["jaro_distance"] <= 2
                ):
                    if sorted_dict_jaro_distance[stats_key]["value"].replace(
                        " ", ""
                    ) in sorted_dict_jaro_distance[stats_key]["ref"].replace(" ", ""):
                        flag = True
                        list_success_path.append(keys)
                        list_success_list.append(ref_fiche)
                        list_success_values.append(values)
                        list_success_provenance.append(
                            "ajouté grâce à l'algo de Jaro-Winkler"
                        )
                        continue
                    else:
                        list_failed_path.append(keys)
                        list_failed_list.append(values)
                        list_failed_provenance.append("jaro bon mais pas match ")
                else:
                    list_failed_path.append(keys)
                    list_failed_list.append(values)
                    list_failed_provenance.append("jaro inférieur a 90% ou sup 2 ")

            else:
                list_failed_path.append(keys)
                list_failed_list.append(values)
                list_failed_provenance.append("jaro vide")
    df_success = pd.DataFrame(
        {
            "Chemin du fichier": list_success_path,
            "Référence Fiche": list_success_list,
            "lists": list_success_values,
            "dict": list_success_provenance,
        },
    )
    print(df_success)

    df_failed = pd.DataFrame(
        {
            "Chemin du fichier": list_failed_path,
            "Référence Fiche": list_failed_list,
            "dict": list_failed_provenance,
        },
    )
    print(df_success.shape)
    df_success.to_csv(
        name_file_success,
        sep=";",
        index=False,
        encoding="utf-8-sig",
    )
    df_failed.to_csv(
        name_file_failed,
        sep=";",
        index=False,
        encoding="utf-8-sig",
    )
