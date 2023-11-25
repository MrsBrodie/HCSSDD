''' Higher Computing Science
Task: Reading a file (Single Line)
To parse and process a single line CSV file. 
So far all of your files have been comma separated or plain text on seperate lines. Sometimes you may have a single file such as below where all of the text is on a single line 

The file below for example has a list of Ticket Sales (sales.csv) showing the name, date of purchase, number of tickets and the price for 100 people.  We will be writing a program which will read this file and process it into parallel arrays to display the information for each purchase. '''

def readfile():
  namesarray = [None]*100
  datesarray = [None]*100
  ticketsarray = [None]*100
  pricearray = [None]*100
  counter = 0
  
  with open ("sales.csv") as readfile:
    #read the only line in the file
    line = readfile.readline().rstrip("\n")
    #split on the comma
    items = line.split(",")
    #set a loop that will increase in steps of four    
    for purchasecounter in range(0,len(items),4):
      #the counter variable is used to ensure that
      #each element in the parallel arrays is assigned correctly
      #the purchase counter is used to step through the items array
      namesarray[counter] = items[purchasecounter]
      datesarray[counter] = items[purchasecounter+1]
      ticketsarray[counter] = items[purchasecounter+2]
      pricearray[counter] = items[purchasecounter+3]
      counter += 1 
#file now closed
  return namesarray, datesarray, ticketsarray, pricearray 

#now create a a function to display thecontents of the four arrays
def display(namesarray, datesarray, ticketsarray, pricearray):
  print("Names" + "\t" + "Dates" + "\t" + "Tickets" + "\t" + "Price")
  for x in range(len(namesarray)):
    print(namesarray[x]+ "\t" + datesarray[x] + "\t" + ticketsarray[x] + "\t" + pricearray[x]) 

#crete a main function to call all subprograms
def main():
  names, dates, tickets, price = readfile()
  display(names, dates, tickets, price) 

#call the main function 
main() 

 