#Aqui você encontra a ordem de códigos e comandos enviados no Google Coleb
#Para a realização da Análise exploratória junto ao professor

import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

from google.colab import files
uploaded = uploaded = files.upload()

df = df = pd.read_csv("covid_19_data.csv", parse_dates=['ObservationDate', 'Last Update'])

df

df.dtypes

import re
def corrige_colunas(col_name):
    return re.sub(r"[/| ]", "", col_name).lower()


df.columns = [corrige_colunas(col) for col in df.columns]

df

# Quantos estados rwmos informações para o Brasil?
df.loc[df.countryregion == 'Brazil']

#Temos apenas informações a nível de país e não de estado.
brasil = df.loc[
    (df.countryregion == 'Brazil') &
    (df.confirmed > 0)
]

brasil

# Verificar como esta o comportamnto dos casos confirmados no Brasil desde o primeiro caso confirmado.

#Grafico da evolução de casos confirmados
px.line(brasil, 'observationdate', 'confirmed', title='Casos confirmados no Brasil')

#Quantos casos novos temos por dia?

# Função para fazer a contagem de novos casos. 
#Técnica de programação funcional.

brasil['novoscasos'] = list(map(
    lambda x: 0 if (x==0) else brasil['confirmed'].iloc[x] - brasil['confirmed'].iloc[x-1],
    np.arange(brasil.shape[0])
))

brasil

# Visualização contagens de novos casos
px.line(brasil, x='observationdate', y='novoscasos', title='Novos casos por dia',
       labels={'observationdate': 'Data', 'novoscasos': 'Novos casos'})


#Vizualização contagens de novos casos em um novo grafico
#Trace é uma camada de dados 
fig = go.Figure()

fig.add_trace(
    go.Scatter(x=brasil.observationdate, y=brasil.deaths, name='Mortes', mode='lines+markers',
              line=dict(color='red'))
)
#Edita o layout
fig.update_layout(title='Mortes por COVID-19 no Brasil',
                   xaxis_title='Data',
                   yaxis_title='Número de mortes')
fig.show()

#Calcular a taxa de crescimento do COVID desde o primeiro caso.

def taxa_crescimento(data, variable, data_inicio=None, data_fim=None):
    # Se data_inicio for None, define como a primeira data disponível no dataset
    if data_inicio == None:
        data_inicio = data.observationdate.loc[data[variable] > 0].min()
    else:
        data_inicio = pd.to_datetime(data_inicio)
        
    if data_fim == None:
        data_fim = data.observationdate.iloc[-1]
    else:
        data_fim = pd.to_datetime(data_fim)
    
    # Define os valores de presente e passado
    passado = data.loc[data.observationdate == data_inicio, variable].values[0]
    presente = data.loc[data.observationdate == data_fim, variable].values[0]
    
    # Define o número de pontos no tempo q vamos avaliar
    n = (data_fim - data_inicio).days
    
    # Calcula a taxa
    taxa = (presente/passado)**(1/n) - 1

    return taxa*100


# Taxa de crescimento médio do COVID no brasil em todo o periodo

taxa_crescimento(brasil, 'confirmed')


# Taxa de crescimento médio do COVID no brasil em todo o periodo

cresc_medio = taxa_crescimento(brasil, 'confirmed')

print(f"O crescimento médio do COVID no Brasil no período avaliado foi de {cresc_medio.round(2)}%.")


#Taxa de crescimento diaria do COVID no Brasil

def taxa_crescimento_diaria(data, variable, data_inicio=None):
    if data_inicio == None:
        data_inicio = data.observationdate.loc[data[variable] > 0].min()
    else:
        data_inicio = pd.to_datetime(data_inicio)
        
    data_fim = data.observationdate.max()
    n = (data_fim - data_inicio).days
    taxas = list(map(
        lambda x: (data[variable].iloc[x] - data[variable].iloc[x-1]) / data[variable].iloc[x-1],
        range(1,n+1)
    ))
    return np.array(taxas)*100


