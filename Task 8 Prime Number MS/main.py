#function to get input 

def GetNo():
  number = int(input("Enter a number:"))
  return number 

 
 

#function to check if prime 

def CheckIfPrime(number): 
  #assigning values
  prime = ""
  count = 0
  denom = 2 
  for counter in range(0,number-2):
    prime=number%denom
    denom = denom + 1
  
  if prime == 0:
    count = count + 1
    #display 
  elif count > 0:
    print(number,"is not a prime number")
  else:
    print(number,"is a prime number") 

#main program 

number = GetNo()
CheckIfPrime(number)
