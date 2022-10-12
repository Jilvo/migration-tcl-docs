import os
import sys
import pandas as pd
import re
from pathlib import Path
from timeit import default_timer as timer

start = timer()

DIRNAME = f"""Z:\PDF"""

with open("input_datas/20220410 Bellecour A & D Provisoires.xls") as f:
    print(f)


def create_arbo():
    """On crée l'arborescence"""
    list_arbo = []
    list_success_path = []
    list_failed_path = []
    df = pd.read_csv(
        "input_datas\Semaly.csv", sep=";", error_bad_lines=False, encoding="cp1252"
    )
    print(df)
    # print(df["Chemin"])
    for index, row in df.iterrows():
        path_origin = row["Chemin"]
        path_tif = path_origin.replace("PDF", "TIF")
        path_tif = path_tif.replace("pdf", "tif")
        path_tif = path_tif.replace("K:\INT-Sply-pat\Plans Numerises", "Z:")
        print("APRES", path_tif)
        path_to_check = Path(path_tif)
        if path_to_check.is_file():
            print("le fichier existe", path_to_check)
            list_success_path.append(path_to_check)
        else:
            list_failed_path.append(path_to_check)
            # print("Le fichier existe pas", path_to_check)
            pass
        df_success = pd.DataFrame(
            {
                "Chemin du fichier": list_success_path,
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

    # for path, subdirs, files in os.walk(DIRNAME):
    #     for name in files:
    #         try:
    #             print(os.path.join(path, name))
    #             list_arbo.append(os.path.join(path, name))
    #         except Exception as e:
    #             print(e.args)
    # df = pd.DataFrame(
    #     list_arbo,
    # )
    # df.to_csv(
    #     "output_datas/arborescence_semaly.csv",
    #     sep="\t",
    #     index=False,
    #     encoding="utf-8-sig",
    # )


# create_arbo()

end = timer()
print(end - start)
