import os
import sys
import pandas as pd
from fichiers_et_constantes import *
import collections
import glob

# dirpath = f"F:\Tcl\{str(210)} à {str(213)} - Métro C - stations\Croix-Paquet"
DIRNAME = [
    # f"""X:""",
    f"""F:\Tcl""",
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
    # f"""F:\Tcl\{str(210)} à {str(213)} - Métro C - stations\Croix-Paquet""",
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
list_carac = [
    "<",
    ">",
    ":",
    "«",
    "|",
    "?",
    "*",
    ".",
    "&",
    "/",
    "+",
    "%",
    ")",
    "(",
    "[",
    "]",
    "{",
    "}",
    "#",
    "¨",
    "^",
    "°",
    "'",
    "<>",
    "@",
    "=",
    "~",
    "$",
    "€",
    ";",
    ",",
]
dico_carac = {
    "<": 0,
    ">": 0,
    ":": 0,
    "«": 0,
    "|": 0,
    "?": 0,
    "*": 0,
    ".": 0,
    "&": 0,
    "/": 0,
    "+": 0,
    "%": 0,
    ")": 0,
    "(": 0,
    "[": 0,
    "]": 0,
    "{": 0,
    "}": 0,
    "#": 0,
    "¨": 0,
    "^": 0,
    "°": 0,
    "'": 0,
    "<>": 0,
    "@": 0,
    "=": 0,
    "~": 0,
    "$": 0,
    "€": 0,
    ";": 0,
    ",": 0,
}
for dir in DIRNAME:
    # for dir in list_dossier:
    # print(dir)
    # for dir in DIRNAME:
    for path, subdirs, files in os.walk(dir):
        # print(path)
        for name in files:
            try:
                print("AFTER ", os.path.join(path, name))
                length += 1
                list_arbo.append(os.path.join(path, name))
                for i in list_carac:
                    if i in os.path.join(path, name):
                        dico_carac[i] += 1
                # if "<" in os.path.join(path, name):
                #     length_dwg += 1
                # elif ">" in os.path.join(path, name):
                #     length_dwg += 1
                # elif ":" in os.path.join(path, name):
                #     length_dwg += 1
                # elif "«" in os.path.join(path, name):
                #     length_dwg += 1
                # elif "|" in os.path.join(path, name):
                #     length_dwg += 1
                # elif "?" in os.path.join(path, name):
                #     length_dwg += 1
                # elif "*" in os.path.join(path, name):
                #     length_dwg += 1
                # elif "." in os.path.join(path, name):
                #     length_dwg += 1
                # elif "&" in os.path.join(path, name):
                #     length_dwg += 1
                # elif "/" in os.path.join(path, name):
                #     length_dwg += 1
                # elif "+" in os.path.join(path, name):
                #     length_dwg += 1
                # elif "%" in os.path.join(path, name):
                #     length_dwg += 1
                # elif ")" in os.path.join(path, name):
                #     length_dwg += 1
                # elif "(" in os.path.join(path, name):
                #     length_dwg += 1
                # elif "[" in os.path.join(path, name):
                #     length_dwg += 1
                # elif "]" in os.path.join(path, name):
                #     length_dwg += 1
                # elif "{" in os.path.join(path, name):
                #     length_dwg += 1
                # elif "}" in os.path.join(path, name):
                #     length_dwg += 1
                # elif "#" in os.path.join(path, name):
                #     length_dwg += 1
                # elif "¨" in os.path.join(path, name):
                #     length_dwg += 1
                # elif "^" in os.path.join(path, name):
                #     length_dwg += 1
                # elif "°" in os.path.join(path, name):
                #     length_dwg += 1
                # elif "'" in os.path.join(path, name):
                #     length_dwg += 1
                # elif "<>" in os.path.join(path, name):
                #     length_dwg += 1
                # elif "@" in os.path.join(path, name):
                #     length_dwg += 1
                # elif "=" in os.path.join(path, name):
                #     length_dwg += 1
                # elif "~" in os.path.join(path, name):
                #     length_dwg += 1
                # elif "$" in os.path.join(path, name):
                #     length_dwg += 1
                # elif "€" in os.path.join(path, name):
                #     length_dwg += 1
                # elif ";" in os.path.join(path, name):
                #     length_dwg += 1
                # elif "," in os.path.join(path, name):
                #     length_dwg += 1
            except Exception as e:
                error += 1

print("dico_carac", dico_carac)
df = pd.DataFrame(dico_carac.items())
df.to_csv(
    "output_datas\liste_carac_interdit.csv",
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
