import os
import sys
import pandas as pd
import re
import time

from pathlib import Path
from timeit import default_timer as timer
from fichiers_et_constantes import *

start = timer()

list_arbo = []


def create_arbo():
    """On crée l'arborescence"""
    DIRNAME = f"""Z:\PDF"""
    for path, subdirs, files in os.walk(DIRNAME):
        for name in files:
            try:
                print(os.path.join(path, name))
                list_arbo.append(os.path.join(path, name))
            except Exception as e:
                print(e.args)
    df = pd.DataFrame(
        list_arbo,
    )
    df.to_csv(
        ARBO_PDF,
        sep=";",
        index=False,
        encoding="utf-8-sig",
    )


def create_arbo_tif():
    """On crée l'arborescence"""
    # DIRNAME = f"""Z:\TIF\Ligne_A\Bellecour"""
    DIRNAME = f"""Z:\TIF"""
    for path, subdirs, files in os.walk(DIRNAME):
        for name in files:
            try:
                if os.path.join(path, name)[-4:] == ".tif":
                    print(os.path.join(path, name))
                    list_arbo.append(os.path.join(path, name))
                else:
                    pass
            except Exception as e:
                print(e.args)
    df = pd.DataFrame(
        list_arbo,
    )
    df.to_csv(
        ARBO_TIF,
        sep=";",
        index=False,
        encoding="utf-8-sig",
    )


def split_arbo(
    path,
):
    """On formate le format du chemin"""
    return path.split("\\")


def create_file_semaly_pdf():
    df_arbo = pd.read_csv(
        ARBO_PDF,
        sep=";",
        error_bad_lines=False,
        # encoding="utf-8-sig",
        encoding="cp1252",
    )

    df_with_meta = pd.read_csv(
        LISTES_URL_SEMALY,
        sep=";",
        error_bad_lines=False,
        encoding="cp1252",
    )

    # print(df_arbo)
    # print(df_with_meta)
    df_meta_listes_url = []
    # for index_meta, row_meta in df_with_meta.iterrows():
    #     df_meta_listes_url.append(row_meta["Chemin"].upper())
    df_meta_listes_url = df_with_meta["Chemin"].tolist()
    # print(df_meta_listes_url)
    list_success_path = []
    list_failed_path = []
    list_niveau_1 = []
    list_niveau_2 = []
    # list_zone = []
    list_niveau_3 = []
    list_niveau_plans = []
    list_indice = []
    list_libelle = []
    list_code_ouvrage = []
    # list_intitule_ouvrage = []
    list_ligne = []
    list_extension = []
    for index, row in df_arbo.iterrows():
        # print(row["Chemin"])
        # print("df_meta_listes_url", df_meta_listes_url)
        if row["Chemin"].upper() in df_meta_listes_url:
            # print("ok")
            index_list = df_meta_listes_url.index(row["Chemin"].upper())

            # print(df_with_meta.loc[index_list])
            # print("****************************************************************")
            # print(df_with_meta.loc[index_list, "Plan"])
            # print(df_with_meta.loc[index_list]["Plan"])
            list_niveau_1.append(df_with_meta.loc[index_list]["NIVEAU 1"])
            list_niveau_2.append(df_with_meta.loc[index_list]["NIVEAU 2"])
            # list_zone.append(df_with_meta.loc[index_list]["Zone"])
            list_niveau_3.append(df_with_meta.loc[index_list]["NIVEAU 3"])
            list_niveau_plans.append(df_with_meta.loc[index_list]["N° PLAN"])
            list_indice.append(df_with_meta.loc[index_list]["INDICE"])
            list_libelle.append(df_with_meta.loc[index_list]["LIBELLE"])
            list_success_path.append(row["0"])
            list_code_ouvrage.append(df_with_meta.loc[index_list]["Plan"])
            list_ligne.append(df_with_meta.loc[index_list]["Plan"][0])
            list_extension.append("PDF")
            # list_intitule_ouvrage.append(df_with_meta.loc[index_list]["Intitulé Ouvrage"])
            # list_ligne.append(df_with_meta.loc[index_list]["Ligne"])
            # list_extension.append(df_with_meta.loc[index_list]["Extension"])
        else:
            list_failed_path.append(row["Chemin"])
    df_success = pd.DataFrame(
        {
            "NIVEAU 1": list_niveau_1,
            "NIVEAU 2": list_niveau_2,
            # "Zone": list_zone,
            "NIVEAU 3": list_niveau_3,
            "NUM_PLAN": list_niveau_plans,
            "INDICE": list_indice,
            "LIBELLE": list_libelle,
            "Chemin": list_success_path,
            "Code Ouvrage": list_code_ouvrage,
            # "Intitulé Ouvrage": list_intitule_ouvrage,
            "Ligne": list_ligne,
            "Extension": list_extension,
        }
    )

    df_failed = pd.DataFrame(
        {
            "Chemin du fichier": list_failed_path,
        }
    )
    df_success.to_csv(
        "output_datas/listes des succes Semaly PDF.csv",
        sep=";",
        index=False,
        encoding="utf-8-sig",
    )
    df_failed.to_csv(
        "output_datas/listes des echecs Semaly PDF.csv",
        sep=";",
        index=False,
        encoding="utf-8-sig",
    )


