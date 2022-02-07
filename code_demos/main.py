import TA, section, csv


def inBurg(app):			# Checks if the TA object passed to it is in Ellensburg and able to TA
	if app.student_info[7] == "No" :
		return False
	else :
		
		return True
		
def all_subj(SectionArray):			#A method to pull all unique subjects that are being offered, no duplicates
	offered = set([])
	for numb in SectionArray.classes:
		offered.add(numb.unorg[1])
	return offered
	pass

def ClassPos(cat_numb):		#Finds the position of the class in the array so that it can be compared to the experience array in the TA object.
	i = 0
	for classes in offered:
		if classes != cat_numb:
			i += 1
		elif  classes == cat_numb:
			return i
		else:
			return None

def qualified(TA_obj,cat_numb):		#Checks if the TA is qualified for the specified class number
	loc = ClassPos(cat_numb)
	if TA_obj.exp[loc] != 'X':
		return False
	else :
		return True
	
def timeCheck(TA_obj,dayMap,hour):		#the individual section will contain the days that the section meets along with the hours.
		for day in dayMap:
			print(hour)
			if TA_obj.time[day][hour] == 1:
				return True
			else:
				return False
			pass
			#print(TA_obj.time[day][hour])
	
	
	
	
#BASICALLY THIS METHOD AND THE METHOD PRECEDING IT ARE GOING TO BE USED TO LOCATED THE CORRECT [DAY] AND [HOUR] ON THE TAs TIME SCHEDULE.
						#	TA.time[Day][Hour]
						#creates a stack of integers that will represent different days of the week 	
						#[M,T,W,TH]
						#[0,1,2,3]
						#for example, a class that meets "M T TH" would return [0,1,3]
						
	
def dayMap(days):
	rep = set([])
	i = 0
	for letter in days:
		if i > 3 :
			i-=1
		if i > 4 :
			return rep
		else:
			if (letter != " "):
				rep.add(i)
				i+=1
				
			else:
				
				i+=1
	return rep
			
def AM_PM(time_string):
	numb = ['0','0']
	index = 0
	numb[0] = time_string[0]
	numb[1] = time_string[1]
	if numb[1] != ':':
		index = int(numb[0]) * 10
		index += int(numb[1])
	else:
		index = int(numb[0])
	
	if time_string[len(time_string)-4] == '5':
		index += 1
	if time_string[len(time_string)-2] == 'A' or index > 11:
		return index-8
	else:
		return index+4
		


TAs = TA.TaArr("studs.csv")

C = section.SectionArr("schedule.csv",45)
offered = sorted(all_subj(C))



for class_sections in C.classes : #Class section 
	poss = []
	CID = class_sections.info['Cat']
	daySet = dayMap(class_sections.info['Days'])
	time_stringS = class_sections.info['Start']
	print(time_stringS)
	if time_stringS != ':AM':
		if int(time_stringS[0]) > 3:
			print("Outside of TA-able hours")
			pass
		else:
			time_stringS = AM_PM(class_sections.info['Start'])
			time_stringE = AM_PM(class_sections.info['End'])
			for student in TAs.applicants:							#Students
				if inBurg(student):
					if qualified(student,CID):
						if timeCheck(student,daySet,time_stringS):
							print("Pass")
	else:
		pass

	




	
	
	
	

