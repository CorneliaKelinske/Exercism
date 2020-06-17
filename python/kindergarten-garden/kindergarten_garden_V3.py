PLANT_NAMES = {"R": "Radishes", "C": "Clover", "G": "Grass", "V": "Violets", "0":"Did not plant anything"}
STUDENTS = [
            "Alice", "Bob", "Charlie", "David",
            "Eve", "Fred", "Ginny", "Harriet",
            "Ileana", "Joseph", "Kincaid", "Larry"
    ]

class Garden:
     def __init__(self, diagram, students=STUDENTS):
         self.students = sorted(students)
         self.garden = {}
         for student in self.students:
             self.garden[student] = []            
         for line in diagram.splitlines():            
            for plant_index, plant in enumerate(line):                 
                self.garden[self.students[plant_index // 2]].append(plant)         

     def plants (self, student):
        return [PLANT_NAMES[plant] for plant in self.garden[student]]

    

    


        