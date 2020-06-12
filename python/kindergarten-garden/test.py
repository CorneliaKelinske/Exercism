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
        #print(index)

        keys = []

        # print(self.diagram)
        for item in self.diagram:
            # print(item)
            # print(item[index*2])
            # print(item[index*2+1])
            keys.append(item[index*2])
            keys.append(item[index*2 + 1])
            
            # print(keys)
        return [PLANT_NAMES[x] for x in keys]

garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
print(garden.plants("Bob"))