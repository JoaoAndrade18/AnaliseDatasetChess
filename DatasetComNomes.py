import csv

# quantidade de players {white_id, black_id}
def players():
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

    print(len(white_id), len(black_id))
    print(white_id[0], black_id[0])

def remove_duplicados():
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

    # Removendo os valores duplicados
    white_id = list(set(white_id))
    black_id = list(set(black_id))

    # Somando a quantidade de players
    quantidade_de_players = white_id + black_id
    quantidade_de_players = list(set(quantidade_de_players))
    quantidade_de_players = len(quantidade_de_players)
    print(quantidade_de_players)

def combined():
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

    combined_ids = list(zip(white_id, black_id))
    print(len(combined_ids))
    print(combined_ids[1])

if __name__ == "__main__":
    remove_duplicados()


