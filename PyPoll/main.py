import os
import csv
from types import CoroutineType

poll_csv = os.path.join("Resources","election_data.csv")

total_votes = 0
win_count = 0
cand_list = []
unique_cand = []
vote_count = []
vote_perc = []
cand_votes = {}

with open(poll_csv) as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    
    for row in csv_reader:
        total_votes += 1
        cand_name = row[2]

        if cand_name not in cand_list:
            cand_list.append(cand_name)
            cand_votes[cand_name] = 0
        
        cand_votes[cand_name] = cand_votes[cand_name] + 1
    
    for cand in cand_votes:
        votes = cand_votes.get(cand)
        vote_perc = (float(votes) / float(total_votes))
        percentage = "{:.3%}".format(vote_perc)

        if votes > win_count:
            win_count = votes
            win_cand = cand
        
        cand_perc_votes = f"{cand}: {percentage} ({votes})\n"
        print(percentage)

    
        print(f'Election Results')
        print(f'-------------------------')
        print(f"Total Votes: {total_votes:,}")
        print(f'-------------------------')
        print(percentage)
        print(f'-------------------------')


    
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
=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{percentage}
-------------------------
Winner: 
-------------------------'''

# print(output)
