import os
import sys
import pandas as pd

# dirname = f"""H:\Tcl"""
# dirname = f"""\\Serber\Terrain\MAGGALY"""
# dirname = f"""F:\Tcl\{str(800)} à {str(843)} - Surface"""
dirname = f"""F:\Tcl\{str(900)} - Lignes Fortes - C1 C2 C3 C13"""
# dirname = f"""F:\Tcl\{str(105)} à 122 - Métro A - stations\Bonnevay\Station\{str(0)}4 Télétrans\AL99ALM0901FB0000E20GS050307"""
# dirname = f"""H:\Tcl\{str(1002)} - Métro ABC - communs"""
# dirname = f"""H:/Tcl/130 à 137 - Métro B - stations/Brotteaux"""
DIRNAME = [
    # f"""F:\Tcl\{str(0)}01 - Métro - communs""",
    # f"""F:\Tcl\{str(0)}02 - Métro ABC - communs""",
    # f"""F:\Tcl\{str(0)}03 - Métro AB - communs""",
    # f"""F:\Tcl\{str(100)} - Métro A - communs""",
    # f"""F:\Tcl\{str(101)} - Métro A - interstations""",
    # f"""F:\Tcl\{str(102)} - Métro B - communs""",
    # f"""F:\Tcl\{str(103)} - Métro B - interstations""",
    # f"""F:\Tcl\{str(105)} à {str(122)} - Métro A - stations""",
    # f"""F:\Tcl\{str(130)} à {str(137)} - Métro B - stations""",
    # f"""F:\Tcl\{str(200)} - Métro C - communs""",
    # f"""F:\Tcl\{str(201)} - Métro C - interstations""",
    # f"""F:\Tcl\{str(210)} à {str(213)} - Métro C - stations""",
    # f"""F:\Tcl\{str(300)} - Métro D - communs""",
    # f"""F:\Tcl\{str(301)} - Métro D - interstations""",
    # f"""F:\Tcl\{str(302)} - Funiculaires - communs""",
    f"""F:\Tcl\{str(303)} - Liaison BD""",
    # f"""F:\Tcl\{str(305)} à {str(322)} - Métro D - stations""",
    # f"""F:\Tcl\{str(330)} à {str(332)} - Funiculaires - stations""",
    # f"""F:\Tcl\{str(500)} - Tramway - communs""",
    # f"""F:\Tcl\{str(500)} - Tramway Rhone Express - communs""",
    f"""F:\Tcl\{str(500)} - Tramway T1 - communs""",
    f"""F:\Tcl\{str(500)} - Tramway T2 - communs""",
    f"""F:\Tcl\{str(500)} - Tramway T3 - communs""",
    f"""F:\Tcl\{str(500)} - Tramway T4 - communs""",
    f"""F:\Tcl\{str(500)} - Tramway T5 - communs""",
    f"""F:\Tcl\{str(500)} - Tramway T6 - communs""",
    # f"""F:\Tcl\{str(501)} - Tramway T1 - stations""",
    # f"""F:\Tcl\{str(501)} - Tramway T2 - stations""",
    # f"""F:\Tcl\{str(501)} - Tramway T3 - stations""",
    # f"""F:\Tcl\{str(501)} - Tramway T4 - stations""",
    # f"""F:\Tcl\{str(501)} - Tramway T5 - stations""",
    # f"""F:\Tcl\{str(501)} - Tramway T6 - stations""",
    f"""F:\Tcl\{str(800)} à {str(843)} - Surface""",
    # f"""F:\Tcl\{str(900)} - Lignes Fortes - C1 C2 C3 C13""",
]
# print(dirname)
length = 0
length_dwg = 0
length_see = 0
list_arbo = []
error = 0
for dir in DIRNAME:
    for path, subdirs, files in os.walk(dir):
        # print(path)
        for name in files:
            try:
                print("AFTER ", os.path.join(path, name))
                length += 1
                list_arbo.append(os.path.join(path, name))
                if os.path.join(path, name)[-4:] == ".dwg":
                    length_dwg += 1
                    if length_dwg % 10 == 0:
                        print("actual length dwg: ", length_dwg)
                if os.path.join(path, name)[-4:] == ".see":
                    length_see += 1
                    if length_see % 10 == 0:
                        print("actual length see: ", length_see)
            except Exception as e:
                error += 1
# df = pd.DataFrame(
#     list_arbo,
# )
# df.columns = ["path"]
# df.to_csv(
#     "output_datas/arborescence_tcl.csv", sep="\t", index=False, encoding="utf-8-sig"
# )
print("Total length = ", length)
print("Total length DWG FILES = ", length_dwg)
print("Total length SEE FILES = ", length_see)
print("Total error = ", error)
