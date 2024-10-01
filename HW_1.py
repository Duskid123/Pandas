# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd

def getMedPricedIndecies(list):
    new_list = []
    for i in range(len(list)):
        if list[i] == 'med':
            new_list.append(i)
    return new_list

def getHighPricedAndNotLowMaintenenceIndecies(list, list2):
    new_list = []
    for i in range(len(list)):
        if list[i] == 'high':
            if list2[i] != 'low':
                new_list.append(i)
    return new_list


def main():    
    Cov = pd.read_csv("./cars-sample35.txt", sep=',', 
                      names=['Price', 'Maintenance cost', 'Number of doors', 
                                         'Number of passengers', 'Luggage capacity', 
                                         'Safety rating', 'Classification of vehicle'])
    
    medPricedIndex = getMedPricedIndecies(Cov['Price'])
    
    print(medPricedIndex)
    
    Passengers = []
    for value in medPricedIndex:
        Passengers.append(Cov['Number of passengers'][value])
    print(Passengers)
    
    highRoller = getHighPricedAndNotLowMaintenenceIndecies(
        Cov['Price'], Cov['Maintenance cost'])
    print(highRoller)
    
    listComp = [index for index, value in enumerate(Cov['Price']) if value == 'med']
    print(listComp)
    
    listComp2 = [Cov['Number of passengers'][index] for index in listComp]
    print(listComp2)
    
    listComp3 = [i for i, value in enumerate(Cov['Price']) 
                 if value == 'high' if Cov['Maintenance cost'][i] != 'low']
    
    print(listComp3)

    nlist = [[1, 2, 3], ['A', 'B', 'C'], [4, 5],['D', 'E'] ]
    
    new_list = [column for row in nlist for column in row]
    print(new_list)
    
    
if __name__ == "__main__":
    main()
