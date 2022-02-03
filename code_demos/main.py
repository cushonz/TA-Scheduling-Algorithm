import TA, section

TAs = TA.TaArr("studs.csv")

classes = section.SectionArr("schedule.csv",45)

for stud in range(0,50):
	print(TAs.applicants[stud].student_info[0])
