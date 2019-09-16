# Detect the anomaly, able to detect either row/ column.
# The input is assumed to be sorted, with both row sorted(from good performance student to poor performance studet)
# and column sorted (good performance item and poor performance item).
# input: The input format is assumed to be a 2-d matrix/ array, with each cell representing the score (0/1/2/3..)

# For testing purpose, the 2-d matrix will be a 4*4 matrix, initialised with ones and zeros.
# The element of the inner array is the result of a student.

from scipy.stats.stats import pearsonr
import numpy
import copy

Matrix = [[1,1,1,1], [1,1,1,0], [1,1,1,0], [1,1,0,0], [1,2,0,0]]
def detectDimenstion(matrix):
    """
    Return a tuple of dimension of the 2-d matrix.
    The first element is the number of student, the second number is the number of items.
    :param matrix: the 2-d matrix of Guttman Chart
    :return: A tuple containing the number of student and numebr of items.
    """
    return (matrix.__len__(), matrix[0].__len__())
# Calculate the summation of student score.
def sumStudentScore(matrix):
    return map(sum,matrix)
# Calculate the summation of item/skill/assessment score.
def sumItemScore(matrix):
    result = []
    for i in range(len(matrix[0])):
        sum_item = sum([row[i] for row in matrix])
        result.append(sum_item)
        # print([row[i] for row in matrix])
        # print(sum([row[i] for row in matrix]))
    print(result)
    return result
    # print([row[1] for row in matrix])

def appendStudentSum(matrix):
    result = list(sumStudentScore(matrix))
    print(matrix.__len__())
    real_matrix = copy.deepcopy(matrix)
    real_matrix.append(result)  # Student result is appended.
    return real_matrix

def detectStudentIrregular(matrix):
    print("hello")


a = [1,4,6]
b = [1,1,1]

# print(pearsonr(a,b))
# print(numpy.corrcoef(a,b))
# detectStudentIrregular(Matrix)
# for i in sumStudentScore(Matrix):
#     print(i)
# for i in appendStudentSum(Matrix):
#     print(i)
# for i in appendStudentSum(Matrix):
#     print(i)
print(detectDimenstion(Matrix))

sumItemScore(Matrix)
