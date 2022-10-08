#Ramya Nivedha Raja
#Module 3
#October 7th 2022

#import modules
import os
import csv

#store csv path as variable
csvpath = os.path.join('Resources', 'budget_data.csv')

#data storage
net_total = []
monthly_change = []
month_counter = []

#reading csv file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #gets values for month total and sum of all months
    for row in csvreader:
        net_total.append(int(row[1]))
        month_counter.append(row[0])

    #gets value for sum of net_total
    net_total_output = sum(net_total)

    #gets value for lenght of months coutner
    month_counter_output = len(month_counter)

    #gets value for changes in "profit/losses" over entire period
    for i in range(len(net_total)-1):
        #subtract two months and append to monthly change
        monthly_change.append(net_total[i+1]-net_total[i])
    
    #averaging changes
    monthly_change_output = round(sum(monthly_change)/len(monthly_change),2)

    #get max and min of monthly change
    greatest_inc = max(monthly_change)
    greatest_dec = min(monthly_change)

    #get date for max and min of monthly change
    greatest_inc_date = monthly_change.index(greatest_inc) +1
    greatest_dec_date = monthly_change.index(greatest_dec) +1

    #read header of csv file and output
    #print(f"CSV Header: {csv_header}")
    #print(csvreader)

#Financial Analysis Print
print(f"Financial Analysis")
print(f"-----------------------------------------------------------------")
print(f"Total Months: {month_counter_output}" )
print(f"Total:  ${net_total_output}")
print(f"Average Change: {monthly_change_output}")
print(f"Greatest Increase in Profits: {month_counter[greatest_inc_date]} ${greatest_inc}")
print(f"Greatest Decrease in Profits: {month_counter[greatest_dec_date]} ${greatest_dec}")

#creating text file
summary_file = os.path.join("analysis", "Financial_Analysis_Summary.txt")

with open(summary_file,"w") as file:
    file.write("Financial Analysis")
    file.write("-----------------------------------------------------------------")
    file.write(f"Total Months: {month_counter_output}" )
    file.write(f"Total:  ${net_total_output}")
    file.write(f"Average Change: {monthly_change_output}")
    file.write(f"Greatest Increase in Profits: {month_counter[greatest_inc_date]} ${greatest_inc}")
    file.write(f"Greatest Decrease in Profits: {month_counter[greatest_dec_date]} ${greatest_dec}")