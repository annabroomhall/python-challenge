import os
import csv
import collections 
from collections import Counter 

csvpath = os.path.join('..','PyPoll', 'Resources','election_data.csv')


#Open file
with open(csvpath, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    header = next(csv_reader)
    
    #create empty Candidate List
    CandidateList = []
    
    #create empty Candidate List
    Votes =[]

    #create Candidate Counters
    Candidate1Count = []
    Candidate2Count = []
    Candidate3Count = []
    Candidate4Count = []

# Create unique candidate name list
with open(csvpath, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    header = next(csv_reader)

    for row in csv_reader:
        if row[2] not in CandidateList:
            CandidateList.append(row[2])

    
#Loop through and use indices to split out the votes to Candidate Lists and add votes to Votes list 
with open(csvpath, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    header = next(csv_reader)

    for row in csv_reader:
        if row[2] == CandidateList[0]:
            Candidate1Count.append(1)
            Votes.append(CandidateList[0])
        elif row[2] == CandidateList[1]:
            Candidate2Count.append(1)
            Votes.append(CandidateList[1])
        elif row[2] == CandidateList[2]:
            Candidate3Count.append(1)
            Votes.append(CandidateList[2])
        elif row[2] == CandidateList[3]:
            Candidate4Count.append(1)
            Votes.append(CandidateList[3])

    #Set the most frequent definition
    def most_frequent(List): 
        occurence_count = Counter(List) 
        return occurence_count.most_common(1)[0][0] 

        List = Votes 
    
    #Print results
    print("Election Results")
    print("-----------------------------------")
    print("Total Votes:", len(Votes))
    print("-----------------------------------")
    print(CandidateList[0],": ", round(len(Candidate1Count)/len(Votes),6)*100,"% (", len(Candidate1Count),")")
    print(CandidateList[1],": ", round(len(Candidate2Count)/len(Votes),6)*100,"% (", len(Candidate2Count),")")
    print(CandidateList[2],": ", round(len(Candidate3Count)/len(Votes),6)*100,"% (", len(Candidate3Count),")")
    print(CandidateList[3],": ", round(len(Candidate4Count)/len(Votes),6)*100,"% (", len(Candidate4Count),")")
    print("-----------------------------------")
    print("Winner: ",most_frequent(Votes))


    my_file = os.path.join('Analysis','PyPoll_Analysis.txt')
    my_file = open(my_file, "w")
    my_file.write("Election Results"+"\n")
    my_file.write("-----------------------------------"+"\n")
    my_file.write("Total Votes: ")
    my_file.write(str(len(Votes))+"\n")
    my_file.write("-----------------------------------"+"\n")
    my_file.write(CandidateList[0]+": " + str(round(len(Candidate1Count)/len(Votes),6)*100) + "% (" + str(len(Candidate1Count))+")"+"\n")
    my_file.write(CandidateList[1]+": " + str(round(len(Candidate2Count)/len(Votes),6)*100) + "% (" + str(len(Candidate2Count))+")"+"\n")
    my_file.write(CandidateList[2]+": " + str(round(len(Candidate3Count)/len(Votes),6)*100) + "% (" + str(len(Candidate3Count))+")"+"\n")
    my_file.write(CandidateList[3]+": " + str(round(len(Candidate4Count)/len(Votes),6)*100) + "% (" + str(len(Candidate4Count))+")"+"\n")
    my_file.write("-----------------------------------"+"\n")
    my_file.write("Winner: "+ most_frequent(Votes))
    my_file.close()