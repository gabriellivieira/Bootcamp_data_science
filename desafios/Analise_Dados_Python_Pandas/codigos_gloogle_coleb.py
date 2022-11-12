#Aqui você encontra a ordem de códigos e comandos enviados no Google Coleb
#Para a realização da Análise exploratória junto a professora

#importando as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("bmh")

#Realizado o upload do arquivo xlsx pela aba de arquivos do Gloogle Coleb

#criando o DataFrame
df = pd.read_excel("AdventureWorks.xlsx")

#Visualização das 5 primeiras linhas
df.head()

#Quantidade de linhas e colunas
df.shape

#Verificando os tipos de dados
df.dtypes

#Qual a receita total?
df["Valor Venda"].sum()

#Qual o custo total? criar coluna de custo total
df["Custo Total"] = df["Custo Unitário"].mul(df["Quantidade"])

df.head(1)

#Qual a soma do Custo Total?
round(df["Custo Total"].sum(), 2)

#Com a receita e o custo toal, podemos achar o Lucro total. Criar uma coluna Lucro com a REceita - Custo
df["Lucro"] = df["Valor Venda"] - df["Custo Total"]

df.head(1)

#Lucro Total
round(df["Lucro"].sum(), 2)

#Criar coluna com total de dias para enviar o produto
df["Tempo Envio"] = df["Data Envio"] - df["Data Venda"]

df.head(1)

#Extraindo apenas os dias
df["Tempo Envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days

df.head(1)

df["Tempo Envio"].dtype

df.isnull().sum()

#Para saber lucro por marca, vamos agrupar por ano e marca.
df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum()

#Configurando o formato dos números float para não aparecer em notação
pd.options.display.float_format = '{:20,.2f}'.format

#Resetando o index, criando uma variavel para que as informações do lucro por marca e ano retorne em tabela
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum().reset_index()
lucro_ano

#Qual o total de produtos vendidos?
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)

#Grafico total de produtos vendidos
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False).plot.barh(title="Total Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("Produto");

#Grafico Lucro por ano
df.groupby(df["Data Venda"].dt.year)["Lucro"].sum().plot.bar(title="Lucro X Ano")
plt.xlabel("Ano")
plt.ylabel("Receita");

df.groupby(df["Data Venda"].dt.year)["Lucro"].sum()

#Selecionando apenas as vendas de 2009
df_2009 = df[df["Data Venda"].dt.year == 2009]

df_2009.head()

#Grafico de Lucro x Mês
df_2009.groupby(df_2009["Data Venda"].dt.month)["Lucro"].sum().plot(title="Lucro X Mês")
plt.xlabel("Mês")
plt.ylabel("Lucro");

#Grafico de Lucro x Marca
df_2009.groupby("Marca")["Lucro"].sum().plot.bar(title= "Lucro X Marca")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal');

#Grafico de Lucro x Classe
df_2009.groupby("Classe")["Lucro"].sum().plot.bar(title= "Lucro X Classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal');

#Estatistica
df["Tempo Envio"].describe()

#Grafico de boxplot
plt.boxplot(df["Tempo Envio"]);

#Histograma
plt.hist(df["Tempo Envio"]);

#Tempo mínimo de envio
df["Tempo Envio"].min()

#Tempo máximo de envio
df["Tempo Envio"].max()

#Identificando o outlier
df[df["Tempo Envio"] == 20]

#Salvar a analise em um novo excel
df.to_csv("AdventureWorks_analise.csv", index=False)