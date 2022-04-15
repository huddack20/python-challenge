"""
PyBank main.py, which analyzes data of bank profit/losses. 
It shows how each month revenue is changed from the previous month.

"""

import csv
import os

budget_data_csv = os.path.join('..', 'Resources', 'budget_data.csv')

def main():

    with open(budget_data_csv) as csvfile:

        reader = csv.reader(csvfile)
        next(reader) # skip the the first line, the header in csv

        total_amount = 0.0
        num_months = 0
        Greatest = 0.0
        G_month = ""
        Lowest = 0.0
        L_month = ""
        Avg_change = 0.0

        initial = 0.0
        prev_pl = 0.0
        pl_change = 0.0
        pl_change_list = []
        month_list = []

        for i, row in enumerate(reader):
            
            # the first row of the data, the initial profit or losses
            if i == 0:
                initial = row[1]
                prev_pl = initial
                total_amount = total_amount + float(row[1])
                num_months += 1

            else:

                total_amount = total_amount + float(row[1])
                num_months += 1

                current_pl = row[1]
                pl_change = float(current_pl) - float(prev_pl)

                    # Assign current profit/losses to previous profit/losses
                prev_pl = current_pl

                    # Append profit/losses/current month to lists
                pl_change_list.append(pl_change)
                month_list.append(row[0])

        Avg_change = sum(pl_change_list)/len(pl_change_list)

        Greatest = max(pl_change_list)
        Lowest = min(pl_change_list)

        year = num_months/12.0
        
        G_month = month_list[pl_change_list.index(max(pl_change_list))]
        L_month = month_list[pl_change_list.index(min(pl_change_list))]

        print("\n\'\'\'")
        print("Financial Analysis")
        print("------------------------------")
        print("Total Months: %d" % num_months)
        print("Total years: %.2f" % year)
        print("Total: $%.2f" % total_amount)
        print("Average Change: $%.2f" % Avg_change)
        print("Greatest Increase in Profits: %s ($%.2f)" % (G_month, Greatest))
        print("Greatest Decrease in Profits: %s ($%.2f)" % (L_month, Lowest))
        print("\'\'\'")

    with open('result_pybank.txt', "w") as o_file:

        o_file.write("\'\'\'\n")
        o_file.write("Financial Analysis\n")
        o_file.write("------------------------------\n")
        o_file.write("Total Months: %d\n" % num_months)
        o_file.write("Total: $%.2f\n" % total_amount)
        o_file.write("Average Change: $%.2f\n" % Avg_change)
        o_file.write("Greatest Increase in Profits: %s ($%.2f)\n" % (G_month, Greatest))
        o_file.write("Greatest Decrease in Profits: %s ($%.2f)\n" % (L_month, Lowest))
        o_file.write("\'\'\'")

        csvfile.close()
        o_file.close()

if __name__ == '__main__':
    main()
