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
	
		self.sect_dict = {
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
		
		
		self.info = line
				
		self.sect_dict['Subj'] = self.info[0]
		self.sect_dict['Cat'] = self.info[1]
		self.sect_dict['Sec'] = self.info[2]
		self.sect_dict['Title'] = self.info[3]
		self.sect_dict['Name'] = self.info[4]
		self.sect_dict['Days'] = self.info[5]
		self.sect_dict['Start'] = self.info[6]
		self.sect_dict['End'] = self.info[7]
		self.sect_dict['Facil'] = self.info[8]
		self.sect_dict['Campus'] = self.info[9]
		
		
		


		

