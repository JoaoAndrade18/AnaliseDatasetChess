# %% criar tabela de exemplo para um jogador com mais de uma ocorrencia


import matplotlib.pyplot as plt
import csv
from matplotlib.markers import MarkerStyle

data = []
with open('../analyzes-complete-final-final.csv', mode='r') as file:
    csv_data = csv.DictReader(file, delimiter=',')
    for row in csv_data:
        # if row[' white_id'].strip() == 'daniel_likes_chess': 
        #     data.append(row[' jogadas_white'].split("|"))
        if row[' black_id'].strip() == 'taranga': 
            data.append(row[' jogadas_black'].split("|"))
            
array_x = []       
array_y = []
# start_positions = []  
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


for end_x, end_y, l in end_positions:
    plt.axhline(y=end_y, xmax=l/comprimento, color='gray', linestyle='-', linewidth=0.5)
    # plt.axhline(y=end_y, xmin=end_x, xmax=end_x+1, color='gray', linestyle='--', linewidth=0.5)
plt.yticks(range(len(data)), [f'{i}' for i in range(len(data))])
plt.yscale('linear')
plt.xticks(range(0, comprimento, 5), [f'{i}' for i in range(0, comprimento, 5)])
# adicionar grade
# plt.grid(True)

# corta o eixo y para comprimir o gráfico
# plt.ylim(-1, len(data))
plt.style.use('seaborn-v0_8-ticks')
plt.grid(True, linestyle='--', alpha=0.7)

# adicionar labels
plt.ylabel('Numero de Partidas')
plt.xlabel('Numero de Movimentos')
plt.title("Taranga - Jogadas por Partida")
plt.show()
# %%
