"""
Ce script permet la copie des fichiers en echecs sur un autre serveur afin de ne pas ralentir la migration, dans un but de les traiter petit à petit dans un futur proche
"""

import os
import shutil
import pandas as pd
import distutils.dir_util
import re
from pathlib import Path

df = pd.read_csv(
    "output_datas\listes des echecs ligne T1 Perrache Montrochet.csv",
    sep=";",
    error_bad_lines=False,
    encoding="cp1252",  # encoding="utf-8-sig",
)
list_of_path = df["Chemin du fichier"].tolist()


for i in list_of_path:
    try:
        path = re.findall("(.*)\\\\", i)
        path_cut = path[0]
        path_cut = path_cut.replace("F:\\", "")
        file = i.replace(path[0], "")
        file = file.replace("\\", "")
        dest = "output_datas/copy"
        dest_path = dest + "/" + path_cut
        path_cut = "/" + path_cut
        path = Path(dest_path)
        path.mkdir(parents=True)
        destination_file = dest_path + "/" + file
        shutil.copy(i, destination_file)
    except Exception as e:
        print(e.args)