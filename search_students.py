from com.abc.college.student import Student

''' slist = [
    Student(name='mehul', gender='m', roll=10, marks=90),
    Student(name='jane', gender='f', roll=5, marks=86),
    Student(name='jill', gender='f', roll=23, marks=67)
] '''

smap = {
    10: Student(name='mehul', gender='m', roll=10, marks=90),
    5: Student(name='jane', gender='f', roll=5, marks=86),
    23: Student(name='jill', gender='f', roll=23, marks=67)
}

roll = int(input('Enter roll to search: '))

''' for student in slist:
    if student.roll == roll:
        print(student.getdetails())
        break
else:
    # will execute when the corresponding for block is exhausted (there is no break encountered)
    print('Student not found') '''

if roll in smap:
    student = smap[roll]
    print(student.getdetails())
else:
    print('student not found')