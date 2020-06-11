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
        print(index)

        keys = []

        print(list(enumerate(self.diagram)))
        for item[1] in enumerate(self.diagram):
            #print(item)
            keys.append(item[1][index])
            keys.append(item[1][index + 1])
            print(keys)
        return keys

garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
print(garden.plants("Bob"))