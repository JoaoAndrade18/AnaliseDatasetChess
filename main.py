# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 15:25:17 2023

@author: artur
"""

import csv
import matplotlib.pyplot as plt

# %% 
data = []
with open('analyzes-complete-final.csv', mode='r') as file:
    csv_data = csv.reader(file, delimiter=',')
    
    for row in csv_data:
        data.append(row)

# Separar partidas em matches
matches = [[]]
for row in data:
    if(row == []):
        matches.append([])
    else:
        matches[-1].append(row)

# %% Distribuição dos movimentos
count_movements_match = []
for match in matches:
    count_movements_match.append( len(match) )

# %% Descricao
print( 'Numero de partidas: %d' %  len(matches) )
print( 'Numero de movimentos: %d' %  len(data) )


# %% Gerar gráficos
plt.figure()
plt.hist(count_movements_match)
plt.title('Distribuicao de movimentos por partidas')

plt.figure()
plt.boxplot(count_movements_match)
# plt.title('Distribuicao de movimentos por partidas')

# %% Pegar movimentos
count_agrees = []
#getPositions(move)

for match in matches:
    count_agrees.append( 0 )
    for move in match:
        if(move[1] == move[3]):
            count_agrees[-1] += 1


plt.figure()
plt.hist(count_agrees)
