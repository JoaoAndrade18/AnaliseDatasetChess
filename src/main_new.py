# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 15:25:17 2023

@author: artur
"""

import csv
import numpy as np
import matplotlib.pyplot as plt

# %% funcao de sequencias
def getSeqs(arr, obj=None):
    '''
    

    Parameters
    ----------
    arr : TYPE
        DESCRIPTION.
    obj : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    Example
    -------
    [5,5,5,9,9,5,9,5,9,9,9]
        
    '''    
    last = arr[0]
    res = [ [1, last] ]
    for i in range(len(arr[1:])):
        if(arr[i] == last):
            res[-1][0] += 1
        else:
            last = arr[i]
            res.append( [ 1, last ] )
            
    
    if(obj != None):
        nres = []
        for r in res:
            if(r[1] == obj):
                nres.append(r[0])
        if(len(nres) == 0):
            return [0]
        return nres
    return res

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
plt.hist(count_movements_match, color='red')
plt.title('Distribuicao de movimentos por partidas')

# %% Pegar movimentos
count_agrees = []
#getPositions(move)
# Quantidade de movimentos que coincidem por partida

for match in matches:
    count_agrees.append( 0 )
    for move in match:
        if(move[1] == move[3]):
            count_agrees[-1] += 1

plt.figure()
plt.hist(count_agrees)

# %% By players
count_rates_players = []
j = 0
id_one_mov = []

for match in matches[:-1]:
    if(len(match)==1):
        id_one_mov.append(j)
        j += 1
        continue
    whites = []
    blacks = []
    for i in range(len(match)):
        if( i % 2 == 0 ):
            whites.append( match[i] )
        else:
            blacks.append( match[i] )
            
    tax_whites = [i[-1] for i in whites]
    seqs_whites = max(getSeqs(tax_whites, 'True'))
    tax_true_whites = tax_whites.count('True')
    
    tax_blacks = [i[-1] for i in blacks]
    seqs_blacks = max(getSeqs(tax_blacks, 'True'))
    tax_true_blacks = tax_blacks.count('True')
    
    count_rates_players.append( [ len(tax_whites),  tax_true_whites, tax_true_whites/len(tax_whites), seqs_whites ])
    count_rates_players.append( [ len(tax_blacks),  tax_true_blacks, tax_true_blacks/len(tax_blacks), seqs_blacks ])
    j += 1
    
#%% Comparar duas variáveis
# plt.figure()
fig, ax = plt.subplots()
count_rates_players = np.array(count_rates_players)
ax.scatter(count_rates_players[:,0], count_rates_players[:,2], marker='*', color='purple')
ax.set_ylabel('Razão de movimentos coincidentes com total', fontsize=15)
ax.set_xlabel('Total de movimentos', fontsize=15)
plt.show()

# %% Sequencias
fig, ax = plt.subplots()
count_rates_players = np.array(count_rates_players)
ax.scatter(count_rates_players[:,0], count_rates_players[:,3], marker='*', color='green')
ax.set_ylabel('Maior sequencia', fontsize=15)
ax.set_xlabel('Total de movimentos', fontsize=15)
plt.show()

# %% 
