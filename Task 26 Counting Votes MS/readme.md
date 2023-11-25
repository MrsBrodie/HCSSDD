# Task 26: Vote Counter

A local council is trialling an electronic voting system. 

There are 4 parties in the election with the following candidates:
❏	Abolish exams! - Candidate J Smith
❏	Apple Party - Candidate G Bloggs
❏	Party against Homework - Candidate A N Other
❏	Rampant Vikings - Candidate T Thunderson

Each voting console will save a file in the following format:
Voter ID, Party Name, Candidate Name and whether the vote was VALID or SPOILED.

An example from the file is shown below:
1,Apple Party,G Bloggs,VALID
2,Abolish Exams,J Smith,SPOILED
3,Abolish Exams,J Smith,VALID

For the trial there are 5 files produced from the 5 electronic voting machines, each file will contain 100 records. The results are stored in the files voting1.csv, voting2.csv, voting3.csv, voting4.csv and voting5.csv

Your task is to create a program that will process the 5 files created by the machines and display the total for each candidate and the winning candidate and number of votes. Any votes marked as SPOILED should not count towards a party. 
The output should be similar to below:

Machine files read ok…

Apple Party 66 votes
Rampant Vikings 61  votes
Party against Homework 67 votes
Abolish Exams! 63 votes

The winner is A N Other from the Party against Homework party with 67 votes.

