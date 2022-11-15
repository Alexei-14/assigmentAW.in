import csv

def searchID():
    flag = 0
    Uid = input("Enter the UID you want to search: ")
    csvFile = csv.reader(open('users-sorted.csv','r'))

    for row in csvFile:
        if Uid == row[0]:
            print(row)
            flag = 1
    
    if flag == 0:
        print("No user avaliable wih this Unique ID") 

def searchName():
    flag = 0
    Uid = input("Enter the User name you want to search: ")
    csvFile = csv.reader(open('users-sorted.csv','r'))

    for row in csvFile:
        if Uid == row[1]:
            print(row)
            flag = 1
    
    if flag == 0:
        print("No user avaliable wih this User Name") 


searchID()
searchName()
