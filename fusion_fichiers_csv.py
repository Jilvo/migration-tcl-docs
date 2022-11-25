import pandas as pd

# merging two csv files
df = pd.concat(
    map(
        pd.read_csv,
        [
            "output_datas\listes des succes Tram Ligne T5 complet.csv",
            "output_datas\listes des succes Liaison b_d complet.csv",
        ],
    ),
    ignore_index=True,
)
print(df)

df.to_csv(
    "output_datas/fusion.csv",
    sep=";",
    index=False,
    encoding="cp1252",
)
