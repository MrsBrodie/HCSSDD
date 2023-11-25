from collections import namedtuple
import csv

with open("oscars.csv") as csvfile:
    reader = csv.reader(csvfile)
    Winner = namedtuple("Winner", "index year age name movie")

    for row in reader:
        current_winner = Winner(row[0], row[1], row[2], row[3], row[4])
        print(current_winner.name + " won the Oscar  " + current_winner.movie + " in " + current_winner.year)
        print (f"{current_winner.name} won the oscar for {current_winner.movie} in  {current_winner.year}")