# CS480-Project
Git Repository for CS480 project

The project so far :
  Loops through all classes
    Extracts important infromation about the class
    Loop through all students
      check student info against class info and discard non matches.
      print list.
      
      
This approach was simple yet effective. Infromation is neatly indexed and easily accesible.

Moving forward we will need to implements a few more specific checks as well as making assignments in different order to optimize the end result of all assignments.

---------------------------------------------------------------------------------------------------
# Update 2/23/22

The code currently is capable of organizing and assiging students to the 392 and 492 positions

I have added the ability for 392 students to fill a 492 position when the 492 students have been depleted, that way no TA positions are going unfilled.

Thus far the code performs the following checks:
	
	* Time conflicts
	* Location Conflicts
	* Student Experience
	
After passing all of these tests a student will be added to a list of eligible students.

Assignments will then be made from this list.
