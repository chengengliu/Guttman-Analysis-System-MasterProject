import sys
sys.path.append("..")
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

file = importFile('test.xlsx')
array = importFile.readfile(file)
# array's column and row are flipped, use transpose function to make it correct
newarray = importFile.transpose(file, array)
print(newarray)
importFile.sort2darray(file, newarray)
for i in newarray:
    print(i)
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