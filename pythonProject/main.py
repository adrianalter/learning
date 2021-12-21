def can_see_stage(matrix):
    rows = len(matrix)
    seeStage = True
    columns = len(matrix[1])
    #print("rows ", rows)
    #print("columns ", columns)

    for k in range(columns): #k = 0
        for i in (range(0, rows - 1)): #i = 0
            for j in range(columns): #j = 0
                if(j == k):
                    #print("sono allineato, valore: ", matrix[i][j])
                    if(matrix[i][j] >= matrix[i+1][j]):
                        seeStage = False
                        print(seeStage)
                        return False








if __name__ == '__main__':
    rows = 3
    columns = 4
    sum = 0

    can_see_stage([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    can_see_stage([
        [0, 0, 0],
        [1, 1, 1],
        [2, 2, 2]
    ])

    can_see_stage([
        [2, 0, 0],
        [1, 1, 1],
        [2, 2, 2]
    ])

    can_see_stage([
        [1, 0, 0],
        [1, 1, 1],
        [2, 2, 2]
    ])





