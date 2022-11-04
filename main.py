"""
Script principal dans lequel sont lancées les lignes complètes, SERBER,PRET...
"""
import menu_arborescence

Lunch_Menu = menu_arborescence.MainExtraction()

# PRET
Lunch_Menu.main(
    DIRNAME=f"""F:\Tcl\Prêt Plans""",
    name_file_arbo="output_datas/arborescence_tcl_pret_complet.csv",
    name_file_success="output_datas/listes des succes Prêt Complet.csv",
    name_file_failed="output_datas/listes des echecs Prêt Complet.csv",
    input_user=9,
)
# SERBER
Lunch_Menu.main(
    DIRNAME=f"""G:""",
    name_file_arbo="output_datas/arborescence_tcl_serber_complet.csv",
    name_file_success="output_datas/listes des succes Serber Complet.csv",
    name_file_failed="output_datas/listes des echecs Serber Complet.csv",
    input_user=8,
)

# Métro A

# Métro B

# Métro C

# Métro D

# Métro Communs


# METRO ABC,AB,A,B,C,D COMMUNS

# T1

# T2

# T3

# T4

# T5

# T6

# TRAM COMMUNS

# RHONE EXPRESS COMMUNS
Lunch_Menu.main(
    DIRNAME=f"""F:\Tcl\500 - Tramway Rhone Express - communs""",
    name_file_arbo="output_datas/arborescence_tcl_serber_complet.csv",
    name_file_success="output_datas/listes des succes Serber Complet.csv",
    name_file_failed="output_datas/listes des echecs Serber Complet.csv",
    input_user=8,
)

# FUNI COMMUNS

# FUNI COMMUNS + STATIONS

# Lignes Fortes

# Surface
# list a traiter type
# ['ALSACE UTN 1 ET UMS', 'ALSACE UTN 2', 'ARCHIVES S/STATIONS', 'CENTRE S/STATION', 'COMMUNS BUS', 'COMMUNS S/STATION', 'COMMUNS SURFACE', 'CROIX ROUSSE S/STATION', 'DAUPHINE S/STATION', 'DIVERS SURFACE', 'DUCHERE PARC RELAIS', 'DUCHERE S/STATION', 'DUCHERE SITE PROPRE', 'GRANDCLEMENT S/STATION', 'SST ACHILLE LIGNON', 'SST BAUMER GRAPPINIERE', 'SST CALUIRE', 'SST DREVET', 'SST FOCH', 'SST MICHELET', 'SST MOBILE', 'SST TERME', 'SST THOREZ', 'SST
# TONKIN', 'SST VAISE', 'SST VENDOME', 'SURFACE', 'SURFACE L.A.', 'UT AUDIBERT', 'UT CALUIRE', 'UT GIVORS', 'UT LA SOIE', 'UT LES PINS', 'UT OULLINS', 'UT PARMENTIER', 'UT PERRACHE', 'UT PERRACHE CONFLUENCE', 'UT VAISE']
