# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 15:25:17 2023

@author: artur
"""

# %%
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

# %% open csv of analyzes
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
        
# %% open csv of games
white_id = []
with open('games.csv', mode='r') as file:
    csv_data = csv.reader(file)
    for row in csv_data: 
        white_id.append(row[8])    
    white_id = white_id[1:]

black_id = []
with open('games.csv', mode='r') as file:
    csv_data = csv.reader(file)
    for row in csv_data: 
        black_id.append(row[10]) 
    black_id = black_id[1:]

matches_ids = []

for i, match in enumerate(matches):
    matches_ids.append( [ white_id[i], black_id[i], match ] )


# %% Distribuição dos movimentos
count_movements_match = []
for match in matches:
    count_movements_match.append( len(match) )

# %% Descricao
# print( 'Numero de partidas: %d' %  len(matches) )
# print( 'Numero de movimentos: %d' %  len(data) )


# %% Gerar gráficos
# plt.figure()
# plt.hist(count_movements_match, color='red')
# plt.title('Distribuicao de movimentos por partidas')

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
plt.title('Quantidade de movimentos que coincidem por partida')

# %% By players
count_rates_players = []
j = 0
id_one_mov = []

# Variavel retangular de movimentos: 80% < movements > total_moves == 10 
focus_moves = []

# Identificador para cada match
match_id = []

match_players = []

count_match_players_id = []

focus_match_players_id = []

for id, match in enumerate(matches):
    if(len(match)==1):
        id_one_mov.append(j)
        j += 1
        continue
    whites = []
    blacks = []
    for i in range(len(match)):
        if( i % 2 == 0 ):
            whites.append( match[i] )
            match_players.append( [ id, match[i] ] )
        else:
            blacks.append( match[i] )
            match_players.append( [ id, match[i] ] )
            
    match_id.append(id)

    tax_whites = [i[-1] for i in whites]
    seqs_whites = max(getSeqs(tax_whites, 'True'))
    tax_true_whites = tax_whites.count('True')
    
    tax_blacks = [i[-1] for i in blacks]
    seqs_blacks = max(getSeqs(tax_blacks, 'True'))
    tax_true_blacks = tax_blacks.count('True')
    
    
    count_rates_players.append( [ len(tax_whites),  tax_true_whites, tax_true_whites/len(tax_whites), seqs_whites ])
    count_rates_players.append( [ len(tax_blacks),  tax_true_blacks, tax_true_blacks/len(tax_blacks), seqs_blacks ])
    
    count_match_players_id.append( [ id, len(tax_whites), tax_true_whites/len(tax_whites), ] )
    count_match_players_id.append( [ id, len(tax_blacks), tax_true_blacks/len(tax_blacks), ] )

    
    if (len(tax_whites) >= 10) and (tax_true_whites/len(tax_whites) >= 0.8):
        focus_moves.append( [ len(tax_whites), tax_true_whites/len(tax_whites) ] )
        focus_match_players_id.append( [ id, len(tax_whites), tax_true_whites/len(tax_whites) ] )
    
    if (len(tax_blacks) >= 10) and (tax_true_blacks/len(tax_blacks) >= 0.8):
        focus_moves.append( [ len(tax_blacks), tax_true_blacks/len(tax_blacks) ] )
        focus_match_players_id.append( [ id, len(tax_blacks), tax_true_blacks/len(tax_blacks) ] )   
    
    j += 1

    
#%% Comparar duas variáveis
# plt.figure()
fig, ax = plt.subplots()
count_rates_players = np.array(count_rates_players)
ax.scatter(count_rates_players[:,0], count_rates_players[:,2], marker='*', color='purple', alpha=0.5)
ax.set_ylabel('Razão de movimentos coincidentes', fontsize=12.5)
ax.set_xlabel('Total de movimentos por player', fontsize=15)
plt.show()

fig.savefig("./images/razao-de-movimentos-coincidentes.png") 

# %% Sequencias
fig, ax = plt.subplots()
count_rates_players = np.array(count_rates_players)
ax.scatter(count_rates_players[:,0], count_rates_players[:,3], marker='*', color='green', alpha=0.5)
ax.set_ylabel('Maior sequencia', fontsize=15)
ax.set_xlabel('Total de movimentos por player', fontsize=15)
plt.show()

fig.savefig("./images/maior-sequencia-movimentos.png") 

# %% focus moves
fig, ax = plt.subplots()
focus_moves = np.array(focus_moves)
ax.scatter(focus_moves[:,0], focus_moves[:,1], marker='*', color='blue', alpha=0.5)
ax.set_ylabel('Razão de movimentos coincidentes', fontsize=12.5)
ax.set_xlabel('Total de movimentos por player', fontsize=15)
plt.show()

fig.savefig("./images/razao-de-movimentos-coincidentes-80-percento.png") 


# %% focus moves v2
focus_moves = np.array(focus_moves)
plt.hist2d(focus_moves[:,0], focus_moves[:,1], bins=40, cmap='Blues')
plt.colorbar()

# %% Tabela com ids
table_players_id = []

tax_percent_ids = []

final_list_ids = []

for i in range(187):
    table_players_id.append(focus_match_players_id[i][0])
    
for a in range(187): 
     final_list_ids.append(matches_ids[table_players_id[a]])
     
for b in range(40076):
    if count_match_players_id[b][0] in table_players_id:
        tax_percent_ids.append(count_match_players_id[b][2])

with open('table_players_id.csv', "w", newline='') as file:
    for j, index in enumerate(final_list_ids):
        file.write( f"{ index[0] }, { index[1] }, { tax_percent_ids[j*2] }, { tax_percent_ids[j*2+1] } \n" )      
    file.write("\n")
    
    
    
# %%
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5)) # 1 linha, 2 colunas

# # Plotando o primeiro conjunto de dados no primeiro subplot
# ax1.bar(count_rates_players[:,0], count_rates_players[:,3], color='purple', alpha=0.5)
# ax1.set_ylabel('Razão de movimentos coincidentes', fontsize=12.5)
# ax1.set_xlabel('Total de movimentos por player', fontsize=15)
# ax1.set_title('Gráfico 1')

# # Plotando o segundo conjunto de dados no segundo subplot
# ax2.bar(count_rates_players[:,0], count_rates_players[:,3], color='blue', alpha=0.5)
# ax2.set_ylabel('Razão de movimentos coincidentes', fontsize=12.5)
# ax2.set_xlabel('Total de movimentos por player', fontsize=15)
# ax2.set_title('Gráfico 2')

# # Ajustando o layout para melhor visualização
# plt.tight_layout()

# # Exibição do gráfico
# plt.show()

