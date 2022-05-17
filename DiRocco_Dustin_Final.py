# Program name: DiRocco_Dustin_Final
# Author: Dustin DiRocco
# Date: 4/12/22
# Summary: Program will open the main function, import information from 2 seperate python files, and list the faviortes from the survey plus the average age.
# Variables:
#   Main: Main function prints out the favorite desserts, favorite cakes, favorite ice cream flavors, and favorite pie flavors
#   Age: Age function takes the average age of all who took the survey. 

# main function reads the files from the favorite desserts surveys and print them out
def main():
    print("The following import prints out the results from a survey. The first lists out the favorite desserts in order, favorite cakes, favorite ice cram flavors,"
          " and finally pie flavors:")
main()

from DiRocco_Dustin_Final_File_Function import *

# age function reads the average age file and prints out the result
def Age():
    print("The following import prints out the average age of people who took the survey. Use AvAge.txt to import this file.")
Age()

from DiRocco_Dustin_Final_average_age import *




