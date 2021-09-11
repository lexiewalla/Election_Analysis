# Election_Analysis
Module 3 - Python

### Overview
The purpose of this election audit was to put our new python skills to the test to help figure out who won the Colorado election! In this module we took the large data set of votes and broke it down into sections. We were able to find out who the winner of the Election was, how many votes they had and the percentage of votes they had. We found out how many votes and the percentage of votes each county had, as well the county that had the most votes.  In this module we learned how to pull data files into our terminal to read and analyze, and how to write data to output to a file. I was able to find all this data using membership and logical operators in decision statements to find the winner of the election and the county that had the most votes. I created lists and dictionaries to hold the data in the decision statements. I used repetition statements to go through the data to find the total number of votes, and total number of votes for each person. I also used f strings to print out all my data findings. 

## Election-Audit Results

•	There were 369,711 total votes in the election. I was able to find this by initializing a variable to 0 and then adding 1 each time it iterated through the data.  

<img width="218" alt="total_votes" src="https://user-images.githubusercontent.com/45208773/132957506-0f7d6edc-8d8d-4f05-aab7-8cbfe2e5b7f5.PNG">

•	There were three counties in the election, Denver, Arapahoe and Jefferson. Denver was the count that had the highest number of votes with 306,055, 82.8%. Jefferson had 38,822, 10.5% and Arapahoe had 24,801, 6.7% of the votes. Using the code shown below I was able to write a for loop to find how many votes each county had and the percentage of each of them. COUNTY_RESULTS

<img width="510" alt="county_results" src="https://user-images.githubusercontent.com/45208773/132957469-108581ef-c3db-46a9-b667-34580f4a0261.PNG">


•	The county of Denver ended up winning by a landslide! I was able to find that by using a decision statement. 

<img width="525" alt="Denver_Win" src="https://user-images.githubusercontent.com/45208773/132957516-2c4ce6a8-1922-4f71-857d-d0ad9f0b3b19.PNG">

•	There were three candidates in the election, Diane DeGette, Charles Casper Stockham, and Raymon Anthony Doanne. Diane Degette won the election with 272,892 votes which was 73.8% of the total votes. Charles Casper Stockham came in second with 85,213 votes, 23.0% and Raymon Anthony Doanne in last with 11,606 votes, 3.1%. Again, using a decision statement and a for loop we were able to figure out how many votes each candidate had and the percentage of votes they received. 

<img width="412" alt="candidate_count" src="https://user-images.githubusercontent.com/45208773/132957454-c5dbc0f9-82cf-44f2-98af-dba1bf9c94ab.PNG">



•	Diane Degette was the winner of the election with 272,892 votes and that was 73.8% of the total votes in the election.


## Election Audit Summary

This was a great way to audit the election. If we were to audit another election, we could modify it so that we could see how many votes each candidate got in each county. This way we could see who is in the lead in each county, to see how it differs over the entire state. Then we could compare the candidate’s status from one county to the next. 

Another way we could modify the script would be to audit by political party. We could add another line of data to the election results, by determining which political party each ballot ID was associated with. We could then analyze how many republican voters are voting republican, how many democratic voters are voting democrat or vice versa where republicans are voting democrat or democrat voting republican, in this election. We could do a total analysis on political party study using this information by adding one more piece to the data set which would be political party. 











