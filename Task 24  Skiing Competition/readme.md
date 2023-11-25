# Task 24: Skiing Competition

In a local downhill skiing competition the competitors have to pass through a maximum of 9 gates. There are 4 teams  

Aberdeen Juniors, Slalom Fun, Dundee Dry and Glasgow Juniors 
 
There are 5 competitors from each team 
 
For every gate missed or hit there is a 0.5 second penalty. The last piece of information in the file e.g. 1269 is a list of the gate numbers they faulted at. So for example 1269  would mean that there were 4 gates missed or hit so there is a 2.0 second penalty to be added. 
 
The competitors name, race number, team, race time along with the penalties are stored in the file skiing.csv 
 
A sample of data is shown below: 

 

Joe Bloggs,2,Aberdeen Juniors,48.2,1269 

**Create a program that will **

*Read and process the file to calculate the total time for each competitor ( incorporating any penalties) 

*Store the data in an appropriate record structure 

*List the final times per team 

*Display the individual winner (individual best time inclusive of penalties) 
 
Your output should be similar to below: 

 

Final Total Times 

Aberdeen Juniors: 392.9 seconds 

Dundee Dry: 409.1 seconds 

Glasgow Juniors: 360.6 seconds 

Slalom Fun: 360.6 seconds 

Individual Winner: Brendis Woodland of Glasgow Juniors 

**Extension **

Display the winning team ( best total time) and  in the event of a tie the team with the lowest amount of penalties will win. 
 
For example: 
  
 

The winner was: Glasgow Junior with a total time of 360.6 seconds 

 