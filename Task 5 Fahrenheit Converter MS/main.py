'''Higher Computing Science
Task 4: Fahrenheit Converter
You are going to create a program that uses a function to take in the value in Celsius and convert it into Fahrenheit.  The output will be formatted to two decimal places. The formula is: (celsius * 1.8) + 32. The top level design below should be refined as appropriate. '''

#Function to get celcius input
def getCelcius():
  celcius=float(input("Enter the temperature in celcius: "))
  return celcius

#Function to calculate Fahrenheit
def calcFar():
  far=(celcius*1.8)+32
  far=float(round(far,2))
  return far


#main body of the program where the functions/procedures are called
celcius= getCelcius()
far=calcFar()
print(celcius, "degrees centigrade is", format(far,".2f"), "farenheit")