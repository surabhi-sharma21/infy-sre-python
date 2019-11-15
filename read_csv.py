from csv import reader, writer
from com.abc.lib.student_ops import get_grade
path = 'data/students.csv' # relative path

with open(path) as fp:
    csv_reader = reader(fp)
    with open('data/students_grade.csv', mode='wt') as fd:
            csv_writer = writer(fd)
            for row in csv_reader:
                # print(row) # list of tokens for a csv row
                name, marks = row[0], row[-1]
                grade = get_grade(float(marks))

                csv_writer.writerow([name, grade])
