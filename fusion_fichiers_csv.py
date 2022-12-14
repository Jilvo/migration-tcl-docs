import pandas as pd
import os

# merging two csv files
def fusion():
    print(" Ce script va vous permettre de fusionner des fichiers CSV ")
    print("Bien faire attention au chemin du fichier, car sinon il faudra recommencer")
    print(
        "Y a t-il une modification humaine sur le fichier ? Si vous ne savez pas, ouvrez les fichiers CSV, sauvegardez les en format csv avec séparateur en ';' ."
    )
    modif_encode = input("Il a été modifié ? : (O/N) ")
    list_files = []
    flag = False
    while not flag:
        print(
            "Voulez vous ajouter un fichier CSV sous format 'nom_du_fichier', le script rajoutera l'extension et le sous dossier output_datas"
        )
        input_choice = input("O / N : ")
        if input_choice.upper() == "O":
            path_file = input("Entrez le nom du fichier : ")
            path_file = "fusion_finale\\" + path_file + ".csv"
            path = os.path.join(path_file)
            list_files.append(path)
            print("path_file = ", path)
        elif input_choice.upper() == "N":
            flag = True
        else:
            print("Je ne comprend pas votre réponse, réessayez ")

    df = pd.concat(
        map(
            pd.read_csv,
            list_files,
        ),
        ignore_index=True,
    )
    print(df)
    encoding = ""
    if modif_encode.upper() == "O":
        encoding = "cp1252"
    else:
        encoding = "utf-8-sig"
    df.to_csv(
        "fusion_finale/fusion.csv",
        sep=";",
        index=False,
        encoding=encoding,
    )


fusion()
