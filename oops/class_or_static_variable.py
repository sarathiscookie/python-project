# Python doesn’t have the static keyword. All variables that are assigned a value in the class declaration are class variables.

class Student:

    stream = "CSE"

    def __init__(self, name):
        self.name = name

    def get_student_name(self):
        print(self.name)

student_one = Student("Peter")
student_two = Student("Smith")

student_one.get_student_name() # Peter
student_two.get_student_name() # Smith

print(student_one.stream) # CSE
print(student_two.stream) # CSE

student_one.stream = "ECE"
print(student_one.stream) # ECE

print(Student.stream) # CSE

Student.stream = "MEC"
print(student_one.stream) # ECE
print(student_two.stream) # MEC




