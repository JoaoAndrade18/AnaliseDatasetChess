# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:16:54 2024

@author: PC
"""
import csv

players = []


Unknown = []

with open('table_players_id.csv', mode='r') as file:
    csv_data = csv.reader(file)
    for row in csv_data: 
        # Decidir a Tax
        if row[2] > row[3]:
            players.append( [ row[0], str(row[2]) ] )    
        elif row[2] < row[3]:
            players.append( [ row[1], str(row[3]) ] )                          
        else:
            Unknown.append(row)