'''

USAGE MANUAL/INTERFACE Introduction:


Section I.  Source Code Reading Instructions:

    This anomaly_detect.py file contains both helper functions(which has no relation with algorithms) and
    Algorithms implementation functions, as well as interface functions(used by other modules). This file also contains
    a main function, forinternal testing purpose, which is not meant to be read. Two interfaces functions that should be used
    by other modulesare 'return_correlation(original_data, is_student, flag)' and
    'return_irregular_column_index(original_data, is_student)', which will be introduced in further details in the following section.


Section II. Module usage (interface):

Special notice:

    The function clean_input(original_data) must be used, if Yi Wang's package gives me the inputs with both
    columns name and rows name. This is to be confirmed, whether he or I should make the data format conherent.

1. To get the correlation, for either the student or the items/criteria:

call the function:
    'return_correlation(original_data, is_student, flag)'
Input Description:

    Original_data: where the input is the original data (it is supposed to be nested list)
    This function assumes that the input data is sorted. However, if the data is not sorted, the function will perform sorting
    inside.

    is_student: Is a boolean variable, can be either True or False. This boolean values specifies whether you want to get
    student correlation (row), or item/criteria correlation(column). For example,
    If 'is_student' is set to True, the program will return the correlation calculated for rows.

    flag: This is for testing algorithm purpose. It is a string, can either be 'Accumulation', or 'Correlation'.
        'Accumulation' will use the accumulated value of the column/student, while 'Correlation' is simple calculate the
        data.
Notice: Two different ways of calculating correlation are implemented and can be retrieved. Which way is better needs to
be tested using test results.

2. To get the irregular columns:

call the function:
    'return_irregular_index(original_data, is_student)'
Input Desciption:

    Original_data: where the input is the original data (it is supposed to be nested list)
    This function assumes that the input data is sorted. However, if the data is not sorted, the function will perform sorting
    inside.

    is_student: Is a boolean variable, can be either True or False. This boolean values specifies whether you want to get
    student correlation (row), or item/criteria correlation(column). For example,
    If 'is_student' is set to True, the program will return the correlation calculated for rows.

Notice: For now I have not implemented the cluster algorithm for detecting unusual behaviour. This will be added in sprint3.
Current method is to set a threshold value and to see if the value is below the threshold. （阈值）


Section III. Helper functions:

    As mentioned in Section I, there are several helper functions only used for data re-formatting and sorting purposes.
    These functions can be skipped and has no relation with the algorithms implementations.
    The helper functions include:

    detectDimenstion(matrix)
    sumStudentScore(matrix)
    sumItemScore(matrix)
    sortBasedOnStudent(matrix, studentSum)
    sortBasedOnItem(matrix, itemSum)
    cal_median(matrix, summation)
    cal_average(matrix, summation, number)
    retrieve_average_per_item(matrix, itemsum)
    transpose_matrix(matrix)

    The above mentioned functions can be skipped while you read the code.
'''
# TODO: The code for calculating similarity can be refactored and improved, to calculate together with correlation. 今天不做了， 明天代码重构写。


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


# The following functions are helper functions that deal with data. Either clean/sort/manipulate the input data.
# There is no algorithm involved in above functions.
#######################################################################################################################

# This function will be used if Yi Wang's module returns the follwing data to me:

# [['file', 'test1', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7', 'test8'], ['student1', 1, 1, 0, 0, 0, 0, 0,
# 0], ['student2', 0, 1, 0, 0, 0, 0, 0, 0], ['student3', 1, 1, 1, 0, 0, 0, 0, 0], ['student4', 1, 1, 1, 1, 0, 0, 0, 0],
# ['student5', 1, 1, 1, 1, 1, 0, 0, 0], ['student6', 1, 1, 1, 1, 1, 1, 0, 0], ['student7', 0, 1, 1, 1, 1, 1, 1, 0],
# ['student8', 1, 1, 0, 1, 1, 1, 1, 1], ['student9', 1, 1, 1, 1, 0, 1, 1, 1], ['student10', 1, 1, 0, 0, 1, 1, 1, 1],
# ['student11', 1, 1, 1, 0, 1, 1, 0, 1]]
# It is necessary to clean the original_data to get the desired format like [[...], [...]],
# without any names of columns/rows.
def clean_input(original_data):
    removed_header = original_data[1:]
    for i in range(len(removed_header)):
        removed_header[i] = removed_header[i][1:]
    # print(removed_header)
    return removed_header


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
    """
    Summation of student total scores.
    :param matrix: the original data.
    :return: list that containing each students' scores.
    """
    return list(map(sum, matrix))


def sumItemScore(matrix):
    """
    Summation of item scores.
    :param matrix:  The original data.
    :return:    List that containing each column's scores.
    """
    result = []
    for i in range(len(matrix[0])):
        sum_item = sum([row[i] for row in matrix])
        result.append(sum_item)
    return result


