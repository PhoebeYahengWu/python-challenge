import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

totalMonths = 0
total = 0
Profit_Losses = []
change = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        totalMonths = totalMonths + 1
        total = total + int(row[1])
        Profit_Losses.append(int(row[1]))




for i in range(1,len(Profit_Losses)):
    change.append(Profit_Losses[i]-Profit_Losses[i-1])
    i = i + 1

print(round(sum(change)/len(change),2))