students = [['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90]]

def second_highest(students):
	grades = [s[1] for s in students] # only take the result out
	grades = sorted(grades, reverse=True)
	second = grades[1] # grades[0] is the highest, so grades[1] is the second hightest.

	# next, let's find out who has this result
	# in students list, s[0] is name and s[1] is the result
	second_highest_student = [s[0] for s in students if s[1] == second]
	for student in second_highest_student:
		print(student)

second_highest(students)