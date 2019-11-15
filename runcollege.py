from com.abc.college.student import Student
from com.abc.college.professor import Professor

s = Student(name='mehul', gender='m', roll=10, marks=90)
# 4003
# Student.__init__(4003, name='mehul', gender='m', roll=10, marks=90)

p = Professor(name='jane', gender='f', subjects=['Physics', 'Chemistry'])

i = 10

print(i)
# Internally
# print(i.__str__())
# print(int.__str__(i))

print(s)
# print(s.__str__())
# print(Student.__str__(s))

print(p)
# print(p.__str__())
# print(Professor.__str__(s))

''' print(s.name)
print(s.gender)
print(p.name)
print(p.gender) '''

print(s.getdetails())
# Student.getdetails(s)

print(p.getdetails())
# Professor.getdetails(p)