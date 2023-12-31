import csv

#Create Path to datasee
budget_data = r"C:\Users\danie\OneDrive\Documents\MSU Data Bootcamp Docs\Module 3 - Python\Module 3 Challenge\PyBank\Resources\budget_data.csv"
with open (budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
    total_months = 0
    total_profits = 0
    results = []

    #Find the total number of months in dataset   
    for row in csv_reader:
        month = row[0]
        profit = row[1]
        total_months += 1
        total_profits += int(profit)
        results.append((month, profit))

average = (total_profits / total_months)
max_profit = max(results, key=lambda x: int(x[1]))
min_profit = min(results, key=lambda x: int(x[1]))
print(max_profit)



#Print and Export results

output = f'''
Financial Analysis
---------------------
Total Months: {total_months:,}
Total Profits: {total_profits:,}
Average Change: {average:.3f}
Greatest Increase in Profits: {max_profit:}
Greatest Decrease in Profits: {min_profit:}
''' 

print(output)

with open('my_report_PyBank.txt', 'w') as f:
    f.writelines(output)