import os
import csv

#construct the file path for the CSV file
election_data = "/Users/derricksmith/Python_Challenge/PyPoll/Resources/election_data.csv"

#Declare variables
total_votes = (0)
Candidates_with_votes = {}
percentage_of_votes = 0
Number_of_Candidate_votes = ["",0] #store as candidate name, amount
winner_of_election = [""] #store as candidate name
max_votes = 0

#open the csv file
with open(election_data) as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter=",")


    #iterate through the CSV rows
    for row in csv_reader:
        Candidate_name = row['Candidate']
        #count the total number of votes
        total_votes += 1
        if Candidate_name in Candidates_with_votes:
            Candidates_with_votes[Candidate_name] +=1
        else:
            Candidates_with_votes[Candidate_name] = 1


        
            # Calculate the percentage of votes each candidate won and print results
print("Election Results")
print(f"Total Votes Cast: {total_votes}\n")
print("Votes Per Candidate:")
for Candidate, count in Candidates_with_votes.items():
    percentage = (count / total_votes) * 100
    print(f"{Candidate}: {count} votes, {percentage:.2f}%")

#determine the winner
    if count > max_votes:
        max_votes = count
        winner_of_election = Candidate

#print the winner
print(f"Winner: {winner_of_election} with {max_votes} votes")

