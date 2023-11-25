#Mrs Brodie 
#Higher Course Assessment
#31/01/2020

def newmembers():
  print("What is your first name?")
  firstName=input()
  #nameArray.append(firstName)
  print("What is your surname?")
  surName=input()
  #surnameArray.append(surName)
  print("What is your category?")
  category=input()
  #categoryArray.append(category)
  return(firstName,surName,category)

def password():
  while password != password[]


def ReadDetails():
  nameArray=[None]*10
  surnameArray=[None]*10
  categoryArray=[None]*10
  passwordArray=[None]*10
  items=[]
  counter=0
  
  with open('members.csv')as readfile:
    line=readfile.readline().rstrip('\n')
    while line:
      items=line.split(",")
      nameArray[counter]=items[0]
      surnameArray[counter]=items[1]
      categoryArray[counter]=items[2]
      passwordArray[counter]=items[3]
      counter= counter+1
      line=readfile.readline().rstrip('\n')
    input("File read please press any key to continue")
    return nameArray,surnameArray,categoryArray,passwordArray

def DisplayDetails(nameArray,surnameArray,categoryArray,passwordArray):
  print("")
  for counter in range(len(nameArray)):
    print(nameArray[counter]+surnameArray[counter]+categoryArray[counter])
  
names, surnames, categories, passwords=ReadDetails()
newmembers()
DisplayDetails(names, surnames, categories, passwords)
