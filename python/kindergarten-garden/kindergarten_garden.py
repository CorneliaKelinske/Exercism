PLANT_NAMES = {"R": "Radishes", "C": "Clover", "G": "Grass", "V": "Violets", "0":"Did not plant anything"}
STUDENTS = [
            "Alice", "Bob", "Charlie", "David",
            "Eve", "Fred", "Ginny", "Harriet",
            "Ileana", "Joseph", "Kincaid", "Larry"
    ]
class Garden:
    def __init__(self, diagram, students=STUDENTS):
        self.diagram = diagram
        self.students = students
        self.stud_plants = self._students_plants()
        self.adjusted_diagram = self._adjust_diagram()
       
    def _adjust_diagram(self):
        rows = self.diagram.splitlines()
        full_garden = []       
    
        while len(rows[0]) <= len(self.students) * 2:
            rows[0] += "00"
        while len(rows[1]) <= len(self.students) * 2:
            rows[1] += "00"
          
        full_garden.append(rows[0])
        full_garden.append(rows[1])
        return full_garden

    def _assign_index(self):
        index = 0
        indexes = {}
        self.students.sort()
        for student in self.students:
            indexes.update({student:(index, index+1)})
            index += 2
        return indexes

    def _students_plants(self):        
        kids_indexes = self._assign_index()                        
        plants_short = {}
        plant_rows = self._adjust_diagram()
    
        for student in kids_indexes:
            plants_short.update({student:[plant_rows[0][kids_indexes[student][0]], plant_rows[0][kids_indexes[student][1]], plant_rows[1][kids_indexes[student][0]], plant_rows[1][kids_indexes[student][1]]]})       
            
        return plants_short            
                

    def plants(self, name):
        plants_full = []
        for item in self.stud_plants[name]:
                for letter in item:
                    plants_full.append(PLANT_NAMES[letter])
        
        return plants_full 



     
