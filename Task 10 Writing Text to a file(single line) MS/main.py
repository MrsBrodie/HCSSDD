'''Higher Computing Science
Task 10: Writing to a text file(single line)
Write a program that will ask the user to enter a message and then store it in a new text file. '''


#Create a function that will create a new text file and allow the user to write contents to the text file.  
#"newtextfile.txt" is the name of the text file that will be created
#the, "a" is used to append the contents of the text file
def writefile(filecontents):
  with open("newtextfile.txt","a") as writefile:
    writefile.write(filecontents + "\n")
    print("F I L E U P D A T E D")
  return

#Create a function that will allow the user to enter a message
#the message will then be added to the file.
def message():
  filecontents = input("ENTER MESSAGE:")
  return filecontents


filecontents=message()
writefile(filecontents)