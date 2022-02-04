import TA, section, csv
#

def inBurg(app):			# Checks if the TA object passed to it is in Ellensburg and able to TA
	
	if app.student_info[7] == 'No' :
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
		if cat_numb != classes:
			i += 1
		elif cat_numb == classes:
			return i
		else:
			return None

def qualified(TA_obj,cat_numb):		#Checks if the TA is qualified for the specified class number
	loc = ClassPos(cat_numb)
	return TA_obj.exp[loc+2]
	
def timeCheck(TA_obj,dayMap,hour):		#the individual section will contain the days that the section meets along with the hours.
		for day in dayMap:
			print(TA_obj.time[day][hour])
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
				print(letter)
				rep.add(i)
				i+=1
				
			else:
				
				i+=1
	return rep
			
				

TAs = TA.TaArr("studs.csv")

C = section.SectionArr("schedule.csv",45)
offered = sorted(all_subj(C))
print(offered)
print(len(C.classes[2].info['Days']))
print(C.classes[2].info['Days'])
dm = dayMap(C.classes[2].info['Days'])
print(dm)
timeCheck(TAs.applicants[0],dm,0)
print(TAs.applicants[1].time)




	
	
	
	

