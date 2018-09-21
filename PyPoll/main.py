#Primary Import
import os
import csv
import collections

#File location path set
csvpath = os.path.join("election_data.csv")

#Reads the CSV in
with open(csvpath,newline="", encoding="utf-8") as election:

#Stores CSV lines into "csvreader" and skips/removes header. Sets candidates_list list
    csvreader = csv.reader(election,delimiter=",")
    header = next(csvreader)
    candidates_list = []

# For loop through csvreader and sets row "3" as "candidate". Fills the candidates_list
    for row in csvreader:
        candidate = row[2]
        candidates_list.append(candidate)

#Imports counter function and creates function winner(candidates_list)
from collections import Counter
def winner(candidates_list):

#Convert list of candidates_list in candidate_dictionary
    vote_count = Counter(candidates_list)
    candidates_dictionary = {}

#Loops through each value in vote_count list and sets new list. Second loop fills
    for value in vote_count.values():
        candidates_dictionary[value] = []

    for (key,value) in vote_count.items():
        candidates_dictionary[value].append(key)
    total_votes = sum(vote_count.values())
    c = Counter(candidates_dictionary).most_common()
    Candidate_key_Length = len(sorted(candidates_dictionary.keys(),reverse=True))

#Creates output text file save location. Next lines opens the file and imprints the desired output
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

#Runs loop to print desired outputs. Also calculates votes per candidate and the percentage of the overall vote. Then finds the correct winner candidate name
        for i in range(Candidate_key_Length):
            CandidateVotes = sorted(candidates_dictionary.keys(),reverse=True)[i]
            Percentage = (CandidateVotes/total_votes)*10   
            print(candidates_dictionary[CandidateVotes]) 
            print(Percentage) 
            print(CandidateVotes)  
            
            file.write(f"{candidates_dictionary[CandidateVotes]}: {Percentage} ({CandidateVotes})")

        Winner = sorted(candidates_dictionary.keys(),reverse=True)[0]

        if len(candidates_dictionary[Winner])>1:
            print(sorted(candidates_dictionary[Winner])[0])
        else:
            print(candidates_dictionary[Winner][0])
            file.write(f"Winner: {candidates_dictionary[Winner]}")

#Runs new created function
winner(candidates_list)