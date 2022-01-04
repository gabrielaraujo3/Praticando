from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

cotacao_bovespa = web.DataReader('^BVSP', data_source='yahoo', start="01-01-2020", end="01-01/-2022")
display(cotacao_bovespa)
cotacao_bovespa["Adj Close"].plot(figsize=(15, 10))
plt.show()

tabela_empresas = pd.read_excel("Empresas.xlsx")
display(tabela_empresas)
for empresa in tabela_empresas['Empresas']:
    print(empresa)
    cotacao = web.DataReader(f'{empresa}.SA', data_source='yahoo', start="01-01-2021", end="02-01-2021")
    display(cotacao)
    cotacao["Adj Close"].plot(figsize=(15, 10))
    plt.show()
