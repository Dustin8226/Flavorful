# Program name: DiRocco_Dustin_Final
# Author: Dustin DiRocco
# Date: 4/12/22
# Summary: Program will read a file that lists the ages, add them together and get the average. 
# Variables
#   AvAge: The average age of those who took the survey

#Code reads all the ages, gets the average and prints it
def AvAge():
    #file name is AvAge.txt
    filename = input("Enter a file name: ")
    with open(filename) as f:
        data = [int(line) for line in f]

    print ("There were" , len(data) , "numbers in the file.")
    print ("The average is ", sum(data)/len(data), ".")

AvAge()
