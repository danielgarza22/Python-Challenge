# Daniel Garza Homework

# Imported modules
import os
import csv

# Assign a name to the path where the csv file is located
poll_csv = os.path.join("Resources","election_data.csv")

# Create variables
total_votes = 0
max_value = 0
cand_list = []
vote_perc = []
cand_votes = {}
winner = ['',0]

# Open and read csv file
with open(poll_csv) as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    
    # Created a loop to calculate total votes
    for row in csv_reader:
        total_votes += 1
        cand_name = row[2]

        # Created condition to get the candidate names and votes
        if cand_name not in cand_list:
            cand_list.append(cand_name)
            cand_votes[cand_name] = 0

        cand_votes[cand_name] = cand_votes[cand_name] + 1

# Print out the first part of the analysis and the total of votes needed
output = f'''
---------------------------------
***      Election Results    ***
---------------------------------
Total Votes:\t{total_votes:,}
---------------------------------
'''
# Create a loop to get the votes amount in a percentage format
for cand in cand_votes:
    votes = cand_votes.get(cand)
    vote_perc = (float(votes) / float(total_votes))
    percentage = "{:.3%}".format(vote_perc)

    #Loop to get the winner
    if votes > winner[1]:
        winner[0] = cand
        winner[1] = votes
    
    # Get and print the candidates with their respective percentage and votes.
    cand_perc_votes = f'{cand}:      \t{percentage}\t({votes})\n'
    output += cand_perc_votes

# Print the Winner
output += f'---------------------------------\n'
output += f'Winner: {winner[0]}'
output += f'\n---------------------------------\n'

# Create a file and save PyBank Analysis to a file
print(output)
# open('Analysis/PyPoll_Analysis.txt','w').write(output)
