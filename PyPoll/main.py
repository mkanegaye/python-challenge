#Import modules
import os
import csv
election_csv = os.path.join("PyPoll/Resources/election_data.csv")

#Creating lists
candidates_list = []
Stockham = []
DeGette = []
Doane = []
count = 0
results = []

#Read CSV file
with open(election_csv) as election_file:
    csvreader = csv.reader(election_file, delimiter= ",")
    csvheader = next(csvreader)

    #Count total votes
    for row in csvreader:
        count = count +1
    
    #Counting votes for unique candidates, creating lists of votes for unique candidates
        if row[2] not in candidates_list:
            candidates_list.append(row[2])
    # print(candidates_list)

        if row[2] == "Charles Casper Stockham":
            Stockham.append(row[2])
        elif row[2] == "Diana DeGette":
            DeGette.append(row[2])
        else:
            Doane.append(row[2])

#Calculating Percentages of votes rec'd
Stockham_total = len(list(Stockham))
DeGette_total = len(list(DeGette))
Doane_total = len(list(Doane))

Stockham_per = Stockham_total / count
DeGette_per = DeGette_total / count
Doane_per = Doane_total / count

results = [Stockham_per,DeGette_per,Doane_per]
winner = max(results)
winner_name = candidates_list[results.index(winner)]

#Print to screen
print("Election Results")
print("----------------------------")
print(f"Total Votes: {count}")
print("----------------------------")
print(f"Charles Casper Stockham: {Stockham_per:.3%} ({Stockham_total})")
print(f"Diana DeGette: {DeGette_per:.3%} ({DeGette_total})")
print(f"Raymon Anthony Doane: {Doane_per:.3%} ({Doane_total})")
print("----------------------------")
print(f"Winner: {winner_name}")
print("----------------------------")

#Export to text file
with open("PyPoll/analysis/results.txt", "w") as text:
    text.write("Election Results\n")
    text.write("----------------------------\n")
    text.write(f"Total Votes: {count}\n")
    text.write("----------------------------")
    text.write(f"Charles Casper Stockham: {Stockham_per:.3%} ({Stockham_total})\n")
    text.write(f"Diana DeGette: {DeGette_per:.3%} ({DeGette_total})\n")
    text.write(f"Raymon Anthony Doane: {Doane_per:.3%} ({Doane_total})\n")
    text.write("----------------------------\n")
    text.write(f"Winner: {winner_name}\n")
    text.write("----------------------------\n")