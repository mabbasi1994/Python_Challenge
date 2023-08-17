import os
import csv
input_file= os.path.join("/Users/marmar/Documents/bootcamp/dataanalytics/Module 3/Python_Challenge/PyBank/Resources/budget_data.csv")
output_file= os.path.join("/Users/marmar/Documents/bootcamp/dataanalytics/Module 3/Python_Challenge/PyBank/Analysis//Return_budget.txt")

total_months = 0
net_total = 0
change_list = []
month_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999]

with open(input_file) as finance:
    csvreader = csv.reader(finance, delimiter=",")
    header = next(csvreader)
    
    # Initialize the previous profit/loss value
    previous_profitloss = 0
    
    for row in csvreader:
        total_months += 1
        net_total += int(row[1])

        # Track the net change
        net_change = int(row[1]) - previous_profitloss
        change_list.append(net_change)
        month_change.append(row[0])

        # Update the previous profit/loss for the next iteration
        previous_profitloss = int(row[1])

        # Calculate the increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

             # Calculate the decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

            # Calculate the average
    average = round(sum(change_list) / len(change_list), 2)

    # Generate summary output
    output = (f"Financial Analysis\n"
              f"----------------------------\n"
              f"Total Months: {total_months}\n"
              f"Total Revenue: ${net_total}\n"
              f"Average Revenue Change: ${average}\n"
              f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
              f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output to the terminal
    print(output)

# Export the results to the text file
    with open(output_file, "w") as txt_file:
        txt_file.write(output)



