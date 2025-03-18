# Importando as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Carregando a planilha
df = pd.read_csv("date/datasheet.csv")

# Exibindo as primeiras linhas do DataFrame para análise inicial
print(df.head())
print("============================================")

# Calcular e exibir as medidas de tendência central (média, mediana e moda)
media = df.mean(numeric_only=True)  # Média das colunas numéricas
mediana = df.median(numeric_only=True)  # Mediana das colunas numéricas
moda = df.mode(numeric_only=True).iloc[0]  # Moda das colunas numéricas

# Exibindo resultados arredondados com duas casas decimais
print(f"Média:\n{media.round(2)}")
print("============================================")
print(f"Mediana:\n{mediana.round(2)}")
print("============================================")
print(f"Moda:\n{moda.round(2)}")
print("============================================")

# Calcular e exibir as medidas de dispersão (variância e desvio padrão)
variacao = df.var(numeric_only=True)  # Variância
desvio_padrao = df.std(numeric_only=True)  # Desvio padrão

# Exibindo os resultados
print(f"Variação:\n{variacao.round(2)}")
print("============================================")
print(f"Desvio padrão:\n{desvio_padrao.round(2)}")
print("============================================")

# Criando histogramas para explorar a distribuição dos dados
colunas = ["Idade", "Salario", "Experiencia", "Horas_Trabalho_Semanal", "Satisfacao"]
df[colunas].hist(bins=20, figsize=(12, 8), grid=False)  # Histogramas das colunas selecionadas

# Normalizando os dados para o boxplot
df_normalize = df.copy()  # Criando uma cópia do DataFrame
escala = MinMaxScaler()  # Inicializando o escalador MinMax
columns_menores = [col for col in colunas if colunas != "Salario"]  # Selecionando as colunas a normalizar
df_normalize[columns_menores] = escala.fit_transform(df[columns_menores])  # Normalizando os dados

# Criando um boxplot para identificar outliers
plt.figure(figsize=(12, 8))
sns.boxenplot(data=df_normalize[colunas])
plt.xticks(rotation=45)
plt.title("Boxplot")

# Gerando a matriz de correlação e criando o heatmap
matriz_correlacao = df[colunas].corr()  # Calculando a matriz de correlação
print(matriz_correlacao)  # Exibindo a matriz de correlação
plt.figure(figsize=(10, 8))
sns.heatmap(matriz_correlacao, annot=True, cmap="coolwarm", fmt=".3", linewidths=0.5)
plt.title("Matriz de Correlação - Heatmap")

# Ajustando o layout para evitar sobreposições
plt.tight_layout()

# Normalizando os dados antes da aplicação do PCA
dados = df[colunas].values  # Obtendo os valores das colunas selecionadas
dados_normal = (dados - media.values) / desvio_padrao.values  # Normalizando os dados
matriz = np.cov(dados_normal.T)  # Calculando a matriz de covariância

# Aplicando PCA
autovalores, autovetores = np.linalg.eig(matriz)  # Obtendo autovalores e autovetores
indices_ordenados = np.argsort(autovalores)[::-1]  # Ordenando os autovalores em ordem decrescente
autovalores = autovalores[indices_ordenados]
autovetores = autovetores[:, indices_ordenados]

# Obtendo os dois primeiros componentes principais
PC1 = autovetores[:, 0]
PC2 = autovetores[:, 1]

# Projetando os dados normalizados nos componentes principais
dados_pca = np.dot(dados_normal, np.array([PC1, PC2]).T)
df_pca = pd.DataFrame(dados_pca, columns=["PC1", "PC2"])

# Calculando a variância explicada pelos componentes principais
variancia_explicada = autovalores / np.sum(autovalores)
print(f"Variância explicada - PC1: {variancia_explicada[0]:.2%}, PC2: {variancia_explicada[1]:.2%}")

# Plotando a projeção PCA
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df_pca["PC1"], y=df_pca["PC2"])
plt.xlabel("Componente Principal 1")
plt.ylabel("Componente Principal 2")
plt.title("Projeção PCA dos Dados Normalizados")
plt.grid()

# Exibindo os gráficos
plt.show()
