import pandas as pd
import matplotlib.pyplot as plt

file_path = "Brightness-Luminance-2026-04-20-18-54-10.xlsx"
df = pd.read_excel(file_path)

print(df.head())
print("\nКолонки:", df.columns)

mid = len(df) // 2
without_glasses = df.iloc[:mid]
with_glasses = df.iloc[mid:]

mean_without = without_glasses['Luminance'].mean()
mean_with = with_glasses['Luminance'].mean()

difference = mean_without - mean_with
percent_loss = (difference / mean_without) * 100

print("\nРезультати")
print(f"Середня освітленість без окулярів: {mean_without:.2f}")
print(f"Середня освітленість з окулярами: {mean_with:.2f}")
print(f"Різниця: {difference:.2f}")
print(f"Втрати світла: {percent_loss:.2f}%")

plt.figure()

plt.plot(without_glasses['t'], without_glasses['Luminance'], label='Без окулярів')
plt.plot(with_glasses['t'], with_glasses['Luminance'], label='З окулярами')

plt.xlabel("Час (t)")
plt.ylabel("Освітленість (Luminance)")
plt.title("Вплив сонцезахисних окулярів на освітленість")
plt.legend()

plt.show()

df['Luminance_diff'] = df['Luminance'].diff()

print("\nОпис статистики:")
print(df['Luminance'].describe())
