import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

energy_dataset = pd.read_csv('energy_dataset_12000.csv')

X = energy_dataset.drop('energy_consumption', axis=1)
y = energy_dataset['energy_consumption']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA()
X_pca = pca.fit_transform(X_scaled)

print("Explained variance ratio:", pca.explained_variance_ratio_)
print("Сума поясненої варіації:", np.sum(pca.explained_variance_ratio_))

plt.figure(figsize=(8,5))
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('Кількість компонент')
plt.ylabel('Накопичена пояснена дисперсія')
plt.title('Вибір кількості головних компонент')
plt.show()

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

pca_df = pd.DataFrame(X_pca, columns=['PC1', 'PC2'])
pca_df['energy_consumption'] = y

print("\nКореляція PC з energy_consumption:")
print(pca_df.corr()['energy_consumption'])

plt.figure(figsize=(8,6))
plt.scatter(pca_df['PC1'], pca_df['PC2'], c=y, cmap='viridis', alpha=0.6)
plt.colorbar(label='Energy consumption')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('PC1 vs PC2 з урахуванням енергоспоживання')
plt.show()

components_df = pd.DataFrame(pca.components_, columns=X.columns, index=['PC1', 'PC2'])

plt.figure(figsize=(12,6))
sns.heatmap(components_df, cmap='coolwarm', annot=True)
plt.title('Внесок ознак у головні компоненти')
plt.show()

for i in range(2):
    print(f"\nТоп фактори для PC{i+1}:")
    print(components_df.iloc[i].sort_values(ascending=False))

corr_matrix = energy_dataset.corr()

plt.figure(figsize=(10,8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Кореляційна матриця')
plt.show()

corr_with_target = corr_matrix['energy_consumption'].sort_values(ascending=False)

print("\nКореляція ознак з energy_consumption:")
print(corr_with_target)

print("\nПОРІВНЯННЯ:")
print("Найбільш впливові ознаки за кореляцією:")
print(corr_with_target.head(5))

print("\nНайбільш впливові ознаки за PCA (PC1):")
print(components_df.loc['PC1'].abs().sort_values(ascending=False).head(5))