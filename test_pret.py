import os
import sys


# dirname = f"""H:\Tcl"""
# dirname = f"""H:\Tcl\{str(210)} à {str(213)} - Métro C - stations\Croix-Paquet"""
# dirname = f"""H:\Tcl\{str(130)} à 137 - Métro B - stations\Brotteaux"""
list_direname = [
    f"""H:\Tcl\{str(500)} - Tramway - communs""",
    f"""H:\Tcl\{str(500)} - Tramway Rhone Express - communs""",
    f"""H:\Tcl\{str(500)} - Tramway T1 - communs""",
    f"""H:\Tcl\{str(500)} - Tramway T2 - communs""",
    f"""H:\Tcl\{str(500)} - Tramway T3 - communs""",
    f"""H:\Tcl\{str(500)} - Tramway T4 - communs""",
    f"""H:\Tcl\{str(500)} - Tramway T5 - communs""",
    f"""H:\Tcl\{str(500)} - Tramway T6 - communs""",
    f"""H:\Tcl\{str(501)} - Tramway T1 - stations""",
    f"""H:\Tcl\{str(501)} - Tramway T2 - stations""",
    f"""H:\Tcl\{str(501)} - Tramway T3 - stations""",
    f"""H:\Tcl\{str(501)} - Tramway T4 - stations""",
    f"""H:\Tcl\{str(501)} - Tramway T5 - stations""",
    f"""H:\Tcl\{str(501)} - Tramway T6 - stations""",
]
# dirname = f"""H:/Tcl/130 à 137 - Métro B - stations/Brotteaux"""
# print(dirname)
length = 0
length_dwg = 0
error = 0
for url in list_direname:
    for path, subdirs, files in os.walk(url):
        # print(path)
        for name in files:
            try:
                # print("****************************************************************")
                # print("BASE URL", os.path.join(path, name))
                # path.replace("\\", "/")
                # slash_path = os.path.join(path, name)
                # new_path = slash_path.replace(os.sep, "/")
                # print("AFTER", new_path)
                print("AFTER ", os.path.join(path, name))
                length += 1
                if os.path.join(path, name)[-4:] == ".dwg":
                    length_dwg += 1
                    # print("actual length: ", length_dwg)
                    if length_dwg % 10 == 0:
                        print("actual length: ", length_dwg)
            except Exception as e:
                error += 1

print("Total length = ", length)
print("Total length DWG FILES = ", length_dwg)
print("Total error = ", error)
