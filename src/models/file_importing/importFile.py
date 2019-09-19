import sys
sys.path.append("..")
import math
import pandas as pd
from pandas import DataFrame
from src.models.excel_processing.exceloutput import exceloutput


class importFile:
    def __init__(self, fileName):
        self.fileName = fileName


    def readfile(self):
        """
        # read an excel file and store it in a 2d array
        :return: a 2d array containing all information from that excel file
        """
        df = pd.read_excel (open(self.fileName, 'rb'))
        dict = df.to_dict(orient='dict')
        array = []
        for key in dict.keys():
            temparray = []
            temparray.append(str(key))
            for index in dict[key]:
                temparray.append(dict[key][index])
            array.append(temparray)
        # nrow + 1 includes header
        return array


    def transpose(self, array):
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


    def sort2darray(self,array):
        """
        # sort the imported excel file as 2d array
        :param array: a 2d array
        :return: a sorted 2d array, sort from left to right and also from top to bottom
        """
        #header = array.pop(0)
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
            for j in range(1, len(array[0]) -1 - i):
                count1 = 0
                count2 = 0
                for k in range(1, len(array) - 1):
                    count1 += int(array[k][j])
                    count2 += int(array[k][j+1])
                if count1 < count2:
                    for k in range(len(array)):
                        array[k][j], array[k][j+1] = array[k][j+1], array[k][j]
        return array

    def get_neighbours(self, radius):
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

    def calculate_radius(self, array):
        """
        this function is to calculate radius according to an array's size
        :param array: a 2d array
        :return: radius that will be used in calculating neighbour values of a certain area
        """
        size = len(array) * len(array[0])
        radius = math.log(size) / 2
        return round(radius)

    def odd_cells(self, matrix, neighbours):
        """
        this function is to find anomalies in a 2d array
        :param matrix: a 2d array
        :param neighbours: neighbours of a particular cell, in order to calculate the cell's neighbours value
        :return: an array of sets of anomalies' coordinates
        """
        cells = []
        threshold = 0.8
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                count_zeros = 0
                count_ones = 0
                total_neighbours = 0
                for (x, y) in neighbours:
                    if i + x > 0 and i + x < len(matrix) and j + y > 0 and j + y < len(matrix[0]):
                        total_neighbours += 1
                        if matrix[i + x][j + y] == 0:
                            count_zeros += 1
                        else:
                            count_ones += 1
                if matrix[i][j] == 0 and count_ones / total_neighbours > threshold:
                    cells.append((i, j))
                elif matrix[i][j] > 0 and count_zeros / total_neighbours > threshold:
                    cells.append((i, j))
        return cells

file = importFile('test.xlsx')
array = importFile.readfile(file)
# array's column and row are flipped, use transpose function to make it correct
newarray = importFile.transpose(file, array)
newarray = importFile.sort2darray(file, newarray)
"""
calculate corresponding radius based on the size of a 2d array
"""
radius = importFile.calculate_radius(file, newarray)
"""
get neighbour coordinates of a particular cell
"""
neighbours = importFile.get_neighbours(file,radius)
"""
find anomalies in that 2d array
"""
cells = importFile.odd_cells(file, newarray, neighbours)

"""
create an instance of exceloutput class
"""
excel = exceloutput(newarray)
"""
write 2d array data to
"""
exceloutput.writetoExcel(excel)
"""
highlight anomaly area by painting the background color
"""
exceloutput.highlightarea(excel, 2, 4, 2, 4)
"""
store total score of each row and column to the excel file, note it's not to the array
"""
exceloutput.addtotalscore(excel)
"""
correlation values should be received from Victor's module
"""
correlation1 = [1,2,3,4,5,6,7,8,9,10,11]
correlation2 = [1,2,3,4,5,6,7,8]
"""
store correlation values to the excel, note it's not to array
"""
exceloutput.addcorrelation(excel, correlation1, 'row')
exceloutput.addcorrelation(excel,correlation2, 'column')
exceloutput.addborder(excel,2,4,2,4)
#####################################################################################
#the following function is crucial, it's the only way to close the file and export it
#####################################################################################
exceloutput.closeWorkbook(excel)