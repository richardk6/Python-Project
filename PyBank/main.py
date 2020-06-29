import os
import csv


bank_csv = os.path.join("Resources", "BankData.csv")

# Open and read csv
with open(bank_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csv_reader)
    print(f"Financial Analysis")
    print("--------------------------")

    num_rows = 0
    total = 0
    change = 0
    previous = 0
    avelist = []
    max_profit = ["", 0]
    min_profit = ["", 99999]
    
    for row in csv_reader:
        num_rows += 1
        total = int(row[1]) + total
        change = int(row[1]) - previous
        # for first time change = 867884 - 0
        # avelist[867884] aprox 1000
        avelist.append(change)
        previous = int(row[1])
        # print(avelist)

        if change > max_profit[1]:
            max_profit[0] = row[0]
            max_profit[1] = change
        if change < min_profit[1]:
            min_profit[0] = row[0]
            min_profit[1] = change
    averagechange = sum(avelist[1:]) / (len(avelist) - 1)
    print(f"Total Months: {(num_rows)}")
    print(f"Total of Profit/Losses: ${(total)}")
    print(f"Average Change: {averagechange}")
    print(f"Greatest Increase in Profits: {max_profit[0], max_profit[1]}")
    print(f"Greatest Decrease in Profits: {min_profit[0], min_profit[1]}")