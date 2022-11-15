import pandas as pd
from fichiers_et_constantes import *

with open("datas/error_exceptionNotFOUND.txt", "r") as txt_file:
    print(txt_file.readlines())

read_file = pd.read_csv(r"datas/error_exceptionNotFOUND.txt", delimiter="/n")
read_file.to_csv(r"datas/compte.csv", index=None, encoding="ansii")