# In case the user accidently provides an unsorted Guttman Chart, sort the chart based on student first.
def sortBasedOnStudent(matrix, studentSum):
    """
    Sort the original data/matrix, in case the user uploads an unsorted data.
    This sort is based on the student performance/scores.
    :param matrix:  The original data.
    :param studentSum:  List of Summation of student scores.
    :return:    The original data after sorting.
    """
    # matrix.sort(key = lambda x: x[len(matrix)-2])
    result = [x for (y, x) in sorted(zip(studentSum, matrix), key=lambda pair: pair[0])]
    return list(reversed(result))


# Receive a real_matrix (with student and item summation appended)
def sortBasedOnItem(matrix, itemSum):
    """
    Sort the original data/matrix, in case the user uploads an unsorted data.
    This sort is based on the item/column performace/scores.
    :param matrix:  The original data.
    :param itemSum:  List of Summation of student scores.
    :return:    The original data after sorting.
    """
    index = list(range(len(itemSum)))
    sublist_item = list(zip(itemSum, index))
    sublist_item = sorted(sublist_item, key=lambda x: x[0], reverse=True)  # Order that the inner list should follow.
    sorted_item_order = [x[1] for x in sublist_item]
    result = copy.deepcopy(matrix)
    for i in range(len(itemSum)):
        temp_student = list(zip(sorted_item_order, result[i]))
        temp_student = sorted(temp_student, key=lambda x: x[0])
        temp_student_list = [x[1] for x in temp_student]
        result[i] = temp_student_list
    return result


# Can return either the median of the students scores, or the median of the items.
def cal_median(matrix, summation):
    """
    Helper function. Not used for now. It will be used in the next phase, when dividing the partitions
    It calculate the median of summation list.
    :param matrix:  null
    :param summation: A list of summations
    :return:  The median of the summations
    """
    if len(summation) % 2 == 0:
        median = summation[int(len(summation) / 2)] + summation[int(len(summation) / 2) - 1]
        return median / 2
    else:
        median = summation[math.floor(len(summation) / 2)]
        return median


def cal_average(matrix, summation, number):
    """
    Can return either the average of the students scores, or the average score of the items.
    Not used for now, maybe useful for later usage.
    :param matrix: null
    :param summation:   A list of summation.
    :param number:  Number of element in summation.
    :return:    Average of the summation.
    """
    return sum(summation) / number


# Return the average score of item, per student.
def retrieve_average_per_item(matrix, itemsum):
    """
    Retrieve the average of the summation, per student.
    :param matrix:  The original input matrix data.
    :param itemsum: Either studentSum or itemSum
    :return:    Average
    """
    # Initialise a matrix to store items average results. len(matrix) is the number of student.
    result = []
    for i in range(len(itemsum)):
        result.append(itemsum[i] / len(matrix))
    return result


# This will be helpful for later use.
def transpose_matrix(matrix):
    """
    Transpose of the input matrix. The output is a 2-d/ nested list, but with row: items  and column: students.
    This function doesn't modify the original data, except the format(performa a transpose function on the original data)
    :param matrix:  The original input data.
    :return:    The original input data after performing transpose.
    """
    result = [list(x) for x in zip(*matrix)]
    # print(result)
    return result


# The inputs are in transposed form.
def detect_full_score(matrix):
    full_score = []
    for criteria in matrix:
        full_score.append(max(criteria))
    return full_score


# Receive a student matrix. Wants to accumulate the score rate accumulated matrix.
# Assume the input is cleaned and sorted. No more sorting needed.
def cal_scorerate_accumulated_matrix(matrix):
    # Accumulated score for all students.
    transposed = transpose_matrix(matrix)

    accumulated_score = []
    full_marks = detect_full_score(transposed)
    full_marks_accumulated = numpy.cumsum(full_marks).tolist()

    for i in range(len(matrix)):
        accumulated_score.append(numpy.cumsum(matrix[i]).tolist())
    scorerate_accumulated = []

    for item in accumulated_score:
        temp = []
        for i in range(len(item)):
            temp.append(item[i] / full_marks_accumulated[i])
        scorerate_accumulated.append(temp)

    return scorerate_accumulated

def get_0staddv_index(matrix):
    """
    Return the positions of item that has a zero standard deviation.
    :param matrix:  The input data after cleaning up.
    :return:    Indexes of students that have zero standard deviation.
    """
    zero_staddv_index = []
    try:
        for i in range(len(matrix)):
            if numpy.std(matrix[i]) == 0:
                zero_staddv_index.append(i)
    except:
        pass

    return zero_staddv_index


