# TA class

The TA class contains several lists that represent different 'chunks' of related data about any particular TA applicant.

These lists are:

	General info
	
	Availability
	
	Experience
	
This makes accessing data easy so that checks can be performed easily, this class is purely for building the data structure and contains no methods that are intended to be used outside of its constructor.

# Section Class

The section class much like that TA class is purely for storing data.

The section class is simply a dictionary that contains the general information about the class
including the TAs that are assigned to the class section.

# Driver Code

The intake of information is managed by the TA, and Section classes. These classes parse information from the provided CSV file and break them into more manageable pieces. 

assignTA.py is responsible for assigning TA applicants to an appropriate position based on the following data points
	
	Class time vs TA availability
	
	Class location vs TA Location
	
	Class subject vs TA experience
	
after each of these is checked a student will be considered "eligible", if a student is eligible for the TA position they will be added to a list of eligible TAs

This list is then sorted by graduation year, in an effort to prioritize students that are trying to wrap up their time at CWU.

Lastly this array is then split into an array of 392 applicant and an array of 492 applicants.

Assignments are then made from the top down, if a student ID is present in the the list called "assigned" the next student will be selected.

Following assignment a student should be removed from the overall list at which point the for loop will repeat this process again for the next class section.
