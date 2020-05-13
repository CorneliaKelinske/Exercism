plant_names = {"R": "Radishes", "C": "Clover", "G": "Grass", "V": "Violets"}
kids_indexes = {"Alice":(0,1), "Bob" : (2,3) , "Charlie" : (4,5), "David" : (6,7),
            "Eve" : (8,9), "Fred" : (10, 11), "Ginny" : (12, 13), "Harriet" : (14, 15),
            "Ileana" : (16, 17), "Joseph" : (18, 19), "Kincaid" : (20, 21), "Larry" : (22, 23)}


class Garden:
    def __init__(self, diagram, students=[
            "Alice", "Bob", "Charlie", "David",
            "Eve", "Fred", "Ginny", "Harriet",
            "Ileana", "Joseph", "Kincaid", "Larry"
    ]):
        self.diagram = diagram
        self.students = students
    
    #here I need to define a function that orders the students alphabetically and returns the new kids_indexes
    def assign_index(self):
        self.students.sort()
        return self.students
    
        
    
    def plants(self, name):
            rows = self.diagram.split("\n")

            plants_short = [(item[kids_indexes[name][0]], item[kids_indexes[name][1]]) for item in rows]
            plants_long = []

            for item in plants_short:
                for letter in item:
                    plants_long.append(plant_names[letter])
        
            return plants_long
        


garden = Garden("VVCCGG\nVVCCGG")
print(garden.assign_index())
print(garden.plants("Alice"))
