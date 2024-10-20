from school import School

class Subject:
    def __init__(self,name,teacher) -> None:
        self.name = name
        self.teacher = teacher
        self.max_marks = 100
        self.pass_marks = 33
        

    def exam(self,students):
        for student in students:
            marks = self.teacher.evaluate_exam()
            student.marks[self.name] = marks
            student.subject_grade[self.name] = School.calculate_grade(marks)

