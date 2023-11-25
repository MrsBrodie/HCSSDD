#function to open and read the file 

def readDetails():
  attraction=[None]*26
  category=[None]*26
  visitors=[None]*26
  daysOpen=[None]*26
  height=[None]*26
  counter=0


  with open("attractions.csv") as readfile:    #read the first 
    line=readfile.readline().rstrip('\n')
    while line:   #while this line has a value 
      items=line.split(",")       #split the file on each comma
      attraction[counter]=str(items[0] )   #first element has the name
      category[counter]=str(items[1] )     #second element has the category
      visitors[counter]=int(items[2] )    #third element has the number of visitor
      daysOpen[counter]=int(items[3] )          #fourth element has the number of days open
      height[counter]=str(items[4] )  #fifth element has the height restrictions
      counter+=1
      line=readfile.readline().rstrip('\n')
    input("File read complete, please press enter")
    
    return attraction, category, visitors, daysOpen,height

def PopularAttractions(attraction, visitors):
  
  #create a variable to initially be set to 0 
  
  maxposition = visitors[0]
  position=0
  for counter in range(len(visitors)):
    if visitors[counter] > maxposition:
      maxposition=visitors[counter]
      position=counter

  print ("The most popular attaction is",attraction[position] )
    

def unPopularAttractions(AttractionArray, TotalVisitors):
  
  minposition = visitors[0]
  position=0
  for counter in range(len(visitors)):
    if visitors[counter] < minposition:
      minposition=visitors[counter]
      position=counter

  print ("The most popular attaction is",attraction[position] )
    
def writeService(attraction, category, daysOpen):
  days=[None]*26
  for i in range(len(attraction)):
    if category[i]=="Roller Coaster":
      days[i]=(int(daysOpen[i])%90)
      if 90-days[i]<=7:
        with open ("Service.csv","w") as writefile:
          line=(attraction[i]+","+category[i]+","+str(daysOpen[i])+"\n")
          writefile.write(line)
  print("FILE WRITTEN") 
  return 

def heightrestrictions(attraction, height):
  total=0
  for i in range(len(attraction)):
    if (height[i])[:1]=="1":
      total=total+1
  print("The total number of attractions which are taller than 1m is ", total)
      

attraction, category, visitors, daysOpen, height=readDetails()
PopularAttractions(attraction, visitors)
unPopularAttractions(attraction, visitors)
writeService(attraction,category, daysOpen)
heightrestrictions(attraction, height)
