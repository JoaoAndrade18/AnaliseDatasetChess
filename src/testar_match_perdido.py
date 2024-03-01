import csv

games1 = [] 
with open('games.csv', 'r') as file: 
    csvfile = csv.reader(file) 
    for linhas in csvfile:
        games1.append(linhas[4])
    games1 = games1[1:]

# tranforme games1 em int
for i in range(len(games1)):
    games1[i] = int(games1[i])


games2 = []
with open('analyzes-complete-final.csv', mode='r') as file:
    csv_data = csv.reader(file)
    for row in csv_data:
        games2.append(row)

# Separar partidas em matches
matches = [[]]
for row in games2:
    if(row == []):
        matches.append([])
    else:
        matches[-1].append(row)

# trandorme matches em int
for i in range(len(matches)):
    matches[i] = len(matches[i])

print(matches[20055])
print(games1[20055])
print(len(matches))
print(len(games1))

for i in range(20058):
    if games1[i] != matches[i]:
        print("Match perdido: ", games1[i], matches[i])
        print("Match perdido: ", i)
        # print("Jogada: ", games1[i])
        break
