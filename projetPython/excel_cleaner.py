import pandas as 
df = pd.read_excel("pharmacielapaix.xlsx")

df = df.drop_duplicates()
df = df.dropna(how="all")

df.to_excel("pharmacie_propre.xlsx", index=False)

print("Nettoyage terminé !")