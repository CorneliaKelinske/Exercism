class School:
    def __init__(self):
        self.all_students = {}
        

    def add_student(self, name, grade):
        if grade in self.all_students:
            self.all_students[grade].append(name)
        else:
            self.all_students.update({grade:[name]})
        return self.all_students

    def roster(self):
        pass

    def grade(self, grade_number):
        pass

school = School()
print(school.add_student(name="Aimee", grade=2))
print(school.add_student(name="Bert", grade=2))