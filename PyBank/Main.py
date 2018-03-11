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

with open(Data_1, newline="", encoding = 'latin-1') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    month = 0
    total_revenue = 0
    for row in csvreader:
        print(row[1])
        month += 1 
        if month != 1: 
            total_revenue = total_revenue + int(row[1])   
print("Total Months: " + str(month - 1))

print(total_revenue)

print(total_revenue / (month -1))