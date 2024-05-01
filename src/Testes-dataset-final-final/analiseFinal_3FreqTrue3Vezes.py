# %% 

import csv
from collections import Counter

# Função que retorna True se o jogador tiver mais de 3 movimentos iguais em sequência
def get_player_final(data):
    freq = 0
    last = 0
    nvezes = 0
    for i in data:
        last = freq
        if i == '1':
            freq += 1
            
        elif last >=3 and i == '0':
            nvezes += 1
            freq = 0

        else:
            freq = 0

    if nvezes >= 3:
        return True
    else:
        return False

# Lista para armazenar os nomes dos jogadores e seus movimentos se forem maiores que 10	e se a função get_player_final retornar True
datawhite = [[]]
datablack = [[]]
winners = [[]]

with open('../analyzes-complete-final-final.csv', mode='r') as file:
    csv_data = csv.DictReader(file, delimiter=',')
    for row in csv_data:
        if row[' jogadas_white'].strip().split("|") != ['']:
            data = row[' jogadas_white'].strip().split("|")
            if len(data) >= 10:
                if get_player_final(data):
                    datawhite[-1].append(row[' white_id'].strip())
                    datawhite[-1].append(data)
                    datawhite.append([])
                    winners[-1].append(str('white'))
                    winners[-1].append(row[' white_id'].strip())
                    winners[-1].append(row[' winner'].strip())
                    winners[-1].append(row[' white_rating'].strip())
                    winners[-1].append(row[' black_rating'].strip())
                    winners.append([])

        if row[' jogadas_black'].strip().split("|") != ['']:
            data = row[' jogadas_black'].strip().split("|")
            if len(data) >= 10:
                if get_player_final(data):
                    datablack[-1].append(row[' black_id'].strip())
                    datablack[-1].append(data)
                    datablack.append([])
                    winners[-1].append(str('black'))
                    winners[-1].append(row[' black_id'].strip())
                    winners[-1].append(row[' winner'].strip())
                    winners[-1].append(row[' black_rating'].strip())
                    winners[-1].append(row[' white_rating'].strip())
                    winners.append([])
datawhite.pop()
datablack.pop()
winners.pop()

# %% Lista com os nomes unicos dos jogadores

nomes_unicos = set()
for linha in datawhite:
    if not linha:
        break
    nomes_unicos.add(linha[0])

for linha in datablack:
    if not linha:
        break
    nomes_unicos.add(linha[0])
nomes_unicos = list(nomes_unicos)

# %% Lista que filtra os jogadores com mais de 5 partidas

listaJogadoresFinal = []
for row in datawhite:
    for item in row:
        listaJogadoresFinal.append(item)
        break

for row in datablack:
    for item in row:
        listaJogadoresFinal.append(item)
        break

playerCounts = Counter(listaJogadoresFinal)

dict_players = {}
# passe o conteudo de playerCounts para dict_players
for player, count in playerCounts.items():
    dict_players[player] = count


# Modo dicionario
dic_more_moves = {}
winners2 = []
lastPlayer = ''
for player, count in dict_players.items():
    if count > 5:
        dic_more_moves[player] = count
        if lastPlayer != player:
            lastPlayer = player
            for row in winners:
                if row[1] == player:
                    winners2.append(row)

# Modo lista
listaComOsJogadoresSelecionados = [[]]
for player, count in dic_more_moves.items():
    listaComOsJogadoresSelecionados[-1].append(str(player)) 
    listaComOsJogadoresSelecionados[-1].append(str(count))
    listaComOsJogadoresSelecionados.append([])
listaComOsJogadoresSelecionados.pop()

# %% Lista final com os jogadores selecinados e seus movimentos

finalList = [[]]
for player in listaComOsJogadoresSelecionados:
    for row in datawhite:
        if player[0] == row[0]:
            finalList[-1].append(row[0])
            finalList[-1].append(row[1])
            finalList.append([])

    for row in datablack:
        if player[0] == row[0]:
            finalList[-1].append(row[0])
            finalList[-1].append(row[1])
            finalList.append([])
finalList.pop()


# %% Criação do(s) grafico(s)

import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle

def plot_graph(playerName, data, winners2, rating, maiorRating):
    array_x = []       
    array_y = []
    end_positions = [] 
    y = 0

    for row in data:
        x = 0
        for element in row:
            if int(element):
                array_x.append(x)
                array_y.append(y)
            x = x+1
        # start_positions.append(y)  
        end_positions.append((x, y, len(row)))    
        y = y+1

    plt.scatter(array_x, array_y, marker=MarkerStyle('|'))
    comprimento = max([len(i) for i in data])

    aux = 0
    for end_x, end_y, l in end_positions:
        # if winners2[aux][0] == winners2[aux][2]:
        #     plt.axhline(y=end_y, xmax=l/comprimento, color='green', linestyle='-', linewidth=0.5)
        #     aux += 1
        # else:
        #     plt.axhline(y=end_y, xmax=l/comprimento, color='red', linestyle='-', linewidth=0.5)
        #     aux += 1
        plt.axhline(y=end_y, xmax=l/comprimento, color='gray', linestyle='-', linewidth=0.5)
        if winners2[aux][0] == winners2[aux][2]:
            plt.plot(end_x + 1, end_y, marker='o', markersize=8, markerfacecolor='green', markeredgewidth=0)
            aux += 1
        else:
            plt.plot(end_x + 1, end_y, marker='o', markersize=8, markerfacecolor='red', markeredgewidth=0)
            aux += 1
        
    plt.yticks(range(len(data)), [f'{i}' for i in range(len(data))])
    plt.yscale('linear')
    plt.xticks(range(0, comprimento, 5), [f'{i}' for i in range(0, comprimento, 5)])

    # adicionar grade
    plt.grid(True, linestyle='--', alpha=0.7)

    # adicionar style
    plt.style.use('seaborn-v0_8-ticks')

    # adicionar legenda


    # corta o eixo y para comprimir o gráfico
    # plt.ylim(-1, len(data))

    # adicionar labels

    plt.ylabel('Number of matches')
    plt.xlabel('Number of moves')
    plt.title(f"Match of {playerName} - µ{rating} - Best:{maiorRating}")
    plt.show()

win = []
rating = []
maiorRating = 0
data = []
# iniciar com o primeiro jogador da lista
lastPlayer = finalList[0][0]
for player in finalList:
    if player[0] != lastPlayer:
        for row in winners2:
            if row[1] == str(lastPlayer):
                win.append(row)
                if row[0] == 'white':
                    rating.append(int(row[3]))
                    if int(row[3]) > maiorRating:
                        maiorRating = int(row[3])
                else:
                    rating.append(int(row[4]))
                    if int(row[4]) > maiorRating:
                        maiorRating = int(row[4])
        plot_graph(lastPlayer, data, win, round((sum(rating)/len(rating))), maiorRating)
        win.clear()
        data.clear()
        rating.clear()
        maiorRating = 0
        data.append(player[1])
        lastPlayer = player[0]
    else:
        data.append(player[1])


# %%
