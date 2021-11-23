import csv
with open("HeightWeight.csv", newline='') as f :
    reader =csv.reader(f)
    file_data= list(reader)

file_data.pop(0)

newData = []

for i in range(len(file_data)):
    number = file_data[i][1]
    newData.append(float(number))

newData.sort()

n = len(newData)

if n%2 == 0 :
    median1 = float(newData[n//2])
    median2 = float(newData[n//2 - 1])

    median = (median1 + median2) / 2
else:
    median = newData[n//2]

print("The median is " + str(median))