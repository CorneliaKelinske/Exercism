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
        return sorted(self.all_students[grade_number])
         
        

school = School()
print(school.add_student(name="Hubert", grade=2))
print(school.add_student(name="Bert", grade=2))
print(school.grade(2))