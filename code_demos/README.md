# How to setup/Run

When you run the assignTA.py file the file shows a list of all the classes that need a TA and it first gives off a list of all the classes that need a student. 
The information that is given is the Subject of the class, then the proffesor for that class, the start time, and finally it give the option for a 392 class or a 492 class.
The code prints all of these and it look like this:


Subject: CS392
Professor: Palmquist,Bruce C
Start Time: :AM
392 Assignment: None
492 Assignment: None


Some of those classes have the 392/492 Assignment filled with the class number that the students will be assigned to. 

This is all done automatically by priority and the left over students that either one didn't qualify, or two didnt have the time slot open will be put on the list at the end.

Are program is ran in python and you will need to use python 3. The program is ran by using 3 files :

# assignTA.py:

  This is the driver code that will sort out the students to see what classes they can go into.

# TA.py:

  This file builds a TA object the organizes the TA information inside the object.

# section.py

  This file makes a directiry of all the classes to put the students in.
  
You must bave both csv files in your code (provided by the teacher) and they must be named students.csv and schedule.csv. 
another thing is that they must be in the same directory as the code.
