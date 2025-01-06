# Machine Learning

## Tipos/ Modelos

### Aprendizado Supervisionado: O modelo é treinado com dados rotulados (ex.: imagens de maçãs e bananas com rótulos correspondentes).

    Algorítimos principais
		Classificador Naive Bayer
		KNN - K Nearest Neighbor: Para rótulos com sim ou não
		Regressão Logística: Para rótulos com sim ou não
		Regressão Linear: Quando não temos um rótulo binário. Ex: Sim ou Não em uma lista de Maus (ou bons) pagadores.
		Árvore de Decisão
		Modelagem por agrupamento

### Aprendizado Não Supervisionado: O modelo tenta identificar padrões ou agrupamentos nos dados sem rótulos (ex.: agrupamento de imagens de frutas sem saber que são maçãs ou bananas).

    Distância Euclidiana
	Clusters
	Algorítimos principais
		K-Means
		DBSCAN
		Cluster Hierárquico
		Análise de Componentes Principais (PCA)
		Apriori
		T-distributed Stochatis Neighbours Embedding (T-SNE)

Aprendizado por Reforço: O modelo aprende através de tentativa e erro, recebendo recompensas ou punições (ex.: um agente que aprende a jogar um jogo maximizando a pontuação).

## Variáveis

### Categoricas

### Numericas


### Dummies

O uso de variáveis dummy é uma técnica comum no pré-processamento de dados categóricos para modelos de aprendizado de máquina. O uso é comum em :

- Modelos Lineares: Regressão Linear e Logística
- Modelos Baseados em Distância: K-Nearest Neighbors (KNN)
- Modelos que Não Lidam Bem com Ordinalidade: Árvores de Decisão e Florestas Aleatórias

## Pré-processamento

### Manual

dados['fumante']= dados['fumante'].map({'sim':1,'não':0})
dados = pd.get_dummies(dados, columns=['gênero','região'], drop_first=True)


### Auto

**from** sklearn**.**preprocessing **import** LabelEncoder
le **=** LabelEncoder**(**)


## Treinamento

### Stratify

Garante que a divisão dos dados preserve a proporção de classes em ambos os conjuntos (treinamento e teste). Isso é particularmente útil quando você tem um conjunto de dados desbalanceado, ou seja, onde algumas classes são mais representadas do que outras.

## Padronização

Use quando os dados seguem uma distribuição normal ou quando o algoritmo de machine learning assume que os dados são normalmente distribuídos.
	sklearn.preprocessing é padronização
	Padronização é Normalização Z Score

Referência: Machine Learning/Aula 4/Normalização e padronização de dados - Feature Scaling.ipynb

## Normalização

Use quando os dados não seguem uma distribuição normal ou quando você deseja que os dados estejam em uma escala específica, como entre 0 e 1.

Referência: Machine Learning/Aula 4/Normalização e padronização de dados - Feature Scaling.ipynb

## Resíduos

São erros, quanto menor melhor.


## PCA

Usado para simplifcar bancos com muitas colunas. Em colunas, não linhas.

### Modelos de Regressão

### Desafios de aprendizagem de máquina

Algoritmos ruins
Dados ruins (poucos dados, ou muitos dados com viés, outliers)
Dados não representativos (Qualitativo, Quantitativo discreto, Quantitativo continúo)
Sobreajuste (overfiting)
	Quando o modelo funciona com os dados de treinamento, mas não generaliza com novos dados de entrada. Se a acurácia é 100% pode ser sobreajuste
	Simplificar o modelo
	Coletar mais dados
	Reduzir ruído (remover outlier)
	Regularizar
Subajuste dos dados (underfiting)
	Soluções
		Selecionar um modelo mais poderoso
		Feature engineering
		Reduzir as regularizações
Falta de testes e validação do algotirmo
	Base de treino, teste e validação cruzadas

Site kaggle para base de dados

Antes de criar um modelo
	Coleta > Limpeza > Transformação
	Treinamento
	Ajustes finais

Trash in, Trash Out

Redução de Dimensionalidade
Base de dados com muitas colunas (maldição da alta dimensionalidade) - Dimensão = número de colunas na base de dados.

PCA (Análise de componentes principais)
Agrupar dados em componentes. É como um guia que vai criar representações das colunas em componentes.

Estruturados
Semi Estruturados
Não estruturados
Dados Temporáis

---

Deep Learning
Rede Neural

Desvantagens
Necewssidade de muitos dados
Falta de clareza
Problemas de generalização
Dificuldade com dados complexos (pensamento abstrato)
Alto custo computacional
Conhecimentos prévios
Confusão entre correlação e casualidade
Risco de víes
Limitações em raciocínio

Redes
FeedForward (Entra > processa > saí)
Backpropagation
Neural Recorrente (Google tradutor)
Convulacional (filtros usados para detectar pedaços específicos - Passando para próximas camadas somente dados positivos)

---

Redes Adversariais Gerativas (GANS) - Áudio, imagens
Codificadores Automáticos Variacionais (VAES) - Processamento de dados

---

A base de dados:
Espécie	Comprimento do Abdômen	Comprimento das Antenas
Gafanhoto	0.5	7
Gafanhoto	0.5	6
Esperança	9.87	7
Esperança	7.12	6.6

usando o código:
from sklearn.model_selection import train_test_split
x = dados[['Comprimento do Abdômen', 'Comprimento das Antenas']]
y = dados['Espécie']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify=y,random_state=42)

retorna
list(y_train).count('Gafanhoto') = 40
list(y_train).count('Esperança') = 40

porém com este outro conjunto, não retorna nada por que?

base de dados
idade	gênero	imc	filhos	fumante	região	encargos
56	feminino	29.774373714007336	2	sim	sudoeste	31109.88976
46	masculino	25.857394655216346	1	não	nordeste	26650.7026
32	masculino	23.014839993647488	0	não	sudoeste	21459.0379
29	feminino	27.500000000000000	1	não	nordeste	20234.5678

código:
x = dados[['encargos', 'gênero']]
y = dados['idade']
w = dados['fumante']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify=w, random_state=42)
