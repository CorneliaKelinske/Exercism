plant_names: {"R": "Radishes", "C": "Clover", "G": "Grass", "V": "Violets"}


class Garden:
    def __init__(self, diagram, students=[
            "Alice", "Bob", "Charlie", "David",
            "Eve", "Fred", "Ginny", "Harriet",
            "Ileana", "Joseph", "Kincaid", "Larry"
    ]):
        self.diagram = diagram
        self.students = students
        pass


garden = Garden("RC\nGG")
print(garden.diagram)
