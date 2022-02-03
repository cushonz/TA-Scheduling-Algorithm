import csv




class TaArr:
	
	def countIn(self,filename):	# A simple method to count the number of lines in our CSV file.
	
		with open(filename,'r') as csv_file:
			data = csv.reader(csv_file)
			(next(data)) # Skip
			(next(data)) # header
			i = 0
			for line in data:
				i+=1
		return i

	def __init__(self,filename):
		
		size = self.countIn(filename)
	
		self.applicants = [None] * size
		
		with open(filename,'r') as csv_file:
			data = csv.reader(csv_file)
			(next(data)) # Skip
			(next(data)) # Skip
			i = 0
			for line in data:
				self.applicants[i] = TA(line)
				i+=1
				#print(line)
				# Parse each line of the CSV and extract each applicant who will be assigned to position i
				
			pass
	
	

	

#-------------------------------------------------------------------------------------------------

 
class TA :

	def __init__(self, line):	
		
		
		self.numbCol = 60
		
		self.parentArr = [0] * self.numbCol
		
		
		self.student_info = [0] * 8
		
		self.time = [
		
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0]
		
		]
		
		self.exp = ['X'] * 20
		
		#self.CSVin("studs.csv", self.parentArr)	
		self.splitArr(line)
		

	def countIn(self,filename):	
	
		with open(filename,'r') as csv_file:
			data = csv.reader(csv_file)
			(next(data)) # Skip
			(next(data)) # header
			i = 0
			for line in data:
				i+=1
		return i
			
	def CSVin(self,filename,target_Arr):
		with open(filename,'r') as csv_file: 
			data = csv.reader(csv_file)
			next(data) #Skip
			next(data) #Header
			i = 0
			for line in data:
				target_Arr[i] = line
				i+=1
		pass
	
	def splitArr(self,parentArr):
		for i in range(0,4):
			for j in range(0,8):
				if parentArr[j+7] == 'No':
					self.time[i][j] = 0
				elif parentArr[j+7] == 'Open':
					self.time[i][j] = 1
				else :
					self.time[i][j] = 3
		
		# ("Time table populated.")
		
		for info in range(0,8):
			self.student_info[info] = parentArr[info]
		#print ("Student infromation updated.")
		
		for info in range(40,42):
			if (parentArr[info] == 'No'):
				self.exp[info-40] = False
			elif (parentArr[info] == 'Yes'):
				self.exp[info-40] = True
				
		for info in range(43,63):
			if (parentArr[info] == 'X'):
				self.exp[info-43] = True
			else :
				self.exp[info-43] = False
				
		
				


			
pass


