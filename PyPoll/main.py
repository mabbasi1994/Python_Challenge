import os
import csv
 
election_data_csv= os.path.join ("/Users/marmar/Documents/bootcamp/dataanalytics/Module 3/Python_Challenge/PyPoll/Resources/election_data.csv")
file_to_output= os.path.join ("/Users/marmar/Documents/bootcamp/dataanalytics/Module 3/Python_Challenge/PyPoll/Analysis//election_data.txt")

totalVotes = 0 
votesPerCandidate = {}

# Open election_data CSV file
with open(election_data_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)  

#Count votes for each candidate
    for row in csvreader:
        totalVotes += 1
        candidate = row[2]
        votesPerCandidate[candidate] = votesPerCandidate.get(candidate, 0) + 1

# Calculate and print election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalVotes}")
print("-------------------------")

for candidate, votes in votesPerCandidate.items():
    percentage = (votes / totalVotes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-------------------------") 

winner = max(votesPerCandidate, key=votesPerCandidate.get)
print(f"Winner: {winner}")

# Write results to an output file
with open(file_to_output, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("---------------------------------------\n")
    txt_file.write(f"Total Vote: {totalVotes}\n")
    txt_file.write("---------------------------------------\n")
    for candidate, votes in votesPerCandidate.items():
        percentage = (votes / totalVotes) * 100
        txt_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    txt_file.write("---------------------------------------\n")
    txt_file.write(f"The winner is: {winner}\n")
    txt_file.write("---------------------------------------\n")
