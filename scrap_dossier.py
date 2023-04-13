import os
import sys
import pandas as pd
from fichiers_et_constantes import *
import collections
import glob


# for path, dirs, files in os.walk(f"F:\Tcl"):
#     print(path)
#     for filename in files:
#         extensions[os.path.splitext(filename)[1].lower()] += 1

# for key, value in extensions.items():
#     print("Extension: ", key, " ", value, " items")
# dict_extension = dict(extensions)
# print(dict_extension)
# df = pd.DataFrame(dict_extension.items())
# df.to_csv(
#     "output_datas\liste_extension.csv",
#     sep=";",
#     index=False,
#     encoding="utf-8-sig",
# )


root_path = "F:\Tcl"
# root_path = f"""F:\Tcl\{str(1)}05 à 122 - Métro A - stations"""

visited_dirs = set()  # ensemble pour éviter les doublons

for dirpath, dirnames, filenames in os.walk(root_path):
    # détermine la profondeur actuelle en comptant le nombre de répertoires parents
    depth = dirpath.count(os.path.sep) - root_path.count(os.path.sep)
    if depth <= 1:  # ne va pas plus loin que 2 sous-dossiers
        for dirname in dirnames:
            full_path = os.path.join(dirpath, dirname)
            if full_path not in visited_dirs:  # évite les doublons
                if full_path[-1] not in [
                    "0",
                    "1",
                    "2",
                    "3",
                    "4",
                    "5",
                    "6",
                    "7",
                    "8",
                    "9",
                ]:
                    visited_dirs.add(full_path)
                    print(full_path)
df = pd.DataFrame(visited_dirs)
df.to_csv(
    "output_datas\liste_des_sous_dossiers.csv",
    sep=";",
    index=False,
    encoding="utf-8-sig",
)
