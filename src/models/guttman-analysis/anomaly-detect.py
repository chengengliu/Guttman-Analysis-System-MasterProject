# Detect the anomaly, able to detect either row/ column.
# The input is assumed to be sorted, with both row sorted(from good performance student to poor performance studet)
# and column sorted (good performance item and poor performance item).
# input: The input format is assumed to be a 2-d matrix/ array, with each cell representing the score (0/1/2/3..)

# For testing purpose, the 2-d matrix will be a 4*4 matrix, initialised with ones and zeros.
# The element of the inner array is the result of a student.

import pandas as pd
import copy
import math
import numpy
from numpy import dot
from numpy.linalg import norm



# test = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0], [1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1]]
# test_data = [[1],[0],[1],[0],]
# print(len(test[0]))
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
    return list(reversed(result))
# Receive a real_matrix (with student and item summation appended)
def sortBasedOnItem(matrix, itemSum):

    index = list(range(len(itemSum)))
    sublist_item = list(zip(itemSum, index))
    sublist_item = sorted(sublist_item,key = lambda x:x[0], reverse=True)  # Order that the inner list should follow.
    sorted_item_order = [x[1] for x in sublist_item]
    # print("Sorted_item_order")
    # print(sorted_item_order)
    result = copy.deepcopy(matrix)
    for i in range(len(itemSum)):
        temp_student = list(zip(sorted_item_order, result[i]))
        temp_student = sorted(temp_student, key=lambda x:x[0])
        temp_student_list = [x [1] for x in temp_student]
        result[i] = temp_student_list
    return result
# Can return either the median of the students scores, or the median of the items.
def cal_median(matrix, summation):
    if len(summation) %2 ==0:
        median = summation[int(len(summation)/2)] + summation[int(len(summation)/2)-1]
        return median/2
    else:
        median = summation[math.floor(len(summation)/2)]
        return median
# Can return either the average of the students scores, or the average score of the items.
def cal_average(matrix, summation, number):
    return sum(summation)/number

# Return the average score of item, per student.
def retrieve_average_per_item(matrix, itemsum):
    # Initialise a matrix to store items average results.
    result = []
    for i in range(len(itemsum)):
        result.append(itemsum[i]/len(matrix))
    return result

# Transpose of the input matrix. The output is a 2-d/ nested list, but with row: items  and column: students.
# This function doesn't modify the original data, except the format(performa a transpose function on the original data)
# This will be helpful for later use.
def retrieve_items_columns(matrix):
    result = [list(x) for x in zip(*matrix)]
    print(result)
    return result
# [0.24999999999999997, -0.07912414523193152, -2.7755575615628914e-17, 0.40824829046386296]
def retrieve_correlation_columns(matrix):
    result = []
    for i in range(len(matrix)):
        result.append(cal_correlation_items(matrix, i))
    return  [j for i in result for j in i]

def cal_correlation_items(matrix, current_index):
    # If the row you want to check is the first column or the last column, only check the column after it or before it.
    result = []
    if current_index == 0:
        result.append(numpy.corrcoef(matrix[current_index], matrix[current_index+1])[0,1])
    elif current_index == len(matrix)-1:
        result.append(numpy.corrcoef(matrix[current_index], matrix[current_index-1])[0,1])
    else:
        temp = numpy.corrcoef(matrix[current_index],
                                  matrix[current_index+1])[0,1] + numpy.corrcoef(
            matrix[current_index],matrix[current_index-1])[0,1]
        result.append(temp/2.0)
    return result
#
#
# def mean(itemlist):
#     total = 0
#     for i in itemlist:
#         total += float(i)
#     mean = total/len(itemlist)
#     return mean
#
# ###
# # Here is a bug: How do you deal with all ones???? Standard Deviation will be zero.
# def stand_dev(itemlist):
#     dev = 0.0
#     for i in range(len(itemlist)):
#         dev += (itemlist[i] -mean(itemlist))**2
#     dev = dev**(1/2.0)
#     return dev
#
# def correlation_column(itemlist1, itemlist2):
#     # Calculate means and standard deviations for two lists.
#     x_mean = mean(itemlist1)
#     y_mean = mean(itemlist2)
#     x_stand_dev = stand_dev(itemlist1)
#     y_stand_dev = stand_dev(itemlist2)
#     numerator = 0.0
#     for i in range(len(itemlist1)):
#         numerator += (itemlist1[i]-x_mean) * (itemlist2[i]-y_mean)
#     denominator = x_stand_dev * y_stand_dev
#     result = numerator/denominator
#     return result

def detectStudentIrregular(data_list):
    print()

