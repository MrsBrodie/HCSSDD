# Task 20: 5k running times

A local running club is running a 5k run competition. Over 2 days the runners run two 5k races. The runners times are recorded in a file below.  Their  name, category (Junior, Senior or Elite) and bib number along with their times are stored. A sample of the file runnertimes.csv  is shown below:

Lyven Natale,Elite,512,12:07:49,12:07:14

Your task is to read and process the file. The data should be stored in suitable data structures and written in a modular manner. 

The program must offer the following functions:

❏	Allow the user to enter a bib number or name (non case specific) to display the runners details (with an appropriate message if not found) 
❏	Display the quickest and slowest times for the Elite category on both days.
❏	Display the total amount of all Junior or Senior contestants with a qualifying time of 22min (0:22:00) for either race and also save these details to a new file. When writing the file you can simplify the algorithm by opening a file before traversing an array and then closing it at the end. This will mean that you do not have to repeatedly open and close files

HINT: You can use < and > on strings just as with numbers.
