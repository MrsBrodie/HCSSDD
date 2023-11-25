#Higher Computing Science
#creating records and arrays of records

from dataclasses import dataclass


@dataclass
#creating the data structure for a record(class) in Python
#first thing you do is name each field such as "name" etc
#secondly state the data type you are using such as "str" etc
class baker:
	name: str = "name"
	score: int = 0
	school: str = "Forfar Academy"
	level: str = "Secondary"


#reads file and stores each line a a dataclass as a record called baker,
#these are stored in an array called baking
def readfile():

	#create a blank array called baking to store each instance of baker (record)
	#baking is an array of records
	baking = []
	with open("baking.csv", "r") as readfile:
		line = readfile.readline()
		while line:
			items = line.rstrip('\n').split(",")
			#populating each record with data from the 4 items in the CSV
			#file and adding the record to the baking array
			baking.append(baker(items[0], int(items[1]), items[2], items[3]))

			line = readfile.readline().rstrip('\n')
		input("File read complete, please press enter")
	return baking


#This function traverses the baking array looking at the field called level
#to determine if it is primary or secondary then adds to the primary total or the secondary total.


def countBakers(baking):
	primary = 0
	secondary = 0
	#check each record (baker) in the array of records (baking)
	#looking at the "level" field for data matching the
	#information inside ""
	for baker in baking:
		if baker.level == "Primary":
			primary += 1
		elif baker.level == "Secondary":
			secondary += 1
	print("Primary: ", primary, "Secondary: ", secondary)
	return primary, secondary


#this function creates an array to store each level required, primary or secondary.
def getBakersOfLevel(baking, level):
	bakersOfLevel = []
	for baker in baking:
		if baker.level == level:
			bakersOfLevel.append(baker)
	return bakersOfLevel


#this function creates an array of the best bakers for each level
def bestBaker(bakers):
	bestBaker = bakers[0]
	for baker in bakers:
		if baker.score > bestBaker.score:
			bestBaker = baker
	return bestBaker


def displayBaker(bakers):
	primaryBakers = getBakersOfLevel(baking, "Primary")
	secondaryBakers = getBakersOfLevel(baking, "Secondary")

	#Using the array created in getBakersoflevel (now called
	#bestSecondary)- find the Secondary school with the highest score
	#the details associated with the highest score will be displayed
	bestSecondary = bestBaker(secondaryBakers)
	print("The highest score in secondary is", bestSecondary.score,
	      bestSecondary.name, "from", bestSecondary.school)

	#Using the array created in getBakersoflevel (now called bestprimary)-
	#find the Primary school with the highest score
	#the details associated with the highest score will be displayed
	bestprimary = bestBaker(primaryBakers)
	print("The highest score in primary is", bestprimary.score,
	      bestprimary.name, "from", bestprimary.school)


#Creating a function to allocate each pupil to a school,
#we can then use the score for each pupil associated with
#that school to generate an average score for said school.
def averageScore(bakers, school):
	schoolBakers = []
	counter = 0
	SchoolScore = 0
	average = 0
	for counter in range(len(bakers)):
		for baker in bakers:
			if baker.school == school:
				schoolBakers.append(baker)
			counter += 1
	for baker in schoolBakers:
		SchoolScore = SchoolScore + baker.score
		average = SchoolScore / len(schoolBakers)
	return average


#using the previous function to create an array of averages for each school
def schoolAverage(bakers):
	averageA = averageScore(bakers, "Aberdeen Academy")
	averageS = averageScore(bakers, "St Saviours")
	averageI = averageScore(bakers, "Inverlamond Academy")
	averageL = averageScore(bakers, "Linlathen")
	averageAB = averageScore(bakers, "AiryBrae")

	averages = []
	averages.append(averageA)
	averages.append(averageS)
	averages.append(averageI)
	averages.append(averageL)
	averages.append(averageAB)
	print(averages)
	return averages


#creating a procedure to find out the highest average school stored in the array
def highestAverageScore(averages):
	highestAverage = averages[0]

	for average in averages:
		if average > highestAverage:
			highestAverage = average

	if highestAverage == averages[0]:
		print("Aberdeen has the highest average score of: ", highestAverage)
	elif highestAverage == averages[1]:
		print("St Saviours has the highest average score of: ", highestAverage)
	elif highestAverage == averages[2]:
		print("Inverlamond Academy has the highest average score of: ",
		      highestAverage)
	elif highestAverage == averages[3]:
		print("Linlathen has the highest average score of: ", highestAverage)
	elif highestAverage == averages[4]:
		print("AiryBrae has the highest average score of: ", highestAverage)


#calling the subprograms in order to execute the program
baking = readfile()
primary, secondary = countBakers(baking)
displayBaker(baking)
averages = schoolAverage(baking)
highestAverageScore(averages)
