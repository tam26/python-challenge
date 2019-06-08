import os
import csv
import statistics

csvpath = os.path.join('..', 'Py_Bank', 'budget_data.csv')

total_months = []
total = []

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

    for i in csvreader:
        total_months.append(i[0])

        total.append(int(i[1]))

maxpos = total.index(max(total)) 
minpos = total.index(min(total))
    
# The total number of months included in the dataset
print("Financial Analysis")
print("------------------------------------------")

print(f"Total Months: {len(total_months)}")

# The net total amount of "Profit/Losses" over the entire period
print(f"Total Profits/Losses: ${sum(total)}")

# The average of the changes in "Profit/Losses" over the entire period
print(f"Average Change: ${round(statistics.mean(total),2)}")

# The greatest increase in profits (date and amount) over the entire period
print(f"Greatest Increase in Profits: {total_months[maxpos]} ${max(total)}")

# The greatest decrease in losses (date and amount) over the entire period
print(f"Greatest Decrease in Profits: {total_months[minpos]} ${min(total)}")


file = open("budget_data", "w") 
file.write(F"Financial Analysis\n ------------------------------------------\n Total Months: {len(total_months)}\n Total Profits/Losses: ${sum(total)}\n Average Change: ${round(statistics.mean(total),2)}\n Greatest Increase in Profits: {total_months[maxpos]} ${max(total)}\n Greatest Decrease in Profits: {total_months[minpos]} ${min(total)}")