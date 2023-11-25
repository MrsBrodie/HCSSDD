''' Higher Computing Science
Task 12: Creating a CSV file

 A teacher is writing a program to automate some SQA processes for their school.  

They want a program that will allow them to enter Forenames, Surnames and Scottish Candidate Numbers (SCN’s). The program should then export the data into a Comma Separated File which could be used to import into a database. '''

#create a function that will ask for pupil details.
def inputDetails():
  pupils = int(input("Enter number of pupils:"))
  #create 3 blank arrays based on the number of pupils the user specifies
  forenames = [None]*pupils
  surnames = [None]*pupils
  SCN = [None]*pupils

  #create a loop that will run for the number of pupils the user specifies. i means index and it relates to the number the loop is currently at. The index always starts at 0.
  for i in range(pupils):
    #get the forename for each pupil            
    forenames[i] = input("Enter forename of pupil " + str(i+1) + " : " )
    #get the surname for each pupil
    surnames[i] = input("Enter surname of pupil " + str(i+1) + " : " )
    #get the SCN for each pupil
    SCN[i] = input("Enter SCN of pupil " + str(i+1) + " : " )
  
  return forenames, surnames, SCN 

#create a procedure that will create a csv file called SCN.csv and write the contents of each array while adding a comma between each element of the array.
def writeFile(forenames, surnames, SCN):
  with open ("SCN.csv","w") as writeFile:
    for i in range(len(forenames)):
      line = SCN[i] + "," + forenames[i] + "," + surnames[i] + "\n"
      writeFile.write(line)
  print("FILE WRITTEN") 

#The main1 function will call all subprograms
def main1():
  SCN, forenames, surnames = inputDetails()
  writeFile(forenames,surnames,SCN) 

#Call the main function
main1() 