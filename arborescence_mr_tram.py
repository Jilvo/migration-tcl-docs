import os, time
import sys
import pandas as pd
import re
from fichiers_et_constantes import *


def split_arbo(
    path,
):
    """On formate le format du chemin"""
    return path.split("\\")


def create_arbo():
    """On crée l'arborescence"""
    list_arbo = []
    list_file_name = []
    list_plan = []
    list_indice = []
    list_titre = []
    list_format = []
    list_time = []
    for path, subdirs, files in os.walk(DIRNAME_MRTRAM):
        for name in files:
            try:
                if (
                    not "Thumbs" in os.path.join(path, name)
                    and "." in os.path.join(path, name)[-5:]
                ):
                    # print(os.path.join(path, name))

                    # Référence
                    path_modify = os.path.join(path, name).replace(
                        "H:", "K:\INT-SVLY-NASPROD2\Doc_Terrain_tram"
                    )
                    list_split = split_arbo(path_modify)
                    list_arbo.append(path_modify)
                    ref = list_split[-1]
                    list_file_name.append(ref)

                    # Indice
                    # print("ref debut", ref)
                    # indice = indice[0]
                    # print("indice", indice)
                    try:
                        # print("ici")
                        indice = re.findall("-(\D{1}\d*.?\d*)_", ref)
                        indice = indice[0]
                        print(indice)
                        list_indice.append(indice)
                        ref = ref.replace("-" + indice, "")
                    except Exception as e:

                        if "_Indice_" in ref:
                            indice = re.findall("_Indice_(.*)[.]", ref)
                            indice = indice[0]
                            list_indice.append(indice)
                            ref = ref.replace("_Indice_" + indice, "")
                        else:
                            list_indice.append(" ")

                    # Titre
                    if re.match("^[^_]+(?=_)", ref):
                        if "Nomenclature" in ref:
                            titre = re.findall("^[^_]+(?=_)", ref)
                            titre = titre[0]
                            list_titre.append(titre)
                            ref = ref.replace(titre, "")

                            plan = re.findall("_(.*)[.]", ref)
                            plan = plan[0]
                            list_plan.append(plan)
                            ref = ref.replace(plan, "")
                        else:
                            titre = re.findall("_(.*)[.]", ref)
                            titre2 = titre[0]
                            list_titre.append(titre2)
                            ref = ref.replace(titre2, "")

                            plan = re.findall("^[^_]+(?=_)", ref)
                            plan = plan[0]
                            list_plan.append(plan)
                            ref = ref.replace(plan, "")
                    else:
                        if len(ref) < 7:
                            plan = re.findall("(.*)[.]", ref)
                            plan = plan[0]
                            list_plan.append(plan)
                            list_titre.append(" ")
                        else:
                            titre = re.findall("(.*)[.]", ref)
                            titre2 = titre[0]
                            list_titre.append(titre2)
                            list_plan.append(" ")

                    # Plan

                    # Format
                    # print("ref avant format fichir", ref)

                    format = re.findall("[.](.*)", ref)
                    format = format[0]
                    list_format.append(format)
                    ref = ref.replace(format, "")
                    # date
                    modTimesinceEpoc = os.path.getmtime(os.path.join(path, name))
                    modificationTime = time.strftime(
                        "%d-%m-%Y %H:%M", time.localtime(modTimesinceEpoc)
                    )
                    list_time.append(modificationTime)
                else:
                    pass
            except Exception as e:
                print(e.args)
    print(len(list_arbo))
    print(len(list_file_name))
    print(len(list_plan))
    print(len(list_indice))
    print(len(list_titre))
    print(len(list_format))
    print(len(list_time))
    df = pd.DataFrame(
        {
            "Chemin": list_arbo,
            "Reference": list_file_name,
            "Plan": list_plan,
            "Indice": list_indice,
            "Titre": list_titre,
            "Format": list_format,
            "Date": list_time,
        }
    )

    df.to_csv(
        NOM_FICHIER_SORTIE_MR_TRAM,
        sep=";",
        index=False,
        encoding="utf-8-sig",
    )


def comp_between_arbo_and_arborescence_mr_tram_pdu():
    df_t1_t2 = pd.read_csv(
        "output_datas/arborescence_mr_tram.csv",
        sep=";",
        error_bad_lines=False,
        encoding="utf-8-sig",
    )
    df_mr_tram_meta = pd.read_csv(
        METADONNES_MR_TRAM,
        sep=";",
        error_bad_lines=False,
        encoding="cp1252",
    )
    list_success_path = []
    list_time_path = []
    list_file_name = []
    # list_failed_path = []
    # print(df_t1_t2["0"][0])
    # print(df_mr_tram_pdu["Chemin"][0])
    list_reference = df_mr_tram_meta["Reference"].values.tolist()
    list_reference_date = df_t1_t2["Date"].values.tolist()
    list_path_link = df_t1_t2["Chemin"].values.tolist()
    # for key, value in enumerate(list_df_mrtram):
    #     # update_value = value.replace(" ", "")
    #     # update_value = re.findall("^(.+)\.", update_value)
    #     # update_value = update_value[0]
    #     # update_value = update_value.replace(".", "")
    #     list_df_mrtram[key] = value
    print("list_reference", list_reference)
    # print(df_mr_tram_pdu["Chemin"].values.tolist())
    for index, row in df_t1_t2.iterrows():
        flag = False
        path_origin = row["Chemin"]
        path_modify = path_origin.replace("H:", "K:\INT-SVLY-NASPROD2\Doc_Terrain_tram")
        print("path_modif", path_modify)
        list_split = split_arbo(path_modify)
        file_name = list_split[-1]
        # for index_meta, row_meta in df_mr_tram_meta.iterrows():

        # path_modify = path_modify.replace(" ", "")
        # path_modify = re.findall("^(.+)\.", path_modify)
        # path_modify = path_modify[0]
        # path_modify = path_modify.replace(".", "")
        # print(row["0"])
        if file_name in list_reference:
            print("ok", file_name)
            inde = list_path_link.index(path_origin)
            print(list_path_link.index(file_name))
            list_success_path.append(path_modify)
            list_time_path.append(list_reference_date[inde])
            list_file_name.append(file_name)

        # if path_modify in row_meta["Reference"]:
        #     # print("ok")
        #     flag = True
        #     list_success_path.append(path_modify)
        #     list_time_path.append(row["Date"])
        #     list_file_name.append(file_name)
        if flag == False:
            list_success_path.append(path_modify)
    df_success = pd.DataFrame(
        {
            "Chemin": list_success_path,
            "Reference": list_file_name,
            "Date": list_time_path,
        }
    )

    df_failed = pd.DataFrame(
        {
            "Chemin du fichier": list_failed_path,
        }
    )

    df_success.to_csv(
        "output_datas/listes des succes MR TRAM T1T2.csv",
        sep=";",
        index=False,
        encoding="utf-8-sig",
    )
    df_failed.to_csv(
        "output_datas/listes des echecs MR TRAM T1T2.csv",
        sep=";",
        index=False,
        encoding="utf-8-sig",
    )
    print(df_success)


# def comp_between_arbo_and_arborescence_mr_tram_t5_t6():
#     pass


create_arbo()
# comp_between_arbo_and_arborescence_mr_tram_pdu()