def in_danger_list(danger_list, current_index):
    """
    Return True if the number is in the zero standard deviation list.
    Return False if the number is not in the list.
    :param danger_list:
    :param current_index:
    :return:
    """
    for index in danger_list:
        if index == current_index:
            # print("current index data has zero standard deviation. Skip the data. ")
            return True
    return False


# Above functions are helper functions that deal with data. Either clean/sort/manipulate the input data.
# There is no algorithm involved in above functions.
#######################################################################################################################

def retrieve_correlation_similarity(matrix, flag):
    """
    Retrieve the correlation between each column. This function utilises cal_correlation_items
    :param matrix:  The transposed matrix, that has the same data but expressed in the different way (to simplify calculation)
    :return:    A list of correlation calculated.
    """
    accumulation_result = []
    correlation_result = []
    similarity_result = []

    scorerate = cal_scorerate_accumulated_matrix(matrix)

    # A list of zero standard deviation items. So called dangerous list.
    zero_stddiv_list = get_0staddv_index(matrix)
    zero_stddiv_accumulated_list = get_0staddv_index(scorerate)

    # Test if the accumulated zero standard deviation list is empty.
    # If it is empty, do not perform the boundary check.
    if zero_stddiv_accumulated_list:
        accumulation_0stddv_is_empty = False # Exist 0 standard deviation accumulation data
    else:
        accumulation_0stddv_is_empty = True
    if zero_stddiv_list:
        data_0stddv_is_empty = False    # Exist 0 standard deviation data.
    else:
        data_0stddv_is_empty = True

    # Traverse each column/ or row.
    for i in range(len(matrix)):
        similarity_result.append(cal_correlation_items(matrix, i, 'Similarity', scorerate,
                                                       zero_stddiv_accumulated_list, accumulation_0stddv_is_empty))
        if not data_0stddv_is_empty and in_danger_list(zero_stddiv_list, i):
            print("SKIP!!!!! There are all zeros data in the dataset. " + str(i))
            # TODO: 如果试着参与运算呢？
            # continue
        if not accumulation_0stddv_is_empty and in_danger_list(zero_stddiv_accumulated_list, i):
            print("SKIP. There are full scores student!", i)
            # continue
        accumulation_result.append(cal_correlation_items(matrix, i, 'Accumulation', scorerate,
                                                         zero_stddiv_accumulated_list, accumulation_0stddv_is_empty))
        correlation_result.append(cal_correlation_items(matrix, i, 'Correlation', scorerate,
                                                        zero_stddiv_accumulated_list, data_0stddv_is_empty))

    # for i in range(len(matrix)):
    # for i in range(len(matrix)):
    if flag == 'Correlation':
        return [j for i in correlation_result for j in i]
    elif flag == 'Accumulation':
        return [j for i in accumulation_result for j in i]
    elif flag == 'Similarity':
        return [j for i in similarity_result for j in i]
    # return [j for i in accumulation_result for j in i]

def check_nan(value):
    return math.isnan(value)

