# Detect the anomaly, able to detect either row/ column.
# The input is assumed to be sorted, with both row sorted(from good performance student to poor performance studet)
# and column sorted (good performance item and poor performance item).
# input: The input format is assumed to be a 2-d matrix/ array, with each cell representing the score (0/1/2/3..)

# For testing purpose, the 2-d matrix will be a 4*4 matrix, initialised with ones and zeros.
# The element of the inner array is the result of a student.

from scipy.stats.stats import pearsonr
import pandas as pd
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
    return list(map(sum,matrix))
# Calculate the summation of item/skill/assessment score.
def sumItemScore(matrix):
    result = []
    for i in range(len(matrix[0])):
        sum_item = sum([row[i] for row in matrix])
        result.append(sum_item)
        # print([row[i] for row in matrix])
        # print(sum([row[i] for row in matrix]))
    # print(result)
    return result
    # print([row[1] for row in matrix])

# def appendStudentSum(matrix):
#     result = list(sumStudentScore(matrix))
#     print(matrix.__len__())
#     real_matrix = copy.deepcopy(matrix)
#     real_matrix.append(result)  # Student result is appended.
#     return real_matrix
# def appendItemSum(original_matrix, real_matrix):
#     result = sumItemScore(original_matrix)
#     real_matrix.append(result)
#     return real_matrix




# In case the user accidently provides an unsorted Guttman Chart, sort the chart based on student first.
def sortBasedOnStudent(matrix, studentSum):
    # print(matrix)
    # matrix.sort(key = lambda x: x[len(matrix)-2])
    result = [x for (y,x) in sorted(zip(studentSum, matrix), key=lambda pair:pair[0])]
    # print(result)
    return list(reversed(result))
# Receive a real_matrix (with student and item summation appended)
def sortBasedOnItem(matrix, itemSum):
    print(matrix)
    # print(itemSum)
    # for student in matrix:
    #     for item in student:
    #         print("hello")



def detectStudentIrregular(matrix):
    for s in matrix:
        print("hello")


# Receive a real_matrix (with student and item summation appended)
def detectItemIttegulat(matrix):
    print ("hello")


# print(pearsonr(a,b))
# print(numpy.corrcoef(a,b))
# detectStudentIrregular(Matrix)
# for i in sumStudentScore(Matrix):
#     print(i)
# for i in appendStudentSum(Matrix):
#     print(i)
# for i in appendStudentSum(Matrix):
#     print(i)
# print(detectDimenstion(Matrix))

# sumItemScore(Matrix)
# real_matrix  = appendStudentSum(Matrix)
# print(appendItemSum(Matrix, real_matrix))

# matrix = sortBasedOnStudent(real_matrix)
# print(matrix)
studentSum = sumStudentScore(Matrix)
itemSum = sumItemScore(Matrix)
print(studentSum)
print(itemSum)
sortedMatrixStudent = sortBasedOnStudent(Matrix, studentSum)



#TODO: 可以接受数据的时候存储行 / 列,两个单独的.但是又感觉没有必要.


# Another way of using Pandas
# Sample Format:
#             student0  student1  student2  student3  student4  ItemSum
# item0            1.0       1.0       1.0       1.0       1.0      5.0
# item1            1.0       1.0       1.0       1.0       2.0      6.0
# item2            1.0       1.0       1.0       0.0       0.0      3.0
# item3            1.0       0.0       0.0       0.0       0.0      1.0
# StudentSum       4.0       3.0       3.0       2.0       3.0      NaN
def formatData(matrix):
    studentName = []
    for i in range(len(matrix)):
        studentName.append("student"+str(i))
    data = dict(zip(studentName, matrix))

    data_pd = pd.DataFrame(data, retrieveIndexOfItems(matrix))
    # data_pd.loc['StudentSum'] = sumStudentScore(matrix)
    print(data_pd)
    additional = pd.DataFrame({'ItemSum': sumItemScore(matrix)}, retrieveIndexOfItems(matrix))  # Add column
    print(additional)
    result = pd.concat([data_pd, additional], axis=1, sort= True)
    lis = sumStudentScore(matrix)
    lis.append(None)
    result.loc['StudentSum'] = lis   # Add addtional row
    return result
def retrieveIndexOfItems(matrix):
    item_name = []
    for i in range(len(matrix[0])):
        item_name.append("item"+str(i))
    return item_name
# def sortStudent(matrix):
#     matrix.sort_values('')
print(formatData(Matrix))