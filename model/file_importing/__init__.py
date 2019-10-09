import pandas as pd


def sort_2d_array_mark(array):
    """
    # sort the imported excel file as 2d array according to marks of tasks
    :param array: a 2d array
    :return: a sorted 2d array, sort from left to right and also from top to bottom
    """
    # header = array.pop(0)
    for i in range(1, len(array)):
        for j in range(1, len(array) - i):
            count1 = 0
            count2 = 0
            for k in range(1, len(array[0])):
                count1 += int(array[j][k])
                count2 += int(array[j+1][k])
            if count1 < count2:
                array[j], array[j+1] = array[j+1], array[j]

    for i in range(1, len(array[0]) - 1):
        for j in range(1, len(array[0]) - i):
            count1 = 0
            count2 = 0
            for k in range(1, len(array) - 1):
                count1 += int(array[k][j])
                count2 += int(array[k][j+1])
            if count1 < count2:
                for k in range(len(array)):
                    array[k][j], array[k][j+1] = array[k][j+1], array[k][j]

def sort_2d_array_max_mark(array):
    """
    # sort the imported excel file as 2d array according to Scoring rate
    :param array: a 2d array
    :return: a sorted 2d array, sort from left to right and also from top to bottom
    """
    max_mark = []
    max_mark.append(0)
    for i in range(1, len(array[0])):
        # assume the maximum mark of this task is 1
        max = 1
        for j in range(1, len(array)):
            if max < int(array[j][i]):
                max = int(array[j][i])
        max_mark.append(max)

    # header = array.pop(0)
    for i in range(1, len(array)):
        for j in range(1, len(array) - i):
            count1 = 0.0
            count2 = 0.0
            for k in range(1, len(array[0])):
                count1 += int(array[j][k])
                count2 += int(array[j+1][k])
            if count1 < count2:
                array[j], array[j+1] = array[j+1], array[j]

    for i in range(1, len(array[0]) - 1):
        for j in range(1, len(array[0]) - i):
            count1 = 0.0
            count2 = 0.0
            for k in range(1, len(array) - 1):
                count1 += float(int(array[k][j])/max_mark[j])
                count2 += float(int(array[k][j+1])/max_mark[j+1])
            if count1 < count2:
                for k in range(len(array)):
                    array[k][j], array[k][j+1] = array[k][j+1], array[k][j]


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
    with open(file_name, 'rb') as f:
        df = pd.read_excel(f)
        excel_dict = df.to_dict(orient='dict')
        array = []
        for key in excel_dict.keys():
            temp_array = [str(key)]
            for index in excel_dict[key]:
                temp_array.append(excel_dict[key][index])
            array.append(temp_array)
        for i in range(len(array[0])):
            array[0][i] = str(array[0][i])
    return array
