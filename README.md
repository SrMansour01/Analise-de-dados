# 📊 Atividade Avaliativa – Estatística Descritiva e Análise Exploratória de Dados (EDA)

# Execução do Código

Este projeto utiliza bibliotecas populares do Python para manipulação de dados, visualização e pré-processamento. Siga as etapas abaixo para configurar o ambiente e executar o código.

## Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina (recomenda-se a versão 3.7 ou superior). Você também precisará instalar as bibliotecas necessárias:

- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `numpy`

### Instalando o Python

Se você não tiver o Python instalado, baixe e instale a partir do site oficial: [https://www.python.org/](https://www.python.org/).

## Instalando as Dependências

Recomenda-se o uso de um ambiente virtual para gerenciar as dependências do projeto. Você pode criar e ativar um ambiente virtual com os comandos abaixo:

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

```

## **📍 Questão 1 – Conceitos Fundamentais (2 pontos)**
📌 **Objetivo:** Verificar a compreensão teórica da Estatística Descritiva e EDA.

📝 **Enunciado:** Defina e explique com suas próprias palavras:

1. O que são medidas de tendência central? Dê exemplos.

R: As medidas de tendência central, como média e mediana, desempenham um papel fundamental nos seguintes contextos:

- Normalização de Dados: Para treinar redes neurais de forma eficiente, é prática comum centralizar os dados em torno da média (ou mediana) e escalá-los, garantindo uma variância uniforme. Isso acelera o treinamento e melhora a performance do modelo.

- Análise de Pesos: Durante o treinamento, o monitoramento dos pesos das camadas é essencial para verificar se estão equilibrados ou tendendo a valores extremos.

Exemplo prático: Em modelos de classificação de imagens, normalizar os dados de entrada ajuda a evitar gradientes excessivamente grandes ou pequenos, que podem dificultar a retropropagação.

2. Qual a diferença entre variância e desvio padrão?

R:
- Controle de Overfitting e Regularização: Dados com alta variância podem sinalizar a necessidade de técnicas como dropout para evitar overfitting nas redes neurais.

- Inicialização de Pesos: A escolha da variância apropriada ao inicializar os pesos com distribuições estatísticas (como a normal) é crucial para evitar problemas com gradientes explosivos ou desaparecidos.

Além disso, acompanhar o desvio padrão dos erros da função de custo durante o treinamento ajuda a avaliar a convergência do modelo.

3. Explique o conceito de outliers e cite dois métodos para identificá-los

R: Os outliers podem impactar negativamente o desempenho das redes neurais porque:

- Distorção no Aprendizado: Eles prejudicam a identificação de padrões gerais e podem aumentar o erro do modelo.

- Sensibilidade ao Ruído: Redes neurais afetadas por outliers frequentemente generalizam mal.

Estratégias para lidar com outliers:

- Método do IQR: Utilizar o intervalo interquartil para filtrar ou transformar dados.

- Z-Score: Excluir ou ajustar valores com magnitude ∣𝑍∣ > 3 antes do treinamento.  


## **📍 Questão 5 – Reflexão sobre os Dados (2 pontos)**
📌 **Objetivo:** Interpretar os resultados obtidos.

📝 **Enunciado:** Após executar as análises:

1. Descreva o que você observa no histograma e no boxplot. Há outliers?

R: Sim, há outliers em todas as variáveis, representados pelos pontos fora dos limites das caixas.

- Distribuição dos Dados: As variáveis parecem normalizadas ou padronizadas, situando-se no intervalo de 0 a 1. As medianas estão bem posicionadas, sugerindo diferentes distribuições.

- Assimetria e Dispersão: Variáveis como Salário e Horas de Trabalho Semanal apresentam dispersão elevada, indicando distribuições assimétricas. A variável Experiência tem alta variabilidade, mostrando perfis variados no conjunto de dados.
2. O que a matriz de correlação indica sobre a relação entre as variáveis?

R: A matriz de correlação reflete o grau de associação entre as variáveis, possibilitando as seguintes análises:

- Idade vs. Experiência: É esperada uma correlação positiva, pois idade normalmente implica maior experiência.

- Idade vs. Satisfação: A relação pode variar. Trabalhadores mais velhos podem estar mais ou menos satisfeitos, dependendo do contexto.

- Salário vs. Experiência: Geralmente, maior experiência leva a salários maiores.

- Horas de Trabalho Semanal vs. Salário: Pode haver correlação positiva, já que mais horas trabalhadas podem aumentar a remuneração.