tx_dia = taxa_crescimento_diaria(brasil, 'confirmed')
tx_dia


#Grafico taxa de crescimento de casos confirmados no Brasil

primeiro_dia = brasil.observationdate.loc[brasil.confirmed > 0].min()

px.line(x=pd.date_range(primeiro_dia, brasil.observationdate.max())[1:],
        y=tx_dia, title='Taxa de crescimento de casos confirmados no Brasil',
       labels={'y':'Taxa de crescimento', 'x':'Data'})


#Predição.
#Construção de um modelo de séries temporais para prever os novos casos.
# Primeiro será analisado a série temporal

#Bibliotecas para a predição e vizualização
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

confirmados = brasil.confirmed
confirmados.index = brasil.observationdate
confirmados

#Deponposição
res = seasonal_decompose(confirmados)

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(10, 8))

ax1.plot(res.observed)
ax2.plot(res.trend)
ax3.plot(res.seasonal)
ax4.plot(confirmados.index, res.resid)
ax4.axhline(0, linestyle='dashed', c='black')
plt.show()

# Predizendo o número de casos confirmados com ARIMA
#ARIMA é um método que tenta modelar o futuro em função do passado

!pip install pmdarima

from pmdarima.arima import auto_arima
modelo = auto_arima(confirmados)

#Acredito que seja uma limitação do Google colab ao uso do ARIMA, como o professor avisou no inicio da aula. 
#Estarei informando os códigos passados mesmo não conseguindo rodar no Google Colab. 

pd.date_range('2020-05-01', '2020-05-19')

#Modelo para prever os casos confirmados para os próximos 15 dias
fig = go.Figure(go.Scatter(
    x=confirmados.index, y=confirmados, name='Observed'
))

fig.add_trace(go.Scatter(x=confirmados.index, y = modelo.predict_in_sample(), name='Predicted'))

fig.add_trace(go.Scatter(x=pd.date_range('2020-05-20', '2020-06-05'), y=modelo.predict(15), name='Forecast'))

fig.update_layout(title='Previsão de casos confirmados para os próximos 15 dias',
                 yaxis_title='Casos confirmados', xaxis_title='Data')
fig.show()


#Modelo de crescimento para tentar prever quando que a curva de confirmado por COVID vai achatar
#Usando a biblioteca fbprophet
#O uso da bibliote também tem limitações no Google colab, por isso estarei escrevendo o código passado pelo professor
#mesmo não executando.

#Comando para importante a biblioteca no Anacondas
!conda install -c conda-forge fbprophet -y

from fbprophet import Prophet

# preparando os dados
train = confirmados.reset_index()[:-5]
test = confirmados.reset_index()[-5:]

# renomeia colunas
train.rename(columns={"observationdate":"ds","confirmed":"y"},inplace=True)
test.rename(columns={"observationdate":"ds","confirmed":"y"},inplace=True)
test = test.set_index("ds")
test = test['y']

profeta = Prophet(growth="logistic", changepoints=['2020-03-21', '2020-03-30', '2020-04-25', '2020-05-03', '2020-05-10'])

#pop = 1000000
pop = 211463256 #https://www.ibge.gov.br/apps/populacao/projecao/box_popclock.php
train['cap'] = pop

# Treina o modelo
profeta.fit(train)

# Construindo previsões para o futuro
future_dates = profeta.make_future_dataframe(periods=200)
future_dates['cap'] = pop
forecast =  profeta.predict(future_dates)

fig = go.Figure()

fig.add_trace(go.Scatter(x=forecast.ds, y=forecast.yhat, name='Predição'))
fig.add_trace(go.Scatter(x=test.index, y=test, name='Observados - Teste'))
fig.add_trace(go.Scatter(x=train.ds, y=train.y, name='Observados - Treino'))
fig.update_layout(title='Predições de casos confirmados no Brasil')
fig.show()