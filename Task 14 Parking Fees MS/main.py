#function to create arrays to store the csv file data, open and read the file

def readDetails():
  licencearray=[None]*100
  datearray=[None]*100
  time1array=[None]*100
  time2array=[None]*100
  counter=0

  with open("times.csv") as readfile:
    #read the first line of the file
    line=readfile.readline().rstrip('\n')
    #while this line has a value (there is some text)
    while line:
      #split the file on each comma
      items=line.split(",")
      #first element has the licence
      licencearray[counter]=items[0]
      #second element has the date
      datearray[counter]=items[1]
      #third element is the arrival time
      time1array[counter]=items[2]
      #fourth element is the departure time
      time2array[counter]=items[3]
      #the counter is used to keep count of the number of records created
      counter+=1
      #creates a new line after the fourth element has been created
      line=readfile.readline().rstrip('\n')
    input("File read complete, please press enter")
    return licencearray,datearray,time1array,time2array

def costofparking(time1array, time2array):
  #create an array to store the parking cost for each record
  costarray=[None]*100
  #create an array to store the total time parked so a cost can be calculated
  timearray=[None]*100
  
  #create a loop to calculate the total time parked and from this the nested if will work out the parking cost for each record
  for x in range(len(time1array)):
    timearray[x]=float(time2array[x])-float(time1array[x])
    if timearray[x] <1.00:
      costarray[x]="£1.00"
    elif timearray[x]>=1.00 and timearray[x]<2.00:
      costarray[x]="£2.20"
    elif timearray[x]>=2.00 and timearray[x]<3.00:
      costarray[x]="£3.30"
    elif timearray[x]>=3.00 and timearray[x]<4.00:
      costarray[x]="£4.40"
    elif timearray[x]>=4.00 and timearray[x] <12.00:
      costarray[x]="£12.00"
    elif timearray[x]>=12.00:
      costarray[x]="£20.00"
  return costarray

#create a procedure that will create a new file called cost.csv, the total cost along with the licence, 
#date and times of parking and departure.
def writeFile(licencearray,datearray,time1array,time2array,costarray):
  with open ("cost.csv","w") as writeFile:
    for i in range(len(licencearray)):
      line = licencearray[i] + "," + datearray[i] + "," + time1array[i] + "," + time2array[i]+ "," + costarray[i] +"\n"
      writeFile.write(line)
  print("FILE WRITTEN") 
#create a procedure that will call all functions and procedures 
def main():
  licence,dates,time1,time2 = readDetails()
  cost=costofparking(time1,time2)
  writeFile(licence, dates,time1,time2,cost)

#call the main function
main()

  