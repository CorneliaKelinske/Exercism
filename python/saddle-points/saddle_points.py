
def column(m, i):
     return [item[i] for item in m]

def saddle_points(matrix):
    row_maxes = []
    saddle_points = []
    for item in matrix:
        if (len(item)) < len(max(matrix, key=len)):
            raise ValueError("irregular matrix")
    
    for idx, row in enumerate(matrix):       
        for ind, item in enumerate(row):
            if item == max(row):
                row_maxes.append((idx,ind))

    for item in row_maxes:        
        if matrix[item[0]][item[1]] == min(column(matrix,item[1])):
            saddle_points.append(item)
   
    return [{"row" : item[0]+1, "column" : item[1]+1} for item in saddle_points]

print(saddle_points([[1, 2, 3], [3, 1, 2], [2, 3, 1]]))