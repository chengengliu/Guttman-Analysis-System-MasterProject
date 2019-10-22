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

    sumItemScore(matrix)
    transpose_matrix(matrix)

    The above mentioned functions can be skipped while you read the code.
'''

import copy
import math
import numpy
from numpy import dot
from numpy.linalg import norm


def clean_input(original_data):
    removed_header = original_data[2:]
    # print("Removed Header , ", removed_header)
    for i in range(len(removed_header)):
        removed_header[i] = removed_header[i][1:]
    # print(removed_header)
    return removed_header


def sum_item_score(matrix):
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


def detect_full_score(matrix):
    """
    The function assumes that the input data is splited already into small pieces of questions.
    So the full mark of each question should be 1. It now just aligns the dimension with the input data.
    :param matrix:  Input data.
    :return:    A matrix that is full of ones, which has the same dimension as the input matrix.
    """
    full_score = []
    for criteria in matrix:
        full_score.append(1)
    return full_score


# Receive a student matrix. Wants to accumulate the score rate accumulated matrix.
# Assume the input is cleaned and sorted. No more sorting needed.
def cal_scorerate_accumulated_matrix(matrix, is_student):
    transposed = transpose_matrix(matrix)

    accumulated_score = []
    scorerate_accumulated = []

    full_marks = detect_full_score(transposed)  # Full mark for each question.
    # print(full_marks)
    # if is_student:

    full_marks_accumulated = numpy.cumsum(full_marks).tolist()
    # print("This is the accumulated full marks, ", full_marks_accumulated)

    for i in range(len(matrix)):
        accumulated_score.append(numpy.cumsum(matrix[i]).tolist())
    # print("This is the accumulated score, ", accumulated_score)

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
            return True
    return False


def irregular_calculation(matrix, flag, is_student):
    scorerate = cal_scorerate_accumulated_matrix(matrix, is_student)

    zero_stddiv_accumulated_list = get_0staddv_index(scorerate)

    accumulation_result = []
    similarity_result = []
    correlation_result = []

    if zero_stddiv_accumulated_list:
        accumulation_0stddv_is_empty = False  # Exist 0 standard deviation accumulation data
    else:
        accumulation_0stddv_is_empty = True

    # Remove the element that contains zero standard deviation.
    matrix_copy = copy.deepcopy(matrix)
    for e in reversed(zero_stddiv_accumulated_list):
        matrix_copy.pop(e)

    scorerate = cal_scorerate_accumulated_matrix(matrix_copy, is_student)
    for i in range(len(matrix_copy)):
        similarity_result.append(irregular_cal(matrix_copy, i, 'Similarity', scorerate,
                                               zero_stddiv_accumulated_list, accumulation_0stddv_is_empty))
        accumulation_result.append(irregular_cal(matrix_copy, i, 'Accumulation', scorerate,
                                                 zero_stddiv_accumulated_list, accumulation_0stddv_is_empty))
        correlation_result.append(irregular_cal(matrix_copy, i, 'Correlation', scorerate,
                                                zero_stddiv_accumulated_list, accumulation_0stddv_is_empty))
    # Data needs to be put back.
    # The value is not full. There are values deleted.
    temp = [j for i in accumulation_result for j in i]
    for e in zero_stddiv_accumulated_list:
        temp.insert(e, 0.0)

    if flag == 'Correlation':
        return [j for i in correlation_result for j in i]
    elif flag == 'Accumulation':
        return temp
    elif flag == 'Similarity':
        return [j for i in similarity_result for j in i]


def return_irregular_index(original_data, is_student, flag):
    """
    Return the index of irregular column/ row.
    :param original_data: The original data.
    :param is_student:  A boolean value, specifying if the user wants the row/column detection.
    :return:    A list of irregular pattern.
    """
    sorted_item = original_data

    matrix = sorted_item
    transpose = transpose_matrix(matrix)

    if not is_student:
        columns_similarity = irregular_calculation(transpose, flag, is_student)
        return detect_item_irregular(columns_similarity, transpose)
    elif is_student:
        student_similarity = irregular_calculation(matrix, flag, is_student)
        return detect_item_irregular(student_similarity, matrix)


def irregular_cal(matrix, current_index, flag, scorerate, danger_accumulated_list, is_empty):
    correlation_result = []
    accumulation_correlation_result = []
    similarity_result = []
    range_correlation = math.floor(math.sqrt(len(matrix))) - 1

    temp_correlation = 0.0
    temp_accumulation_correlation = 0.0
    temp_similarity = 0.0
    calculation_counter = 0
    for i in range(range_correlation):
        if (current_index - i - 1) <= 0:
            try:
                temp_correlation_mid = numpy.corrcoef(matrix[current_index], matrix[current_index + i + 1])[0, 1]
                temp_accumulation_correlation_mid = \
                    numpy.corrcoef(scorerate[current_index], scorerate[current_index + i + 1])[0, 1]
                temp_similarity_mid = dot(matrix[current_index], matrix[current_index + i + 1]) / (
                        norm(matrix[current_index]) *
                        norm(matrix[current_index + i + 1]))

                temp_accumulation_correlation += temp_accumulation_correlation_mid
                temp_correlation += temp_correlation_mid
                temp_similarity += temp_similarity_mid
                calculation_counter += 1

            except:
                pass
        elif (current_index + i + i) >= (len(matrix) - 1):
            try:
                temp_correlation_mid = numpy.corrcoef(matrix[current_index], matrix[current_index - i - 1])[0, 1]
                temp_accumulation_correlation_mid = \
                    numpy.corrcoef(scorerate[current_index], scorerate[current_index - i - 1])[0, 1]
                temp_similarity_mid = dot(matrix[current_index], matrix[current_index - i - 1]) / (
                        norm(matrix[current_index]) *
                        norm(matrix[current_index - i - 1]))

                temp_accumulation_correlation += temp_accumulation_correlation_mid
                temp_correlation += temp_correlation_mid
                temp_similarity += temp_similarity_mid

                calculation_counter += 1

            except:
                pass
        else:
            try:
                temp_accumulation_correlation_mid = \
                    numpy.corrcoef(scorerate[current_index], scorerate[current_index - i - 1])[0, 1]
                temp_correlation_mid = numpy.corrcoef(matrix[current_index], matrix[current_index - i - 1])[0, 1]
                temp_similarity_mid = dot(matrix[current_index], matrix[current_index - i - 1]) / (
                        norm(matrix[current_index]) *
                        norm(matrix[current_index - i - 1]))

                temp_accumulation_correlation += temp_accumulation_correlation_mid
                temp_correlation += temp_correlation_mid
                temp_similarity += temp_similarity_mid

                calculation_counter += 1

            except:
                pass
            try:
                temp_correlation_mid = numpy.corrcoef(matrix[current_index], matrix[current_index + i + 1])[0, 1]
                temp_accumulation_correlation_mid = \
                    numpy.corrcoef(scorerate[current_index], scorerate[current_index + i + 1])[0, 1]
                temp_similarity_mid = dot(matrix[current_index], matrix[current_index + i + 1]) / (
                        norm(matrix[current_index]) *
                        norm(matrix[current_index + i + 1]))

                temp_accumulation_correlation += temp_accumulation_correlation_mid
                temp_correlation += temp_correlation_mid
                temp_similarity += temp_similarity_mid

                calculation_counter += 1

            except:
                pass

    correlation_result.append(temp_correlation / calculation_counter)
    accumulation_correlation_result.append(temp_accumulation_correlation / calculation_counter)
    similarity_result.append(temp_similarity / calculation_counter)

    if flag == 'Accumulation':
        return accumulation_correlation_result
    elif flag == 'Correlation':
        return correlation_result
    elif flag == 'Similarity':
        return similarity_result


def detect_item_irregular(similarities, matrix):
    """
    Detect if the column/item is irregular. If it is irregular, append its position to the list.
    If the average score of the two lists are smaller than 0.5(for now, I don't know how good the data will be, let's try 0.5 for now)
    This parameter will change as development goes.
    :param similarities:
    :return:
    :param similarity1: Similarity calculated between each column.
    :param matrix:  Data input. Either has row as student(matrix), or has row as items/criteria(needs to call transpose to
    re-format the data)
    :return: the list of index/position that is irregular
    """
    result = []
    # Set the boundary value for the number of irregular detection.
    range_irregular = math.floor(math.log(len(matrix)))

    positions = [i for i in range(len(matrix))]
    potential_list = list(zip(similarities, positions))
    potential_list = sorted(potential_list, key=lambda x: x[0])
    zero_result = []

    for i in potential_list[0:range_irregular]:
        if i[0] < 0.0:
            result.append(i[1])
    return result


# Getter for correlations
# The INTERFACE exposed to the outside package.
# Notice that the second arg is a Bool, the thrid arg is a string
#
def return_correlation(original_data, is_student, flag):
    """
    Return the correlations of each column. This is the interface exposed to other modules.
    The input data is assumed to be sorted. If it is not, the following sorted matrix will sort the data input.
    :param original_data:   Original data.
    :param is_student:  A boolean value, specifying if the user wants the row/column detection.
    :return: A list of correlations of each item/column.
    """
    sorted_item = original_data

    # Orginal data is manipulated into either matrix(student as row) or transpose(criteria as row)
    matrix = sorted_item
    transpose = transpose_matrix(matrix)

    # Retrieve the correlation of columns, use transpose
    if not is_student:
        return irregular_calculation(transpose, flag, is_student)
    elif is_student:
        return irregular_calculation(matrix, flag, is_student)


def irregular_box(matrix):
    if len(matrix[0]) < 2 or len(matrix) < 4:
        return []
    section_qty = min(math.floor(math.sqrt(len(matrix[0]))), 5)
    min_height = math.ceil(math.sqrt(len(matrix)))
    sample_height = math.ceil(math.log(len(matrix)))

    item_sum = sum_item_score(matrix)
    item_diff = [item_sum[i] - item_sum[i + 1] for i in range(len(item_sum) - 1)]
    tuple_diff = [(item_diff[i], i) for i in range(len(item_diff))]
    tuple_diff.sort(reverse=True)
    selected_tuple = tuple_diff[:section_qty - 1]
    selected_col = [i for _, i in selected_tuple]
    selected_col.append(-1)
    selected_col.append(len(matrix[0]) - 1)
    selected_col.sort()
    result = []
    for i in range(len(selected_col) - 1):
        best = 99999999
        best_j_k = (-1, -1)
        col1, col2 = selected_col[i] + 1, selected_col[i + 1]
        pre_box_sample_sum = sum([sum(row[col1: col2 + 1]) for row in matrix[:sample_height]])
        pre_box_sample_correct_rate = pre_box_sample_sum / (sample_height * (col2 - col1 + 1))
        post_box_sample_sum = sum([sum(row[col1: col2 + 1]) for row in matrix[-sample_height:]])
        post_box_sample_correct_rate = post_box_sample_sum / (sample_height * (col2 - col1 + 1))

        for j in [0] + list(range(math.ceil(min_height / 2), len(matrix))):
            pre_box_sum = 0
            for n in range(j):
                pre_box_sum += sum(matrix[n][col1: col2 + 1])
            pre_box_correct_rate = pre_box_sample_correct_rate if j == 0 \
                else pre_box_sum / (j * (col2 - col1 + 1))

            box_sum = -1
            post_box_sum = -1
            for k in range(j + min_height - 1, len(matrix)):
                if box_sum == -1:
                    box_sum, post_box_sum = 0, 0
                    for n in range(j, k + 1):
                        box_sum += sum(matrix[n][col1: col2 + 1])
                    for n in range(k + 1, len(matrix)):
                        post_box_sum += sum(matrix[n][col1: col2 + 1])
                else:
                    edge_row_sum = sum(matrix[k][col1: col2 + 1])
                    box_sum += edge_row_sum
                    post_box_sum -= edge_row_sum
                box_correct_rate = box_sum / ((k - j + 1) * (col2 - col1 + 1))

                post_box_correct_rate = post_box_sample_correct_rate if k + 1 == len(matrix) \
                    else post_box_sum / ((len(matrix) - k - 1) * (col2 - col1 + 1))

                dis = 2 + (abs(box_correct_rate - 0.5) ** 2) * 3 - \
                    (abs(pre_box_correct_rate - box_correct_rate) ** 2) - \
                    (abs(post_box_correct_rate - box_correct_rate) ** 2)

                dis *= 1 + (k - j) / (len(matrix) ** 1.5) if abs(box_correct_rate - 0.5) < 0.4 \
                    else 10 - (k - j) / (len(matrix) ** 1.5)

                if dis < best:
                    best = dis
                    best_j_k = (j, k)
        result.append((col1, col2, best_j_k))
    # print("BOXES: ", result)
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
            # print((i, j))
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
    return round(radius) + 1


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
    threshold = 0.90
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
                cells.append((i, j))
            elif matrix[i][j] > 0 and count_zeros / total_neighbours > threshold:
                cells.append((i, j))
    return cells
