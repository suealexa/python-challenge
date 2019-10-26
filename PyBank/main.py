import os
import csv

#initialize the variables
month = 0
total_revenue = 0
last_month_revenue = 0
this_month_revenue = 0
revenue_change = 0
monthly_change = []
months = []

#open the budget_data.csv and read rows
csvpath = 'budget_data.csv'
#print(csvreader)
print(csvpath)
with open(csvpath) as csvfile:
  
# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header
    next(csvreader)

   # loop to get monthly revenue changes 
    for row in csvreader:
        months.append(row[0])
        this_month_revenue = int(row[1])
        total_revenue = total_revenue + this_month_revenue
        if month >= 1:
            revenue_change = this_month_revenue - last_month_revenue
            monthly_change.append(revenue_change)

        last_month_revenue = this_month_revenue 
        month += 1
        

    # Month by month analysis
sum_monthly_change = sum(monthly_change)

average_change = round(sum_monthly_change/(month - 1), 2)
max_change = max(monthly_change)
min_change = min(monthly_change)
max_month_index = monthly_change.index(max_change) + 1
min_month_index = monthly_change.index(min_change)
max_month = months[max_month_index] 
min_month = months[min_month_index]
    
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {month} ")
print(f"Total Revenue: ${total_revenue}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in profits: {max_month} (${max_change})")
print(f"Greatest Decrease in profits: {min_month} (${min_change})")

#write it to a text file
output_path = os.path.join("PyBank_output.txt")
# open the file
with open (output_path, 'w', newline='') as txtfile:
    # write rows
    txtfile.write("Financial Analysis\n")
    txtfile.write("-----------------------\n") 
    txtfile.write(f"Total Months: {month}\n")
    txtfile.write(f"Total: ${total_revenue}\n")
    txtfile.write(f"Average change: ${average_change}\n")
    txtfile.write(f"Greatest increase in profits: {max_month} (${max_change})\n")
    txtfile.write(f"Greatest decrease in profits: {min_month} (${min_change})\n")

