import csv
import os
#The data we need to retrieve.

#assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

#assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the election results and read the file 
with open(file_to_load) as election_data: 

# to do: read and analyze the data here
# read the file object with the reader function
    file_reader= csv.reader(election_data)

#print the header row
    headers = next(file_reader)
    print(headers)

#1. The total number of votes cast.
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote