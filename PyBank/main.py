# Daniel Garza Homework

# Imported modules
import os
import csv

# Assign a name to the path where the csv file is located
budget_csv = os.path.join("Resources","budget_data.csv")

# Open and read csv file
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    # Create variables
    months = 0
    total = 0
    prev_rev = 0
    total_ch = 0
    inc = ['',0]
    dec = ['',0]

    # Created a loop
    for i,row in enumerate(csv_reader):
        rev = int(row[1])
        months += 1
        total += rev

        # Average Change
        change = rev - prev_rev
        prev_rev = rev
        if i == 0:
            change = 0
        total_ch += change

        #  Greatest increase
        if change > inc[1]:
            inc[0] = row[0]
            inc[1] = change

        #  Greatest decrease
        if change < dec[1]:
            dec[0] = row[0]
            dec[1] = change

# Create analysis report
analysis_output = f'''
Financial Analysis
----------------------------
Total Months: {months}
Total: ${total:,}
Average  Change: ${total_ch/(months-1)}
Greatest Increase in Profits: {inc[0]} (${inc[1]:,})
Greatest Decrease in Profits: {dec[0]} (${dec[1]:,})'''

#print analysis report
print(analysis_output)

# Create a file and save PyBank Analysis to a file
analysis_file = os.path.join("Analysis","PyBank_Analysis.txt")
with open(analysis_file,"a") as f:
    print(output, file=f)
