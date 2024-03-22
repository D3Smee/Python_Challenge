import os
import csv

# Construct the file path for the CSV file
budget_data = os.path.join("..", "/Users/derricksmith/Downloads/Starter_Code 3/PyBank/Resources/budget_data.csv")

# Initialize variables
total_months = 0
total_profit_losses = 0
previous_month_profit_losses = None
monthly_changes = []
greatest_increase = ["", 0]  # Store as [date, amount]
greatest_decrease = ["", float("inf")]  # Store as [date, amount]

# Open the CSV file
with open(budget_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row
    header = next(csv_reader)
    
    # Iterate through the CSV rows
    for row in csv_reader:
        # Count the total months
        total_months += 1
        
        # Calculate the total profit/losses
        total_profit_losses += int(row[1])
        
        # Calculate the monthly change in profit/losses
        if previous_month_profit_losses is not None:
            monthly_change = int(row[1]) - previous_month_profit_losses
            monthly_changes.append(monthly_change)
            
            # Check for greatest increase in profits
            if monthly_change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = monthly_change
            
            # Check for greatest decrease in profits
            if monthly_change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = monthly_change
        
        previous_month_profit_losses = int(row[1])
    
    # Calculate the average change in "Profit/Losses"
    average_change = sum(monthly_changes) / len(monthly_changes) if monthly_changes else 0

# Print the analysis
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

def write_file(data):
    file_name = 'PyBank.txt'