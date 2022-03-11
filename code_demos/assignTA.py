import TA
import section
import csv


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
	#print("location: " + str(loc))
	if TA_obj.exp[loc+2] != 'X':
		return False
	else :
		return True
	
def timeCheck(TA_obj,dayMap,hour):		#the individual section will contain the days that the section meets along with the hours.
		for day in dayMap:
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
						
						#stopped writing comments because no one else works on this lol
	
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
		
		


def Qmap(Q):
	if Q == "Winter":
			return 1
	elif Q == "Spring":
			return 2
	elif Q == "Summer":
			return 3
	else :
			return 4

def prioritizeQ(elig):

	wint = []
	spring = []
	summer = []
	fall = []
	
	ta_sorted = []
	
	for ta in elig:
		ta.mult = Qmap(ta.student_info[4])
		if Qmap(ta.student_info[4]) == 1:
			wint.append(ta)
		if Qmap(ta.student_info[4]) == 2:
			spring.append(ta)
		if Qmap(ta.student_info[4]) == 3:
			summer.append(ta)
		if Qmap(ta.student_info[4]) == 4:
			fall.append(ta)
			
	for ta in wint:
		ta_sorted.append(ta)
		
	for ta in spring:
		ta_sorted.append(ta)
		
	for ta in summer:
		ta_sorted.append(ta)
		
	for ta in fall:
		ta_sorted.append(ta)
	
	return ta_sorted
		

def prioritizeY(by_quarter):
	now = []
	next = []
	fut = []
	sorted_tas = []
	
	for ta in by_quarter:
		if (ta.student_info[5] == '2022'):
			now.append(ta)
		elif (ta.student_info[5] == '2023'):
			next.append(ta)
		elif (ta.student_info[5] == '2024'):
			fut.append(ta)
	for ta in now:
		sorted_tas.append(ta)
	for ta in next:
		sorted_tas.append(ta)
	for ta in fut:
		sorted_tas.append(ta)
	
	return sorted_tas
	
def posSplit(elig):
	TA1 = []
	TA2 = []
	for ta in elig:
		if ta.student_info[6] == '392':
			TA1.append(ta)
		elif ta.student_info[6] == '492':
			TA2.append(ta)
	return TA1,TA2
		


TAs = TA.TaArr("students.csv")

C = section.SectionArr("schedule.csv",45)
offered = sorted(all_subj(C))

elig = []
assigned = []

C.classes.reverse()

for class_sections in C.classes : #Class section 
	CID = class_sections.info['Cat']
	daySet = dayMap(class_sections.info['Days'])
	time_stringS = class_sections.info['Start']
	
	if time_stringS != ':AM':
		if int(time_stringS[0]) > 3:
			
			pass
		else:
			time_stringS = AM_PM(class_sections.info['Start'])
			time_stringE = AM_PM(class_sections.info['End'])
			for student in TAs.applicants:#Students

				if inBurg(student) and qualified(student,CID) and timeCheck(student,daySet,time_stringS):
					elig.append(student)
			
		gq = prioritizeY(elig)
			
		all_ = posSplit(gq)
			
		TA492 = all_[1]
		TA392 = all_[0]
		assigned = set(assigned)

		if (class_sections.info['TA392_ID'] == None):
			i = 0
			j = 0
			if TA392:
				while (TA392[i].student_info[2] in assigned and i < len(TA392)-1):
					i+=1
				if (i < len(TA392)-1):
					class_sections.info['TA392_ID'] = TA392[i].student_info[2]
				else:
					class_sections.info['TA392_ID'] = None
				
				
		if (class_sections.info['TA492_ID'] == None):
			if TA492 :	
				while (TA492[j].student_info[2] in assigned and j < len(TA492)-1):
					j+=1
				if (j < len(TA492)-1):
					class_sections.info['TA492_ID'] = TA492[j].student_info[2]
				else:
					class_sections.info['TA492_ID'] = None
			else:
				print("No eligible TA's in 492 array, using next 392 student.")
				if TA392:
					while (TA392[i].student_info[2] in assigned and i < len(TA392)-1):
						i+=1
					if (i < len(TA392)):
						class_sections.info['TA492_ID'] = TA392[i].student_info[2]
					else:
						class_sections.info['TA492_ID'] = None	
						print("No TA available")	
								
		
		assigned.add(class_sections.info['TA392_ID'])
		assigned.add(class_sections.info['TA492_ID'])		
			
	else:
		pass
print("Resulting Assignments")
for x in C.classes :
	print("--------------------------------------\nSubject: CS"+x.info['Cat'])
	print("Professor: "+x.info['Name'])
	print("Start Time: "+x.info['Start'])
	print("392 Assignment: "+str(x.info['TA392_ID']))
	print("492 Assignment: "+ str(x.info['TA492_ID']))
ca = []
print("\nThe following students have not been assigned TA positions\n-----------------------------------------------------------")
for student in TAs.applicants:
	if student.student_info[2] not in assigned:
		print(student.student_info[1]+", "+student.student_info[0])
		ca.append(student.student_info[1]+", "+student.student_info[0])




	
	
	
	

