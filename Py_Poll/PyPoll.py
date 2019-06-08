import os
import csv

csvpath = os.path.join('..', 'Py_Poll', 'election_data.csv')

total_votes = []
voters = []
unique_voters = []

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

    for i in csvreader:
        total_votes.append(i[0])
        voters.append(i[2])
        
print("Election Results")
print("---------------------")
print(f"Total Votes: {len(total_votes)}")
print("---------------------")        
   

Khan = voters.count('Khan')
Correy = voters.count('Correy')
Li = voters.count('Li')
O_Tooley = voters.count("O'Tooley")

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
print(f"Khan: {round((Khan/len(total_votes))*100,3)}% {Khan}")
print(f"Correy: {round((Correy/len(total_votes))*100,3)}% {Correy}")
print(f"Li: {round((Li/len(total_votes))*100,3)}% {Li}")
print(f"O'Tooley: {round((O_Tooley/len(total_votes))*100,3)}% {O_Tooley}")

# The winner of the election based on popular vote.
print("---------------------")
print("Khan")
print("---------------------")  

file = open("election_data", "w") 
file.write(F"Election Results\n---------------------\nTotal Votes: {len(total_votes)}\n---------------------\nKhan: {round((Khan/len(total_votes))*100,3)}% {Khan}\nCorrey: {round((Correy/len(total_votes))*100,3)}% {Correy}\nLi: {round((Li/len(total_votes))*100,3)}% {Li}\nO'Tooley: {round((O_Tooley/len(total_votes))*100,3)}% {O_Tooley}\n---------------------\nKhan\n---------------------")
