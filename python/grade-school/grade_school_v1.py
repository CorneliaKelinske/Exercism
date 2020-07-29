from collections import defaultdict

class School:
    def __init__(self):
        self.all_students = defaultdict(list)

    def add_student(self, name, grade):
        self.all_students[grade].append(name)       
        return self.all_students

def roster(self):
        roster_complete = []
        roster = [sorted(self.all_students[number]) for number in sorted(self.all_students)]
        for item in roster:
            for name in item:
                roster_complete.append(name)
        return roster_complete

def grade(self, grade_number):
    return sorted(self.all_students.get(grade_number, []))     
   