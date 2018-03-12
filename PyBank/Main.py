#Your task is to create a Python script that analyzes the records to calculate each of the following:

#The total number of months included in the dataset

#The total amount of revenue gained over the entire period

#The average change in revenue between months over the entire period

#The greatest increase in revenue (date and amount) over the entire period

#The greatest decrease in revenue (date and amount) over the entire period

import os
import csv

Data_1 = "Budget_data_1.csv"
Data_2 = "Budget_data_2.csv"
lastmonth_value = ["", 0];

with open(Data_1, newline="", encoding = 'latin-1') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    month = 0
    total_revenue = 0
    increased_value = ["", 0];
    decreased_value = ["", 0];
    
    for row in csvreader:
        print(row[1])
        month += 1 
        if month != 1: 
            total_revenue = total_revenue + int(row[1]) 
            if lastmonth_value != 0 and (increased_value[1] < int(row[1]) - lastmonth_value[1]):
                increased_value[0] = row[0]
                increased_value[1] = int(row[1]) -lastmonth_value[1]
                print("Value Increased: " + str(increased_value[1]))
            
            # print(row[0])
            if lastmonth_value != 0 and (decreased_value[1] > int(row[1]) - lastmonth_value[1]):
                decreased_value[0] = row[0]
                decreased_value[1] = int(row[1]) - lastmonth_value[1]
                print("Value Decreased: " + str(decreased_value[1]))
            lastmonth_value[1] = int(row[1])
            lastmonth_value[0] = row[0]
print("Total Months: " + str(month - 1))

print("Total Revenue: " + str(total_revenue))

print("Average Revenue: " + str(total_revenue / (month -1)))

print("Increase Date: " + str(increased_value))

print("Decreased Date: " + str(decreased_value))