import csv
from collections import Counter

with open("HeightWeight.csv", newline='') as f :
    reader =csv.reader(f)
    file_data= list(reader)

file_data.pop(0)

newData = []

for i in range(len(file_data)):
    number = file_data[i][1]
    newData.append(float(number))

data = Counter(newData)

mode_data_range= {
    "50 - 60": 0,
    "60 - 70": 0,
    "70 - 80": 0
}

for height, occurence in data.items():
    if 50 < float(height) < 60 :
        mode_data_range["50 - 60"] += occurence
    elif 60 < float(height) < 70:
        mode_data_range["60 - 70"] += occurence
    elif 70 < float(height) < 80:
        mode_data_range["70 - 80"] += occurence

mode_range = 0
mode_occurence = 0

for range, occurence in mode_data_range.items():
    if occurence > mode_occurence: 
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence

mode = float((mode_range[0] + mode_range[1])/2)
print(f"mode is {mode: 2f}")