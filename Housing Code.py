import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("C:\Arquivos\Documentos\Courses\CCP\Housing.csv")

df_recent = df[df["closed_roll_year"] == 2022]

df_prices = df_recent.loc[:, "misc_exemption_value":"assessed_personal_property_value"]

print(df_prices.head())