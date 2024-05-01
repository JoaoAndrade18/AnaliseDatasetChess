# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 10:41:28 2024

@author: PC
"""
# %%
# import libraries
import csv
import matplotlib.pyplot as plt

# %%
# open datasets 
with open("analyzes-complete-final.csv", "r") as file:
    reader = csv.reader(file)
    data = list(reader)

# Separar partidas em matches
matches = [[]]
for row in data:
    if(row == []):
        matches.append([])
    else:
        matches[-1].append(row)

# %% 
white_id = []
black_id = []
white_rating = []
black_rating = []
winner = []
opening_fly = []
with open("games.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        winner.append(row[6])
        opening_fly.append(row[-1])
        white_id.append(row[8])
        black_id.append(row[10])
        white_rating.append(row[9])        
        black_rating.append(row[11])
        
    winner = winner[1:]
    opening_fly = opening_fly[1:]
    white_rating = white_rating[1:]
    black_rating = black_rating[1:]
    white_id = white_id[1:]
    black_id = black_id[1:]

# %% Versao para getseq

all_plays = [[]]        
black_plays = [[]]
white_plays = [[]]
for match in matches:
    for i, row in enumerate(match):
        white_plays[-1].append( 1 if row[-1] == "True" else 0 ) if i % 2 == 0 else black_plays[-1].append( 1 if row[-1] == "True" else 0 )
        all_plays[-1].append( 1 if row[-1] == "True" else 0 )
            
    all_plays.append([])
    white_plays.append([])
    black_plays.append([])
    
white_plays2 = []
black_plays2 = []
all_plays2 = []
for partida in white_plays:
    white_plays2.append('|'.join(map(str, partida)))
    
for partida in black_plays:
    black_plays2.append('|'.join(map(str, partida)))
    
for partida in all_plays:
    all_plays2.append('|'.join(map(str, partida)))
    
# %%

# Get sequence

def getseq(game):
    max_seq = 0
    seq_atual = 0
    
    for play in game:
        if play == 1:
            seq_atual += 1
            max_seq = max(max_seq, seq_atual)
        else:
            seq_atual = 0
    
    return max_seq
    
max_seq_white = []
for game in white_plays: 
    max_seq_white.append(getseq(game))

max_seq_black = []
for game in black_plays: 
    max_seq_black.append(getseq(game))
    
    
# %% write new dataset

with open("analyzes-complete-final-final.csv", "w", newline="") as file:
    for j in range(20057):
        if j == 0:
            x =  "jogadas_all, jogadas_white, jogadas_black, white_id, black_id, winner, white_rating, black_rating, opening_fly, max_sequence_white, max_sequence_black"       
            file.write(x)
            file.write("\n")
        else:
            x = f"{all_plays2[j-1]},{white_plays2[j-1]},{black_plays2[j-1]},{white_id[j-1]},{black_id[j-1]},{winner[j-1]},{white_rating[j-1]},{black_rating[j-1]},{opening_fly[j-1]},{max_seq_white[j-1]},{max_seq_black[j-1]}"       
            file.write(x)
            file.write("\n")
            
########## O dataset final fica com 20057 partidas    
  
# %%  
# ANALISES
###############################################################
###############################################################

# %% grafico de sequencia

grafical_sequence_whites = [[]]
grafical_sequence_blacks = [[]]
data = []
with open('analyzes-complete-final-final.csv', mode='r') as file:
    csv_data = csv.reader(file, delimiter=',')
    for row in csv_data:
        data.append(row)
    data = data[1:]

for row in data:
    grafical_sequence_whites[-1].append(row[1])
    grafical_sequence_whites.append([]) 
    
for row in data:
    grafical_sequence_blacks[-1].append(row[2])
    grafical_sequence_blacks.append([])
    
# %%

grafical_sequence_whites_f = []
for i in grafical_sequence_whites:
    grafical_sequence_whites_f.append(str(i).replace('|', ','))
    
grafical_sequence_blacks_f = []
for i in grafical_sequence_blacks:
    grafical_sequence_blacks_f.append(str(i).replace('|', ','))

# %%

player_id_x_jogadas = []
for row in data:
    player_id_x_jogadas.append(row[3])
    

            
            
            
# %%

from itertools import groupby


dic = [{"nome":"joao", "idade": 23}, {"nome":"ze", "idade": 13}, {"nome":"joao", "idade": 2}, {"nome":"ze", "idade": 20}]         
for nome, pessoas in groupby(dic, key=lambda x: x["nome"]):
    print()

    