import os
import sys
import pandas as pd
import re
from timeit import default_timer as timer
from fichiers_et_constantes import *


def comparaison_entre_fichier_natifs_et_pdf_darfeuille():
    df_succes = pd.read_csv(
        "output_datas\listes des succes Liaison b_d complet.csv",
        sep=";",
        error_bad_lines=False,
        encoding="utf-8-sig",
    )
    df_darfeuille = pd.read_csv(
        f"input_datas\{str(20221010)}_ExtratTCLDoc complete modifié.csv",
        sep=";",
        error_bad_lines=False,
        encoding="cp1252",
    )
    print(df_succes)
    print(df_succes.shape)
    list_ref = df_darfeuille["REFFIC"].values.tolist()
    for index, row in df_succes.iterrows():
        # print(row)
        print(row["Référence Fiche"])
        if row["Référence Fiche"] in list_ref:
            ind = list_ref.index(row["Référence Fiche"])
            print("ok")
            print(
                f"""{df_darfeuille.loc[index,"REFFIC"]} et {df_darfeuille.loc[index,"LIBSITE"]}"""
            )


comparaison_entre_fichier_natifs_et_pdf_darfeuille()
