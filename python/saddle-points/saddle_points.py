# def saddle_points(matrix):
#     coordinates =[[index2,index1] for index1,value1 in enumerate(matrix) for index2,value2 in enumerate(value1)]
#     return coordinates


# def is_saddle_number(matrix, x, y):
#     pass

# print(saddle_points([[4, 5, 4], [3, 5, 5], [1, 5, 4, 5]]))

 

# def row(matrix, index):
#     return matrix[index].copy()

def column(m, i):
     return [item[i] for item in m]

def saddle_points(matrix):
    row_maxes = []
    saddle_points = []
    for item in matrix:
        if (len(item)) < len(max(matrix, key=len)):
            item.append(0)
    
    for row in matrix:
        for ind, item in enumerate(row):
            if item == max(row):
                #print (item)
                row_maxes.append((matrix.index(row),ind))
    for item in row_maxes:
        if matrix[item[0]][item[1]] == min(column(matrix,item[1])):
            saddle_points.append(item)
       

 

    
    return [{"row" : item[0]+1, "column" : item[1]+1} for item in saddle_points]

print(saddle_points([[4, 5, 4], [3, 5, 5], [1, 5, 4]]))