def cal_correlation_items(matrix, current_index, flag, scorerate, danger_accumulated_list, is_empty):
    """
    Calculate the correlation of columns or rows.
    :param matrix: The transposed matrix, that has the same data but expressed in the different way (to simplify calculation)
    :param current_index: Current index of the column
    :flag: Specifying either 'Accumulation' -> calculate in accumulative way and use accumulative data or
    'Correlation' -> calculate in a normal way.
    :return: A list of correlation calculated.
    """
    # If the row you want to check is the first column or the last column, only check the column after it or before it.
    # result = []
    # print("LENGTH OF MATRIX: ", len(matrix))

    numpy.seterr(all='raise')
    # with numpy.errstate(divide='ignore'):
    #     numpy.float64(1.0) / 0.0
    #
    correlation_result = []
    accumulation_correlation_result = []

    accumulate_current = numpy.cumsum(matrix[current_index])
    # print("ACCUMULATE_CURRENT and matrix[current_index]", accumulate_current, matrix[current_index])
    similarity_result = []

    # Retrieve the square root of number of items (the matrix is in transposed form). This will
    # be the range of calculating the neighbourhood of the column when calculating the correlation.
    range_correlation = math.floor(math.sqrt(len(matrix)))
    # print(range_correlation)

    # If the column is the first column, calculate the correlation within the range but only for the column after it.
    # Try-except is to prevent extreme cases, but generally it will not be used.
    if current_index == 0:
        temp_correlation = 0.0
        temp_accumulation_correlation = 0.0
        temp_similarity = 0.0
        # if not is_empty and in_danger_list(danger_accumulated_list, current_index):

        for i in range(range_correlation):
            if not is_empty and in_danger_list(danger_accumulated_list, current_index + i + 1):
                print("SKIP")
                continue
            try:
                temp_correlation_mid = numpy.corrcoef(matrix[current_index], matrix[current_index + i + 1])[0, 1]
                temp_accumulation_correlation_mid = \
                numpy.corrcoef(scorerate[current_index], scorerate[current_index + i + 1])[0, 1]
                temp_similarity_mid = dot(matrix[current_index], matrix[current_index + i + 1]) / (
                        norm(matrix[current_index]) *
                        norm(matrix[current_index + i + 1]))
                if (check_nan(temp_accumulation_correlation_mid) or check_nan(temp_correlation_mid) or check_nan(
                        temp_similarity_mid)):
                    temp_similarity_mid, temp_accumulation_correlation_mid, temp_correlation_mid = (0.0, 0.0, 0.0)

                temp_accumulation_correlation += temp_accumulation_correlation_mid
                temp_correlation += temp_correlation_mid
                temp_similarity += temp_similarity_mid

                # if check_nan(numpy.corrcoef(scorerate[current_index], scorerate[current_index + i + 1])[0, 1]):
                #     temp_similarity, temp_accumulation_correlation, temp_correlation = (0.0, 0.0, 0.0)
                # else:
                #
                #     temp_correlation += numpy.corrcoef(matrix[current_index], matrix[current_index + i + 1])[0, 1]
                #     # Change the way of calculating score_rate
                #     # temp_accumulation_correlation += \
                #     # numpy.corrcoef(accumulate_current, numpy.cumsum(matrix[current_index + i + 1]))[0, 1]
                #     temp_accumulation_correlation += \
                #         numpy.corrcoef(scorerate[current_index], scorerate[current_index + i + 1])[0, 1]
                #
                #     temp_similarity += dot(matrix[current_index], matrix[current_index + i + 1]) / (
                #             norm(matrix[current_index]) *
                #             norm(matrix[current_index + i + 1]))
            except:
                pass
        # if check_nan(temp_accumulation_correlation):
        #     temp_correlation, temp_accumulation_correlation, temp_similarity = (0,0,0)

        correlation_result.append(temp_correlation / range_correlation)
        accumulation_correlation_result.append(temp_accumulation_correlation / range_correlation)
        similarity_result.append(temp_similarity / range_correlation)
        # result.append(numpy.corrcoef(matrix[current_index], matrix[current_index + 1])[0, 1])

    # If the column is the last column, calculate the correlation within the range but only for the column before it.
    # Try-except is to prevent extreme cases, but generally it will not be used.
    elif current_index == len(matrix) - 1:
        temp_correlation = 0.0
        temp_accumulation_correlation = 0.0
        temp_similarity = 0.0
        for i in range(range_correlation):
            if not is_empty and in_danger_list(danger_accumulated_list, current_index - i - 1):
                print("SKIP LAST")
                continue
            try:
                temp_correlation_mid = numpy.corrcoef(matrix[current_index], matrix[current_index - i - 1])[0, 1]
                temp_accumulation_correlation_mid = \
                numpy.corrcoef(scorerate[current_index], scorerate[current_index - i - 1])[0, 1]
                temp_similarity_mid = dot(matrix[current_index], matrix[current_index - i - 1]) / (
                        norm(matrix[current_index]) *
                        norm(matrix[current_index - i - 1]))
                if (check_nan(temp_accumulation_correlation_mid) or check_nan(temp_correlation_mid) or check_nan(
                        temp_similarity_mid)):
                    temp_similarity_mid, temp_accumulation_correlation_mid, temp_correlation_mid = (0.0, 0.0, 0.0)

                temp_accumulation_correlation += temp_accumulation_correlation_mid
                temp_correlation += temp_correlation_mid
                temp_similarity += temp_similarity_mid

                # if check_nan(numpy.corrcoef(scorerate[current_index], scorerate[current_index + i + 1])[0, 1]):
                #     temp_similarity, temp_accumulation_correlation, temp_correlation = (0.0, 0.0, 0.0)
                # else:
                #
                #     temp_correlation += numpy.corrcoef(matrix[current_index], matrix[current_index - i - 1])[0, 1]
                #
                #     # Change the way of calculating score_rate
                #     # temp_accumulation_correlation += \
                #     # numpy.corrcoef(accumulate_current, numpy.cumsum(matrix[current_index - i - 1]))[0, 1]
                #
                #     temp_accumulation_correlation += \
                #         numpy.corrcoef(scorerate[current_index], scorerate[current_index - i - 1])[0, 1]
                #
                #     temp_similarity += dot(matrix[current_index], matrix[current_index - i - 1]) / (
                #             norm(matrix[current_index]) *
                #             norm(matrix[current_index - i - 1]))
            except:
                pass
        # if check_nan(temp_accumulation_correlation):
        #     temp_correlation, temp_accumulation_correlation, temp_similarity = (0,0,0)

        correlation_result.append(temp_correlation / range_correlation)
        accumulation_correlation_result.append(temp_accumulation_correlation / range_correlation)
        similarity_result.append(temp_similarity / range_correlation)

        # print(temp_similarity, "Last similarity ")
        # print(temp_correlation, "Last correlation ")
        # print(temp_accumulation_correlation, "Last one ")
        # result.append(numpy.corrcoef(matrix[current_index], matrix[current_index - 1])[0, 1])
    # When the current column is neither the first column nor the last column(a.k.a the general column),
    # calculate the correlation between the current column and the columns (within the range) before it and after it.
    else:
        temp_correlation = 0.0
        temp_accumulation_correlation = 0.0
        temp_similarity = 0.0
        for i in range(range_correlation):
            # print("range of CORRELATION", range_correlation)
            # if current_index - i < 0 or (current_index + i) >= (len(matrix)-1):
            #     continue
            # 向左到头， 只往右加
            if current_index - i <= 0:
                if not is_empty and in_danger_list(danger_accumulated_list, current_index + i + 1):
                    continue
                try:
                    temp_correlation_mid = numpy.corrcoef(matrix[current_index], matrix[current_index + i + 1])[0, 1]
                    temp_accumulation_correlation_mid = numpy.corrcoef(scorerate[current_index], scorerate[current_index + i + 1])[0, 1]
                    temp_similarity_mid = dot(matrix[current_index], matrix[current_index + i + 1]) / (
                                norm(matrix[current_index]) *
                                norm(matrix[current_index + i + 1]))
                    if(check_nan(temp_accumulation_correlation_mid) or check_nan(temp_correlation_mid) or check_nan(temp_similarity_mid)):
                        temp_similarity_mid, temp_accumulation_correlation_mid, temp_correlation_mid = (0.0, 0.0, 0.0)

                    temp_accumulation_correlation += temp_accumulation_correlation_mid
                    temp_correlation += temp_correlation_mid
                    temp_similarity += temp_similarity_mid


                    # TODO: 整体修改。
                    # if check_nan(numpy.corrcoef(scorerate[current_index], scorerate[current_index + i + 1])[0, 1]):
                    #     # temp_similarity, temp_accumulation_correlation, temp_correlation = (0.0, 0.0, 0.0)
                    #     pass
                    # else:
                    #
                    #     temp_correlation += numpy.corrcoef(matrix[current_index], matrix[current_index + i + 1])[0, 1]
                    #
                    #     # Change the way of calculating score_rate
                    #     # temp_accumulation_correlation += \
                    #     #     numpy.corrcoef(accumulate_current, numpy.cumsum(matrix[current_index + i + 1]))[0, 1]
                    #     temp_accumulation_correlation += \
                    #         numpy.corrcoef(scorerate[current_index], scorerate[current_index + i + 1])[0, 1]
                    #
                    #     temp_similarity += dot(matrix[current_index], matrix[current_index + i + 1]) / (
                    #             norm(matrix[current_index]) *
                    #             norm(matrix[current_index + i + 1]))
                    continue
                except:
                    print("ENTER THE EXCEPTION", i, " " , current_index)
                    pass
            # 向右到头， 只往左减
            if (current_index + i) >= (len(matrix) - 1):
                if not is_empty and in_danger_list(danger_accumulated_list, current_index - i - 1):
                    continue
                try:
                    temp_correlation_mid = numpy.corrcoef(matrix[current_index], matrix[current_index - i - 1])[0, 1]
                    temp_accumulation_correlation_mid = \
                        numpy.corrcoef(scorerate[current_index], scorerate[current_index - i - 1])[0, 1]
                    temp_similarity_mid = dot(matrix[current_index], matrix[current_index - i - 1]) / (
                            norm(matrix[current_index]) *
                            norm(matrix[current_index - i - 1]))
                    if (check_nan(temp_accumulation_correlation_mid) or check_nan(temp_correlation_mid) or check_nan(
                            temp_similarity_mid)):
                        temp_similarity_mid, temp_accumulation_correlation_mid, temp_correlation_mid = (0.0, 0.0, 0.0)

                    temp_accumulation_correlation += temp_accumulation_correlation_mid
                    temp_correlation += temp_correlation_mid
                    temp_similarity += temp_similarity_mid

                    # TODO：整体修改
                    # if check_nan(numpy.corrcoef(scorerate[current_index], scorerate[current_index + i + 1])[0, 1]):
                    #     pass
                    # else:
                    #     temp_correlation += numpy.corrcoef(matrix[current_index], matrix[current_index - i - 1])[0, 1]
                    #
                    #     # Change the way of calculating score_rate
                    #     # temp_accumulation_correlation += \
                    #     #     numpy.corrcoef(accumulate_current, numpy.cumsum(matrix[current_index - i - 1]))[0, 1]
                    #     temp_accumulation_correlation += \
                    #         numpy.corrcoef(scorerate[current_index], scorerate[current_index - i - 1])[0, 1]
                    #
                    #     # print("Temp Accumulation , Current Index:  and ------ ", temp_accumulation_correlation,
                    #     #       current_index, "------", matrix[current_index - i - 1])
                    #
                    #     temp_similarity += dot(matrix[current_index], matrix[current_index - i - 1]) / (
                    #             norm(matrix[current_index]) *
                    #             norm(matrix[current_index - i - 1]))
                    continue
                # The index may beyond the range, if the current column is near the tail or the head of the list.
                except:
                    print("ENTER THE EXCEPTION", i, " " , current_index)
                    pass
            else:
                if not is_empty and in_danger_list(danger_accumulated_list, current_index - i - 1):
                    print()
                    continue
                # TODO: REMOVE Except. Remember to put it back (indent)
                try:
                    temp_correlation_mid = numpy.corrcoef(matrix[current_index], matrix[current_index - i - 1])[0, 1]
                    temp_accumulation_correlation_mid = \
                    numpy.corrcoef(scorerate[current_index], scorerate[current_index - i - 1])[0, 1]
                    temp_similarity_mid = dot(matrix[current_index], matrix[current_index - i - 1]) / (
                            norm(matrix[current_index]) *
                            norm(matrix[current_index - i - 1]))
                    if (check_nan(temp_accumulation_correlation_mid) or check_nan(temp_correlation_mid) or check_nan(
                            temp_similarity_mid)):
                        temp_similarity_mid, temp_accumulation_correlation_mid, temp_correlation_mid = (0.0, 0.0, 0.0)

                    temp_accumulation_correlation += temp_accumulation_correlation_mid
                    temp_correlation += temp_correlation_mid
                    temp_similarity += temp_similarity_mid

                    # if check_nan(numpy.corrcoef(scorerate[current_index], scorerate[current_index + i + 1])[0, 1]):
                    #     temp_similarity, temp_accumulation_correlation, temp_correlation = (0.0, 0.0, 0.0)
                    # else:
                    #
                    #     temp_correlation += numpy.corrcoef(matrix[current_index], matrix[current_index - i - 1])[0, 1]
                    #
                    #     # Change the way of calculating score_rate
                    #     # temp_accumulation_correlation += \
                    #     # numpy.corrcoef(accumulate_current, numpy.cumsum(matrix[current_index - i - 1]))[0, 1]
                    #     temp_accumulation_correlation += \
                    #         numpy.corrcoef(scorerate[current_index], scorerate[current_index - i - 1])[0, 1]
                    #
                    #     # print("Temp Accumulation , Current Index:  and ------ ", temp_accumulation_correlation, current_index, "------", matrix[current_index - i - 1])
                    #
                    #     temp_similarity += dot(matrix[current_index], matrix[current_index - i - 1]) / (
                    #             norm(matrix[current_index]) *
                    #             norm(matrix[current_index - i - 1]))
                # The index may beyond the range, if the current column is near the tail or the head of the list.
                except:
                    print("ENTER THE EXCEPTION")
                    pass
                if not is_empty and in_danger_list(danger_accumulated_list, current_index + i + 1):
                    continue
                # TODO: REMOVE Except
                try:
                    temp_correlation_mid = numpy.corrcoef(matrix[current_index], matrix[current_index + i + 1])[0, 1]
                    temp_accumulation_correlation_mid = numpy.corrcoef(scorerate[current_index], scorerate[current_index + i + 1])[0, 1]
                    temp_similarity_mid = dot(matrix[current_index], matrix[current_index + i + 1]) / (
                                norm(matrix[current_index]) *
                                norm(matrix[current_index + i + 1]))
                    if(check_nan(temp_accumulation_correlation_mid) or check_nan(temp_correlation_mid) or check_nan(temp_similarity_mid)):
                        temp_similarity_mid, temp_accumulation_correlation_mid, temp_correlation_mid = (0.0, 0.0, 0.0)

                    temp_accumulation_correlation += temp_accumulation_correlation_mid
                    temp_correlation += temp_correlation_mid
                    temp_similarity += temp_similarity_mid

                    # if check_nan(numpy.corrcoef(scorerate[current_index], scorerate[current_index + i + 1])[0, 1]):
                    #     temp_similarity, temp_accumulation_correlation, temp_correlation = (0.0, 0.0, 0.0)
                    # else:
                    #
                    #     temp_correlation += numpy.corrcoef(matrix[current_index], matrix[current_index + i + 1])[0, 1]
                    #
                    #     # Change the way of calculating score_rate
                    #     # temp_accumulation_correlation += \
                    #     # numpy.corrcoef(accumulate_current, numpy.cumsum(matrix[current_index + i + 1]))[0, 1]
                    #     temp_accumulation_correlation += \
                    #         numpy.corrcoef(scorerate[current_index], scorerate[current_index + i + 1])[0, 1]
                    #
                    #     # print("Temp Accumulation , Current Index:  and +++++++", temp_accumulation_correlation, current_index)
                    #
                    #     temp_similarity += dot(matrix[current_index], matrix[current_index + i + 1]) / (
                    #             norm(matrix[current_index]) *
                    #             norm(matrix[current_index + i + 1]))
                except:
                    print("ENTER THE EXCEPTION")
                    pass
        correlation_result.append(temp_correlation / (2 * range_correlation))
        accumulation_correlation_result.append(temp_accumulation_correlation / (2 * range_correlation))
        similarity_result.append(temp_similarity / (2 * range_correlation))
    # print("Accumulation Result: @@@@@@@@", accumulation_correlation_result)
    if flag == 'Accumulation':
        return accumulation_correlation_result
    elif flag == 'Correlation':
        return correlation_result
    elif flag == 'Similarity':
        return similarity_result