# Receive a real_matrix (with student and item summation appended)
def detectItemIttegulat(matrix):
    print ("hello")

#TODO: 我认为这个算法可以分为三部分： 1. detect周围的correlation(1-2个?)，correlation 的比值应该小于 多少多少，这个比值应该调参，目前来说还不知道。 correlation部分应该占比1/2
#TODO： 2. 计算当前item与整体items的similarty， 用cosine夹角计算。 占比1/2
#TODO: 3. 四分之一法，暴力规划四部分区域大小， 检测有无异常行为。 这部分占比小，但是如果检测出来，就应该加一个flag， 告诉之前的算法，当前item有存在不合格风险。

# TODO: RoadMap : We can treate the problem as a anomaly detection problem and apply outelier detection algorithms, including
# TODO: 基于密度异常点检测 / 基于邻近度异常点检测等等。 Isolation Forest看起来是个不错的选择。 而且Isolation Forest 在sklearn有实现，调包可完成。

# 'Four Partition'

'''
According to the median of the items and students numbers, as well as students performance, 
The following 'Four Partitions' algorithm is implemented. 
Since the counter will start from the top left, block 'A' will be the most compentent student, answerign the easiest items/questions. 
This block tend to have a low percentage of false. If detect a zero/false, falge this student and this items. Even though it may 
not effect the total correlation performace, the anomaly shows that there is unusual/odd zero. 
Similarly, the percentage of block 'B' and block 'C', containing zeros/false will be higher than blcok 'A'. Detection in these
two areas will not flag the student or items. The flags will be raised only if the anomaly 

          |  
    A     |    B
          |  
          |
---------- ----------
          |  
    C     |    D     
          |  
          |


'''
def main():
    Matrix = [[0, 1, 1, 1], [1, 1, 1, 0], [1, 1, 1, 0], [1, 1, 0, 0], [1, 2, 0, 0]]
    print(Matrix)
    studentSum = sumStudentScore(Matrix)
    itemSum = sumItemScore(Matrix)
    print(studentSum)
    print(itemSum)
    sortedMatrixStudent = sortBasedOnStudent(Matrix, studentSum)  # After sorting based on student summation.
    sortedMatrixItem = sortBasedOnItem(sortedMatrixStudent, itemSum)  # After sorting based on item summation.
    matrix = sortedMatrixItem
    print(matrix)

    # After sorting the data, both item_summation and student_summation records should be sorted.
    # Keep the orginal order unchanged.
    student_sum_copy = copy.deepcopy(studentSum)
    item_sum_copy = copy.deepcopy(itemSum)
    student_sum_copy.sort()
    item_sum_copy.sort()
    student_sum_copy = list(reversed(student_sum_copy))
    item_sum_copy = list(reversed(item_sum_copy))

    student_score_median = cal_median(matrix, student_sum_copy)
    item_median = cal_median(matrix, item_sum_copy)
    student_score_ave = cal_average(matrix, student_sum_copy, len(studentSum))
    item_ave = cal_average(matrix, item_sum_copy, len(itemSum))

    ave_per_item = retrieve_average_per_item(matrix, item_sum_copy)  # Average of each column. Sorted list.
    items_in_matrix = retrieve_items_columns(matrix)

    # This is the result to return back to the server, a list of correlation, in the order with each columns.
    correlation_of_columns = retrieve_correlation_columns(items_in_matrix)
    print(correlation_of_columns)
    print(numpy.corrcoef(items_in_matrix[0], items_in_matrix[1])[0,1])





if __name__ == '__main__':
    main()





###############################################################################
####### Any code bleow this line are depreciated(the use of pandas)
###############################################################################
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

# These two functions will return the headers for columns and rows after the data is sorted.
# The order of both columns and rows are sorted.
def retrieve_column_headers(data):
    return list(data.columns.values)
def retrieve_row_headers(data):
    return list(data.index)


# def sortStudent(matrix):
#     matrix.sort_values('')

# data = formatData(Matrix)
# # print(data)
# data= sortStudentandItems(data)
# data_list = [tuple(x) for x in data.to_records(index=True)]

# print(data_list)
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
# row_header = retrieve_row_headers(data)
# column_header = retrieve_column_headers(data)

# data2 = formatData(test)
# print(data2)
# data2_sort = sortStudentandItems(data2)
# print(data2[data2.columns[1:]].corr()[:-1])
# print("test 2: Correlation between one column and multiple coluns: ")
# print(data2[['1','2','3','4','5','6','7','8','9','10','0','12']].corrwith(data2['11']))

# correlation = pd.DataFrame()
# for a in list('0'):
#     for b in list(data.columns.values):
#         correlation.loc[a,b] = data.corr().loc[a,b]

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