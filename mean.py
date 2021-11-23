import csv 
with open("HeightWeight.csv", newline='') as f: 
    reader = csv.reader(f)
    file_data= list(reader)

file_data.pop(0)

newData = [] 

for i in range(len(file_data)) :
    number = file_data[i][1] 
    newData.append(float(number))

n = len(newData)
total = 0

for x in newData:
    total = total + x

mean = total/n
print("The mean/average is " + str(mean))