def similarity_between_column_whole(matrix, ave_per_student):
    """
    Calculate the similarity between each column and the whole table(student average score). This calculation is based on cosine,
    which generated by dot product divided by normalised production.
    :param matrix:  The transposed matrix, that has the same data but expressed in the different way (to simplify calculation)
    :param ave_per_student: The average score each column, per student.
    :return: A list of similarities of each column/item.
    """
    similarity = []
    for i in range(len(matrix)):
        cosine = dot(matrix[i], ave_per_student) / (norm(matrix[i]) * norm(ave_per_student))
        similarity.append(cosine)
    return similarity


# Not implemented yet.
def detect_student_irregular(matrix):
    print("hello")


def detect_item_irregular(similarities, matrix):
    """
    Detect if the column/item is irregular. If it is irregular, append its position to the list.
    If the average score of the two lists are smaller than 0.5(for now, I don't know how good the data will be, let's try 0.5 for now)
    This parameter will change as development goes.
    :param similarity1: Similarity calculated between each column.
    :param matrix:  Data input. Either has row as student(matrix), or has row as items/criteria(needs to call transpose to
    re-format the data)
    :return: the list of index/position that is irregular
    """
    result = []
    # Set the boundary value for the number of irregular detection.
    # TODO: 这个range是取floor好还是ceil好。
    range_irregular = math.floor(math.log(len(matrix)))

    positions = [i for i in range(len(matrix))]
    potential_list = list(zip(similarities, positions))
    potential_list = sorted(potential_list, key=lambda x: x[0])
    # print(potential_list)
    # print(range_irregular)
    for i in potential_list[0:range_irregular]:
        # print("i is ::::: -> ",i, "RAnge of irregular: ", range_irregular)
        if i[0] < 0:  # 阈值。 之后要检改变。 当前implementation并没有应用cluster
            result.append(i[1])

    # average_sim = [(x + y) / 2 for (x, y) in zip(similarity1, similarity2)]
    # result = []
    # for i in range(len(average_sim)):
    #     if average_sim[i] < 0.5:
    #         result.append(i)
    return result


