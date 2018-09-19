#Import

import os
import csv
import collections

# File Location

csvpath = os.path.join("election_data.csv")

#Default Read mode

with open(csvpath,newline="", encoding="utf-8") as election:

# Store contents

    csvreader = csv.reader(election,delimiter=",")

    header = next(csvreader)
    
    candidates = []

#Define row 3 as candidate

    for row in csvreader:
        candidate = row[2]

        candidates.append(candidate)


from collections import Counter

def winner(candidates):

#Convert list of candidates in cand_dictionary

    votes = Counter(candidates)

    cand_dict = {}

    for value in votes.values():
        cand_dict[value] = []

    for (key,value) in votes.items():
        cand_dict[value].append(key)

    total_votes = sum(votes.values())
    c = Counter(cand_dict).most_common()

    x = len(sorted(cand_dict.keys(),reverse=True))
    output = os.path.join("election_results.txt")

    with open(output, "w+") as file:   

        file.write("Election Results")
        file.write("\n")
        file.write("-----------------------")
        file.write("\n")
        file.write(f"Total Vote: {total_votes}")
        file.write("\n")
        file.write("-----------------------")
        file.write("\n")

        for i in range(x):
            voteByCandidate = sorted(cand_dict.keys(),reverse=True)[i]
            votePercentage = (voteByCandidate/total_votes)*10   
            print(cand_dict[voteByCandidate]) 
            print(votePercentage) 
            print(voteByCandidate)  
            
            file.write(f"{cand_dict[voteByCandidate]}: {votePercentage} ({voteByCandidate})")

        Winner = sorted(cand_dict.keys(),reverse=True)[0]

        if len(cand_dict[Winner])>1:
            print(sorted(cand_dict[Winner])[0])
        else:
            print(cand_dict[Winner][0])
            file.write(f"Winner: {cand_dict[Winner]}")

winner(candidates)