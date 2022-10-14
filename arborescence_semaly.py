import os
import sys
import pandas as pd
import re

from pathlib import Path
from timeit import default_timer as timer

start = timer()

DIRNAME = f"""Z:\TIF"""
list_arbo = []

# with open("input_datas/20220410 Bellecour A & D Provisoires.xls") as f:
#     print(f)


def create_arbo():
    """On crée l'arborescence"""
    for path, subdirs, files in os.walk(DIRNAME_SERBER):
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
        "output_datas\arborescence_semaly_tif.csv",
        sep="\t",
        index=False,
        encoding="utf-8-sig",
    )


def split_arbo(
    path,
):
    """On formate le format du chemin"""
    return path.split("\\")


def comp_between_arbo_and_arborescence_semaly_pdu():
    df_tif = pd.read_csv(
        "output_datas/arborescence_semaly_tif.csv",
        sep=";",
        error_bad_lines=False,
        encoding="utf-8-sig",
    )
    df_semaly_pdu = pd.read_csv(
        "input_datas\Semaly.csv", sep=";", error_bad_lines=False, encoding="cp1252"
    )
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
    list_ligne = []
    list_extension = []
    print(df_tif)
    print(df_semaly_pdu)
    print(df_semaly_pdu["Chemin"][0])
    for index, row in df_tif.iterrows():
        path_origin = row[0]
        path_tif = path_origin.replace("TIF", "PDF")
        path_tif = path_tif.replace("tif", "pdf")
        path_tif = path_tif.replace("Z:", "K:\INT-Sply-pat\Plans Numerises")
        print(path_tif)
        path_to_check = Path(path_tif)
        for index_pdu, row_pdu in df_semaly_pdu.iterrows():
            if path_tif == row_pdu["Chemin"]:
                print("TROUVE", path_tif)
                print("le fichier existe", path_to_check)
                list_niveau_1.append(row_pdu["NIVEAU 1"])
                list_niveau_2.append(row_pdu["NIVEAU 2"])
                list_zone.append(row_pdu["Zone"])
                list_niveau_3.append(row_pdu["NIVEAU 3"])
                list_niveau_plans.append(row_pdu["NUM_PLAN"])
                list_indice.append(row_pdu["INDICE"])
                list_libelle.append(row_pdu["LIBELLE"])
                list_success_path.append(path_to_check)
                list_code_ouvrage.append(row_pdu["Code Ouvrage"])
                list_ligne.append(row_pdu["Ligne"])
                list_extension.append(row_pdu["Extension"])
            else:
                # list_failed_path.append(path_to_check)
                pass
        df_success = pd.DataFrame(
            {
                "NIVEAU 1": list_niveau_1,
                "NIVEAU 2": list_niveau_2,
                "Zone": list_zone,
                "NIVEAU 3": list_niveau_3,
                "NUM_PLAN": list_niveau_plans,
                "INDICE": list_indice,
                "LIBELLE": list_libelle,
                "Chemin": list_success_path,
                "Code Ouvrage": list_code_ouvrage,
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
            "output_datas/listes des succes Semaly TIF into PDF.csv",
            sep=";",
            index=False,
            encoding="utf-8-sig",
        )
        df_failed.to_csv(
            "output_datas/listes des echecs Semaly TIF into PDF.csv",
            sep=";",
            index=False,
            encoding="utf-8-sig",
        )


# def create_arbo():
#     """On crée l'arborescence"""
#     list_arbo = []
#     list_success_path = []
#     list_failed_path = []
#     list_niveau_1 = []
#     list_niveau_2 = []
#     list_zone = []
#     list_niveau_3 = []
#     list_niveau_plans = []
#     list_indice = []
#     list_libelle = []
#     list_code_ouvrage = []
#     list_ligne = []
#     list_extension = []
#     df = pd.read_csv(
#         "input_datas\Semaly.csv", sep=";", error_bad_lines=False, encoding="cp1252"
#     )
#     print(df)
#     # print(df["Chemin"])
#     count = 0
#     for index, row in df.iterrows():
#         count += 1
#         print(count)
#         path_origin = row["Chemin"]
#         path_tif = path_origin.replace("PDF", "TIF")
#         path_tif = path_tif.replace("pdf", "tif")
#         path_tif = path_tif.replace("K:\INT-Sply-pat\Plans Numerises", "Z:")
#         print("APRES", path_tif)
#         path_to_check = Path(path_tif)
#         if path_to_check.is_file():
#             print("le fichier existe", path_to_check)
#             list_niveau_1.append(row["NIVEAU 1"])
#             list_niveau_2.append(row["NIVEAU 2"])
#             list_zone.append(row["Zone"])
#             list_niveau_3.append(row["NIVEAU 3"])
#             list_niveau_plans.append(row["NUM_PLAN"])
#             list_indice.append(row["INDICE"])
#             list_libelle.append(row["LIBELLE"])
#             list_success_path.append(path_to_check)
#             list_code_ouvrage.append(row["Code Ouvrage"])
#             list_ligne.append(row["Ligne"])
#             list_extension.append(row["Extension"])
#         else:
#             list_failed_path.append(path_to_check)
#             # print("Le fichier existe pas", path_to_check)
#             pass
#         df_success = pd.DataFrame(
#             {
#                 "NIVEAU 1": list_niveau_1,
#                 "NIVEAU 2": list_niveau_2,
#                 "Zone": list_zone,
#                 "NIVEAU 3": list_niveau_3,
#                 "NUM_PLAN": list_niveau_plans,
#                 "INDICE": list_indice,
#                 "LIBELLE": list_libelle,
#                 "Chemin": list_success_path,
#                 "Code Ouvrage": list_code_ouvrage,
#                 "Ligne": list_ligne,
#                 "Extension": list_extension,
#             }
#         )

#         df_failed = pd.DataFrame(
#             {
#                 "Chemin du fichier": list_failed_path,
#             }
#         )
#         df_success.to_csv(
#             "output_datas/listes des succes Semaly TIF into PDF.csv",
#             sep=";",
#             index=False,
#             encoding="utf-8-sig",
#         )
#         df_failed.to_csv(
#             "output_datas/listes des echecs Semaly TIF into PDF.csv",
#             sep=";",
#             index=False,
#             encoding="utf-8-sig",
#         )

#     # for path, subdirs, files in os.walk(DIRNAME):
#     #     for name in files:
#     #         try:
#     #             print(os.path.join(path, name))
#     #             list_arbo.append(os.path.join(path, name))
#     #         except Exception as e:
#     #             print(e.args)
#     # df = pd.DataFrame(
#     #     list_arbo,
#     # )
#     # df.to_csv(
#     #     "output_datas/arborescence_semaly.csv",
#     #     sep="\t",
#     #     index=False,
#     #     encoding="utf-8-sig",
#     # )


# create_arbo()
comp_between_arbo_and_arborescence_semaly_pdu()

end = timer()
print(end - start)
