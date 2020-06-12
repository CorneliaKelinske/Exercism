PLANT_NAMES = {"R": "Radishes", "C": "Clover", "G": "Grass", "V": "Violets", "0":"Did not plant anything"}
STUDENTS = [
            "Alice", "Bob", "Charlie", "David",
            "Eve", "Fred", "Ginny", "Harriet",
            "Ileana", "Joseph", "Kincaid", "Larry"
    ]

class Garden:
     def __init__(self, diagram, students=STUDENTS):
         self.students = sorted(students)
         self.diagram = diagram.splitlines()

     def plants(self, name):
        index = self.students.index(name)        
        plants_short = []       
        for item in self.diagram:            
            plants_short.append(item[index*2])
            plants_short.append(item[index*2 + 1])
            
        return [PLANT_NAMES[x] for x in plants_short]

garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
print(garden.plants("Bob"))