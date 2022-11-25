"""
Ce script permet la copie des fichiers en echecs sur un autre serveur afin de ne pas ralentir la migration, dans un but de les traiter petit à petit dans un futur proche
"""

import os
import shutil
import pandas as pd
import distutils.dir_util
import re
from fichiers_et_constantes import *
from pathlib import Path

df = pd.read_csv(
    FICHIER_ECHECS_A_COPIER_SUR_AUTRE_SERVEUR,
    sep=";",
    error_bad_lines=False,
    encoding="cp1252",  # encoding="utf-8-sig",
)
list_of_path = df["Chemin du fichier"].tolist()

list_why_errors = []
list_echecs = []
for i in list_of_path:
    try:
        path = re.findall("(.*)\\\\", i)
        path_cut = path[0]
        path_cut = path_cut.replace("F:\\", "")
        file = i.replace(path[0], "")
        file = file.replace("\\", "")
        dest_path = DESTINATION_FICHIERS_COPIE + "/" + path_cut
        path_cut = "/" + path_cut
        path = Path(dest_path)
        path.mkdir(parents=True, exist_ok=True)
        destination_file = dest_path + "/" + file
        shutil.copy(i, destination_file)

    except Exception as e:
        print(destination_file)
        list_echecs.append(destination_file)
        list_why_errors.append(e.args)

    df = pd.DataFrame(
        {
            "Chemin du fichier": list_echecs,
            "Raisons Erreurs": list_why_errors,
        }
    )

    df.to_csv(
        "output_datas/erreurs_copies_fichiers_echecs.csv",
        sep=";",
        index=False,
        encoding="utf-8-sig",
    )
    # except Exception as e:
    #     print(e.args)
