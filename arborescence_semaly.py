import os
import sys
import pandas as pd
import re

from pathlib import Path
from timeit import default_timer as timer

start = timer()

DIRNAME = f"""Z:\PDF"""
list_arbo = []

# with open("input_datas/20220410 Bellecour A & D Provisoires.xls") as f:
#     print(f)


def create_arbo():
    """On crée l'arborescence"""
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
        "output_datas/arborescence_semaly_pdf.csv",
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
        "output_datas/arborescence_semaly_pdf.csv",
        sep=";",
        error_bad_lines=False,
        # encoding="utf-8-sig",
        encoding="cp1252",
    )

    df_with_meta = pd.read_csv(
        "output_datas\LISTES URL SEMALY.csv",
        sep=";",
        error_bad_lines=False,
        encoding="cp1252",
    )

    print(df_arbo)
    print(df_with_meta)
    df_meta_listes_url = df_with_meta["Chemin \ modifié"].tolist()
    print(df_meta_listes_url)
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
    # list_ligne = []
    # list_extension = []
    for index, row in df_arbo.iterrows():
        convert_path = row["Chemin modif"]
        # print(convert_path)
        if row["Chemin modif"] in df_meta_listes_url:
            index_list = df_meta_listes_url.index(row["Chemin modif"])
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
            list_success_path.append(row["Chemin modif"])
            list_code_ouvrage.append(df_with_meta.loc[index_list]["Plan"])
            # list_intitule_ouvrage.append(df_with_meta.loc[index_list]["Intitulé Ouvrage"])
            # list_ligne.append(df_with_meta.loc[index_list]["Ligne"])
            # list_extension.append(df_with_meta.loc[index_list]["Extension"])
        else:
            list_failed_path.append(row["Chemin modif"])
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
            # "Ligne": list_ligne,
            # "Extension": list_extension,
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


def comp_between_arbo_and_arborescence_semaly_pdu():
    df_tif = pd.read_csv(
        "output_datas/arborescence_semaly_tif.csv",
        sep=";",
        error_bad_lines=False,
        encoding="utf-8-sig",
    )
    df_semaly_pdu = pd.read_csv(
        "input_datas\Semaly Pierre.csv",
        sep=";",
        error_bad_lines=False,
        encoding="cp1252",
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
    list_intitule_ouvrage = []
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
                list_intitule_ouvrage.append(row_pdu["Intitulé Ouvrage"])
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
                "Intitulé Ouvrage": list_intitule_ouvrage,
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


# create_arbo()
create_file_semaly_pdf()
# comp_between_arbo_and_arborescence_semaly_pdu()

end = timer()
print(end - start)
