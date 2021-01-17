import csv
import os

csv_path = os.path.join("Resources","election_data.csv")

text_path = "election_summary.txt"

# A list to capture the names of candidates
candidates = []

# A list to capture the number of votes each candidate receives
num_votes = []

# A list to capture the percentage of total votes each candidate garners 
percent_votes = []

# A counter for the total number of votes 
total_votes = 0

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        # counter 
        total_votes += 1 

       
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
    
    # Add to percent_votes list 
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
    
    # Find the winning candidate
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

#results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])}"))
print("--------------------------")
print(f"Winner: (winning_candidate)")
print("--------------------------")

#write changes to csv 
with open(text_path, "w") as file:
 file.write("Election Results")
 file.write("--------------------------")
 file.write(str(f"Total Votes: {str(total_votes)}"))
 file.write(str("--------------------------"))
 file.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
 for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
    output.write('{}\n'.format(line))
file.write = "--------------------------"
file.write = str(f"Winner: {winning_candidate}")
file.write("--------------------------")
file.write('{}\n{}\n{}\n'.format(line5, line6, line7))