import os
import sys
import pandas as pd
import re
from timeit import default_timer as timer

start = timer()

# file = f"F:\Tcl\{str(105)} à 122 - Métro A - stations\Foch\800E100\800E100.pdf"


def split_arbo(
    path,
):
    """On formate le format du chemin"""
    return path.split("\\")


def get_station():
    list_files = [
        f"F:\Tcl\{str(105)} à 122 - Métro A - stations\Foch\800E100\800E100.pdf",
        f"F:\Tcl\{str(100)} - Métro A - communs\HF011822\HF11822.tif",
        f"F:\Tcl\{str(101)} - Métro A - interstations\00 Documentation Technique\00 Amiante et Plomb\002EP001443\Liaison Massena_Foch_002EP001443.pdf",
    ]
    df = pd.read_csv(
        "input_datas/listes_arrets_lignes.csv",
        encoding="cp1252",
        sep=";",
    )

    dict_stations = {}
    for site, doss in zip(
        df["Site"].values.tolist(), df["Nom Dossier"].values.tolist()
    ):
        dict_stations[doss] = site
    # print(df["Site"].values.tolist())
    # print(df["Nom Dossier"].values.tolist())
    print(dict_stations)
    for i in list_files:
        list_path = split_arbo(i)
        print("LISTE", list_path)
        if "communs" in list_path[2]:
            print("c'est une communs", list_path)
        elif "interstations" in list_path[2]:
            print("c'est une interstations", list_path)
            continue
        if "stations" in list_path[2]:
            print("la station est ", list_path[3])
            if list_path[3].upper() in df["Site"].values.tolist():
                pass
            print("c'est une station", list_path)


get_station()
