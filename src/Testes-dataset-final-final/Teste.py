import matplotlib.pyplot as plt
import numpy as np

# Dados de disponibilidade e desvio padrão
disponibilidade = {
    'sem HPA': np.array([17.4]),
    'com HPA': np.array([98.7])
}

desvio_padrao = {
    'sem HPA': np.array([4.5]),
    'com HPA': np.array([3.6])
}

# Preparando os dados para o gráfico
labels = list(disponibilidade.keys())
values = [value[0] for value in disponibilidade.values()]
errors = [error[0] for error in desvio_padrao.values()]

# Calculando o topo do erro relativo à disponibilidade
top_errors = [min(value + error, 100) - value for value, error in zip(values, errors)]

# Definindo cores para as barras e os erros
bar_colors = ['lightblue', 'darkorange']
error_colors = ['black', 'black']

# Criando o gráfico de barras
fig, ax = plt.subplots()
bars = ax.bar(labels, values, color=bar_colors)

# Adicionando barras de erro relativas ao topo da barra
for i, (label, value) in enumerate(zip(labels, values)):
    ax.errorbar(label, value, yerr=[[errors[i]], [top_errors[i]]], elinewidth=1, capsize=3, color=error_colors[i], barsabove=True, capthick=1, errorevery=1, ecolor=error_colors[i])

# Adicionando os valores de desvio padrão acima das barras
for i, label in enumerate(labels):
    ax.text(label, values[i] + 1, f'{errors[i]:.2f}', ha='right', va='bottom', color='black')

# Configurações do gráfico
ax.set_title('Disponibilidade do sistema com e sem HPA')
plt.ylabel('Disponibilidade (%)')

# Criando as legendas manualmente com as cores
legend_labels = ['Sem HPA', 'Com HPA']
legend_colors = [bar_colors[0], bar_colors[1]]
ax.legend(bars, legend_labels, loc='upper left')
# ax.legend(legend_colors, legend_labels, loc='upper left')

plt.style.use('seaborn-v0_8-darkgrid')
plt.grid(True, linestyle='--', alpha=0.7)

# Exibindo o gráfico
ax.set_xticks(range(0, len(values)))
ax.set_xticklabels([f'{value}%' for value in values], fontsize=12)
plt.show()
