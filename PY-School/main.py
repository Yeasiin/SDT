from school import School
from classroom import Classroom
from subject import Subject
from person import Student, Teacher


school = School("ABC International","Chittagong")


class1 = Classroom("eight")
class2 = Classroom("nine")
class3 = Classroom("ten")


school.add_classroom(class1)
school.add_classroom(class2)
school.add_classroom(class3)

yeasin = Student("Yeasin", class3)
arfat = Student("Arfat", class2)
emon = Student("Emon",class1)


school.student_admission(yeasin)
school.student_admission(arfat)
school.student_admission(emon)


amin = Teacher("Amin")
akkas = Teacher("Akkas")
shofiq = Teacher("Shofiq")


math = Subject("Math", amin)
science = Subject("Science", akkas)
english = Subject("English", shofiq)


class1.add_subject(math)
class1.add_subject(science)
class1.add_subject(english)

class2.add_subject(math)
class2.add_subject(science)
class2.add_subject(english)

class3.add_subject(math)
class3.add_subject(science)
class3.add_subject(english)

class1.take_semester_final_exam()
class2.take_semester_final_exam()
class3.take_semester_final_exam()


school.add_teacher(math,amin)
school.add_teacher(science,akkas)
school.add_teacher(english,shofiq)



print(school)



