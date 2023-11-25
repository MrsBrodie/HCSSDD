# Task 17 FIND MAX
#Mrs Brodie

# Open file and store in two arrays

def readDetails(filename):
  namesarray=[None]*50
  scoresarray=[None]*50
  items=[]
  counter=0

  with open (filename) as readfile:
    line = readfile.readline().rstrip('\n')
    while line:
      items=line.split(",")
      namesarray[counter] = items[0]
      scoresarray[counter] = int(items[1])
      counter += 1
      line = readfile.readline().rstrip('\n')
    input("File read - press enter")
    return namesarray, scoresarray


def findMax(scoresarray):
  maxscore = scoresarray[0]
  for counter in range(1,len(scoresarray)):
    if scoresarray[counter] > maxscore:
      maxscore=scoresarray[counter]
  print("Highest score is: " + str(maxscore))

filename= "Scores.csv"
names,scores = readDetails(filename)
findMax(scores)



