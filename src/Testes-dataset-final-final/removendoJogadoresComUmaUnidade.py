# %% 

import csv
from collections import Counter

# Lista para armazenar todos os jogadores
all_players_white = []
all_players_black = []
all_players = []
# Abrindo o arquivo CSV
with open('../analyzes-complete-final-final.csv', mode='r') as file:
    csv_data = csv.DictReader(file, delimiter=',')
    # for row in csv_data:
    #     # Adicionando todos os jogadores white à lista
    #     all_players_white.extend(row[' white_id'].strip().split(","))

    # for row in csv_data:
    #     # Adicionando todos os jogadores black à lista
    #     all_players_black.extend(row[' black_id'].strip().split(","))

    for row in csv_data:
        # Adicionando todos os jogadores à lista
        all_players.extend(row[' white_id'].strip().split(","))
        all_players.extend(row[' black_id'].strip().split(","))

# Contando ocorrências de cada jogador
player_counts = Counter(all_players)
# player_whites_counts = Counter(all_players_white)
# player_black_counts = Counter(all_players_black)

# Criando a lista final com jogadores que aparecem mais de uma vez
players_multiple_occurrences = [player for player, count in player_counts.items() if count > 1]

dict_players = {}
# passe o conteudo de player_counts para dict_players
for player, count in player_counts.items():
    dict_players[player] = count


dic_more_moves = {}
dict_one_move = {}
for player, count in dict_players.items():
    if count > 5:
        dic_more_moves[player] = count
    else:
        dict_one_move[player] = count


listaComOsJogadoresSelecionados = [[]]
for player, count in dic_more_moves.items():
    listaComOsJogadoresSelecionados[-1].append(str(player)) 
    listaComOsJogadoresSelecionados[-1].append(str(count))
    listaComOsJogadoresSelecionados.append([])
        

# mostrar o jogador com o maior numero de partidas

maior = 0
for player, count in dic_more_moves.items():
    if count > maior:
        maior = count
        name = player
        
print(f"maior numero de partidas: {maior}, jogador: {name}")
