import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

totalMonths = 0
total = 0
Date = []
Profit_Losses = []
change = []



with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        totalMonths = totalMonths + 1
        total = total + int(row[1])
        Date.append(row[0])
        Profit_Losses.append(int(row[1]))


for i in range(1,len(Profit_Losses)):
    change.append(Profit_Losses[i]-Profit_Losses[i-1])

dictionary = dict(zip(Date[1:], change))

averageChange = round(sum(change)/len(change),2)

greatestIncrease = max(change)
greatestDecrease = min(change)

for x in dictionary:
    if(dictionary[x]==greatestIncrease):
        greatestIncreaseDate = x
    if(dictionary[x]==greatestDecrease):
        greatestDecreaseDate = x

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${total}")
print(f"Average  Change: ${averageChange}")
print(f"Greatest Increase in Profits: {greatestIncreaseDate} (${greatestIncrease})")
print(f"Greatest Decrease in Profits: {greatestDecreaseDate} (${greatestDecrease})")



file_to_output = os.path.join("analysis", "output.txt")
with open(file_to_output, "w") as txt_file:
    line1 = "Financial Analysis"
    line2 = "----------------------------"
    line3 = f"Total Months: {totalMonths}"
    line4 = f"Total: ${total}"
    line5 = f"Average  Change: ${averageChange}"
    line6 = f"Greatest Increase in Profits: {greatestIncreaseDate} (${greatestIncrease})"
    line7 = f"Greatest Decrease in Profits: {greatestDecreaseDate} (${greatestDecrease})"
    txt_file.write('{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(line1, line2, line3, line4, line5, line6, line7))