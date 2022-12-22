import os
import sys
import pandas as pd
from fichiers_et_constantes import *
import collections
import glob

dirpath = f"F:\Tcl\{str(210)} à {str(213)} - Métro C - stations\Croix-Paquet"
DIRNAME = [
    # f"""X:""",
    # f"""F:\Tcl\{str(0)}01 - Métro - communs""",
    # f"""F:\Tcl\Prêt Plans\Prêt 2017""",
    # f"""F:\Tcl\Prêt Plans""",
    # f"""F:\Tcl\Prêt Plans\Prêt 2018""",
    # f"""F:\Tcl\Prêt Plans\Prêt 2019""",
    # f"""F:\Tcl\{str(0)}02 - Métro ABC - communs""",
    # f"""F:\Tcl\{str(0)}03 - Métro AB - communs""",
    # f"""F:\Tcl\{str(100)} - Métro A - communs""",
    # # f"""F:\Tcl\{str(101)} - Métro A - interstations""",
    # f"""F:\Tcl\{str(102)} - Métro B - communs""",
    # # f"""F:\Tcl\{str(103)} - Métro B - interstations""",
    # f"""F:\Tcl\{str(105)} à {str(122)} - Métro A - stations""",
    # f"""F:\Tcl\{str(130)} à {str(137)} - Métro B - stations""",
    # # f"""F:\Tcl\{str(200)} - Métro C - communs""",
    # # f"""F:\Tcl\{str(201)} - Métro C - interstations""",
    # f"""F:\Tcl\{str(210)} à {str(213)} - Métro C - stations""",
    f"""F:\Tcl\{str(210)} à {str(213)} - Métro C - stations\Croix-Paquet""",
    # # f"""F:\Tcl\{str(300)} - Métro D - communs""",
    # # f"""F:\Tcl\{str(301)} - Métro D - interstations""",
    # # f"""F:\Tcl\{str(302)} - Funiculaires - communs""",
    # # f"""F:\Tcl\{str(303)} - Liaison BD""",
    # # f"""F:\Tcl\{str(305)} à {str(322)} - Métro D - stations""",
    # # f"""F:\Tcl\{str(330)} à {str(332)} - Funiculaires - stations""",
    # # f"""F:\Tcl\{str(500)} - Tramway - communs""",
    # # f"""F:\Tcl\{str(500)} - Tramway Rhone Express - communs""",
    # # f"""F:\Tcl\{str(500)} - Tramway T1 - communs""",
    # # f"""F:\Tcl\{str(500)} - Tramway T2 - communs""",
    # # f"""F:\Tcl\{str(500)} - Tramway T3 - communs""",
    # f"""F:\Tcl\{str(500)} - Tramway T4 - communs""",
    # f"""F:\Tcl\{str(800)} à {str(843)} - Surface\{str(0)}0 Ligne Aérienne Trolleybus""",
    # f"""F:\Tcl\{str(800)} à {str(843)} - Surface\{str(0)}0 Ligne Aérienne Trolleybus""",
    # f"""F:\Tcl\{str(800)} à {str(843)} - Surface\{str("U")}nités de Transport""",
    # f"""F:\Tcl\{str(500)} - Tramway T5 - communs""",
    # f"""F:\Tcl\{str(500)} - Tramway T6 - communs""",
    # f"""F:\Tcl\{str(501)} - Tramway T1 - stations""",
    # f"""F:\Tcl\{str(501)} - Tramway T2 - stations""",
    # f"""F:\Tcl\{str(501)} - Tramway T3 - stations""",
    # f"""F:\Tcl\{str(501)} - Tramway T4 - stations""",
    # f"""F:\Tcl\{str(501)} - Tramway T5 - stations""",
    # f"""F:\Tcl\{str(501)} - Tramway T6 - stations""",
    # f"""F:\Tcl\{str(800)} à {str(843)} - Surface""",
    # f"""F:\Tcl\{str(900)} - Lignes Fortes - C1 C2 C3 C13""",
]
length = 0
length_dwg = 0
length_see = 0
length_pdf = 0
length_topo = 0
list_arbo = []
list_dossier = []
error = 0
print(
    "Vous voulez savoir le nombre de fichiers, de DWG,PDF,SEE et Topo dans un ou plusieurs dossiers. "
)
flag = False
# while not flag:
#     print("Vous voulez ajouter un dossier ?")
#     input_choice = input("O / N : ")
#     if input_choice.upper() == "O":
#         path = str(input("Entrez le nom du dossier : "))
#         list_dossier.append(path)
#     elif input_choice.upper() == "N":
#         flag = True
#     else:
#         print("Je ne comprend pas votre réponse, réessayez ")

# # print("list_dossier", list_dossier)
# for dir in DIRNAME:
#     # for dir in list_dossier:
#     # print(dir)
#     # for dir in DIRNAME:
#     for path, subdirs, files in os.walk(dir):
#         # print(path)
#         for name in files:
#             try:
#                 print("AFTER ", os.path.join(path, name))
#                 length += 1
#                 list_arbo.append(os.path.join(path, name))
#                 if os.path.join(path, name)[-4:] == ".dwg":
#                     length_dwg += 1
#                     if length_dwg % 10 == 0:
#                         print("actual length dwg: ", length_dwg)
#                 if os.path.join(path, name)[-4:] == ".pdf":
#                     length_pdf += 1
#                     if length_pdf % 10 == 0:
#                         print("actual length pdf: ", length_pdf)
#                 if os.path.join(path, name)[-4:] == ".see":
#                     length_see += 1
#                     if length_see % 10 == 0:
#                         print("actual length see: ", length_see)
#                 if os.path.join(path, name)[-8:] == "Topo.dwg":
#                     length_topo += 1
#                     if length_topo % 10 == 0:
#                         print("actual length see: ", length_topo)
#             except Exception as e:
#                 error += 1
extensions = collections.defaultdict(int)

for path, dirs, files in os.walk(f"F:\Tcl"):
    print(path)
    for filename in files:
        extensions[os.path.splitext(filename)[1].lower()] += 1

for key, value in extensions.items():
    print("Extension: ", key, " ", value, " items")
dict_extension = dict(extensions)
print(dict_extension)
df = pd.DataFrame(dict_extension.items())
df.to_csv(
    "output_datas\liste_extension.csv",
    sep=";",
    index=False,
    encoding="utf-8-sig",
)


# print("Total length = ", length)
# print("Total length DWG FILES = ", length_dwg)
# print("Total length SEE FILES = ", length_see)
# print("Total length PDf FILES = ", length_pdf)
# print("Total length Topo FILES = ", length_topo)
# print("Total error = ", error)
