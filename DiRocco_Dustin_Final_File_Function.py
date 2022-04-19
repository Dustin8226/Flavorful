# Program name: DiRocco_Dustin_Final_Function
# Author: Dustin DiRocco
# Date: 4/12/22
# Summary: Program will use different functions to read files and list the favorites in order
# Variables

def FavDessert():
    f = open("FavDessert.txt" , "r")
    for x in f:
        print(x)
    f.close()

def FavCake():
    f = open("FavCake.txt" , "r")
    for x in f:
        print(x)
    f.close()

def FavIceCream():
    f = open("FavIC.txt" , "r")
    for x in f:
        print(x)
    f.close()

def FavPie():
    f = open("FavPie.txt" , "r")
    for x in f:
        print(x)
    f.close()


