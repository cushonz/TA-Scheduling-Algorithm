# How to setup/Run

Since the project is written in python it is fairly simple to get setup.

Simply clone the repository and run the following :

![alt_text](/documentation/to_start.png)

After running this the program will run and give the follwing output :

![alt_text](/documentation/finalized_output.png)

The output includes detailed information about all classes and what students were assigned to what TA positions.


This is all done automatically by priority and the left over students that either didn't qualify, or didnt have the time slot open will be put into a list of leftover students at the end of execution.

# assignTA.py:

'AssignTA.py' is the driver code, it utilizes both the TA.py and section.py classes, it is important that all three of these files are kept in the same directory along with the student.csv and schedule.csv files to be used as input.
 
