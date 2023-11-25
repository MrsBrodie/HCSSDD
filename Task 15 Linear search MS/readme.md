# Task 15: Linear Search

**Standard Algorithm**

You are to design and create a program that will allow the stock file for a local garden centre  to be imported and searched ( see example file below)

Yosemite Onion, 18.27

The file is ordered in the order items appear in aisles. So an item at position 0 is located in Aisle 1.

Your program will read the stock file of 200 items (maximum) and then prompt the user to search for an item name (non case specific). It will then return the aisle number that the item is in.

**Top Level Design and Data Flow**
Main Steps	In	Out
1	ReadFile		items(), prices()
2	SearchFile	searchitem,items()	

**Refinements  (partial)**
2.1 PROCEDURE SearchFile (searchitem,items(),prices() )
2.2 FOR counter = 0 TO LEN(items())
2.3 IF items[x] = searchitem THEN
2.4 SEND "Match found at aisle " & (counter + 1) TO DISPLAY
2.5 END IF
2.6 NEXT counter
2.7 END PROCEDURE

 
