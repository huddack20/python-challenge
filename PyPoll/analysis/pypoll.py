import csv
import os

election_data_csv = os.path.join('..', 'Resources', 'election_data.csv')

def main():

    # read mode of csv file 
    with open(election_data_csv, 'r') as csvfile:

        reader = csv.reader(csvfile)
        next(reader) # skip the first line, the header in csv

        # initial variable definition for each candidate
        num_row = 0
        num_charles = 0
        num_diana = 0
        num_raymon = 0

        for row in reader:
    
            num_row += 1
            
            if row[2].startswith("Charles"):
                num_charles += 1

            elif row[2].startswith("Diana"):
                num_diana += 1

            else:
                num_raymon += 1

        # Percentage of votes each candidate won 
        P_charles = (num_charles/num_row)*100.0
        P_diana = (num_diana/num_row)*100.0
        P_raymon = (num_raymon/num_row)*100.0

        if (num_charles > num_diana) and (num_charles > num_raymon):
            winner = "Charles Casper Stockham"
        elif (num_raymon > num_charles) and (num_raymon > num_diana):
            winner = "Raymon Anthony"
        else:
            winner = "Diana Degette"

        print("\n\'\'\'")
        print("Election Results")
        print("------------------------------")
        print("Total Votes: %d" % num_row)
        print("------------------------------")
        print("Charles Casper Stockham: %.3f%% (%d)" % (P_charles, num_charles))
        print("Diana Degette: %.3f%% (%d)" % (P_diana, num_diana))
        print("Raymon Anthony Doane: %.3f%% (%d)" % (P_raymon, num_raymon))
        print("------------------------------")
        print("Winner: %s" % winner)
        print("------------------------------")
        print("\'\'\'")

    # file write mode
    with open('result_pypoll.txt', 'w') as o_file:

        o_file.write("\n\'\'\'\n")
        o_file.write("Election Results\n")
        o_file.write("------------------------------\n")
        o_file.write("Total Votes: %d\n" % num_row)
        o_file.write("------------------------------\n")
        o_file.write("Charles Casper Stockham: %.3f%% (%d)\n" % (P_charles, num_charles))
        o_file.write("Diana Degette: %.3f%% (%d)\n" % (P_diana, num_diana))
        o_file.write("Raymon Anthony Doane: %.3f%% (%d)\n" % (P_raymon, num_raymon))
        o_file.write("------------------------------\n")
        o_file.write("Winner: %s\n" % winner)
        o_file.write("------------------------------\n")
        o_file.write("\'\'\'\n")

        csvfile.close()
        o_file.close()

if __name__ == '__main__':
    main()
