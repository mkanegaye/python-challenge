#Import modules
import os
import csv
budgetcsv = os.path.join("PyBank/Resources/budget_data.csv")

#Creating lists
date = []
monthly_changes_list = []
profit = []

#Read CSV file
with open(budgetcsv) as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter= ",")
    # print(csvreader)

    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    # for row in csvreader:
    #     print(row)

    # #Calculate total number of months in data set
    month_count = len(list(csvreader))


with open(budgetcsv) as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter= ",")
    csv_header = next(csvreader)
    net_PL = 0
    total_changes = 0
    initial_profit=1088983

    # #Calculate Total Profit/Loss
    for row in csvreader:
        net_PL = net_PL + int(row[1])

        #Calculating Average Changes
        profit.append(row[1])
        final_profit = int(row[1])
        monthly_change = final_profit - initial_profit
        monthly_changes_list.append(monthly_change)
        total_changes = total_changes + monthly_change
        initial_profit = final_profit
        average_change = round(total_changes / (month_count -1),2)

        #Greatest Increase/Decrease and date
        increase = max(monthly_changes_list)
        decrease = min(monthly_changes_list)
        date.append(row[0])
        increase_date = date[monthly_changes_list.index(increase)]
        decrease_date = date[monthly_changes_list.index(decrease)]

#Print to screen
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_count}")
print(f"Total ${net_PL}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {increase_date} (${increase})")
print(f"Greatest Decrease in Profits: {decrease_date} (${decrease})")

#Export to text file
with open("PyBank/analysis/analysis.txt", "w") as text:
    text.write("Financial Analysis\n")
    text.write("----------------------------\n")
    text.write(f"Total Months: {month_count}\n")
    text.write(f"Total ${net_PL}\n")
    text.write(f"Average Change: ${average_change}\n")
    text.write(f"Greatest Increase in Profits: {increase_date} (${increase})\n")
    text.write(f"Greatest Decrease in Profits: {decrease_date} (${decrease})")