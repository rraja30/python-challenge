#Ramya Nivedha Raja
#Module 3
#October 7th 2022

#import modules
import os
import csv

#store csv path as variable
csvpath = os.path.join('Resources', 'election_data.csv')

#variables
total_votes = 0 
charles_votes = 0
diana_votes = 0
ray_votes = 0

#open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #don't need header
    header = next(csvreader)
    #loop through each row
    for row in csvreader:
        #count all the votes
        total_votes = total_votes + 1
        #count each canditates votes
        if row [2] == "Charles Casper Stockham":
            charles_votes = charles_votes + 1
        elif row [2] == "Diana DeGette":
            diana_votes = diana_votes + 1
        elif row [2] == "Raymon Anthony Doane":
            ray_votes = ray_votes + 1
    
list_of_candiates =  ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
list_of_votes = [charles_votes, diana_votes, ray_votes]

#put together candiates and votes
dict_combo = dict(zip(list_of_candiates, list_of_votes))
#get winner
key = max(dict_combo, key=dict_combo.get)

#calculate percentages
charles_perc = round((charles_votes/total_votes)*100,3)
diana_perc =  round((diana_votes/total_votes)*100, 3)
ray_perc = round((ray_votes/total_votes)*100, 3)

#print information
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {charles_perc}% ({charles_votes})")
print(f"Diana DeGette: {diana_perc}% ({diana_votes})")
print(f"Raymon Anthony Doane: {ray_perc}% ({ray_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

#make txt file
election_summary = os.path.join( "analysis", "Election_Results_Summary.txt")

with open(election_summary, "w") as file:
    #input information into file
    file.write(f"Election Results")
    file.write(f"----------------------------")
    file.write(f"Total Votes: {total_votes}")
    file.write(f"----------------------------")
    file.write(f"Charles Casper Stockham: {charles_perc}% ({charles_votes})")
    file.write(f"Diana DeGette: {diana_perc}% ({diana_votes})")
    file.write(f"Raymon Anthony Doane: {ray_perc}% ({ray_votes})")
    file.write(f"----------------------------")
    file.write(f"Winner: {key}")
    file.write(f"----------------------------")





