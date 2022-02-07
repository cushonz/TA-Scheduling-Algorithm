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
		
		self.parentArr = line
		
		
		self.student_info = [0] * 8
		
		self.time = [
		
		[0,0,0,0,0,0,0,0], #Monday
		[0,0,0,0,0,0,0,0], #Tuesday
		[0,0,0,0,0,0,0,0], #Wednesday
		[0,0,0,0,0,0,0,0]  #Thursday
		
		]
		
		self.exp = ['X'] * 27
		
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
				if parentArr[(i*8)+j+8] == 'Conflict' or parentArr[j+8] == 'conflict':
					self.time[i][j] = 0
				elif parentArr[(i*8)+j+8] == 'Open' or parentArr[j+8] == 'open' :
					self.time[i][j] = 1
				else :
					self.time[i][j] = 3
		
		# ("Time table populated.")
		
		for info in range(0,8):
			self.student_info[info] = parentArr[info]
		#print ("Student infromation updated.")
		
		
		
		for info in range(40,62):
			self.exp[info-40] = parentArr[info]
				
		
				


			
pass


