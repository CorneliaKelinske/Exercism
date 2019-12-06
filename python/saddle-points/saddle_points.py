def saddle_points(matrix):
    coordinates =[[index1,index2] for index1,value1 in enumerate(matrix) for index2,value2 in enumerate(value1)]
    return coordinates

print(saddle_points([[4, 5, 4], [3, 5, 5], [1, 5, 4]]))