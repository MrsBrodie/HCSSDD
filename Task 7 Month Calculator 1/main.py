'''Higher Computing Science
Task 7: Month Calculator
You are to write a program that will allow the user to enter the number of the month and display which a message stating whether it has 28(or 29), 30 or 31 days.  

Input should be validated so that only input between 1 and 12 (inclusive)  is accepted. The top level design below should be refined as appropriate. '''

#Step 1: Enter Valid number of Month
def noOfMonth():
  month=int(input("what number of the month is it? "))
  if month >= 1 and month <= 12:
    print("valid input")
    month=month-1
  else:
    print("invalid input")
  
  return month

#Step 2: Find number of days from array
def daysInMonth(month):
  days=[31,28,31,30,31,30,31,31,30,31,30,31]
  months=["January","February","March","April","May","June", "July","August","September","October","November","December"]
  
  return days, months  
  
#Step 3 display number of days
def displayDays(month, months, days):
  print(months[month],"has", days[month],"days")

month=noOfMonth()
days,months=daysInMonth(month)
displayDays(month, months, days)
 

 