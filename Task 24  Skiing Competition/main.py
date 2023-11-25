#Higher Computing Science 
#Task 24:  Skiing Competition

def createSkierRecord (name, racenumber, team, time,penalty,totaltime):
  skier={"name": name , "racenumber": racenumber,"team":team, "time":time,"penalty": str(penalty), "totaltime": totaltime}
  return skier

def readfile(filename):
  skiing=[]
  
  with open (filename) as readfile:
    line = readfile.readline()
    while line:
      items = line.rstrip('\n').split(",")
      totaltime=((len(items[4])*0.5)+float(items[3]))
      skier= createSkierRecord(items[0],items[1],items[2],items[3],items[4],totaltime)
      skiing.append(skier)
      line=readfile.readline().rstrip('\n')  
  return skiing


def finalteams(skiing):
  glasgowJ=[]
  aberdeenJ=[]
  dundeeD=[]
  slalomF=[]
  for skier in skiing:
    if skier["team"]== "Glasgow Juniors":
      glasgowJ.append(skier)
    elif skier["team"]== "Aberdeen Juniors":
      aberdeenJ.append(skier)
    elif skier["team"]== "Dundee Dry":
      dundeeD.append(skier)
    elif skier["team"]=="Slalom Fun":
      slalomF.append(skier)
  return glasgowJ,aberdeenJ,dundeeD, slalomF


def bestSki(skiing):
  maximum=skiing[0]
  for skier in skiing:
    if skier["totaltime"] > maximum["totaltime"]:
      maximum=skier
  return maximum

def totalteamScores(team):
  totalScore=0
  for skier in team:
    totalScore=totalScore+skier["totaltime"]
  return totalScore


filename="skiing.csv"
skiing=readfile(filename)
maximum=bestSki(skiing)
glasgowJ, aberdeenJ, dundeeD, slalomF=finalteams(skiing)
totalScoreA=totalteamScores(aberdeenJ)
totalScoreG=totalteamScores(glasgowJ)
totalScoreD=totalteamScores(dundeeD)
totalScoreS=totalteamScores(slalomF)
print("Individual Winner", maximum )
print("Final Scores")
print("Aberdeen Juniors", round(totalScoreA,2), "seconds")
print("Glasgow Juniors", round(totalScoreG,2), "seconds")
print("Dundee Dry", round(totalScoreD,2), "seconds")
print("Slalom Fun", round(totalScoreS,2), "seconds")






