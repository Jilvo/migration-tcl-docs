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
