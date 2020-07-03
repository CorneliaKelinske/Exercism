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
        roster_complete = []
        roster = [sorted(self.all_students[number]) for number in sorted(self.all_students)]
        for item in roster:
            for name in item:
                roster_complete.append(name)

        return roster_complete

    def grade(self, grade_number):
        if grade_number in self.all_students:
            return sorted(self.all_students[grade_number])
        else:
            return []

    
         
        

school = School()
print(school.add_student(name="Hubert", grade=2))
print(school.add_student(name="Bert", grade=2))
print(school.add_student(name="Elsa", grade =1))
print(school.roster())