import os
import csv

csvpath = os.path.join('..','Pybank', 'Resources','budget_data.csv')

# Open and read the csv
with open(csvpath, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    
    #skip header
    header = next(csv_reader)

    #set up empty lists
    pl = []
    months = []
    pl_change = []

    # loop to add each month to P&L list
    for row in csv_reader:

        pl.append(float(row[1]))
        months.append(row[0])
        
    
    #loop to identify row i minus the row before and add the difference to the rev_change list
    for i in range(1,len(pl)):
        pl_change.append(pl[i] - pl[i-1])   
        #identify average figure in p&l_change list
        avg_change = sum(pl_change)/len(pl_change)
        
        #identify max and min change in p&l_change list
        max_pl_change = max(pl_change)
        min_pl_change = min(pl_change)

        #identify max and min month in p&l_change list - was pulling the month before, +1 adjusted it to reflect correctly.
        max_pl_change_date = str(months[pl_change.index(max(pl_change))+1])
        min_pl_change_date = str(months[pl_change.index(min(pl_change))+1])

    #print in gitbash
    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(months))
    print("Total Revenue: $", sum(pl))
    print("Average Revenue Change: $", round(avg_change,2))
    print("Greatest Increase in Revenue:", max_pl_change_date,"($", max_pl_change,")")
    print("Greatest Decrease in Revenue:", min_pl_change_date,"($", min_pl_change,")")

    #print to file
    pybank_file = os.path.join('Analysis','PyBank_Analysis.txt')
    pybank_file = open(pybank_file, "w")
    pybank_file.write("Financial Analysis"+"\n")
    pybank_file.write("-----------------------------------"+"\n")
    pybank_file.write("Total Months: "+ str(len(months))+"\n")
    pybank_file.write("Total Revenue: $"+ str(sum(pl))+"\n")  
    pybank_file.write("Average Revenue Change: $" + str(round(avg_change,2))+"\n")
    pybank_file.write("Greatest Increase in Revenue: "+ str(max_pl_change_date) + " ($" + str(max_pl_change)+")"+"\n")
    pybank_file.write("Greatest Decrease in Revenue: "+ str(min_pl_change_date) + " ($" + str(min_pl_change)+")")
    pybank_file.close()