# Getter for correlations
# The INTERFACE exposed to the outside package.
### Notice that the second arg is a Bool, the thrid arg is a string
###
def return_correlation(original_data, is_student, flag):
    """
    Return the correlations of each column. This is the interface exposed to other modules.
    The input data is assumed to be sorted. If it is not, the following sorted matrix will sort the data input.
    :param original_data:   Original data.
    :param is_student:  A boolean value, specifying if the user wants the row/column detection.
    :return: A list of correlations of each item/column.
    """
    student_sum = sumStudentScore(original_data)
    print("Student sum is: ", student_sum)
    item_sum = sumItemScore(original_data)
    sorted_student = sortBasedOnStudent(original_data, student_sum)
    sorted_item = sortBasedOnItem(sorted_student, item_sum)

    matrix = sorted_item
    transpose = transpose_matrix(matrix)

    # Retrieve the correlation of columns, use transpose
    if not is_student:
        return retrieve_correlation_similarity(transpose, flag)
    elif is_student:
        return retrieve_correlation_similarity(matrix, flag)


# Getter for irregular columns
# The INTERFACE exposed to the outside package
# Student is a Bool.
def return_irregular_index(original_data, is_student, flag):
    """
    Return the index of irregular column/ row.
    :param original_data: The original data.
    :param is_student:  A boolean value, specifying if the user wants the row/column detection.
    :return:    A list of irregular pattern.
    """
    student_sum = sumStudentScore(original_data)
    item_sum = sumItemScore(original_data)
    # sorted_student = sortBasedOnStudent(original_data, student_sum)
    # sorted_item = sortBasedOnItem(sorted_student, item_sum)
    sorted_item = original_data

    # Orginal data is manipulated into either matrix(student as row) or transpose(criteria as row)
    matrix = sorted_item
    transpose = transpose_matrix(matrix)

    student_sum.sort()
    student_sum = list(reversed(student_sum))
    ave_per_student = retrieve_average_per_item(matrix, student_sum)

    if not is_student:
        columns_similarity = retrieve_correlation_similarity(transpose, flag)
        return detect_item_irregular(columns_similarity, transpose)
    elif is_student:
        student_similarity = retrieve_correlation_similarity(matrix, flag)
        return detect_item_irregular(student_similarity, matrix)


