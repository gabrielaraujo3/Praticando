import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC8bcc905b6f1787096da075f06d2e78f6"
# Your Auth Token from twilio.com/console
auth_token = "5847a705523db51a12b570333c59f66f"
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: R${vendas:.2f}.')
        message = client.messages.create(
            to="+5511957950047",
            from_="+12244354657",
            body=f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: R${vendas:.2f}.')
        print(message.sid)

# Para cada arquivo:

# Verificar se algum valor naquele na coluna vendas daquele

# arquivo é maior que 55.000

# Se for maior que 55.000  - Envia um SMS com o Nome, o mês e as vendas do vendedor

# Caso não seja maior que 55.000 não fazer nada