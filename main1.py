# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv


csvpath = os.path.join('..', 'Resources', 'budget_data.csv')


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    column_header = next(csvreader)
    pnl = []
    change = []
    for line in csvreader:
      pnl.append([line[0],int(line[1])])
    total = 0
    for i in range(len(pnl)-1):
       total += pnl[i][1]
       change.append(pnl[i+1][1] - pnl[i][1])
       avgChange = sum(change) / len(pnl)
maxChange = max(change)
minChange = min(change)
maxChange_index = change.index(maxChange) + 1
minChange_index = change.index(minChange) + 1
maxMonth = pnl[maxChange_index][0]
minMonth = pnl[minChange_index][0]
print("Total Months:", len(pnl))
print("Total: $", total)
print(avgChange)
print(maxMonth, maxChange)
print(minMonth, minChange)
