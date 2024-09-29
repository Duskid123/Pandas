# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd

def GetLists():
    Price = []
    Maintenance_cost =[] 
    Number_of_Doors = []
    Passengers = []
    Luggage = []
    Saftey_Rating = []
    Classification = []
    with open("./cars-sample35.txt", "r") as file:
        for spot in file:
          spot = spot.replace('\n', '')
          list = spot.split(",")
          Price.append(list[0])
          Maintenance_cost.append(list[1])
          Number_of_Doors.append(list[2])
          Passengers.append(list[3])
          Luggage.append(list[4])
          Saftey_Rating.append(list[5])
          Classification.append(list[6])          
    return [Price, Maintenance_cost, Number_of_Doors, Passengers, Luggage, Saftey_Rating, Classification]


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
    lists = GetLists()
    
    medPricedIndex = getMedPricedIndecies(lists[0])
    
    Passengers = []
    for value in medPricedIndex:
        Passengers.append(lists[3][value])
    print(Passengers)
    
    highRoller = getHighPricedAndNotLowMaintenenceIndecies(lists[0], lists[1])
    print(highRoller)
    
    listComp = [index for index, value in enumerate(lists[0]) if value == 'med']
    print(listComp)
    
    listComp2 = [lists[3][index] for index in listComp]
    print(listComp2)
    
    listComp3 = [i for i, value in enumerate(lists[0]) if value == 'high' if lists[1][i] != 'low']
    
    print(listComp3)
    
    Cov = pd.read_csv("cars-sample35.txt", sep=',', 
                      names=['Price', 'Maintenance cost', 'Number of doors', 
                                         'Number of passengers', 'Luggage capacity', 
                                         'Safety rating', 'Classification of vehicle'])
    print(Cov)
    
if __name__ == "__main__":
    main()