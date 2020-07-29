from collections import defaultdict
from collections import OrderedDict


class School:
    def __init__(self):
        self.all_students = defaultdict(list)

    def add_student(self, name, grade):
        self.all_students[grade].append(name)       
        return self.all_students
    
    def roster(self):
        roster_complete = []
        roster = OrderedDict(sorted(self.all_students.items()))
        for k, v in roster.items():
            roster_complete.extend(sorted(v))       
        return roster_complete

    def grade(self, grade_number):       
        return sorted(self.all_students[grade_number])       
        

