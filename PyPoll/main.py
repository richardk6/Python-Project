import os
import csv


election_csv = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csv_reader)

    print(f"Election Results")
    print("--------------------------")
    
    # Define variables
    totvotes = 0
    cand_list = []
    cand_votes = {}
    all_keys = []
    all_items = []
    

    for row in csv_reader:
        totvotes += 1
        name = str(row[2])
    # loop through all candidates
        if name not in cand_list:
    # add it to the list of candidates
            cand_list.append(name)
            cand_votes[name] = 0
    # begin tracking candidate's voter count
        else:
            cand_votes[name] = cand_votes[name] + 1
    print(f"Total Votes: {(totvotes)}")
    print("--------------------------")  
    for key in cand_votes:
        cand_vote_total = cand_votes[key]
        cand_percentage = "{:.3%}".format(cand_vote_total / totvotes)
        print(f"{key}: {cand_percentage} ({cand_vote_total})")
    print("--------------------------")
winner = max(cand_votes, key=cand_votes.get)
print(f"Winner: {winner}")
print("--------------------------")

# Textfile path
txtpath = os.path.join('analysis', "analysis.txt")

    # Write to text file
with open(txtpath, "w", newline="") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("--------------------------\n")
    txtfile.write(f"Total Votes: {(totvotes)}\n")
    txtfile.write("--------------------------\n")
    for key in cand_votes:
        cand_vote_total = cand_votes[key]
        cand_percentage = "{:.3%}".format(cand_vote_total / totvotes)
        txtfile.write(f"{key}: {cand_percentage} ({cand_vote_total})\n")
    txtfile.write("--------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("--------------------------\n")