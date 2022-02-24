Report 2 - Prototypes & Testing 

Zachary Cushon

Current stage:

Logic:
	
	The program currently makes evaluations on if a student is a match for a given TA position, this is done for all students in order to construct a list of eligible students.
	
	This list is then sorted by graduation year and split into and array of 392 applicants and and array of 492 applicants
	
	Once this is done the program will assign student IDs into the 392/492 dictionary listing for the corresponding class.
	
	Theses student ID's will be added to a list of Studend IDs that have been assigned TA positions and will then be removed from the overall pool on the next loop iteration.
		
Bugs so Far:
	
	Currently the only known bug is the re-use of student ID's I have not been able to track down the reason for this yet.
		
	Some thing I have tried to help with troubleshooting include:
		
	1. Print Statements in loops to understand what is running when  
			
	2. Manually making assignments to verify the program is behaving as intended.
		
	3. Print the length of the TA array to find when students are not being removed.
		

Prototype Stages:
	
	The initial prototype can be seen in the documentation folder, the code initially printed out a list of eligible students for each class section given the time,topic, and location of the class section.
	
	
Plan moving Forward:
	
	The priority is to find the reason for duplicate assignments, after fixing this the code will be mostly functional aside from edge cases and some minor optimizations that can be made as far as prioritization goes.
	After fixing the bugs that currently exist in the code the user interface will then begin being developed.	
	Aditionally I would like to add the ability for the assignments to be written to a file or 'pickled'.
