import os
import sys
import pandas as pd
import re
import time

from pathlib import Path
from timeit import default_timer as timer
from fichiers_et_constantes import *

start = timer()

list_arbo = []


def create_arbo():
    """On crée l'arborescence"""
    DIRNAME = f"""X:"""
    for path, subdirs, files in os.walk(DIRNAME):
        for name in files:
            try:
                if os.path.join(path, name)[-8:] == "Topo.dwg":
                    print(os.path.join(path, name))
                    list_arbo.append(os.path.join(path, name))
            except Exception as e:
                print(e.args)
    df = pd.DataFrame(
        list_arbo,
    )
    df.to_csv(
        "output_datas/arborescence_partimoine.csv",
        sep=";",
        index=False,
        encoding="utf-8-sig",
    )


create_arbo()
