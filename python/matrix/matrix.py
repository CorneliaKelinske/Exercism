class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        splitted = self.matrix_string.splitlines()
        re_splitted = [item.split() for item in splitted]
        self.numbers = [[int(num) for num in item] for item in re_splitted]

    def row(self, index):
        t = tuple(self.numbers[index-1])
        return list(t)
       
    def column(self, index):
        return [item[index-1] for item in self.numbers]

m = Matrix("1 2 3\n4 5 6\n7 8 9")

print(m.numbers)
print(m.row(2))
print(m.column(2))
test_row = m.row(2).append(4)
print(m.row(2))
print(m.numbers)





