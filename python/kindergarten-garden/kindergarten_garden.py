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
         self.garden = self.__set_up_garden__()
    

     def __set_up_garden__(self):
        plant_lookup = {}
        for student in self.students:
            index = self.students.index(student)        
            plants_short = []       
            for item in self.diagram:            
                plants_short.append(item[index*2])
                plants_short.append(item[index*2 + 1])
            plant_lookup.update({student: plants_short})
        return plant_lookup

garden = Garden("VRCGVVRVCGGCCGVRGCVCGC\nVRCCCGCRRGVCGCRVVCVGCG")
print(garden.__set_up_garden__())
        