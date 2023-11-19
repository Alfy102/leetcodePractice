def rotate(matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    temp = [list(i) for i in list(zip(*matrix))]
    print(temp)
    res = []
    for i in temp:
        print(i[::-1])
        res.append(i[::-1])
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = res[i][j]

rotate([[1,2,3],[4,5,6],[7,8,9]])