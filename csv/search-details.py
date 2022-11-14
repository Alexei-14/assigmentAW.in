import csv

def search():
    flag = 0
    Uid = input("Enter the you want to search: ")
    csvFile = csv.reader(open('users-sorted.csv','r'))

    for row in csvFile:
        if Uid == row[0]:
            print(row)
            flag = 1
    
    if flag == 0:
        print("No user avaliable wih this Unique ID") 
    

search()