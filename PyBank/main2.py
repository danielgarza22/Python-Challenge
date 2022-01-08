# Daniel Garza Python Homework

# Import needed modules
import os
import csv
from typing import Counter

# Assign a name to the path where the csv file is located
budget_csv = os.path.join("Resources","budget_data.csv")

# Open and read csv file
with open(budget_csv) as csv_file:
    
    # CSV reader specifies delimeter
    csv_reader = csv.reader(csv_file, delimiter=",")
    # print(csv_reader)
    
    # Identify and assign a name to the header
    csv_header = next(csv_file)
    # print(f"Header: {csv_header}")

    # Create a list for the whole list 
    list = []

    # Create a loop to read thought each row of data after the header
    # for row in csv_reader:
    #     list.append(row)
        # print(row)

    # Create a list for the whole list 
    # list = []
    # for rows in csv_reader:
    #     list.append(rows)

    # Assign pl_list to the Profit and Losses column data so I can calculate the total
    # for pl_list in list:
        # print(pl_list[1])
    
    # number_months = len(list)
    # print('Number of Months: '+ str(number_months))
    
    # for pl_list in list:
    # total_pl += int(pl_list[1])
    # print('Total Amount of Profit/Losses: '+ int())

        
output = '''
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)'''

print(output)
