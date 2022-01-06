# Daniel Garza Python Homework

# Import needed modules
import os
import csv

# Assign a name to the path where the csv file is located
budget_csv = os.path.join("Resources","budget_data.csv")

# Open and read csv file
with open(budget_csv) as csv_file:
    
    # CSV reader specifies delimeter
    csv_reader = csv.reader(csv_file, delimiter=",")
    print(csv_reader)
    
    # Identify and assign a name to the header
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Create a loop to read thought each row of data after the header
    for row in csv_reader:
        
        # Print each row after the header
        print(row)

