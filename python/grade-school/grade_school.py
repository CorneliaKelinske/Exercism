class School:
    def __init__(self):
        self.all_students = {}
        

    def add_student(self, name, grade):
    
        if grade in self.all_students:
            self.all_students[grade].append(name)
        else:
            self.all_students.update({grade:[name]})
        students_new = self.all_students
        return students_new

    def roster(self):
        roster = sorted(self.all_students)
        return roster

    #def grade(self, grade_number):
        #return self.all_students
         
        

school = School()
print(school.add_student(name="Hubert", grade=2))
print(school.add_student(name="Bert", grade=2))
print(school.add_student(name="Elsa", grade =1))
print(school.roster())