import math
import textdistance
import pandas as pd


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
                    array[k][j], array[k][j + 1] = array[k][j + 1], array[k][j]


def break_down_marks(array, index):
    indexs = []

    for i in range(1, len(array[0])):
        count = 0
        for string in index[0]:
            if textdistance.hamming.normalized_similarity(string, str(array[0][i])) >= 0.5:
                count += 1
        indexs.append(count)

    transposed_array = transpose(array)

    max_mark = []
    for i in range(1, len(transposed_array)):
        # assume the maximum mark of this task is 1
        max_mark.append(int(max(transposed_array[i][2:])))

    for i in range(len(indexs)):
        if indexs[i] < max_mark[i]:
            raise Exception("the max mark of this task is greater than its total sub-criteria")

    new_array = [index[1], index[0]]

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

    if len(sheet_names) < 2:
        raise Exception('Excel file has less than 2 work sheets')

    df1 = pd.read_excel(xls, sheet_names[0])

    excel_dict1 = df1.to_dict(orient='dict')

    array1 = []
    # read the first worksheet
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
                    math.isnan(array1[i][j]) or array1[i][j] < 0 or \
                    int(math.floor(array1[i][j])) != array1[i][j]:
                raise Exception("Mark data should present starting from B3, non-integer or negative value detected.")
    if snd_row_int_cnt == len(array1) - 1:
        raise Exception("Second row should be item names, digit value detected.")
    if len(item_name) != len(set(item_name)):
        raise Exception("Duplicate item name detected.")
    if len(array1[0][1:]) != len(set(array1[0][1:])):
        raise Exception("Duplicate student name detected.")

    array2 = []

    df2 = pd.read_excel(xls, sheet_names[1])
    excel_dict2 = df2.to_dict(orient='dict')

    for key in excel_dict2.keys():
        temp_array2 = []
        for index in excel_dict2[key]:
            temp_array2.append(excel_dict2[key][index])
        array2.append(temp_array2)

    # exam if the criteria is listed in order
    previous = ""
    for i in range(len(array2[0])):
        if previous > array2[0][i]:
            raise Exception("the criteria in worksheet 2 is not listed in order")
        previous = array2[0][i]
    return array1, array2
