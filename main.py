import csv, os
# read csv
csv_path = os.path.join("Resources","budget_data.csv")

#Set variables
total_months = 0
total_revenue = 0
revenue = []
previous_revenue = 0
month_of_change = []
revenue_change = 0
greatest_dec = ["", 9999999]
greatest_inc= ["", 0]
revenue_change_list = []
revenue_avg = 0

#set the output of the text file
text_path = "budgetdata_summary.txt"

#open csv
with open(csv_path) as budget_data:
	csvreader = csv.DictReader(budget_data)

    #Loop through to find total months
	for row in csvreader:

        #Count the total of months
        	total_months += 1

        #Calculate the total revenue over the entire period
        total_revenue = total_revenue + int(row["Profit/Losses"])

                #Calculate the average change in revenue between months over the entire period
        revenue_change = float(row["Profit/Losses"])- previous_revenue
        previous_revenue = float(row["Profit/Losses"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = [month_of_change] + [row["Date"]]
       

        #The greatest increase in revenue (date and amount) over the entire period
        if revenue_change>greatest_inc[1]:
            greatest_inc[1]= revenue_change
            greatest_inc[0] = row['Date']

        #The greatest decrease in revenue (date and amount) over the entire period
        if revenue_change<greatest_dec[1]:
            greatest_dec[1]= revenue_change
            greatest_dec[0] = row['Date']
    
	revenue_avg = sum(revenue_change_list)/len(revenue_change_list)

#write changes to csv
with open(text_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % total_months)
    file.write("Total Revenue: $%d\n" % total_revenue)
    file.write("Average Revenue Change $%d\n" % revenue_avg)
    file.write("Greatest Increase in Revenue: %s ($%s)\n" % (greatest_inc[0], greatest_inc[1]))
    file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_dec[0], greatest_dec[1]))





