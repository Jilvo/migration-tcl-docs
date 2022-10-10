import os
import sys
import pandas as pd

# dirname = f"""H:\Tcl"""
# dirname = f"""\\Serber\Terrain\MAGGALY"""
dirname = f"""F:\Tcl\{str(210)} à {str(213)} - Métro C - stations\Croix-Paquet"""
# dirname = f"""H:\Tcl\{str(200)} - Métro C - communs"""
# dirname = f"""H:\Tcl\{str(1002)} - Métro ABC - communs"""
# dirname = f"""H:/Tcl/130 à 137 - Métro B - stations/Brotteaux"""
print(dirname)
length = 0
length_dwg = 0
length_see = 0
list_arbo = []
error = 0
for path, subdirs, files in os.walk(dirname):
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
