import os
import csv

election_data = os.path.join("Resources", "election_data.csv")
file_output = os.path.join("election_result.txt")

candidates = []
numVotes = []
percentVotes = []
totalVotes = 0
precentPerCondidate = []
maxVotes = 0

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        totalVotes = totalVotes + 1
        candidate = row[2]

    if candidate in candidates:
        candidate_index = candidates.index(candidate)
        numVotes[candidate_index] = numVotes[candidate_index] + 1
    else:
        candidates.append(candidate)
        numVotes.append(1)


for candidate in range(len(candidates)):
    percentVotes = numVotes[candidate]/totalVotes*100
    precentPerCondidate.append(percentVotes)

    winner = max(numVotes)
    index = numVotes.index(winner)
    winner = candidates[index]


print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(totalVotes)}")
print("--------------------------")
for candidate in range(len(candidates)):
    print(f"{candidates[candidate]}: {str(percentVotes[candidate])} ({str(numVotes[candidate])})")
print("--------------------------")
print(f"Winner: {wininerCandidate}")
print("--------------------------")
