'''Higher Computing Science
Task 9: Converting Numbers
Your task is to create a function to check if a number that has been entered is an integer or not.'''

#function to get input 
def getNo():
  myNumber = float(input("Enter a number :"))
  return myNumber

 
#check number 
def numberNew(myNumber):
  myNewNumber = myNumber+1
  return myNewNumber 

 
#positive or negative 
def displayResult(myNumber,myNewNumber):
  if myNewNumber < 0 and myNewNumber > round((myNumber-0.4),0)+1:
    print(myNumber, "is a negative real number")
  elif myNewNumber > 0 and myNewNumber < round((myNumber),0)+1:
    print(myNumber, "is a positive real number")
  elif myNewNumber < 0 and myNewNumber == myNumber+1:
    print(myNumber, "is a negative integer")
  elif myNewNumber> 0 and myNewNumber == myNumber+1:
    print(myNumber ,"is a positive integer")
  return 


#main program 
def main():
  myNumber=getNo()
  myNewNumber=numberNew(myNumber)
  displayResult(myNumber,myNewNumber) 
  return#

main()