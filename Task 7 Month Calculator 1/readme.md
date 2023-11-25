# Task 7: Month Converter 

You  are to write a program that will allow the user to enter the number of  the month and display which a message stating whether it has 28(or 29),  30 or 31 days. Input should be validated so that only input between 1  and 12 (inclusive)  is accepted. The top level design below should be refined as appropriate. 

**Top Level Design and Data Flow** 

**Main Steps**                                                               **In**                                                         **Out** 

**1** Enter Valid Number of Month 

**2** Find number of days from array 

**3** Display number of days 

A partial design for step 2 is shown below: 

2.1 DECLARE days INITIALLY [31,28,31,30,31,30,31,31,30,31,30,31] 
 2.2 RETURN number of days in month 
  
 

**Extension** 

The user has now requested a modification to the program. They want the program to display the actual month as well. 

For example: 

Please enter the number of the month: **5** 
 **Output: May has 31 days.** 
