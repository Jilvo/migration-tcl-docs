import os
import sys
import pandas as pd
import re
from timeit import default_timer as timer
from difflib import SequenceMatcher
from fichiers_et_constantes import *
import jellyfish
import menu_arborescence
import arborescence_tcl_pret

### Mettre nom du fichiers d'échecs
nom_fichier_echecs = "output_datas/listes des echecs Prêt complet.csv"
name_file_success = "output_datas/fichier_trouve_suite_comp_fich_definitif.csv"
name_file_failed = "output_datas/fichier_echecs_suite_comp_fich_definitif.csv"


Lunch_Menu = menu_arborescence.MainExtraction()

df_extraction_pret = Lunch_Menu.extraction_pret_tcl_reprise_comparaison_definitif()
arborescence_tcl_pret.compare_list_arbo_csv_bi_pret(
    nom_fichier_echecs,
    df_extraction_pret,
    name_file_success,
    name_file_failed,
)
print("Nombre de références dans l'extraction", df_extraction_pret)
print("Chemin du fichier ", name_file_success)
