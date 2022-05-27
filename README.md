# Problem?

This was an algorithm developed for Computer Science 480 at Central Washington University.

The assignment was to create an alogrithm to assign students to Computer Science TA positions based off the given CSV files. How the data would be sorted/prioritized was for the students to decide. (See instructions in class documents)

When considering this problem I had to consider a multitude of different factors, some of which include: 

* Student graduation date/seniority
* Prior Experience
* Time availability
* Location

# Solution!

## Finding Eligible Candidates!

After considering all of the above variables I decided the best way to proceed with assignment would be to create boolean methods to evaluate each variable.

To accomplish this I developed an object called TA to store all CSV data in, the student object consists of fields:

* Student_info (Array of strings containing general info about the student)
* time (2-Dimensional Array used to index different time slots for each day of the week)
* experience (an Array of 1/0 to denote passes or fails in classes.)

I then created the following methods to perform checks on TA objects:

* inBurg (Checks student location in student_info)
* qualified (Ensures that the student has passed the class they are being assign to TA for)
* TimeCheck (evalute the date and time and locate 2D time array)

Student who pass all three tests will be added to a list of potential candidates called Elig.

## Prioritize Eligible Candidates

Since completeing CS392/492 is a graduation requirment at Central Washington University I decided to make the inital sort based on graduation date.

Since many students share graduation dates this is still insufficient and will leave some students unhappy. Since CWU student ID numbers increment as students enroll, this means students with lower student IDs should be prioritized next since they would have seniority.

After sorting by both graduation date and student ID number I then split the array based on if student were applying for the 392 or 492 position(See instructions.) 

Finally students are assigned to TA positions from index 0 to n.






