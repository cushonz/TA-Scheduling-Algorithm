import csv

class SectionArr:
	def __init__(self,filename,numbClasses):
		self.classes = [0] * numbClasses #for array size, wanted to use numpy but was unsure if it is on lab computers.
		
		with open(filename,'r') as csv_file:
			data = csv.reader(csv_file)
			(next(data)) # Skip header
			i = 0
			for line in data:
				self.classes[i] = Section(line) # Parse each line of the CSV and extract values for section object
				i += 1
			pass


class Section:

#This class provides an object that will then be stored in the sectionArr class


	def __init__(self,line):
	
		self.info = {
		'Subj' : None,
		'Cat': None,
		'Sec': None,
		'Title': None,
		'Name': None,
		'Days': None,
		'Start': None,
		'End': None,
		'Facil': None,
		'Campus': None,
		'TA392_ID': None,
		'TA492_ID': None,
		}
		
		
		self.unorg = line
				
		self.info['Subj'] = self.unorg[0]
		self.info['Cat'] = self.unorg[1]
		self.info['Sec'] = self.unorg[2]
		self.info['Title'] = self.unorg[3]
		self.info['Name'] = self.unorg[4]
		self.info['Days'] = self.unorg[5]
		self.info['Start'] = self.unorg[6]
		self.info['End'] = self.unorg[7]
		self.info['Facil'] = self.unorg[8]
		self.info['Campus'] = self.unorg[9]
		
		
		


		

