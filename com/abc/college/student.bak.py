'''
For every class in python, a memory (object) is allocated for it.
1 object per class.
'''

class Student:

    count = 0 # class attribute
    # access - Classname.classattribute

    def __init__(self, name=None, gender=None, roll=None, marks=None):
        # creating attributes in an object
        # constructors

        # object attributes
        self.name = name
        self.gender = gender
        self.roll = roll
        self.marks = marks

        Student.count += 1

         # implicit return will be the object (self)

    def getdetails(self):
        # self - current object s1, s2
        ''' return 'Name: ' + self.name + '\nGender: ' + self.gender + '\nRoll: ' + \
            str(self.roll) + '\nMarks: ' + str(self.marks) '''
        ''' return 'Name: {0}\nGender: {1}\nRoll: {2}\nMarks: {3}'.format(\
            self.name, self.gender, self.roll, self.marks) '''
        return 'Name: {name}\nGender: {gender}\nRoll: {roll}\nMarks: {marks}'.format(\
                roll=self.roll, marks=self.marks, gender=self.gender, name=self.name)

    # object functions
    def getgrade(self):
        marks = self.marks
        if marks > 100 or marks < 0:
            return 'I'
        elif marks >= 70:
            return 'A'
        elif marks >= 60:
            return 'B'
        elif marks >= 40:
            return 'C'
        else:
            return 'F'

    # class function
    # Access - Classname.classfunctioncall()
    def getminattendance():
        # code to fetch the common min attendance criteria from some server
        return 70
    
    def get_name_roll(self):
        return (self.name, self.roll)