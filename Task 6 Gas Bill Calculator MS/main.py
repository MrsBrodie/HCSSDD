'''Higher Computing Science
Task 5: Gas Bill Calculator 
When you submit a gas meter reading it converts the units used to kilowatt hours (kWh).  When receiving a bill your previous and current reading is used to calculate the number of imperial units and then this number is converted to kilowatt hours. Each kilowatt hour costs  3.74p. VAT is also charged on the total due at 5%. 

Create a function that will allow you to pass in the previous reading, current reading , calculate the number of kilowatt hours used (see formula below) and return the amount due (rounded to two decimal places). '''

#Function to get gas units.
def getUnits():
  reading1=int(input("Enter previous reading: "))
  reading2=int(input("Enter current reading: "))
  units=reading2-reading1
  return units

#Function to convert units into kWh
def calckWh(units):
  metricConvert=((units*1.022640)*2.83)
  kWhconvert=((metricConvert*39.3)/3.6)
  kWh=round(kWhconvert,2)
  return kWh

#Function to calculate price
def calcPrice(kWh):
  price=kWh*0.0374
  #add VAT
  price=price+((price*5)/100)
  price=round(price,2)
  return price

#Main program
def main():
  units=getUnits()
  kWh=calckWh(units)
  price=calcPrice(kWh)
  print("You have used", units, "units")
  print("This is", kWh, "kilowatt hours")
  print("Your bill is £",format(price,".2f"))

main() 



