# Task 21: ISBM Version 1

You are to write a program that will allow the user to read the contents of a file - books.txt which will contain the Title, Author, ISBN and Price of 20 books. A sample of the file is below:

When the file has been read the program will allow the user to search the contents of the file on the ISBN field and display the book details  if a book has been found. 

**Top Level Design and Data Flow**
Main Steps	In	Out
1	ReadFile	filename	titles(), authors(), ISBN(), prices() 
2	SearchBookDetails	titles(), authors(), ISBN(), prices() 	

**Refinements  (partial)**
2.	ReadFile
2.1.	SET counter = 0
2.2.	INITIALISE ARRAYS
2.3.	OPEN FILE (filename) FOR READING
2.4.	line = READ line from FILE
2.5.	WHILE NOT EOF
2.6.	SET items = line.split(“,”)
2.7.	titles[counter] = items[0]
2.8.	authors[counter] = items[1]
2.9.	ISBN[counter] = items[2]
2.10.	prices[counter] = items[3]
2.11.	line = READ line from FILE
2.12.	INCREMENT COUNTER
2.13.	END WHILE
2.14.	RETURN titles,authors,ISBN,prices
