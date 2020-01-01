# def saddle_points(matrix):
#     coordinates =[[index2,index1] for index1,value1 in enumerate(matrix) for index2,value2 in enumerate(value1)]
#     return coordinates


# def is_saddle_number(matrix, x, y):
#     pass

# print(saddle_points([[4, 5, 4], [3, 5, 5], [1, 5, 4, 5]]))

 

# def row(matrix, index):
#     return matrix[index].copy()

# def column(matrix, index):
#     return [item[index] for item in matrix]

def saddle_points(matrix):
    row_maxes = []
    for row in matrix:
        for index, item in enumerate(row):
            if item == max(row):
                print (item)
                row_maxes.append(index)
    return row_maxes

print(saddle_points([[4, 5, 6], [3, 5, 5], [1, 5, 4, 5]]))