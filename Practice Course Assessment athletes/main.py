#Practice Course Assessment
#Name:
#SCN Number:
#Date:


def readFile():
  #creating arrays to organise and store the data from the athletes.csv file
  entryID=[None]*30
  location=[None]*30
  forename=[None]*30
  surname=[None]*30
  jumps=[None]*30

  counter=0

#open csv file
  with open("athletes.csv") as readfile:
    line=readfile.readline().rstrip('\n')
#start loop for 30 athletes
    while line:
      items=line.split(",")
#store the information in 5 parllel arrays
      entryID[counter]=(items[0])
      location[counter]=(items[1])
      forename[counter]=(items[2])
      surname[counter]=(items[3])
      jumps[counter]=int(items[4])
      counter+=1
      line=readfile.readline().rstrip('\n')
#end loop
  
#out entryID(), location(), forename(), surname(), jumps()
#pass arrays by reference
  return entryID,location,forename,surname,jumps

#in entryID ,location, forename, surname
def getBib(entryID,location,forename,surname):
  bibValue=[]
#loop for 30 athletes
  for counter in range(30):
#set bibValue to first letter of their forename and full surname and the ASCII value of their location
    firstChar=forename[counter][0]
    secondChar=surname[counter]

    #using the modulus predefined function
    thirdChar=ord(location[counter][0])

    #using the str predefined function
    bib=str(firstChar)+str(secondChar)+str(thirdChar)

    bibValue.append(bib)
    
#create the bibValues.csv file
#write the entryID and bibValue to the file
  with open("bibValues.csv", "w")as writefile:
    for i in range (30):
      line = entryID[i]+","+bibValue[i]+"\n"
      writefile.write(line)

def highestJumps(jumps):
#set maxJumps to the first number in the jumps array
  maxJumps=jumps[0]
  position=0

#start the loop from the second index of the array
  for counter in range(1, len(jumps)):
#loop for 30 athletes
#if the current number of jumps is bigger than maxJumps then set maxJumps to current number
    if jumps[counter] > maxJumps:
      maxJumps=jumps[counter]
#get position of maxJumps
      position=counter
#out maxJumps()
  return maxJumps, position

#in location()
def totalLocations(location):
#set locations to 0
  coatbridge=0
  inverness=0
  kirkcaldy=0
  motherwell=0
  dundee=0
  livingston=0
#start counter for number of atheletes
  for counter in range(len(location)):
#if location is found +1 to the total
    if location[counter]=="Coatbridge":
      coatbridge+=1
    elif location[counter]=="Inverness":
      inverness+=1
    elif location[counter]=="Kirkcaldy":
      kirkcaldy+=1
    elif location[counter]=="Motherwell":
      motherwell+=1
    elif location[counter]=="Dundee":
      dundee+=1
    elif location[counter]=="Livingston":
      livingston+=1
#out coatbridge(),inverness(),kirkcaldy(),motherwell(),dundee(),livingston()
  return coatbridge,inverness,kirkcaldy,motherwell,dundee,livingston


#in maxJumps(),forename(), surname(),coatbridge(),inverness(),kirkcaldy(),motherwell(),dundee(),livingston()
def display(maxJumps, forename, surname,position,coatbridge,inverness,kirkcaldy,motherwell,dundee,livingston):
#print forename and surname at maxJumps position
  print("The winner is",forename[position], surname[position], "with",maxJumps,"jumps")
  print("Coatbridge had", coatbridge,"finalists")
  print("Inverness had", inverness,"finalists")
  print("Kirkcaldy had", kirkcaldy,"finalists")
  print("Motherwell had", motherwell,"finalists")
  print("Dundee had", dundee,"finalists")
  print("Livingston had", livingston,"finalists")


#call all functions
entryID,location,forename,surname,jumps=readFile()
getBib(entryID,location,forename,surname)
maxJumps,position=highestJumps(jumps)
coatbridge,inverness,kirkcaldy,motherwell,dundee,livingston=totalLocations(location)
display(maxJumps, forename, surname,position,coatbridge,inverness,kirkcaldy,motherwell,dundee,livingston)





