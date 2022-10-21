"""
Ce Script crée l'arborescence du serveur SERBER et la retourne sous format CSV
Input : None
Output : output_datas/arborescence_tcl.csv
"""

import os
import sys
import pandas as pd
import re
from timeit import default_timer as timer

start = timer()

DIRNAME = f"""G:\{str(500000)}"""
list_arbo = []

with open("input_datas\parse_filter.txt", encoding="utf-8") as f:
    LIST_PARSE_WORD = f.read().splitlines()


def create_arbo(DIRNAME, name_file_arbo):
    """On crée l'arborescence"""
    for path, subdirs, files in os.walk(DIRNAME):
        for name in files:
            try:
                print(os.path.join(path, name))
                list_arbo.append(os.path.join(path, name))
            except Exception as e:
                print(e.args)
    df = pd.DataFrame(
        {
            "Chemin du fichier": list_arbo,
        },
    )
    # df.to_csv(
    #     "output_datas/arborescence_tcl_pret.csv",
    #     sep="\t",
    #     index=False,
    #     encoding="utf-8-sig",
    # )
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
    df = pd.read_csv(
        name_file_arbo,
        sep=";",
        error_bad_lines=False,
        encoding="utf-8-sig",
    )
    dict_arbo = {}
    list_path = []
    list_list = []
    for index, row in df.iterrows():
        list_split = split_arbo(row["Chemin du fichier"])
        dict_arbo[row["Chemin du fichier"]] = list_split
    for keys, index_element in dict_arbo.items():
        for item in index_element:
            if not re.match("(.*\d{2,}.*)", item):
                # print("Pas de chiffre, on delete", item)
                index_element.remove(item)
                continue
            if re.match("(.*\d{2,}\D{8,})", item):
                # print("2 chiffres et 8 lettres ou plus, on delete", item)
                index_element.remove(item)
                continue
            for parse in LIST_PARSE_WORD:
                try:
                    if parse in item:
                        index_element.remove(item)
                        break
                except Exception as e:
                    pass

            list_path.append(keys)
            list_list.append(index_element or "RIEN")
        try:
            if re.match("^(.+)\.", index_element[-1]):
                last_item_to_parse = re.findall("^(.+)\.", index_element[-1])
                index_element[-1] = last_item_to_parse[0]
        except Exception as e:
            pass
    return dict_arbo


def compare_list_arbo_csv_bi(
    name_file_arbo, df_extraction, name_file_success, name_file_failed, nb_passage
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

    for keys, values in dict_arbo.items():
        print(keys)
        flag = False
        for value in values:
            for ref_fourn, ref_fiche in zip(
                df["Référence fournisseur"], df["Référence fiche"]
            ):

                value = value.upper()
                value = re.sub("(\W?V.*)", "", value)
                # print(ref_fourn)
                ### Recherche basique
                if value == ref_fourn:
                    flag = True
                    list_success_path.append(keys)
                    list_success_list.append(ref_fiche)
                    list_success_values.append(values)
                    break
                ## CONCATENER 2 item de la list
                if len(values) >= 3:
                    conc_values = values[1] + values[2]
                    if re.match("(\D{2}\d{3}\d+)", values[2]):
                        pass
                    elif re.match("(\D{2}\d{3})$", values[2]):
                        conc_values = (
                            values[1] + values[2][:-3] + "000" + values[2][-3:]
                        )
                    elif re.match("(\D{2}\d{3}\D+)", values[2]):
                        a = re.findall("(\D{2}\d{3})", values[2])
                        a = a[0]
                        conc_values = values[1] + a[:-3] + "000" + a[-3:]
                    elif values[1][-3:] == values[2][:3]:
                        conc_values = values[1] + values[2][3:]
                    if conc_values.replace(" ", "") in ref_fourn.replace(" ", ""):
                        flag = True
                        list_success_path.append(keys)
                        list_success_list.append(ref_fiche)
                        list_success_values.append(values)
                        break
                    conc_values_exact = values[1] + values[2]
                    if conc_values_exact.replace(" ", "") in ref_fourn.replace(" ", ""):
                        flag = True
                        list_success_path.append(keys)
                        list_success_list.append(ref_fiche)
                        list_success_values.append(values)
                        break
        if flag == False:
            list_failed_path.append(keys)
            list_failed_list.append(values)
    df_success = pd.DataFrame(
        {
            "Chemin du fichier": list_success_path,
            "Référence Fiche": list_success_list,
            "lists": list_success_values,
        },
    )
    print(df_success)

    df_failed = pd.DataFrame(
        {"Chemin du fichier": list_failed_path, "lists": list_failed_list},
    )
    print(df_success.shape)
    if nb_passage == 1:
        df_success.to_csv(
            name_file_success,
            sep=";",
            index=False,
            encoding="utf-8-sig",
        )
    else:
        df_success.to_csv(
            name_file_success,
            sep=";",
            mode="a",
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


end = timer()
print(end - start)
