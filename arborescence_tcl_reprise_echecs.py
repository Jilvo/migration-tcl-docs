"""
Ce Script crée permet le rattrapage des echecs en comparant à une ligne et  retourne sous format CSV
"""

import os
import sys
import pandas as pd
import re
from timeit import default_timer as timer
from fichiers_et_constantes import *
from difflib import SequenceMatcher
import jellyfish

with open(PARSER_FILTER_FILE, encoding="utf-8") as f:
    LIST_PARSE_WORD = f.read().splitlines()


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
    df = pd.read_csv(
        name_file_arbo,
        sep=";",
        error_bad_lines=False,
        encoding="utf-8-sig",
        # encoding = "cp1252"
    )
    df_stations = pd.read_csv(
        LISTES_ARRETS_LIGNES,
        encoding="cp1252",
        sep=";",
    )
    dict_arbo = {}
    for index, row in df.iterrows():
        list_split = split_arbo(row["Chemin du fichier"])
        dict_arbo[row["Chemin du fichier"]] = list_split
    for index_element in dict_arbo.values():
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


def compare_list_arbo_csv_bi_rattrapage(
    name_file_arbo, df_extraction, name_file_success, name_file_failed
):
    """On itère les lists afin de trouver la référence fournisseur"""
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
        print(keys)
        flag = False
        dict_jaro_distance = {}

        for value in values:
            for ref_fourn, ref_fiche in zip(
                df["Référence fournisseur"], df["Référence fiche"]
            ):
                value = value.upper()
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
                if value.replace("O", "0") == ref_fourn:
                    flag = True
                    list_success_path.append(keys)
                    list_success_list.append(ref_fiche)
                    list_success_values.append(values)
                    list_success_provenance.append("égalité remplacement 0 et O")
                    break
                if re.match("(\D{3}\d{5})", value.replace(" ", "")):
                    value_m = value.replace(" ", "")
                    value_m = value_m[:3] + "00" + value_m[-5:]
                    if value_m == ref_fourn.replace(" ", ""):
                        flag = True
                        list_success_path.append(keys)
                        list_success_list.append(ref_fiche)
                        list_success_values.append(values)
                        list_success_provenance.append("égalité avec ajout 0")
                # if re.match("(\D{3}\d{4})", value.replace(" ", "")):
                #     value_m = value.replace(" ", "")
                #     value_m = value_m[:3] + "-00" + value_m[-4:]
                #     if value_m in ref_fourn.replace(" ", ""):
                #         flag = True
                #         list_success_path.append(keys)
                #         list_success_list.append(ref_fiche)
                #         list_success_values.append(values)
                #         list_success_provenance.append("approximation1")
                # if len(value) > 10:
                #     value_m = value.replace(" ", "")
                #     value_m = value_m[:-3] + "000" + value_m[-3:]
                #     if value_m == ref_fourn.replace(" ", ""):
                #         flag = True
                #         list_success_path.append(keys)
                #         list_success_list.append(ref_fiche)
                #         list_success_values.append(values)
                #         list_success_provenance.append("approximation2")

                # if re.match(".*\D{2}\d{3}$", value.replace(" ", "")):
                #     value_u = value.replace(" ", "")
                #     values_u = value_u[:-3] + "000" + value_u[-3:]
                #     if values_u in ref_fourn.replace(" ", ""):
                #         flag = True
                #         list_success_path.append(keys)
                #         list_success_list.append(ref_fiche)
                #         list_success_values.append(values)
                #         list_success_provenance.append("approximation3")
                #         break
                # value_l_number = re.findall("L\d{4}", value)
                # if len(value_l_number) > 0:
                #     value_l_number = value_l_number[0]
                #     if value_l_number in ref_fourn:
                #         flag = True
                #         list_success_path.append(keys)
                #         list_success_list.append(ref_fiche)
                #         list_success_values.append(values)
                #         list_success_provenance.append("approximation4")
                #         break
                # value_vl_number = re.findall("VL\d{3}", value)
                # if len(value_vl_number) > 0:
                #     value_vl_number = value_vl_number[0]
                #     if value_vl_number in ref_fourn:
                #         flag = True
                #         list_success_path.append(keys)
                #         list_success_list.append(ref_fiche)
                #         list_success_values.append(values)
                #         list_success_provenance.append("approximation5")
                #         break
                # value_parenthese = re.findall("\) (.*)", value)
                # if len(value_parenthese) > 0:
                #     value_parenthese = value_parenthese[0]
                #     if value_parenthese in ref_fourn:
                #         flag = True
                #         list_success_path.append(keys)
                #         list_success_list.append(ref_fiche)
                #         list_success_values.append(values)
                #         list_success_provenance.append("approximation6")
                #         break

                # # # try:
                # # if re.sub("[^A-Za-z0-9]+", "", value) in re.sub(
                # #     "[^A-Za-z0-9]+", "", ref_fourn
                # # ):
                # #     flag = True
                # #     list_success_path.append(keys)
                # #     list_success_list.append(ref_fiche)
                # #     list_success_values.append(values)
                # #     list_success_provenance.append("approximation7")
                # #     break

                # ### Recherche en enlevant 15 caractères si commence par AQ,AL,AY,AE,AL,BW,CC
                # if value[:5] == "GMZ00":
                #     value_zero_minus = value.replace("GMZ00", "GMZ0")
                #     if value_zero_minus in ref_fourn:
                #         flag = True
                #         list_success_path.append(keys)
                #         list_success_list.append(ref_fiche)
                #         list_success_values.append(values)
                #         list_success_provenance.append("approximation8")
                #         break
                # if (
                #     value[:2] == "AQ"
                #     or value[:2] == "A0"
                #     or value[:2] == "AA"
                #     or value[:2] == "AD"
                #     or value[:2] == "AE"
                #     or value[:2] == "AF"
                #     or value[:2] == "AK"
                #     or value[:2] == "AL"
                #     or value[:2] == "AN"
                #     or value[:2] == "AO"
                #     or value[:2] == "AS"
                #     or value[:2] == "AT"
                #     or value[:2] == "AV"
                #     or value[:2] == "AY"
                #     or value[:2] == "BD"
                #     or value[:2] == "BG"
                #     or value[:2] == "BH"
                #     or value[:2] == "BO"
                #     or value[:2] == "BS"
                #     or value[:2] == "BU"
                #     or value[:2] == "BV"
                #     or value[:2] == "BW"
                #     or value[:2] == "CC"
                #     or value[:2] == "CG"
                #     or value[:2] == "CI"
                #     or value[:2] == "CM"
                #     or value[:2] == "CN"
                #     or value[:2] == "CP"
                #     or value[:2] == "CT"
                #     or value[:2] == "CZ"
                #     or value[:2] == "DE"
                #     or value[:2] == "DG"
                #     or value[:2] == "DH"
                #     or value[:2] == "EH"
                #     or value[:2] == "EI"
                #     or value[:2] == "EK"
                #     or value[:2] == "EO"
                #     or value[:2] == "EP"
                #     or value[:2] == "ER"
                #     or value[:2] == "EV"
                #     or value[:2] == "FH"
                #     or value[:2] == "FI"
                #     or value[:2] == "FY"
                #     or value[:2] == "FP"
                #     or value[:2] == "FT"
                #     or value[:2] == "HA"
                #     or value[:2] == "HL"
                #     or value[:2] == "IS"
                # ):
                #     value_last_eight = value[-8:]
                #     if value[:2] == "AA" and len(value) < 9:
                #         value_a = value.replace("AA", "AA-")
                #         if value_a in ref_fourn:
                #             flag = True
                #             list_success_path.append(keys)
                #             list_success_list.append(ref_fiche)
                #             list_success_values.append(values)
                #             list_success_provenance.append("approximation9")
                #             break
                #     if value[:2] == "AQ":
                #         if value_last_eight[:2] == "TS" or value_last_eight[:2] == "TP":
                #             if (
                #                 value_last_eight.replace(
                #                     value_last_eight[1], value_last_eight[1] + " "
                #                 ).count(" ")
                #                 == 2
                #             ):
                #                 value_last_eight = (
                #                     value_last_eight[:2] + " " + value_last_eight[2:]
                #                 )
                #             else:
                #                 value_last_eight = value_last_eight.replace(
                #                     value_last_eight[1], value_last_eight[1] + " "
                #                 )
                #         else:
                #             if (
                #                 value_last_eight.replace(
                #                     value_last_eight[1], value_last_eight[1] + "-"
                #                 ).count(" ")
                #                 == 2
                #             ):
                #                 value_last_eight = (
                #                     value_last_eight[:2] + "-" + value_last_eight[2:]
                #                 )
                #             else:
                #                 value_last_eight = value_last_eight.replace(
                #                     value_last_eight[1], value_last_eight[1] + "-"
                #                 )
                #     # try:
                #     if len(value) >= 8:
                #         if value[-7] == value[-6]:
                #             value_last_eight = value[-8:]
                #             value_remove_double = (
                #                 value_last_eight[:1] + value_last_eight[2:]
                #             )
                #             if value_remove_double in ref_fourn:
                #                 flag = True
                #                 list_success_path.append(keys)
                #                 list_success_list.append(ref_fiche)
                #                 list_success_values.append(values)
                #                 list_success_provenance.append("approximation10")
                #                 break
                #             value_remove_double_space = (
                #                 value_last_eight[:1] + " " + value_last_eight[2:]
                #             )
                #             if not flag and value_remove_double_space in ref_fourn:
                #                 flag = True
                #                 list_success_path.append(keys)
                #                 list_success_list.append(ref_fiche)
                #                 list_success_values.append(values)
                #                 list_success_provenance.append("approximation11")
                #                 break
                #         else:
                #             if (
                #                 value_last_eight.replace(
                #                     value_last_eight[1], value_last_eight[1] + " "
                #                 ).count(" ")
                #                 == 2
                #             ):
                #                 value_last_eight = (
                #                     value_last_eight[:2] + " " + value_last_eight[2:]
                #                 )
                #             else:
                #                 value_last_eight = value_last_eight.replace(
                #                     value_last_eight[1], value_last_eight[1] + " "
                #                 )
                #     # except Exception as e:
                #     #     print("ici")
                #     #     print(e.args)
                #     if value_last_eight in ref_fourn:
                #         flag = True
                #         list_success_path.append(keys)
                #         list_success_list.append(ref_fiche)
                #         list_success_values.append(values)
                #         list_success_provenance.append("approximation12")
                #         break
                #     if flag == False:
                #         value_no_spaces = value.replace(" ", "")
                #         ref_fourn_no_spaces = ref_fourn.replace(" ", "")
                #         if value_no_spaces[-8:] in ref_fourn_no_spaces[-8:]:
                #             flag = True
                #             list_success_path.append(keys)
                #             list_success_list.append(ref_fiche)
                #             list_success_values.append(values)
                #             list_success_provenance.append("approximation13")
                #             break
                # ### Rajouter un tiret après ST,YA,SF,GL
                # list_need_dash = [
                #     "BA",
                #     "BD",
                #     "BL",
                #     "BT",
                #     "EE",
                #     "EQ",
                #     "FA",
                #     "FB",
                #     "FC",
                #     "FD",
                #     "FE",
                #     "FF",
                #     "FN",
                #     "FV",
                #     "GP",
                #     "GL",
                #     "HF",
                #     "HL",
                #     "KG",
                #     "MA",
                #     "MB",
                #     "NT",
                #     "SE",
                #     "SF",
                #     "SG",
                #     "SM",
                #     "SR",
                #     "ST",
                #     "YA",
                #     "YU",
                # ]
                # for dash in list_need_dash:
                #     if dash in value and re.match("\w{2}.?\d{5,}", value):
                #         value = re.findall("\w{2}.?\d{5,}", value)
                #         value = value[0]
                #         value_dash = value.replace(dash, dash + "-")
                #         value_dash_remove_space = value.replace(dash + " ", dash + "-")
                #         value_dash_remove_space_add_zero = value.replace(
                #             dash, dash + "-0"
                #         )
                #         value_dash_remove_space_dash = re.findall(
                #             "(.{2})[-, ]{1}(\d{2,5})", value
                #         )
                #         if len(value_dash_remove_space_dash) > 1:
                #             if len(value_dash_remove_space_dash[0][1]) == 5:
                #                 value_u = (
                #                     value_dash_remove_space_dash[0][0]
                #                     + "-0"
                #                     + value_dash_remove_space_dash[0][1]
                #                 )
                #                 if value_u in ref_fourn:
                #                     flag = True
                #                     list_success_path.append(keys)
                #                     list_success_list.append(ref_fiche)
                #                     list_success_values.append(values)
                #                     list_success_provenance.append("approximation14")
                #                     break
                #             elif len(value_dash_remove_space_dash[0][1]) == 4:
                #                 value_u = (
                #                     value_dash_remove_space_dash[0][0]
                #                     + "-00"
                #                     + value_dash_remove_space_dash[0][1]
                #                 )
                #                 if value_u in ref_fourn:
                #                     flag = True
                #                     list_success_path.append(keys)
                #                     list_success_list.append(ref_fiche)
                #                     list_success_values.append(values)
                #                     list_success_provenance.append("approximation15")
                #                     break
                #             elif len(value_dash_remove_space_dash[0][1]) == 3:
                #                 value_u = (
                #                     value_dash_remove_space_dash[0][0]
                #                     + "-000"
                #                     + value_dash_remove_space_dash[0][1]
                #                 )
                #                 if value_u in ref_fourn:
                #                     flag = True
                #                     list_success_path.append(keys)
                #                     list_success_list.append(ref_fiche)
                #                     list_success_values.append(values)
                #                     list_success_provenance.append("approximation16")
                #                     break
                #         value_dash_zero = value[:2] + "-0" + value[-2:]
                #         if value_dash in ref_fourn:
                #             flag = True
                #             list_success_path.append(keys)
                #             list_success_list.append(ref_fiche)
                #             list_success_values.append(values)
                #             list_success_provenance.append("approximation17")
                #             break
                #         elif value_dash_remove_space in ref_fourn:
                #             flag = True
                #             list_success_path.append(keys)
                #             list_success_list.append(ref_fiche)
                #             list_success_values.append(values)
                #             list_success_provenance.append("approximation18")
                #             break
                #         elif value_dash_remove_space_add_zero in ref_fourn:
                #             flag = True
                #             list_success_path.append(keys)
                #             list_success_list.append(ref_fiche)
                #             list_success_values.append(values)
                #             list_success_provenance.append("approximation19")
                #             break
                #         elif (
                #             value_dash_remove_space_add_zero.replace(" ", "")
                #             in ref_fourn
                #         ):
                #             flag = True
                #             list_success_path.append(keys)
                #             list_success_list.append(ref_fiche)
                #             list_success_values.append(values)
                #             list_success_provenance.append("approximation20")
                #             break

                #         if re.match("(ST\d{6})", value):
                #             value_remove_post = re.findall("(ST\d{6})", value)
                #             value_remove_post = value_remove_post[0]
                #             value_remove_post = value_remove_post.replace("ST", "ST-")
                #             if value_remove_post in ref_fourn:
                #                 flag = True
                #                 list_success_path.append(keys)
                #                 list_success_list.append(ref_fiche)
                #                 list_success_values.append(values)
                #                 list_success_provenance.append("approximation21")
                #                 break
                #         if not flag:
                #             if value in ref_fourn:
                #                 flag = True
                #                 list_success_path.append(keys)
                #                 list_success_list.append(ref_fiche)
                #                 list_success_values.append(values)
                #                 list_success_provenance.append("approximation22")
                #                 break
                #         if not flag:
                #             value_no_spaces = value.replace(" ", "")
                #             if value_no_spaces in ref_fourn:
                #                 flag = True
                #                 list_success_path.append(keys)
                #                 list_success_list.append(ref_fiche)
                #                 list_success_values.append(values)
                #                 list_success_provenance.append("approximation23")
                #                 break
                #         if dash == "SF":
                #             if not flag:
                #                 value_remove_zero = value[:2] + value[3:]
                #                 if value_remove_zero in ref_fourn:
                #                     flag = True
                #                     list_success_path.append(keys)
                #                     list_success_list.append(ref_fiche)
                #                     list_success_values.append(values)
                #                     list_success_provenance.append("approximation24")
                #                     break
                #         if dash == "FA":
                #             if not flag:
                #                 try:
                #                     value_add_zero = value.replace("FA-", "FA-0")
                #                     if value_add_zero in ref_fourn:
                #                         flag = True
                #                         list_success_path.append(keys)
                #                         list_success_list.append(ref_fiche)
                #                         list_success_values.append(values)
                #                         list_success_provenance.append(
                #                             "approximation25"
                #                         )
                #                         break
                #                 except Exception as e:
                #                     value_add_zero = value.replace("FA", "FA-0")
                #                     if value_add_zero in ref_fourn:
                #                         flag = True
                #                         list_success_path.append(keys)
                #                         list_success_list.append(ref_fiche)
                #                         list_success_values.append(values)
                #                         list_success_provenance.append(
                #                             "approximation26"
                #                         )
                #                         break
                #         if dash == "HF":
                #             if not flag:
                #                 value_add_zero = value.replace("HF-", "HF-0")
                #                 if value_add_zero in ref_fourn:
                #                     flag = True
                #                     list_success_path.append(keys)
                #                     list_success_list.append(ref_fiche)
                #                     list_success_values.append(values)
                #                     list_success_provenance.append("approximation27")
                #                     break
                #                 value_add_zero = value.replace("HF", "HF-0")
                #                 if value_add_zero in ref_fourn:
                #                     flag = True
                #                     list_success_path.append(keys)
                #                     list_success_list.append(ref_fiche)
                #                     list_success_values.append(values)
                #                     list_success_provenance.append("approximation28")
                #                     break
                #     if len(value) == 6 and value[:2] == "KG":
                #         value_kg = "KG-00" + value[-4:]
                #         if value_kg in ref_fourn:
                #             flag = True
                #             list_success_path.append(keys)
                #             list_success_list.append(ref_fiche)
                #             list_success_values.append(values)
                #             list_success_provenance.append("approximation29")
                #             break
                # if value[:3] == "ETL":
                #     ref_fourn_no_zero = ref_fourn.replace("0", "")
                #     if value == ref_fourn_no_zero:
                #         flag = True
                #         list_success_path.append(keys)
                #         list_success_list.append(ref_fiche)
                #         list_success_values.append(values)
                #         list_success_provenance.append("approximation30")
                #         break
                # ### On recherche le pattern 800E263
                # if not flag:
                #     if re.match("^(\d{3}E\d{3})$", value):
                #         value_e = value.replace("E", " E ")
                #         if value_e == ref_fourn:
                #             flag = True
                #             list_success_path.append(keys)
                #             list_success_list.append(ref_fiche)
                #             list_success_values.append(values)
                #             list_success_provenance.append("approximation31")
                #             break
                #     if re.match("([A-Z]{2}.*)", value):
                #         value_replace = re.findall("([A-Z]{2}.*)", value)
                #         value_replace = value_replace[0]
                #         ref_fourn_no_spaces = ref_fourn.replace(" ", "")
                #         if value_replace == ref_fourn_no_spaces:
                #             flag = True
                #             list_success_path.append(keys)
                #             list_success_list.append(ref_fiche)
                #             list_success_values.append(values)
                #             list_success_provenance.append("approximation32")
                #             break

                #     if re.match("(\d{3,6}\W*\D{3,5}\W*\d{3,6})", value):
                #         ref_fourn_no_spaces = ref_fourn.replace(" ", "")
                #         value_no_spaces = value.replace(" ", "")
                #         if value_no_spaces == ref_fourn_no_spaces:
                #             flag = True
                #             list_success_path.append(keys)
                #             list_success_list.append(ref_fiche)
                #             list_success_values.append(values)
                #             list_success_provenance.append("approximation33")
                #             break

                # if len(value) == 8:
                #     if value[:2] == "AA":
                #         value_a = value.replace("AA", "AA-")
                #         if value_a in ref_fourn:
                #             flag = True
                #             list_success_path.append(keys)
                #             list_success_list.append(ref_fiche)
                #             list_success_values.append(values)
                #             list_success_provenance.append("approximation34")
                #             break
                # if re.match("([A-Z0-9]{5,})", value):
                #     value_cut_point = re.findall("([A-Z0-9]{5,})", value)
                #     value_cut_point = value_cut_point[0]
                #     ref_fourn_no_spaces = ref_fourn.replace(" ", "")
                #     value_cut_point = value_cut_point.replace(" ", "")
                #     if value_cut_point in ref_fourn_no_spaces:
                #         flag = True
                #         list_success_path.append(keys)
                #         list_success_list.append(ref_fiche)
                #         list_success_values.append(values)
                #         list_success_provenance.append("approximation35")
                #         break
                # if value[:-1].replace(" ", "") == ref_fourn.replace(" ", ""):
                #     flag = True
                #     list_success_path.append(keys)
                #     list_success_list.append(ref_fiche)
                #     list_success_values.append(values)
                #     list_success_provenance.append("approximation36")
                #     break

                jaro_stat = jellyfish.jaro_distance(
                    value.replace(" ", ""), ref_fourn.replace(" ", "")
                )
                jaro_distance = jellyfish.damerau_levenshtein_distance(
                    value.replace(" ", ""), ref_fourn.replace(" ", "")
                )
                dict_jaro_distance[jaro_stat] = {
                    "ref": ref_fourn,
                    "ref_fiche": ref_fiche,
                    "value": value,
                    "jaro_distance": jaro_distance,
                }
            if flag == True:
                print("On vient de trouver la référence")
                break
        if flag == False:
            sorted_dict_jaro_distance = {
                k: dict_jaro_distance[k]
                for k in sorted(dict_jaro_distance, reverse=True)
            }
            # print(
            #     "***********sorted_dict_jaro_distance**********",
            #     sorted_dict_jaro_distance,
            # )
            if len(dict_jaro_distance) > 0:
                stats_key = list(sorted_dict_jaro_distance)[0]
                print("stats_key", stats_key)
                if (
                    stats_key >= 0.95
                    and sorted_dict_jaro_distance[stats_key]["jaro_distance"] <= 1
                ):
                    if (
                        sorted_dict_jaro_distance[stats_key]["value"].replace(" ", "")[
                            -1
                        ]
                        != sorted_dict_jaro_distance[stats_key]["ref"].replace(" ", "")[
                            -1
                        ]
                    ):
                        flag = True
                        # list_success_path.append(keys)
                        # list_success_list.append(
                        #     sorted_dict_jaro_distance[stats_key]["ref_fiche"]
                        # )
                        # list_success_values.append(values)
                        list_failed_path.append(keys)
                        list_failed_list.append(values)
                        list_failed_provenance.append(
                            "Algo supérieur à 95% - 1 carac de diff - en 2nd passe - dernier caract différent"
                        )
                        continue
                    else:
                        flag = True
                        list_success_path.append(keys)
                        list_success_list.append(
                            sorted_dict_jaro_distance[stats_key]["ref_fiche"]
                        )
                        list_success_values.append(values)
                        list_success_provenance.append(
                            "Algo supérieur à 95% - 1 carac de diff - en 2nd passe - pas le dernier caract différent"
                        )
                        continue

                elif (
                    stats_key >= 0.95
                    and sorted_dict_jaro_distance[stats_key]["jaro_distance"] <= 2
                ):
                    print("sup 95")
                    print("stats_key", stats_key)
                    print(
                        "sorted_dict_jaro_distance[stats_key]",
                        sorted_dict_jaro_distance[stats_key],
                    )
                    flag = True
                    list_success_path.append(keys)
                    list_success_list.append(
                        sorted_dict_jaro_distance[stats_key]["ref_fiche"]
                    )
                    list_success_values.append(values)
                    list_success_provenance.append(
                        "Algo supérieur à 95% et 2 de distance"
                    )
                    continue
                else:
                    list_failed_path.append(keys)
                    list_failed_list.append(values)
                    list_failed_provenance.append(
                        f"""jaro inférieur à 90% ou sup 2 {sorted_dict_jaro_distance[stats_key]["ref"]} """
                    )

            else:
                list_failed_path.append(keys)
                list_failed_list.append(values)
                list_failed_provenance.append("Algo vide et aucun match")
    df_success = pd.DataFrame(
        {
            "Chemin du fichier": list_success_path,
            "Référence Fiche": list_success_list,
            "Commentaires": list_success_provenance,
            # "lists": list_success_values,
        },
    )
    print(df_success)

    df_failed = pd.DataFrame(
        {
            "Chemin du fichier": list_failed_path,
            # "Référence Fiche": list_failed_list,
            "Commentaires": list_failed_provenance,
        },
    )
    print(df_success.shape)
    df_success.to_csv(
        name_file_success,
        mode="a",
        sep=";",
        index=False,
        header=False,
        encoding="utf-8-sig",
    )
    df_failed.to_csv(
        name_file_failed,
        sep=";",
        index=False,
        encoding="utf-8-sig",
    )
