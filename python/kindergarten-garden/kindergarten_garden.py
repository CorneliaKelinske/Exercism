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
        self.stud_plants = self.students_plants()
        self.adjusted_diagram = self.adjust_diagram()
       
    def adjust_diagram(self):
        rows = self.diagram.splitlines()
        full_garden = []
        
        item_a = rows[0]
        item_b = rows[1]            
            
        while len(item_a) <= len(self.students) * 2:
            item_a += "00"
        while len(item_b) <= len(self.students) * 2:
            item_b += "00"
          
        # print(item_a)
        # print(item_b)
        full_garden.append(item_a)
        full_garden.append(item_b)
        return full_garden

    def assign_index(self):
        index = 0
        indexes = {}
        self.students.sort()
        for student in self.students:
            indexes.update({student:(index, index+1)})
            index += 2
        return indexes

    def students_plants(self):        
        kids_indexes = self.assign_index()                        
        plants_short = {}
        plant_rows = self.adjust_diagram()

            
        #for student in kids_indexes:
        #print("Hello")
        for student in kids_indexes:
            plants_short.update({student:[plant_rows[0][kids_indexes[student][0]], plant_rows[0][kids_indexes[student][1]], plant_rows[1][kids_indexes[student][0]], plant_rows[1][kids_indexes[student][1]]]})       
            #  plants_short.update({student:[plant_rows[0][kids_indexes[student][0], plant_rows[0][kids_indexes[student][1], plant_rows[1][kids_indexes[student][0],plant_rows[1][kids_indexes[student][1]]}) 
            
        return plants_short
            

                

    def plants(self, name):
        plants_full = []
        for item in self.stud_plants[name]:
                for letter in item:
                    plants_full.append(PLANT_NAMES[letter])
        
        return plants_full 



     
garden = Garden("VRCGVVRVCGGCCGVRGCVCGC\nVRCCCGCRRGVCGCRVVCVGCG")
print(garden.students_plants())
print(garden.assign_index())