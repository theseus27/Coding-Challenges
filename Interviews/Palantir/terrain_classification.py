import math
import os
import random
import re
import sys

#(W)ater, (S)and, (G)rass, (T)rees, (R)ocks

#Terrain    Test Cases      Requirements
#River      0,1,2,18        Unbroken line of W row/column/diag
                            #Found river on 11, when there shouldn't be one
                            #Has to be going up and down OR sideways if sideways is          
                            #longer than vertical??
#Highland   3,4,23          At least 1 elevation over 800
#Waterfall  6,7,10          3 water across, 3 water below w/ lower elevation 
                            #(each row has to be the same?)
                            #Actually it might just be 2 across
#Cliff      5,7,9           Row of rocks above row of rocks/trees w/ lower elevation
                            #Just 1 across??
                            #It could just be rock above anything
                            #14 seems like it should be a cliff but isn't
#Lake       8,12,15
#Beach                      #Bottom row or right column is all R or S, and at least 1 S
#Forest     21,24

#8 vs 9 is weird they seem similar but only 9 is a cliff

def find_river(elevations, features, rows, columns):
    sand = False
    for i in range(rows):
        for j in range(columns):
            if features[i][j] == "S": sand = True      
    #Check columns
    for i in range(columns):
        col = []
        for j in range(rows):
            col.append(features[j][i])
        if col.count("W") == rows: 
            return True
        if col[-1] == "R" and col.count("W") == rows-1:
            return True
        if col[0] == "R" and col.count("W" == rows-1):
            return True
    #Check rows
    #0,1,2,18,30,31,32
    for i in features:
        if i.count("W") == columns and not sand: 
            return True
    #Check diagonals
    d1 = []
    d2 = []
    if (rows == columns):
        for i in range(rows):
            d1.append(features[i][i])
            d2.append(features[i][rows-1-i])
        if d1.count("W") == rows or d2.count("W") == rows: 
            return True
    return False

def find_highland(elevations, features, rows, columns):
    for i in range(rows):
        for j in range(columns):
            if elevations[i][j] >= 800: return True
    return False

def find_waterfall(elevations, features, rows, columns):
    for i in range(rows-1):
        for j in range(columns-1):
            if features[i][j] == "W" and features[i][j+1] == "W" and elevations[i][j] == elevations[i][j+1]:
                if features[i+1][j] == "W" and features[i+1][j+1] == "W" and elevations[i+1][j] == elevations[i+1][j+1]:
                    if elevations[i][j] > elevations[i+1][j] and elevations[i][j+1] > elevations[i+1][j+1]: return True
    return False

def find_cliff(elevations, features, rows, columns):
    allowed = ["R", "T", "W"]
    for i in range(rows):
        for j in range(columns):
            if features[i][j] == "S": return False
        
    for i in range(rows-1):
        for j in range(columns):
            if features[i][j] == "R" and elevations[i][j] >= 50:
                if features[i+1][j] in allowed and elevations[i+1][j] < elevations[i][j]:
                    return True
    return False

def find_lake(elevations, features, rows, columns):
    for i in range(rows-2):
        for j in range(columns-2):
            elevsquare = []
            featsquare = []
            for k in range(i, i+3):
                for l in range(j, j+3):
                    elevsquare.append(elevations[k][l])
                    featsquare.append(features[k][l])
            if featsquare.count("W") == 9 and elevsquare.count(elevsquare[0]) == 9:
                return True
    return False

def find_beach(elevations, features, rows, columns):
    if features[rows-1].count("S") > 0 and features[rows-1].count("S") + features[rows-1].count("R") == columns:
        if features[rows-2].count("S") > 0 and features[rows-2].count("S") + features[rows-2].count("R") == columns:
            return True
    
    secright = []
    right = []
    for i in range(rows):
        right.append(features[i][columns-1])
        secright.append(features[i][columns-2])
    if right.count("S") > 0 and right.count("S") + right.count("R") == rows: 
        if secright.count("S") > 0 and secright.count("S") + secright.count("R") == rows: 
            return True 
    
    return False

def find_forest(elevations, features, rows, columns):
    for i in range(rows-2):
        for j in range(columns-2):
            if features[i][j] == "T" and features[i+1][j] == "T" and features[i+2][j] == "T":
                return True
            if features[i][j] == "T" and features[i][j+1] == "T" and features[i][j+2] == "T":
                return True
    return False

def findTerrainTypes(elevations, features):
    rows = len(elevations)
    columns = len(elevations[0])
    terrains = []
    
    if find_river(elevations,features, rows, columns):
        terrains.append("river")
    
    if find_highland(elevations, features, rows, columns):
        terrains.append("highland")
        
    if find_waterfall(elevations, features, rows, columns):
        terrains.append("waterfall")
        
    if find_cliff(elevations, features, rows, columns):
        terrains.append("cliff")
    
    #Lake
    if find_lake(elevations, features, rows, columns):
        terrains.append("lake")
    
    #Beach
    if find_beach(elevations, features, rows, columns):
        terrains.append("beach")
    
    #Forest
    if find_forest(elevations, features, rows, columns):
        terrains.append("forest")
    
    
    return terrains