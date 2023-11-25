# Task 17: Find Max

**Standard Algorithm**

Write a program which displays an existing list of scores in the file called scores.csv which are read from a file The program should then display a message showing the highest score in the list. 
The scores are  integers between 0 and 9999.

Jessalyn Keeri,3186

**Top Level Design and Data Flow**
Main Steps	In	Out
1	ReadFile		names(),scores()
2	FindMax	names(),scores()	

**Refinements  (partial)**
2.1 SET max = scores[0]
2.2 FOR EACH score in scores()
2.3 IF score(counter) > max THEN
2.4 SET max = scores(counter)
2.5 END IF
2.6 NEXT item 

