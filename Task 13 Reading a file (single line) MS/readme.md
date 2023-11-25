# Task 13: Reading a file 

So far all of your files have been comma separated or plain text on seperate lines. Sometimes you may have a single file such as below where all of the text is on a single line 

The file below for example has a list of Ticket Sales (sales.csv) showing the name, date of purchase, number of tickets and the price for 100 people.  We will be writing a program which will read this file and process it into parallel arrays to display the information for each purchase. 

**Refinements (partial)**

ReadFile(names(), dates(), tickets(),price() ) 

1.1 INITIALISE names, dates, tickets, prices AS ARRAYS [] * 100 

1.2 OPEN filename FOR READ ACCESS 

1.3 SET line = file.readline() 

1.4 SET items = line.split(“,”) 

1.5 FOR purchasecounter = 0 TO LEN(items),STEP 4 

1.6 namesarray[counter] = items[purchasecounter] 

1.7 datesarray[counter] = items[purchasecounter+1] 

1.8 ticketsarray[counter] = items[purchasecounter+2] 

1.9 pricearray[counter] = items[purchasecounter+3] 

1.10 SET counter = counter+1 

1.11 RETURN namesarray,datesarray,ticketsarray,pricearray 

 