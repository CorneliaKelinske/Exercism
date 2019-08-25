class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        splitted = self.matrix_string.splitlines()
        re_splitted = [item.split() for item in splitted]
        self.numbers = [[int(num) for num in item] for item in re_splitted]

    def row(self, index):
        return self.numbers[index-1]
       
    def column(self, index):
        return [item[index-1] for item in self.numbers]






