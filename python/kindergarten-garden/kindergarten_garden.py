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
        self.student_plants = self.plants()
       

    def assign_index(self):
        index = 0
        indexes = {}
        self.students.sort()
        for student in self.students:
            indexes.update({student:(index, index+1)})
            index += 2
        return indexes

    def plants(self):
            rows = self.diagram.splitlines()
            kids_indexes = self.assign_index()
            plants_short = {}

            for student in self.students:
                plants_short.update({student:(item[kids_indexes[student][0]], item[kids_indexes[student][1]]) for item in rows})
            # plants_full = []

            # for item in plants_short:
            #     for letter in item:
            #         plants_full.append(PLANT_NAMES[letter])
        
            return plants_short

 #before: used one name, got the plants for that name, converted the plants.
 #next step: do the same thing for each kid in students. append kid + the plants that go with it to a dict
 #update dict with long names
     
garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
print(garden.plants())