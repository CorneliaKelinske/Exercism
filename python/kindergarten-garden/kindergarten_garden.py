PLANT_NAMES = {"R": "Radishes", "C": "Clover", "G": "Grass", "V": "Violets"}
STUDENTS = [
            "Alice", "Bob", "Charlie", "David",
            "Eve", "Fred", "Ginny", "Harriet",
            "Ileana", "Joseph", "Kincaid", "Larry"
    ]



class Garden:
    def __init__(self, diagram, students=STUDENTS):
        self.diagram = diagram
        self.students = students
    
    
    def assign_index(self):
        index = 0
        indexes = {}
        self.students.sort()
        for student in self.students:
            indexes.update({student:(index, index+1)})
            index += 2
        return indexes
    
        
    
    def plants(self, name):
            rows = self.diagram.splitlines()
            kids_indexes = self.assign_index()

            plants_short = [(item[kids_indexes[name][0]], item[kids_indexes[name][1]]) for item in rows]
            plants_full = []

            for item in plants_short:
                for letter in item:
                    plants_full.append(PLANT_NAMES[letter])
        
            return plants_full
        



