# Task 18: Pupil Marks
#

def readDetails():
  namesarray = [None]*100
  formsarray = [None]*100
  prelimsarray = [None]*100
  coursesarray = [None]*100
  items=[]
  counter = 0

  with open("ComputingMarks.csv") as readfile:
    line=readfile.readline().rstrip('\n')
    while line:
      items=line.split(",")
      namesarray[counter]=items[0]
      formsarray[counter]=items[1]
      prelimsarray[counter]=int(items[2])
      coursesarray[counter]=int(items[3])
      counter += 1
      line=readfile.readline().rstrip('\n')
    input("File read complete. Press enter to continue")
  return namesarray, formsarray, prelimsarray, coursesarray


def findMin(marks):
  minposition=0  
  for counter in range(len(marks)):
    if marks[counter] < marks[minposition]:
      minposition=counter
  return minposition
  
def findMax(marks):
  maxposition=0
  for counter in range(len(marks)):
    if marks[counter] > marks[maxposition]:
      maxposition=counter
  return maxposition
  
  
  
names, forms, prelim, course = readDetails()
minindex=findMin(prelim)
print("The minimum prelim mark was:", prelim[minindex], "from", names[minindex])
maxindex=findMax(prelim)
print("The maximum prelim mark was:", prelim[maxindex], "from", names[maxindex])


minindex=findMin(course)
print("The minimum course mark was:", course[minindex], "from", names[minindex])
maxindex=findMax(course)
print("The maximum course mark was:", course[maxindex], "from", names[maxindex])