#Higher Computng Science
#Task 22: ISBN Version using records

#function to declare one record filename	titles(), authors(), ISBN(), prices() 

def createBook (title, author, isbn, price):
  book={"title": title , "author": author,"ISBN":isbn,"price":price}
  return book

def readBooks(filename):
  allBooks=[]
  
  with open (filename) as readfile:
    line = readfile.readline()
    while line:
      items = line.rstrip('\n').split(",")
      book = createBook(items[0],items[1],items[2],items[3])
      allBooks.append(book)
      line=readfile.readline().rstrip('\n')  
  return allBooks

def searchBooks(allBooks):
  found=False
  choice=input("Please enter the ISBN of the book you are looking for: ")
    
  for book in allBooks:
    if book["ISBN"] == choice:
      found=True
  if found==True:
     print("Item details", book)
  else:
     print("Book not found")
  return 

filename="books.txt"
allBooks=readBooks(filename)
searchBooks(allBooks)



#print(allBooks)