def irregular_box(matrix):
    if len(matrix[0]) < 2:
        return []
    section_qty = math.floor(math.sqrt(len(matrix[0])))
    box_max_height = math.floor(math.sqrt(len(matrix)))
    item_sum = sumItemScore(matrix)
    max_mark = [max([matrix[j][i] for j in range(len(matrix))]) for i in range(len(matrix[0]))]
    item_diff = [float(item_sum[i])/max_mark[i] - float(item_sum[i+1])/max_mark[i+1] for i in range(len(item_sum) - 1)]
    tuple_diff = [(item_diff[i], i) for i in range(len(item_diff))]
    tuple_diff.sort(reverse=True)
    selected_tuple = tuple_diff[:section_qty]
    selected_col = [i for _, i in selected_tuple]
    selected_col.append(-1)
    selected_col.append(len(matrix[0]) - 1)
    selected_col.sort()
    result = []
    for i in range(len(selected_col) - 1):
        best_dis = 1
        best_j_k = (-1, -1)
        col1, col2 = selected_col[i] + 1, selected_col[i + 1]
        for j in range(len(matrix)):
            for k in range(j, min(j + box_max_height, len(matrix))):
                box_sum = 0
                max_mark_sum = 0.01 + (k - j + 1) * sum(max_mark[col1: col2 + 1])
                for n in range(j, k + 1):
                    box_sum += sum(matrix[n][col1: col2 + 1])
                dis = abs((max_mark_sum - box_sum) / max_mark_sum - 0.5)
                if dis < best_dis:
                    best_dis = dis
                    best_j_k = (j, k)
        result.append((col1, col2, best_j_k))
    return result


