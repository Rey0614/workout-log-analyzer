import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("workout_log.csv")
df["weight"] = df["weight"].replace({"8th from top": "40", "7th from top": "35"})
df["weight"] = pd.to_numeric(df["weight"], errors="coerce")
df = df.dropna(subset=["weight"])

max_value = df.groupby("exercise")["weight"].max()
average_value = df.groupby("exercise")["weight"].mean()

# print(max_value)
# print(average_value)

# # 日付型に変化
# df["date"] = pd.to_datetime(df["date"])
# print(df.dtypes)

# ベンチプレスだけに絞る
bench = df[df["exercise"] == "Bench press"]
# print(bench)

# 日付ごとの最高重量
bench_max = bench.groupby("date")["weight"].max()
# print(bench_max)

bench_max.plot(marker="o", title="Bench Press Progress")
plt.ylabel("Max weight (kg)")
plt.grid(True)
plt.savefig("bench_progress.png")