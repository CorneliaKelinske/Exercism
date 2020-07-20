class School:
    def __init__(self):
        self.all_students = {}
        

    def add_student(self, name, grade):
    
        if grade in self.all_students:
            self.all_students[grade].append(name)
        else:
            self.all_students.update({grade:[name]})
        all_students_copy = self.all_students
        return all_students_copy

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
        return []

    
         
        

