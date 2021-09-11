import csv
import os
#The data we need to retrieve.

#assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

#assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize the variable to 0 - a total vote counter
total_votes = 0 

#list of candidates
candidate_options= []

#declare an empty dictionary
candidate_votes = {}

#winning candidate and winning count variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file 
with open(file_to_load) as election_data: 

# to do: read and analyze the data here
# read the file object with the reader function
    file_reader= csv.reader(election_data)

    #read the header row
    headers = next(file_reader)

#1. The total number of votes cast.
#print each row in the CSV file
    for row in file_reader:
        #add to the total vote count
        total_votes += 1


#2. A complete list of candidates who received votes

#print candidate name from each row
        candidate_name = row[2]

#if the candidate does not match any exisiting candidate name...
        if candidate_name not in candidate_options:
            #add the name to the list of candidates
            candidate_options.append(candidate_name)

            #begin tracking each candidate's vote count
            candidate_votes[candidate_name] = 0

        #add a vote to that candidate's count
        candidate_votes[candidate_name] +=1

        #save the results to our text file
with open(file_to_save, "w") as txt_file:

            #print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n"
        )
    print(election_results, end="")
            #save the final vote count to the text file
    txt_file.write(election_results)

        #print(candidate_votes)

            #3. The percentage of votes each candidate won
    #iterate through the candidate list
    for candidate_name in candidate_votes:
        #retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]

        #calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) *100

        #to do: print out each candidate's name, vote count, and percentage of votes to the terminal
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

               #print each candidate, their vote count, and percentage to the terminal
        print(candidate_results)
        #save the candidate results to our text file
        txt_file.write(candidate_results)
        
        #determine winning vote count and candidate
        #determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true then set winning_count = votes and winning_percent = vote_percentage
                winning_counts = votes
                winning_percentage = vote_percentage 
            #and, set the winning candidate equal to the candidate's name 
                winning_candidate = candidate_name 

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_counts:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n"
        )

    print(winning_candidate_summary)

    #save the winning candidate's result to the text file
    txt_file.write(winning_candidate_summary)