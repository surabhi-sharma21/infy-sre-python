# Student IS-A CollegeUser
# subclass IS-A super class
# child class IS-A parent class
# Inheritance

from .collegeuser import CollegeUser

class Student(CollegeUser):
    def __init__(self, name, gender, roll, marks):
        super().__init__(name, gender)
        # Internally
        # CollegeUser.__init__(self, name, gender)

        self.roll = roll
        self.marks = marks

    # method overriding
    # overriden method gets called over the inherited method
    def getdetails(self):
        part1 = super().getdetails() # calls the super class method even inspite
        # of having an overriden method
        part2 = '\nRoll: {0}'.format(self.roll)

        return part1 + part2