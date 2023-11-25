#Higher Computing Science
#Task 21 Using Parallel Arrays

def readfile(filename):
  bookNo = [None]*20
  authorNo = [None]*20
  number = [None]*20
  price = [None]*20
  counter=0
  
  with open(filename) as readfile:
    line=readfile.readline().rstrip('\n')
    while line:
      items=line.split(",")
      bookNo[counter]=items[0]
      authorNo[counter]=items[1]
      number[counter]=items[2]
      price[counter]=items[3]
      counter+=1
      line=readfile.readline().rstrip('\n')
    input("File read complete, please press enter")
  return bookNo, authorNo, number, price 

def searchBook(bookNo, authorNo, number, price):
  found = False
  choice = input("Enter ISBN ")
  for counter in range(0, len(number)):
    if number[counter] == choice:
      found = True
      position = counter
      if found == False:
        print("Not Found")
      else:
        print("Book found:\n")
        print("Titles: ",bookNo[position])
        print("Author: ",authorNo[position])
        print("Price: ",price[position]) 

filename = "books.txt" 
bookNo, authorNo, number, price = readfile(filename) 
searchBook(bookNo, authorNo, number, price) 
