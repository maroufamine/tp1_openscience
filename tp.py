# Importation des données
import pandas as pd
df = pd.read_csv("data.csv")
df

# Calcul des statistiques

df["Value"].mean()
df["Value"].std()

# Visualisation simple


df.plot(kind="bar", x="Sample", y="Value")
