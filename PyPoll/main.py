
import os

# Module for reading CSV files
import csv

# set the path
csvpath = os.path.join('election_data.csv')
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header
    next(csvreader)

    # initialize variables
    all_candidates = {}
    winning_candidate_count = 0
    winning_candidate_name = ""

   
    # read the data
    for row in csvreader:

# match candidate to voter and count votes   
        if row[2] in all_candidates:
           all_candidates[row[2]] += 1

# Start new candidate count           
        else:
            all_candidates[row[2]] = 1
    
    print("Election Results")
    print("------------------------------\n")

    #split dictionary
    total_num_votes = sum(all_candidates.values())
    print(f'Total votes: {total_num_votes}')
    print("--------------------------------\n")
# Specify the file to write to
output_path = os.path.join("PyPoll_output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Total Votes:{total_num_votes}\n")
    txtfile.write("-----------------------------\n")

    for k,v in all_candidates.items():
        print(f'{k}: {100*round(v/total_num_votes,2)}% ({v})')  
        txtfile.write(f'{k}: {100*round(v/total_num_votes,2)}% ({v})\n')
        if (v > winning_candidate_count):
            winning_candidate_count = v
            winning_candidate_name = k
            
    txtfile.write("----------------------------\n")
    txtfile.write(f"Winner : " + winning_candidate_name)
    print("------------------------------------\n")
    print(f"Winner : " + winning_candidate_name)
    #print
    print("-------------------------------------\n")        
           

    


