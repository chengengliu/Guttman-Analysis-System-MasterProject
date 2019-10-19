import math

import pandas as pd
import numpy as np


def sort_2d_array_mark(array):
    """
    # sort the imported excel file as 2d array according to marks of tasks
    :param array: a 2d array
    :return: a sorted 2d array, sort from left to right and also from top to bottom
    """
    # header = array.pop(0)
    # sort rows
    for i in range(2, len(array)):
        for j in range(i, len(array)):
            count1 = 0
            count2 = 0
            for k in range(1, len(array[0])):
                count1 += int(array[i][k])
                count2 += int(array[j][k])
            if count1 < count2:
                array[j], array[i] = array[i], array[j]
    # sort columns
    for i in range(1, len(array[0]) - 1):
        for j in range(1, len(array[0]) - i):
            count1 = 0
            count2 = 0
            for k in range(2, len(array) - 1):
                count1 += int(array[k][j])
                count2 += int(array[k][j + 1])
            if count1 < count2:
                for k in range(len(array)):
                    array[k][j], array[k][j+1] = array[k][j+1], array[k][j]
    # print("Test soring result: ")
    # for i in array:
    #     print(i)
#
# def sort_2d_array_max_mark(array):
#     """
#     # sort the imported excel file as 2d array according to Scoring rate
#     :param array: a 2d array
#     :return: a sorted 2d array, sort from left to right and also from top to bottom
#     """
#     max_mark = []
#     max_mark.append(0)
#     for i in range(1, len(array[0])):
#         # assume the maximum mark of this task is 1
#         max = 1
#         for j in range(1, len(array)):
#             if max < int(array[j][i]):
#                 max = int(array[j][i])
#         max_mark.append(max)
#
#     # header = array.pop(0)
#     for i in range(1, len(array)):
#         for j in range(1, len(array) - i):
#             count1 = 0.0
#             count2 = 0.0
#             for k in range(1, len(array[0])):
#                 count1 += int(array[j][k])
#                 count2 += int(array[j+1][k])
#             if count1 < count2:
#                 array[j], array[j+1] = array[j+1], array[j]
#
#     for i in range(1, len(array[0]) - 1):
#         for j in range(1, len(array[0]) - i):
#             count1 = 0.0
#             count2 = 0.0
#             for k in range(1, len(array) - 1):
#                 count1 += float(int(array[k][j])/max_mark[j])
#                 count2 += float(int(array[k][j+1])/max_mark[j+1])
#             if count1 < count2:
#                 for k in range(len(array)):
#                     array[k][j], array[k][j+1] = array[k][j+1], array[k][j]

def break_down_marks(array, index):
    indexs = []
    for i in range(1, len(array[0])):
        count = 0
        for string in index[0]:
            if string[:3] == str(array[0][i]):
                count += 1
        indexs.append(count)

    new_array = []
    new_array.append(index[1])
    new_array.append(index[0])

    for row in range(1, len(array)):
        tmp = []
        for column in range(1, len(array[0])):
            for i in range(indexs[column - 1]):
                if array[row][column] > 0:
                    tmp.append(1)
                    array[row][column] -= 1
                else:
                    tmp.append(0)
                    array[row][column] -= 1
        # print(tmp)
        new_array.append(tmp)
    # new_array[1][0] = "student_id"
    new_array[0].insert(0, "")
    for i in range(len(array)):
        new_array[i + 1].insert(0, array[i][0])
    return new_array

def non_int_detect(matrix):

    for item in matrix:
        for i in range(len(item)):
            if not isinstance(item[i], int):
                raise Exception('Found non-integer value. Found in data:', item[i])

def transpose(array):
    """
    # transpose the array
    :param array: 2d array
    :return: transposed 2d array
    """
    temp = [[0 for x in range(len(array))] for y in (range(len(array[0])))]
    for i in range(len(array)):
        for j in range(len(array[i])):
            temp[j][i] = array[i][j]
    return temp


def readfile(file_name):
    """
    # read an excel file and store it in a 2d array
    :return: a 2d array containing all information from that excel file
    """
    xls = pd.ExcelFile(file_name)
    sheet_names = xls.sheet_names
    # if there is no se
    if len(sheet_names) < 2:
        raise Exception('Excel file has less than 2 work sheets')

    df1 = pd.read_excel(xls, sheet_names[0])

    excel_dict1 = df1.to_dict(orient='dict')

    array1 = []
    for key in excel_dict1.keys():
        temp_array1 = []
        for index in excel_dict1[key]:
            temp_array1.append(excel_dict1[key][index])

        array1.append(temp_array1)
    for i in range(len(array1[0])):
        array1[0][i] = str(array1[0][i])

    fst_row_int_cnt, snd_row_int_cnt = 0, 0
    item_name = []
    for i in range(1, len(array1)):
        if isinstance(array1[i][0], (float, int)) and int(math.floor(array1[i][0])) == array1[i][0]:
            snd_row_int_cnt += 1
        item_name.append(array1[i][0])
        for j in range(1, len(array1[0])):
            if not isinstance(array1[i][j], (float, int)) or \
                    math.isnan(array1[i][j]) or \
                    int(math.floor(array1[i][j])) != array1[i][j]:
                raise Exception("Mark data should present starting from B3, non-integer value detected.")
    if snd_row_int_cnt == len(array1) - 1:
        raise Exception("Second row should be item names, digit value detected.")
    if len(item_name) != len(set(item_name)):
        raise Exception("Duplicate item name detected.")
    if len(array1[0][1:]) != len(set(array1[0][1:])):
        raise Exception("Duplicate student name detected.")

    array2 = []
    column_of_second_sheet = 0

    df2 = pd.read_excel(xls, sheet_names[1])
    excel_dict2 = df2.to_dict(orient='dict')
    for key in excel_dict2.keys():
        temp_array2 = []
        for index in excel_dict2[key]:
            temp_array2.append(excel_dict2[key][index])
        column_of_second_sheet += 1
        array2.append(temp_array2)

    return array1, array2

    # with open(file_name, 'rb') as f:
    #     df1 = pd.read_excel(f)
    #     excel_dict1 = df1.to_dict(orient='dict')
    #     array1 = []
    #     for key in excel_dict1.keys():
    #         temp_array = [str(key)]
    #         for index in excel_dict1[key]:
    #             temp_array.append(excel_dict1[key][index])
    #         array1.append(temp_array)
    #     for i in range(len(array1[0])):
    #         array1[0][i] = str(array1[0][i])
    # return array1
