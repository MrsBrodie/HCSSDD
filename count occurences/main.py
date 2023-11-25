def countOccurrences(item,theList):
  occurrences=0
  for i in theList:
    if i==item:
      occurrences=occurrences+1
  return occurrences
  
#The list of numbers
theList=[0,1,3-2,4,5,4,2,3,1,99,46,85,88,99,99,99]

#This is the value you are looking to see how many
#times it occurs in the array 
item=99 

occurrences=countOccurrences(item,theList)

#prints how many times the was found in the array 
print(occurrences)