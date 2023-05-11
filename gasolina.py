import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df_gasolina= pd.read_csv('gasolina.csv')
grafico_preco=sns.lineplot(x='dia', y='venda', data=df_gasolina)
plt.savefig('grafico_preco.png')