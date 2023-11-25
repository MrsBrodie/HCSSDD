def Writefile(filecontents):
  with open('helloworld.txt', 'w') as filehandle:
    filehandle.write(message)
    print('File update...')
  
message=input("Please enter your message ")

Writefile(message)
