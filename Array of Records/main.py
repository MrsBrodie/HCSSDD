from dataclasses import dataclass

@dataclass
class trip:
  name: str="name"
  gender: str="f"
  place: str="London"




def readfile():
  tripsList = [trip] * 100
  i=0
  with open("SchoolTrips.csv", "r") as readfile:
    line = readfile.readline()
    while line:
      items = line.rstrip('\n').split(",")
      tripsList[i] = trip(items[0], items[1], items[2])
      tripsList.append(trip)
      i+=1
      line=readfile.readline().rstrip('\n')
    input("File read complete, please press enter")

  return tripsList


def countTrips(tripsList):  
  london=0
  paris=0
  bmx=0
  mB=0
  gW=0
  for i in range(0,100):
    if tripsList[i].place=="London":
      london+=1
    elif tripsList[i].place=="Paris":
      paris+=1
    elif  tripsList[i].place=="BMX":
      bmx+=1
    elif  tripsList[i].place=="Mountain Biking":
      mB+=1
    elif tripsList[i].place=="Gorge Walking":
      gW+=1
    i+=1
  print("London: ", london, "Paris: ", paris, "BMX: ", bmx, "Mountain Biking: ", mB, "Gorge Walking: ",gW)
  return london,paris,bmx,mB,gW

def writeLondon(tripsList):
  with open("London Trip.csv","w") as writefile:
    for i in range(len(tripsList)):
      if tripsList[i].place=="London":
        writefile.write(tripsList[i].name+","+str(tripsList[i].gender)+"\n")

def writeParis(tripsList):
  with open("Paris Trip.csv","w") as writefile:
    for i in range(len(tripsList)):
      if tripsList[i].place=="Paris":
        writefile.write(tripsList[i].name+","+str(tripsList[i].gender)+"\n")

def writeBMX(tripsList):
  with open("BMX Trip.csv","w") as writefile:
    for i in range(len(tripsList)):
      if tripsList[i].place=="BMX":
        writefile.write(tripsList[i].name+","+str(tripsList[i].gender)+"\n")

def writeMountain(tripsList):
  with open("MountainBiking Trip.csv","w") as writefile:
    for i in range(len(tripsList)):
      if tripsList[i].place=="Mountain Biking":
        writefile.write(tripsList[i].name+","+str(tripsList[i].gender)+"\n")

def writeGorge(tripsList):
  with open("Gorge Walking Trip.csv","w") as writefile:
    for i in range(len(tripsList)):
      if tripsList[i].place=="Gorge Walking":
        writefile.write(tripsList[i].name+","+str(tripsList[i].gender)+"\n")

tripsList=readfile()
london,paris,bmx,mB,gW=countTrips(tripsList)
writeLondon(tripsList)
writeParis(tripsList)
writeBMX(tripsList)
writeMountain(tripsList)
writeGorge(tripsList)






