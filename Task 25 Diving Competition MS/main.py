#Higher Computing Science
#Task 25 Diving Competition

def readfile(filename):
  divers=[]
  diving=[]
  items=[]
  counter=0
 
  with open (filename) as readfile:
    line = readfile.readline()
    while line:
      items = line.rstrip('\n').split(",")
      divers=items
      diving.append(divers)
      counter+=1
      line=readfile.readline().rstrip('\n')  
  return divers,diving

def finalscore(diving):
  maxScore=float()
  minScore=float()
  counter=0

  for divers in diving:
    diver=+1
    total=float()
    for diver in divers:
      total=total+float(diver)
      if float(diver)>float(maxScore):
        maxScore=diver
      if float(diver)<float(minScore):
        minScore=diver
    counter+=1
    total=float((total-minScore)-float(maxScore))
    total=round(total,2)
    print("Score",counter,float(total)"MS")
  return 

filename="Diving.csv"
divers, diving=readfile(filename)
print(diving)
finalscore(diving)