def get_neighbours(radius):
    """
    the function is to return all coordinates in a cirle with radius = radius
    :param radius: radius of a circle (diamond)
    :return: an array contains all neighbours' coordinates
    """
    temp = []
    for i in range(0, radius + 1):
        for j in range(0, radius - i + 1):
            print((i, j))
            for k in [-1, 1]:
                for l in [-1, 1]:
                    temp.append((i * k, j * l))
    neighbours = list(dict.fromkeys(temp))
    while (0, 0) in neighbours:
        neighbours.remove((0, 0))
    return neighbours


def calculate_radius(array):
    """
    this function is to calculate radius according to an array's size
    :param array: a 2d array
    :return: radius that will be used in calculating neighbour values of a certain area
    """
    size = len(array) * len(array[0])
    radius = math.log(size) / 2
    return round(radius)


def odd_cells(matrix):
    """
    this function is to find anomalies in a 2d array
    :param matrix: a 2d array
    :param neighbours: neighbours of a particular cell, in order to calculate the cell's neighbours value
    :return: an array of sets of anomalies' coordinates
    """
    max_mark = []
    for i in range(0, len(matrix[0])):
        # assume the maximum mark of this task is 1
        max = 1
        for j in range(0, len(matrix)):
            if max < int(matrix[j][i]):
                max = int(matrix[j][i])
        max_mark.append(max)


    neighbours = get_neighbours(calculate_radius(matrix))
    cells = []
    threshold = 0.8
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            count_zeros = 0
            count_ones = 0
            total_neighbours = 0
            for (x, y) in neighbours:
                if 0 <= i + x < len(matrix) and 0 <= j + y < len(matrix[0]):
                    if matrix[i + x][j + y] == 0:
                        count_zeros += 1
                        total_neighbours += 1
                    else:
                        # substitute with count_ones += matrix[i + x][j + y] if scoring rate is chosen
                        count_ones += 1
                        total_neighbours += 1

            if matrix[i][j] == 0 and count_ones / total_neighbours > threshold:
                # print(count_ones, count_ones + count_zeros, i , j , x , y)
                print(i, j, count_zeros, count_ones, total_neighbours, matrix[4][2])
                cells.append((i, j))
            elif matrix[i][j] > 0 and count_zeros / total_neighbours > threshold:
                # print(i, j, count_zeros, count_ones, total_neighbours)
                cells.append((i, j))
    return cells
