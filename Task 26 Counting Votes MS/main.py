#Higher Computing Science
#Task 26: Counting Votes

def createRecord (number, party,candidate, valid):
  vote={"number": number , "party": party,"candidate":candidate,"valid":valid}
  return vote

def readfile(filename1,filename2,filename3,filename4, filename5):
  votecounts=[]
  with open (filename1) as readfile:
    line = readfile.readline()
    while line:
      items = line.rstrip('\n').split(",")
      vote= createRecord(items[0],items[1],items[2],items[3])
      votecounts.append(vote)
      line=readfile.readline().rstrip('\n') 
  with open (filename2) as readfile:
    line = readfile.readline()
    while line:
      items = line.rstrip('\n').split(",")
      vote= createRecord(items[0],items[1],items[2],items[3])
      votecounts.append(vote)
      line=readfile.readline().rstrip('\n')
  with open (filename3) as readfile:
    line = readfile.readline()
    while line:
      items = line.rstrip('\n').split(",")
      vote= createRecord(items[0],items[1],items[2],items[3])
      votecounts.append(vote)
      line=readfile.readline().rstrip('\n')
  with open (filename4) as readfile:
    line = readfile.readline()
    while line:
      items = line.rstrip('\n').split(",")
      vote= createRecord(items[0],items[1],items[2],items[3])
      votecounts.append(vote)
      line=readfile.readline().rstrip('\n') 
  with open (filename5) as readfile:
    line = readfile.readline()
    while line:
      items = line.rstrip('\n').split(",")
      vote= createRecord(items[0],items[1],items[2],items[3])
      votecounts.append(vote)
      line=readfile.readline().rstrip('\n')           
  return votecounts

def totalVoteCount(votecounts,party):
  totalVotes=0
  for vote in votecounts:
    if vote["party"]==party and vote["valid"]=="VALID":
      totalVotes=totalVotes+1
  print(party, totalVotes, "votes")
  return totalVotes

filename1="Voting1.csv"
filename2="Voting2.csv"
filename3="Voting3.csv"
filename4="Voting4.csv"
filename5="Voting5.csv"
votecounts=readfile(filename1,filename2, filename3,filename4,filename5)
party2=("Apple Party")
totalVotes=totalVoteCount(votecounts,party2)
party3=("Rampant Vikings")
totalVotes=totalVoteCount(votecounts,party3)
party=("Abolish exams!")
totalVotes=totalVoteCount(votecounts,party)
party1=("Party against Homework")
totalVotes=totalVoteCount(votecounts,party1)
totalVotes=totalVoteCount(votecounts,party3)
party=("Abolish exams!")

