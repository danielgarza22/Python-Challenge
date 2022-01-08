import os
import csv

budget_csv = os.path.join("Resources","budget_data.csv")

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    months = 0
    total = 0
    prev_rev = 0
    total_ch = 0
    inc = ['',0]
    dec = ['',0]

    for i,row in enumerate(csv_reader):
        rev = int(row[1])
        months += 1
        total += rev

        # Avg Change
        change = rev - prev_rev
        prev_rev = rev
        if i == 0:
            change = 0
        total_ch += change

        #  Greatest increase
        if change > inc[1]:
            inc[0] = row[0]
            inc[1] = change

        if change < dec[1]:
            dec[0] = row[0]
            dec[1] = change

output = f'''
Financial Analysis
----------------------------
Total Months: {months}
Total: ${total:,}
Average  Change: ${total_ch/(months-1)}
Greatest Increase in Profits: {inc[0]} (${inc[1]:,})
Greatest Decrease in Profits: {dec[0]} (${dec[1]:,})'''

print(output)

analysis_file = os.path.join("Analysis","PyBank_Analysis.txt")
with open(analysis_file,"a") as f:
    print(output, file=f)
