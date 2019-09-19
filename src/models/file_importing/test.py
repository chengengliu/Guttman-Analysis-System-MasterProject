import math

def get_neighbours(radius):
    temp = []
    for i in range(0, radius + 1):
        for j in range(0, radius - i + 1):
            print((i,j))
            for k in [-1, 1]:
                for l in [-1, 1]:
                    temp.append((i * k,j * l))
    neighbours =  list(dict.fromkeys(temp))
    while (0, 0) in neighbours:
        neighbours.remove((0, 0))
    return neighbours


def odd_cells(matrix, neighbours):
    cells = []
    threshold = 0.6
    for i in range(1, len(matrix)):
        count_zeros = 0
        count_ones = 0
        for j in range(1, len(matrix[0])):
            for (x, y) in neighbours:
                if i + x > 1 and i + x < len(matrix) and j + y > 1 and j + y < len(matrix[0]):
                        count_ones += 1
                        count_zeros += 1
            if matrix[i][j] == 0 and count_ones / (count_zeros+count_ones) > threshold:
                cells.append((i, j))
            elif matrix[i][j] > 0 and count_zeros / (count_zeros+count_ones) > threshold:
                cells.append((i,j))
    return cells




array = get_neighbours(2)
print(array)
print(len(array))
print(calculate_radius([[1]]))