def comp_between_arbo_and_arborescence_semaly_pdu():
    print("lunch")
    df_tif = pd.read_csv(
        ARBO_TIF,
        sep=";",
        error_bad_lines=False,
        # encoding="utf-8-sig",
        encoding="cp1252",
    )
    df_with_meta = pd.read_csv(
        "output_datas\listes des succes Semaly PDF.csv",
        sep=";",
        error_bad_lines=False,
        encoding="utf-8-sig",
        # encoding="cp1252",
    )
    print(df_with_meta)
    list_arbo = []
    list_success_path = []
    list_failed_path = []
    list_niveau_1 = []
    list_niveau_2 = []
    list_zone = []
    list_niveau_3 = []
    list_niveau_plans = []
    list_indice = []
    list_libelle = []
    list_code_ouvrage = []
    list_intitule_ouvrage = []
    list_ligne = []
    list_extension = []

    df_meta_listes_url_1 = df_with_meta["Chemin"].values.tolist()
    df_meta_listes_url = [x.upper() for x in df_meta_listes_url_1]
    # print(df_meta_listes_url)
    for index, row in df_tif.iterrows():
        flag = False
        path_origin = row["Chemin coupe"]
        path_tif = path_origin.replace("TIF", "PDF")
        path_tif = path_tif.replace("tif", "pdf")
        # path_tif = path_tif.replace("\\", "\\\\")
        print("path_tif", path_tif.upper())
        # print(row["0"])
        # file_without_letter = path_tif[:-6] + "" + path_tif[-4:]
        reg = re.findall("\W\w{3,}(-.*)\.", path_tif)
        if len(reg) > 0:
            file_without_dash_and_number = path_tif.replace(reg[0], "")
        else:
            file_without_dash_and_number = (
                "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            )
        reg_letter_dash_then_number = re.findall("\W\w{3,}(\w-.*)\.", path_tif)
        if len(reg_letter_dash_then_number) > 0:
            file_without_letter_dash_then_number = path_tif.replace(
                reg_letter_dash_then_number[0], ""
            )
        else:
            file_without_letter_dash_then_number = (
                "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            )
        reg_ = re.findall("\w{3,}(_.*)\.", path_tif)
        if len(reg_) > 0:
            file_without_underscore_and_number = path_tif.replace(
                reg_[0] + ".pdf", ".pdf"
            )
        else:
            file_without_underscore_and_number = (
                "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            )
        reg_letter = re.findall("\d(\D)\.pdf", path_tif)
        # print("reg_letter", reg_letter)
        if len(reg_letter) > 0:
            file_without_letter = path_tif.replace(reg_letter[0] + ".pdf", "")
            print("file_without_letter", file_without_letter)
        else:
            file_without_letter = (
                "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            )

        for list_url in df_meta_listes_url:
            # print("list_url", list_url)
            if (
                path_tif.upper() in list_url
                or file_without_dash_and_number.upper() in list_url
                or file_without_underscore_and_number.upper() in list_url
                or file_without_letter.upper() in list_url
                or file_without_letter_dash_then_number.upper() in list_url
            ):
                # if path_tif.upper() in list_url:
                print("ok", list_url)
                index_list = df_meta_listes_url.index(list_url)
                list_niveau_1.append(df_with_meta.loc[index_list]["NIVEAU 1"])
                list_niveau_2.append(df_with_meta.loc[index_list]["NIVEAU 2"])
                # list_zone.append(df_with_meta.loc[index_list]["Zone"])
                list_niveau_3.append(df_with_meta.loc[index_list]["NIVEAU 3"])
                list_niveau_plans.append(df_with_meta.loc[index_list]["NUM_PLAN"])
                list_indice.append(df_with_meta.loc[index_list]["INDICE"])
                list_libelle.append(df_with_meta.loc[index_list]["LIBELLE"])
                list_success_path.append(path_origin)
                # list_success_path.append(row["Chemin modif"])
                list_code_ouvrage.append(df_with_meta.loc[index_list]["Code Ouvrage"])
                # list_intitule_ouvrage.append(df_with_meta.loc[index_list]["Intitulé Ouvrage"])
                list_ligne.append(df_with_meta.loc[index_list]["Code Ouvrage"][0])
                list_extension.append("TIF")
                # list_extension.append(df_with_meta.loc[index_list]["Extension"])
                # else:
                #     print("non")
                #     list_failed_path.append(row["0"])
                flag = True
                break
            elif (
                path_tif.upper().replace("0", "").replace(" ", "")
                in list_url.replace("0", "").replace(" ", "")
                or file_without_dash_and_number.upper()
                .replace("0", "")
                .replace(" ", "")
                in list_url.replace("0", "").replace(" ", "")
                or file_without_underscore_and_number.upper()
                .replace("0", "")
                .replace(" ", "")
                in list_url.replace("0", "").replace(" ", "")
                or file_without_letter.upper().replace("0", "").replace(" ", "")
                in list_url.replace("0", "").replace(" ", "")
            ):
                # if path_tif.upper() in list_url:
                # print("ok", list_url)
                index_list = df_meta_listes_url.index(list_url)
                list_niveau_1.append(df_with_meta.loc[index_list]["NIVEAU 1"])
                list_niveau_2.append(df_with_meta.loc[index_list]["NIVEAU 2"])
                # list_zone.append(df_with_meta.loc[index_list]["Zone"])
                list_niveau_3.append(df_with_meta.loc[index_list]["NIVEAU 3"])
                list_niveau_plans.append(df_with_meta.loc[index_list]["NUM_PLAN"])
                list_indice.append(df_with_meta.loc[index_list]["INDICE"])
                list_libelle.append(df_with_meta.loc[index_list]["LIBELLE"])
                list_success_path.append(path_origin)
                # list_success_path.append(row["Chemin modif"])
                list_code_ouvrage.append(df_with_meta.loc[index_list]["Code Ouvrage"])
                # list_intitule_ouvrage.append(df_with_meta.loc[index_list]["Intitulé Ouvrage"])
                list_ligne.append(df_with_meta.loc[index_list]["Code Ouvrage"][0])
                list_extension.append("TIF")
                # list_extension.append(df_with_meta.loc[index_list]["Extension"])
                # else:
                #     print("non")
                #     list_failed_path.append(row["0"])
                flag = True
                break

            else:
                pass
                # print("pas ok")
        if not flag:
            # print("Pas bon")
            # print("path_tif echecs", path_tif)
            # print(
            #     f"{file_without_dash_and_number.upper()} , {file_without_underscore_and_number.upper()}, {file_without_letter.upper()} "
            # )

            list_failed_path.append(path_origin)
        df_success = pd.DataFrame(
            {
                "NIVEAU 1": list_niveau_1,
                "NIVEAU 2": list_niveau_2,
                # "Zone": list_zone,
                "NIVEAU 3": list_niveau_3,
                "NUM_PLAN": list_niveau_plans,
                "INDICE": list_indice,
                "LIBELLE": list_libelle,
                "Chemin": list_success_path,
                "Code Ouvrage": list_code_ouvrage,
                # "Intitulé Ouvrage": list_intitule_ouvrage,
                "Ligne": list_ligne,
                "Extension": list_extension,
            }
        )

        df_failed = pd.DataFrame(
            {
                "Chemin du fichier": list_failed_path,
            }
        )
        df_success.to_csv(
            "output_datas/listes des succes Semaly TIF.csv",
            sep=";",
            index=False,
            encoding="utf-8-sig",
        )
        df_failed.to_csv(
            "output_datas/listes des echecs Semaly TIF.csv",
            sep=";",
            index=False,
            encoding="utf-8-sig",
        )


create_arbo()
create_file_semaly_pdf()
create_arbo_tif()
comp_between_arbo_and_arborescence_semaly_pdu()

# end = timer()
# print(end - start)
