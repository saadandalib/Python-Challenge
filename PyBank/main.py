import os
import csv
import sys
import numpy as np


budget_csv = os.path.join("Python-Challenge", "PyBank", "Resources", "budget_data.csv")

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    profit_loss = []
    change = []
    a = 0.00
    b = 0.00
    max_month = " "
    min_month = " "
    
    for row in csv_reader:
       profit_loss.append(float(row[1]))
       if float(row[1]) > a:
          a = float(row[1])
          max_month = row[0]
       elif float(row[1]) < b:
            b = float(row[1])
            min_month = row[0]
                  
            
    for i in range(len(profit_loss)-1):
        change.append(profit_loss[i+1] - profit_loss[i])
         
    total_months = len(profit_loss)
    total_profit = round(sum(profit_loss),2)
    average_change = round(sum(change)/len(change),2)
    greatest_profit = max(profit_loss)
    lowest_profit = min(profit_loss)
    
    results = os.path.join("Python-Challenge", "PyBank", "analysis", "results.txt")
    sys.stdout = open(results, "w")
        
    print(f"Financial Analysis")
    print("------------------------------------------------------")
    
    print(f"Total Months: {str(total_months)}")
    print(f"Total: ${str(total_profit)}")
    print(f"Average  Change: ${str(average_change)}")
    print(f"Greatest Increase in Profits: {max_month} (${str(a)})")
    print(f"Greatest Decrease in Profits: {min_month} (${str(b)})")

    sys.stdout.close()
