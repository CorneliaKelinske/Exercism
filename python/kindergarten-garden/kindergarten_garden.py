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
        self.student_plants = self.students_plants()
       

    def assign_index(self):
        index = 0
        indexes = {}
        self.students.sort()
        for student in self.students:
            indexes.update({student:(index, index+1)})
            index += 2
        return indexes

    def students_plants(self):
            rows = self.diagram.splitlines()
            kids_indexes = self.assign_index()
            plants_short = {}

            for student in self.students:
                plants_short.update({student:[(item[kids_indexes[student][0]], item[kids_indexes[student][1]]) for item in rows]})       
            return plants_short

    #def plants(self, name):



     
garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
print(garden.students_plants())