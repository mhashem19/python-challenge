import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")
file_output = os.path.join("analysis", "budget_analysis.txt")

totalMonths = 0
totalProfites = 0
averageChange = []
dates = []


def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length


with open(budget_data, newline = '') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
        totalMonths = totalMonths + 1  
        totalProfites += int(row[1])
        
        averageChange.append(int(row[1]))
        dates.append(row[0])

        print(totalMonths)
        print(totalProfites)
        print(averageChange)
        print(dates)
 
greatest_increase = max(averageChange)
greatest_index = averageChange.index(greatest_increase)
greatest_date = dates[greatest_index]

greatest_decrease = min(averageChange)
worst_index = averageChange.index(greatest_decrease)
worst_date = dates[worst_index]



print(" Financial Analysis")

print(f" Total Months: {totalMonths}")
print(f"Total Profite: ${int(totalProfites)}")
print(f"Average  Change: ${int(average(averageChange))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")


file_output = open("budget_analysis.txt", "w")

file_output.write(" Financial Analysis\n")

file_output.write(f" Total Months: {totalMonths}\n")
file_output.write(f"Total Profite: ${int(totalProfites)}\n")
file_output.write(f"Average  Change: ${int(average(averageChange))}\n")
file_output.write(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})\n")
file_output.write(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})\n")

