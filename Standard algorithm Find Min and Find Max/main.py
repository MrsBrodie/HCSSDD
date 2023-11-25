#create a subprogram that will read in a text file called ComputingMarks.csv
def readfile():

	#create 4 arrays that will allow 100 instances of each item to be stored
	#and create a counter so it can be used to keep a count of the number of
	#records that have been created.
	names = [None] * 100
	forms = [None] * 100
	scores = [None] * 100
	courseworks = [None] * 100
	counter = 0

	#this will open the file and seperate it into 4 seperate fields with a
	#new line being created after 4 items have been read in.
	with open("ComputingMarks.csv") as readfile:
		line = readfile.readline().rstrip('\n')
		while line:
			items = line.split(",")
			names[counter] = items[0]
			forms[counter] = items[1]
			scores[counter] = items[2]
			courseworks[counter] = items[3]
			counter += 1
			line = readfile.readline().rstrip('\n')
		input("File read complete, please press enter" "\n")

	#the data being returned (Data out) is listed below
	return names, forms, scores, courseworks


#A subprogram that will find and store the smallest exam score in the array.
#(Data in) is listed in the brackets after minScore (scores)
def minScore(scores):
	#create a variable to initially be set to 0
	minposition = 0

	#create a loop that will run for the number of instances of scores (100)
	for counter in range(0, len(scores)):

		#The scores value of the first element is compared to the value stored in
		#minposition[0] which will be the first score in the scores array and if
		#it is smaller that minposition it will become the new value stored in minposition
		if int(scores[counter]) < int(scores[minposition]):
			minposition = counter

	#the data being returned is minposition (Data Out)
	return minposition


#A subprogram that will find and store the largest course work score in the array.
#(Data in) is listed in the brackets after minScore (courseworks)
def maxCourse(courseworks):
	maxposition = 0

	#create a loop that will run for the number of instances of scores (100)
	for counter in range(0, len(courseworks)):

		#The scores value of the first element is compared to the value stored
		#in maxposition[0] which will be the first score in the scores array
		#and if it is smaller that minposition it will become the new
		#value stored in maxposition
		if int(courseworks[counter]) > int(courseworks[maxposition]):
			maxposition = counter

	#the data being returned is maxposition (Data Out)
	return maxposition


#create a subprogram that will find the highest combined scores
def maxCombined(courseworks, scores):
	combined = 0
	counter = 0
	#create a loop that will read compare the combined scores of all students
	#and store the highest score in the combined variable.
	for counter in range(0, len(courseworks)):
		if int(courseworks[counter]) + int(scores[counter]) > int(
		    courseworks[combined]) + int(scores[combined]):
			combined = counter
	return combined


names, forms, scores, courseworks = readfile()
minposition = minScore(scores)

print("the lowest exam score was", scores[minposition], "from",
      names[minposition], "\n")

maxposition = maxCourse(courseworks)
print("the highest coursework was ", int(courseworks[maxposition]), "from",
      names[maxposition], "\n")

combined = maxCombined(courseworks, scores)
print("the highest combined was",
      int(courseworks[combined]) + int(scores[combined]), "from",
      names[combined], "\n")
