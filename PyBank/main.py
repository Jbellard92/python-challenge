#Imports OS and CSV from library
import os
import csv

#File location path set
csvpath = os.path.join("budget_data.csv")

#Opens the CSV
with open(csvpath,newline="", encoding="utf-8") as budget_data:

#Stores CSV lines into "csvreader"
    csvreader = csv.reader(budget_data,delimiter=",")

#Skips/removes header
    header = next(csvreader)

#Sets initial empty lists to be filled later
    months = []
    profit = []
    profit_change = []

#Runs loop through each row in csv (csvreader)
    for row in csvreader:      
        months.append(row[0])
        profit.append(int(row[1]))

#Runs second loop
    for i in range(len(profit)-1):

#Difference between each month
        profit_change.append(profit[i+1]-profit[i])

#Finds the max and min values of the profit_change list
max_increase = max(profit_change)
max_decrease = min(profit_change)

#Searches for the max increase and max decrease and pairs it to the correct month in profit_change list
max_increase_month = profit_change.index(max(profit_change)) + 1
max_decrease_month = profit_change.index(min(profit_change)) + 1


#Statement format for homework. Format strings to input the correct values
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {months[max_increase_month]} (${(str(max_increase))})")
print(f"Greatest Decrease in Profits: {months[max_decrease_month]} (${(str(max_decrease))})")

#Output file to python-challenge folder as a text file
output_file = os.path.join("Financial_Analysis_Summary.txt")

with open(output_file, "w") as file:

#Print to output file
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(months)}")
    file.write("\n")
    file.write(f"Total: ${sum(profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {months[max_increase_month]} (${(str(max_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {months[max_decrease_month]} (${(str(max_decrease))})")