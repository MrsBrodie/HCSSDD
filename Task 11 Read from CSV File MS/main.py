#function to open and read the file 

def readDetails():
  #create two arrays that are blank and will hold 20 elements each
  namesarray=[None]*20
  housesarray=[None]*20
  #create a counter to count of the total number of elements in each array
  counter=0

  #open the file that you intend to read, make sure the file is available in the files section on the left hand side of this window
  with open("PupilDetails.csv") as readfile:
    #read the first line of the file
    line=readfile.readline().rstrip('\n')
    #while this line has a value (there is soome text)
    while line:
      #split the file on each comma
      items=line.split(",")
      #first element has the name
      namesarray[counter]=items[0]
      #second element has the house
      housesarray[counter]=items[1]
      counter+=1
      line=readfile.readline().rstrip('\n')
    input("File read complete, please press enter")
    return namesarray, housesarray

def displayDetails(namesarray, housesarray):
  #adding labels at the top of the output so the data has context
  print("{0:<10s}".format("Name")+"\t"+"{0:<10s}".format("House"))
  print("")
  #create a loop to display each item of each array and format the output inline with the labels above
  for x in range(len(namesarray)):
    print("{0:<10s}".format(namesarray[x])+"\t"+"{0:<10s}".format(housesarray[x]))

#the main function will call all subprograms
def main():
  namesarray,housesarray = readDetails()
  displayDetails(namesarray, housesarray)

#call the main function
main()

  




