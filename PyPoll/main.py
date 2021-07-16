import os
import csv
import numpy as np
import sys



election_csv = os.path.join( "Python-Challenge", "PyPoll", "Resources", "election_data.csv")

with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    print(csv_header)
    
    voter_list = []
    candidate_list = []
    khan_voters = []
    li_voters = []
    otooley_voters = []
    correy_voters = []

    for row in csv_reader:
        voter_list.append(float(row[0]))
        candidate_list.append(row[2])
        if row[2] == 'Khan':
            khan_voters.append(row[2])
        elif row[2] == 'Li':
            li_voters.append(row[2])
        elif row[2] == 'Correy':
            correy_voters.append(row[2])
        else: otooley_voters.append(row[2])
        
    
    total_votes = len(voter_list)
    list_candidates = list(set(candidate_list))  
    khan_votes = len(khan_voters)
    khan_percentage = round((khan_votes /total_votes) * 100 ,2)
    li_votes = len(li_voters)
    li_percentage = round((li_votes /total_votes) * 100 ,2)
    correy_votes = len(correy_voters)
    correy_percentage = round((correy_votes /total_votes) * 100 ,2)
    tooley_votes = len(otooley_voters)
    tooley_percentage = round((tooley_votes /total_votes) * 100 ,2)
    votes_list = [khan_votes, correy_votes, li_votes, tooley_votes]
    winner = max(votes_list)
    
    if winner == khan_votes:
        Winner = 'Khan'
    elif winner == li_votes:
        Winner = 'Li'
    elif winner == tooley_votes:
        Winner = 'Correy'
    else: Winner = "O'Tooley"
    
    results = os.path.join("Python-Challenge", "PyPoll", "analysis", "results.txt")
    sys.stdout = open(results, "w")
    
    print(f"Election Results")
    print("---------------------------------")
    print(f"Total Votes: {total_votes}")
    print("---------------------------------")
    print(f"Candidates: {list_candidates}")
    print("---------------------------------")
    print(f"Khan: {khan_percentage}% ({str(khan_votes)})")
    print(f"Correy: {correy_percentage}% ({str(correy_votes)})")
    print(f"Li: {li_percentage}% ({str(li_votes)})")
    print(f"O'Tooley: {tooley_percentage}% ({str(tooley_votes)})")
    print("---------------------------------")
    print(f"Winner: {Winner}")
    print("---------------------------------")
    
    sys.stdout.close()
    
    
    