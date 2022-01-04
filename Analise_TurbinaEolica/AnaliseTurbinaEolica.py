import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from IPython.display import display

turbina = pd.read_csv('T1.csv')
# print(list(turbina.columns)) MOSTRA TODAS AS COLUNAS EM UMA LISTA

turbina.columns = ['Data/hora', 'ActivePower(kW)', 'WindSpeed(m/s)', 'CurvaTeórica(kWh)', 'DireçãoVento(°)']
del turbina['DireçãoVento(°)']
turbina['Data/hora'] = pd.to_datetime(turbina['Data/hora'])
display(turbina)

sns.scatterplot(data=turbina, x='WindSpeed(m/s)', y='ActivePower(kW)')
plt.show()

sns.scatterplot(data=turbina, x='WindSpeed(m/s)', y='CurvaTeórica(kWh)')
plt.show()

pot_real = turbina['ActivePower(kW)'].tolist()
pot_teorica = turbina['CurvaTeórica(kWh)'].tolist()
pot_max = []
pot_min = []
dentro_limite = []

for potencia in pot_teorica:
    pot_max.append(potencia*1.05)
    pot_min.append(potencia*0.95)

for p, potencia in enumerate(pot_real):
    if potencia >= pot_min[p] and potencia <= pot_max[p]:
        dentro_limite.append('Dentro')
    elif potencia == 0:
        dentro_limite.append('Zero')
    else:
        dentro_limite.append('Fora')

print(dentro_limite.count('Dentro')/len(dentro_limite))

turbina['DentroLimite'] = dentro_limite
display(turbina)

cores = {'Dentro': 'blue', 'Fora': 'red', 'Zero': 'orange'}
sns.scatterplot(data=turbina, x='WindSpeed(m/s)', y='ActivePower(kW)', hue='DentroLimite', s=1, palette=cores)
plt.show()
