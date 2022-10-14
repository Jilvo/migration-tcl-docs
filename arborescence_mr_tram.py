import os
import sys
import pandas as pd
import re
from timeit import default_timer as timer

start = timer()

DIRNAME_MRTRAM = (
    f"""H:\MR tramway\{str(0)}0 Documentation de conception T1T2 02042009"""
)
list_arbo = []


def create_arbo():
    """On crée l'arborescence"""
    for path, subdirs, files in os.walk(DIRNAME_MRTRAM):
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
        "output_datas/arborescence_mr_tram.csv",
        sep="\t",
        index=False,
        encoding="utf-8-sig",
    )


def split_arbo(
    path,
):
    """On formate le format du chemin"""
    return path.split("\\")


def comp_between_arbo_and_arborescence_mr_tram_pdu():
    df_t1_t2 = pd.read_csv(
        "output_datas/arborescence_mr_tram.csv",
        sep=";",
        error_bad_lines=False,
        encoding="utf-8-sig",
    )
    df_mr_tram_pdu = pd.read_csv(
        "input_datas\T1T2.csv", sep=";", error_bad_lines=False, encoding="cp1252"
    )
    list_success_path = []
    list_failed_path = []
    print(df_t1_t2["0"][0])
    print(df_mr_tram_pdu["Chemin"][0])
    list_df_mrtram = df_mr_tram_pdu["Chemin"].values.tolist()
    for key, value in enumerate(list_df_mrtram):
        update_value = value.replace(" ", "")
        update_value = re.findall("^(.+)\.", update_value)
        update_value = update_value[0]
        update_value = update_value.replace(".", "")
        list_df_mrtram[key] = update_value
    print(list_df_mrtram)
    # print(df_mr_tram_pdu["Chemin"].values.tolist())
    for index, row in df_t1_t2.iterrows():
        path_origin = row["0"]
        path_modify = path_origin.replace("H:", "K:\INT-SVLY-NASPROD2\Doc_Terrain_tram")
        path_modify = path_modify.replace(" ", "")
        path_modify = re.findall("^(.+)\.", path_modify)
        path_modify = path_modify[0]
        path_modify = path_modify.replace(".", "")
        # print(row["0"])

        if path_modify in list_df_mrtram:
            # print("ok")
            list_success_path.append(path_modify)
        else:
            list_failed_path.append(path_modify)
            # for index, row in df_t1_t2.iterrows():
            #     print(row["0"])

    df_success = pd.DataFrame(
        {
            "Chemin": list_success_path,
        }
    )

    df_failed = pd.DataFrame(
        {
            "Chemin du fichier": list_failed_path,
        }
    )

    df_success.to_csv(
        "output_datas/listes des succes MR TRAM.csv",
        sep=";",
        index=False,
        encoding="utf-8-sig",
    )
    df_failed.to_csv(
        "output_datas/listes des echecs MR TRAM.csv",
        sep=";",
        index=False,
        encoding="utf-8-sig",
    )
    print(df_success)


# create_arbo()
comp_between_arbo_and_arborescence_mr_tram_pdu()

end = timer()
print(end - start)
