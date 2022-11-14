# import modules
import csv ,operator

# load csv file
filename = 'users-sorted.csv'

data = csv.reader(open('user.csv'),delimiter=',')

# sort data on the basis of age
data = sorted(data, key=operator.itemgetter(1))	

# displaying sorted data
print('After sorting:')

print("Data has been sorted according to their FirstName;")

with open(filename,'w',encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)