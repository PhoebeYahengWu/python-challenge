import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

totalVotes = 0
candidates = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        candidates.append(row[2])
        totalVotes = totalVotes + 1

KhanVotes = candidates.count("Khan")
KhanVotePercent = "{:.3%}".format(KhanVotes/totalVotes)
CorreyVotes = candidates.count("Correy")
CorreyVotePercent = "{:.3%}".format(CorreyVotes/totalVotes)
LiVotes = candidates.count("Li")
LiVotePercent = "{:.3%}".format(LiVotes/totalVotes)
TooleyVotes = candidates.count("O'Tooley")
TooleyVotePercent = "{:.3%}".format(TooleyVotes/totalVotes) 

candidateVoteList = [KhanVotes, CorreyVotes, LiVotes, TooleyVotes]
MostVoted = max(candidateVoteList)

if(KhanVotes==MostVoted):
    winner = "Khan"
elif(CorreyVotes==MostVoted):
    winner = "Correy"
elif(LiVotes==MostVoted):
    winner = "Li"
else:
    winner = "O'Tooley"

print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalVotes}")
print("-------------------------")
print(f"Khan: {KhanVotePercent} ({KhanVotes})") 
print(f"Correy: {CorreyVotePercent} ({CorreyVotes})") 
print(f"Li: {LiVotePercent} ({LiVotes})") 
print(f"O'Tooley: {TooleyVotePercent} ({TooleyVotes})") 
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------") 

file_to_output = os.path.join("analysis", "output.txt")
with open(file_to_output, "w") as txt_file:
    line1 = "Election Results"
    line2 = "-------------------------"
    line3 = f"Total Votes: {totalVotes}"
    line4 = "-------------------------"
    line5 = f"Khan: {KhanVotePercent} ({KhanVotes})"
    line6 = f"Correy: {CorreyVotePercent} ({CorreyVotes})"
    line7 = f"Li: {LiVotePercent} ({LiVotes})"
    line8 = f"O'Tooley: {TooleyVotePercent} ({TooleyVotes})"
    line9 = "-------------------------"
    line10 = f"Winner: {winner}"
    line11 = "-------------------------"
    txt_file.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11))

