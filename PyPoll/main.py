import os
import csv
from types import CoroutineType

poll_csv = os.path.join("Resources","election_data.csv")

with open(poll_csv) as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    total_votes = 0
    cand_votes = 0
    canddidate = int(csv_reader[2])
    
    for row in csv_reader:
        total_votes += 1
    
    for cand_votes in csv_reader[0]:
        cand_votes_perc = 



    
output = f'''
Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------
=================================================================
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------'''

print(output)
