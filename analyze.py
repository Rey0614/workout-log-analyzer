import pandas as pd

df = pd.read_csv("workout_log.csv")
df["weight"] = df["weight"].replace({"8th from top": "40", "7th from top": "35"})
df["weight"] = pd.to_numeric(df["weight"], errors="coerce")
df = df.dropna(subset=["weight"])

result = df.groupby("exercise")["weight"].max()
print(result)