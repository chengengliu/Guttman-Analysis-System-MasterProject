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

test = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0], [1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1]]
test_data = [[1],[0],[1],[0],]
print(len(test[0]))
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

def detectMedian(data,data_list):
    print()
# These two functions will return the headers for columns and rows after the data is sorted.
# The order of both columns and rows are sorted.
def retrieve_column_headers(data):
    return list(data.columns.values)
def retrieve_row_headers(data):
    return list(data.index)


# Calculate correlation between columns.
# Require that there are at least 5 students.


def calculate_correlation_columns(data, row_header, column_header):
    print()



def detectStudentIrregular(data_list):
    for s in data:
        print(s)


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









# Another way of using Pandas. The following code will clean and sort the data.
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
        studentName.append(str(i))
    data = dict(zip(studentName, matrix))

    data_pd = pd.DataFrame(data, retrieveIndexOfItems(matrix))
    # data_pd.loc['StudentSum'] = sumStudentScore(matrix)
    additional = pd.DataFrame({'ItemSum': sumItemScore(matrix)}, retrieveIndexOfItems(matrix))  # Add column
    result = pd.concat([data_pd, additional], axis=1, sort= True)
    lis = sumStudentScore(matrix)
    lis.append(None)
    result.loc['StudentSum'] = lis   # Add addtional row
    return result
def retrieveIndexOfItems(matrix):
    item_name = []
    for i in range(len(matrix[0])):
        item_name.append(str(i))
    return item_name
def sortStudentandItems(data):
    data = data.sort_values(by= ['ItemSum'], ascending=False)
    # print(data)
    data = data.sort_values(by='StudentSum', axis = 1, ascending=False)
    # print(data)
    return data

# def sortStudent(matrix):
#     matrix.sort_values('')
data = formatData(Matrix)
# print(data)
data= sortStudentandItems(data)
data_list = [tuple(x) for x in data.to_records(index=True)]
# print(data_list)
detectStudentIrregular(data_list)
# detectStudentIrregular(data)
# print("Correlation: ")
'''
Correlation: 
                   1         0         2         3  StudentSum
1           1.000000  0.979796  0.821584  0.580948    0.000000
0           0.979796  1.000000  0.894427  0.632456         NaN
2           0.821584  0.894427  1.000000  0.707107    0.645497
3           0.580948  0.632456  0.707107  1.000000    0.790569
StudentSum  0.000000       NaN  0.645497  0.790569    1.000000'''
# print(data.T.corr())
# The above correlation is not correct? Probably.

# This will return the correlation between each column.
# print(data['1'].corr(data['0']))
# print(data['1'].corr(data['4']))
# print(data['1'].corr(data['2']))
# print("Correlation between one column and multiple columns: ")
# print(data[['1','2','3','4']].corrwith(data['0']))

# print(retrieve_column_headers(data))
# print(retrieve_row_headers(data))
row_header = retrieve_row_headers(data)
column_header = retrieve_column_headers(data)

data2 = formatData(test)
# print(data2)
data2_sort = sortStudentandItems(data2)
# print(data2[data2.columns[1:]].corr()[:-1])
# print("test 2: Correlation between one column and multiple coluns: ")
# print(data2[['1','2','3','4','5','6','7','8','9','10','0','12']].corrwith(data2['11']))

correlation = pd.DataFrame()
for a in list('0'):
    for b in list(data.columns.values):
        correlation.loc[a,b] = data.corr().loc[a,b]
# print("Correlation")
# print(data2_sort['8'].corr(data2_sort['5']))
# print("data 12 ")
# print(data2_sort['10'])
# print(data2_sort['11'])
# print(data2_sort['1'])

def calculateRowCorrelation(data):
    # print(data.T.corr().unstack().reset_index(name="corr"))
    # print(data.T.corr())
    print()
# calculateRowCorrelation(data2_sort)