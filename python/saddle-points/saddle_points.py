def saddle_points(matrix):
    coordinates =[[index2,index1] for index1,value1 in enumerate(matrix) for index2,value2 in enumerate(value1)]
    return coordinates


def is_saddle_number(matrix, x, y):
    pass

print(saddle_points([[4, 5, 4], [3, 5, 5], [1, 5, 4, 5]]))