import csv
import matplotlib.pyplot as plt

games = []
with open('analyzes-complete-final.csv', mode='r') as file:
    csv_data = csv.reader(file)
    for row in csv_data:
        games.append(row)

# Separar partidas em matches
matches = [[]]
for row in games:
    if(row == []):
        matches.append([])
    else:
        matches[-1].append(row)

# quantidade de movimentos que coincidem por partidas
count_agrees = []
for match in matches:
    count_agrees.append( 0 )
    for move in match:
        if(move[1] == move[3]):
            count_agrees[-1] += 1

# quantidade de movimentos por partida
count_movements_match = []
for match in matches:
    count_movements_match.append( len(match) )

# Análise da frequência das aberturas (branco e preto)
opening_freq_white = {}
opening_freq_black = {}

for match in matches:
    if len(match) >= 2:  # Verifica se há movimentos para ambos os lados
        first_move_white = match[0][0]  # Cor da primeira jogada (branco)
        opening_white = match[0][1]  # Movimento de abertura do branco
        first_move_black = match[1][0]  # Cor da primeira jogada (preto)
        opening_black = match[1][1]  # Movimento de abertura do preto

        # Para as jogadas do branco
        if first_move_white not in opening_freq_white:
            opening_freq_white[first_move_white] = {}
        if opening_white not in opening_freq_white[first_move_white]:
            opening_freq_white[first_move_white][opening_white] = 1
        else:
            opening_freq_white[first_move_white][opening_white] += 1

        # Para as jogadas do preto
        if first_move_black not in opening_freq_black:
            opening_freq_black[first_move_black] = {}
        if opening_black not in opening_freq_black[first_move_black]:
            opening_freq_black[first_move_black][opening_black] = 1
        else:
            opening_freq_black[first_move_black][opening_black] += 1

# Porcentagem de movimentos que coincidem por partida
percentage_agrees = []
for match in matches:
    total_moves = len(match)
    if total_moves > 0:
        agrees = sum(1 for move in match if move[1] == move[3])
        percentage = (agrees / total_moves) * 100
        percentage_agrees.append(percentage)
print(len(percentage_agrees))

# Gerar histograma
plt.figure()
plt.hist(percentage_agrees, bins=20, edgecolor='black')
plt.title('Porcentagem de Movimentos que Coincidem por Partida')
plt.xlabel('Porcentagem')
plt.ylabel('Número de Partidas')
plt.show()


# white
plt.figure()
for color, openings in opening_freq_white.items():
    openings_sorted = dict(sorted(openings.items(), key=lambda item: item[1], reverse=True))
    plt.bar(openings_sorted.keys(), openings_sorted.values(), label=f"{color} - Abertura")
    plt.title('Frequência das Aberturas')
    plt.xlabel('Movimento de Abertura')
    plt.ylabel('Quantidade')
    plt.legend()
    plt.show()

# black
plt.figure()
for color, openings in opening_freq_black.items():
    openings_sorted = dict(sorted(openings.items(), key=lambda item: item[1], reverse=True))
    plt.bar(openings_sorted.keys(), openings_sorted.values(), label=f"{color} - Abertura")
    plt.title('Frequência das Aberturas')
    plt.xlabel('Movimento de Abertura')
    plt.ylabel('Quantidade')
    plt.legend()
    plt.show()

# %% Gerar gráficos
plt.figure()
plt.hist(count_agrees)
plt.title('movimentos que coincidem com o movimento do motor por partida')
plt.show()

plt.figure()
plt.hist(count_movements_match)
plt.title('Distribuicao de movimentos por partidas')
plt.show()

plt.figure()
plt.boxplot(count_movements_match)
plt.title('Distribuicao de movimentos por partidas com boxplot')
plt.show()
