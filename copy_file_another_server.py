"""
Ce script permet la copie des fichiers en echecs sur un autre serveur afin de ne pas ralentir la migration, dans un but de les traiter petit à petit dans un futur proche
"""

import os
import shutil
import pandas as pd

df = pd.read_csv(
    "output_datas\listes des echecs ligne T1 Perrache Montrochet.csv",
    sep=";",
    error_bad_lines=False,
    encoding="utf-8-sig",
)
list_of_path = df["Chemin du fichier"].tolist()


for i in list_of_path:
    try:
        # dest = os.path.join("output_datas\copy", str(i)[2:])
        print("i", i)
        # print("dest", dest)
        # dstfolder = os.path.dirname(dest)
        # if not os.path.exists(dstfolder):
        #     os.makedirs(dstfolder)
        # shutil.copy(str(i), dest)
        # print("File copied successfully.")
        shutil.copytree(i, r"output_datas\copy")
    except Exception as e:
        print(e.args)
