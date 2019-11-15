from com.abc.college.student import Student

print(Student.count) # 0
# s1 = Student() # 4003 - Student object
# Internally
# 1. 4003 - Student object
# 2. Student.__init__(4003)

s1 = Student('mehul', 'm', 10, 90)
# Internally
# 1. 4003 - Student object
# 2. Student.__init__(4003, 'mehul', 'm', 10, 90)


# create an attribute in an object
''' s1.name = 'mehul'
s1.gender = 'm'
s1.roll = 10
s1.marks = 90 '''


''' s2 = Student() # 4006 - Student object
s2.name = 'jane'
s2.gender = 'f'
s2.roll = 11
s2.marks = 64 '''

s2 = Student(gender='f', roll=11, marks=64, name='jane')

# access the attribute from an object
''' print(s1.name)
print(s1.roll)
print(s2.name)
print(s2.roll) '''

print(s1.getdetails())
# Internally
# print(Student.getdetails(s1))

print(s1.getgrade())
# Student.getgrade(s1)

tu = s1.get_name_roll()
''' name = tu[0]
roll = tu[1] '''
name, roll = tu # tuple unpacking
# Student.get_name_roll(s1)

print(Student.count) # 2


print(s2.getdetails())
# Internally
# print(Student.getdetails(s2))

print(s2.getgrade())

s3 = Student(name='jill', roll=15, marks=69, gender='f') # 4006 - Student object
''' s3.student_name = 'jil'
s3.gen = 'f'
s3.r = 15
s3.marks = 69 '''

print(s3.getdetails())

print(Student.count) # 3

# accessing class functions
print(Student.getminattendance())
# Internally
# print(Student.getminattendance())


