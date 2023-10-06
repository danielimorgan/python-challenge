import os
import csv

#Create Path to dataset
budget_data = os.path.join('PyBank', 'Resources', 'budget_data.csv')
print(budget_data)
with open (budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
    total_months = 0
    total_profits = 0

    for row in csv_reader:
        total_months = total_months + 1 
        total_profits = int(row[1])
        print(total_profits)
#Find the total number of months in dataset
#for row in csv_reader:
 #   months = row[0]
  #  profits = row[1]
    

#Find the total amount of profit

#Find the average price transition

#Find the largest increase (date and amount)

#Find the largest decrease (date and amount)

#Print and Export results