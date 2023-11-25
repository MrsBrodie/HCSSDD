# Task 11: Reading from a CSV File

Your task is to read the contents of a file which contains details of 20 pupil names and their guidance house. 
The structure of the file is as follows: 

 

Nichola,Blackfriars 
James,Collyhill 
Nichola,Blackfriars 
James,Collyhill 

 

You will read the file and import the contents of the existing file (PupilDetails.csv) into two parallel arrays, one storing the pupil names and one for guidance houses.  

The file has already been made for you. You will then output the file in the format below: 

 

Pupil Name:                     Guidance House 
Nichola                               Blackfriars 

James                                 Collyhill 

**Refinements** 

1.1 OPEN FILE PupilDetails.csv for READ ACCESS 

1.2 WHILE file.txt IS NOT BLANK 

1.3 READ next line of file 
1.4 SET newarray = split line on “,” 

1.5 SET names(counter) = newarray(0) 

1.6 SET houses(counter) = newarray(1) 

1.7  READ next line of file 

1.8 END WHILE 

1.9 CLOSE FILE 