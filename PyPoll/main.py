import os
import csv


bank_csv = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(bank_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csv_reader)

    print(f"Election Results")
    print("--------------------------")
    
    # Define variables
    wordcount1 = 0
    candidate1 = "Khan"
    wordcount2 = 0
    candidate2 = "O'Tooley"
    wordcount3 = 0
    candidate3 = "Li"
    wordcount4 = 0
    candidate4 = "Correy"
    num_rows = 0
    name = 0
    votes = 0
    candlist = []

    for row in csv_reader:
        num_rows += 1
        name = str(row[2])
        candlist.append(name)
        if candidate1 in row[2]:
            wordcount1 += 1
        if candidate2 in row[2]:
            wordcount2 += 1
        if candidate3 in row[2]:
            wordcount3 += 1
        if candidate4 in row[2]:
            wordcount4 += 1
    percentage1 = (wordcount1 / num_rows) * 100
    percentage2 = (wordcount2 / num_rows) * 100
    percentage3 = (wordcount3 / num_rows) * 100
    percentage4 = (wordcount4 / num_rows) * 100
    candidates = str(set(candlist))
    print(f"Total Votes: {(num_rows)}")
    print("--------------------------")
    # Switch to printing these to dictionaires
    print(candidate1, percentage1, wordcount1)
    print(candidate2, percentage2, wordcount2)
    print(candidate3, percentage3, wordcount3)
    print(candidate4, percentage4, wordcount4)
    
    print("--------------------------")
    popularvotes = {
        "Khan": wordcount1,
        "O'Tooley": wordcount2,
        "Li": wordcount3,
        "Correy": wordcount4
        }
    print(f"Winner: {max(popularvotes, key = popularvotes.get)}")
