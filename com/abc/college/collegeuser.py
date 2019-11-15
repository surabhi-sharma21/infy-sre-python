class CollegeUser(object):
    # every class in python implicitly inherits from the class object
    # object does not inherit from anything else
    def __init__(self, name, gender):
        # self - Student, Professor, sub class object
        self.name = name
        self.gender = gender

    def getdetails(self):
        # self - Student object, Professor object, sub class object
        return 'Name: {0}\nGender: {1}'.format(self.name, self.gender)

    def __str__(self):
        return 'Name: {0}\nGender: {1}'.format(self.name, self.gender)