"""
Ce script permet la copie des fichiers en echecs sur un autre serveur afin de ne pas ralentir la migration, dans un but de les traiter petit à petit dans un futur proche
"""

import os
import shutil
import pandas as pd
from distutils.dir_util import copy_tree

df = pd.read_csv(
    "output_datas\listes des echecs ligne T1 Perrache Montrochet.csv",
    sep=";",
    error_bad_lines=False,
    encoding="utf-8-sig",
)
list_of_path = df["Chemin du fichier"].tolist()


for i in list_of_path:
    try:
        dest = "output_datas\copy"

        print("i", i)
    except Exception as e:
        print(e.args)
