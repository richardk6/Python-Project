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
    num_rows = 0

    for row in csv_reader:
        num_rows += 1
    print(f"Total Votes: {(num_rows)}")