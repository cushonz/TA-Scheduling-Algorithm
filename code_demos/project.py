class TA :
	def __init__(self,name,SID,avail,standing,qual):
		self.name = name
		self.stud_ID = SID  				#Student ID number
		self.avail = avail        			#Student availability as a list of ints, this list will be 
		               				#checked against the list of all possible sections for the TA to be assigned to
                               				#could quick sort the list for efficiency but it will likely be a list of 5-10 ints max


		self.senior = standing    #bool to denote 392/492
		self.qualified = qual    #Array of CS classes that the TA has passed
		
pass

class Section:

	assist492 = None
	assist392 = None

	def __init__(self,start,prof,size,subj,cid,blk = None,req = None):
	
		self.class_id = cid
		self.professor = prof
		self.course    = subj
		self.start_time = start 	#assumed 50 minute periods, it is assumed that if an hour is listed in TA availability the TA is available for the entire hour
		self.blk_lst = blk
		self.req = req

	def assign(self,TA):									#Loop through all subject the TA has passed and compare it to the coure name to ensure no
		for subj in TA.qualified:							#TA's will be assigned to classes that they are unable to help students with.
			if subj == self.course:
				return self.checkblk(TA)
		print("This student is not qualified to TA for the chosen course.")
		return False
		
	def checkblk(self, TA):
		if self.blk_lst != None:
			for student_id in self.blk_lst:
				if TA.stud_ID == student_id :
					return False 						#This student and professor dont get along, lets not do this matching
		else :
			return self.checkHour(TA) 						#pass TA to the next check because they were not present on the black list


	def checkReq(self,TA):
		if self.req != None :
			for student_id in self.req:
				if TA.stud_id == req :
					return finalize(TA)
		


	def checkHour(self,TA):
		for hour in TA.avail:
			if hour == self.start_time :
				return self.finalize(TA)
		print("This student is not free during the hour the class is taught.")	#This may not be a problem because some TA positions are strictly grading
		return False									#will play by ear
	
	def finalize(self,TA):                   						#Determines if the TA will have the 392 or 492 position
		if TA.senior :
			if self.assist492 == None:     					#checks to make sure this position is not already assigned,  
				self.assist492 = TA           				 #it would be awkward to explain an error on this portion to a student.
				return True
		else:
			if self.assist392 == None:  
				self.assist392 = TA
				return True
	
	
			 


available_hours = {1,2,3,4,5,6,7,8}
classes_taken = {110,310}
zach = TA("Zach",40979699,available_hours,True,classes_taken)

cs310 = Section(2,"Professor Lietart",30,310,0,blk = {40979699})	#In this case I have blacklisted myself and requested no one. Class starts at 2. Other than the black list I would be eligble
print(cs310.assign(zach))


#From here we essentially need to try to see if there is some way that we can get bulk data in
#I think we have a good foundation here to be one of the best in the class if we can get some of these things working :)
#Lets work hard and get our 'A'
