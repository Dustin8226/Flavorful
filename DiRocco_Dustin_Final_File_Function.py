# Program name: DiRocco_Dustin_Final_Function
# Author: Dustin DiRocco
# Date: 4/12/22
# Summary: Program will use different functions to read files and list the favorites in order
# Variables:
#   FavDessert is the favorite dessert
#   FavCake is the favorite cake flavor
#   FavIceCream is the favorite ice cream flavor
#   FavPie is the favorite pie flavor

#Code reads the files from the surveys taken and prints off the results.

def FavDessert():
    f = open("FavDessert.txt" , "r")
    lines = f.read().split('\n')
    print(lines)

def FavCake():
    f = open("FavCake.txt" , "r")
    lines = f.read().split('\n')
    print(lines)
    
def FavIceCream():
    f = open("FavIceCream.txt" , "r")
    lines = f.read().split('\n')
    print(lines)
    
def FavPie():
    f = open("FavPie.txt" , "r")
    lines = f.read().split('\n')
    print(lines)

FavDessert()
FavCake()
FavIceCream()
FavPie()
