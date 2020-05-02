plant_names: {"R": "Radishes", "C": "Clover", "G": "Grass", "V": "Violets"}
kids_indexe: {"Alice":(0,1), "Bob" : (2,3) , "Charlie" : (4,5), "David" : (6,7),
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
    
    def plants(self, name):
            return name
        


garden = Garden("RC\nGG")
print(garden.diagram)
print(garden.plants("Alice"))
