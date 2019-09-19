import xlsxwriter

class exceloutput:
    def __init__(self, array):
        self.array = array
        self.workbook = xlsxwriter.Workbook('output.xlsx')
        self.worksheet = self.workbook.add_worksheet()
        self.count = 0
        self.cell_format = self.workbook.add_format({'bold': True})


    def writetoExcel(self):
        """
        # write data to excel file
        :return: null
        """
        for i in range(len(self.array)):
            for j in range(len(self.array[0])):
                self.worksheet.write(i, j, self.array[i][j])


    def addtotalscore(self):
        """
        # add total score at the end of each row and column
        :return: null
        """
        cell_format = self.workbook.add_format({'bold': True})
        # total score of rows
        self.worksheet.write(0, len(self.array[0]), 'total score', cell_format)
        self.worksheet.write(len(self.array), 0, 'total score', cell_format)
        for i in range(1, len(self.array)):
            count = 0
            for j in range(1, len(self.array[0])):
                count += self.array[i][j]
            self.worksheet.write(i, len(self.array[0]), count, cell_format)
        # total score of columns
        for i in range(1, len(self.array[0])):
            count = 0
            for j in range(1, len(self.array)):
                count += self.array[j][i]
            self.worksheet.write(len(self.array), i, count, cell_format)


    def addcorrelation(self, array, types):
        """
        # add correlation, input type is 1D array
        :param array: 1d array, containing correlation information
        :param types: a string, either 'row' or 'column'
        :return: null
        """
        cell_format = self.workbook.add_format({'bold': True})
        if types == 'row':
            self.worksheet.write(0, len(self.array[0]) + 1, 'correlation', cell_format)
            for i in range(1, len(self.array)):
                self.worksheet.write(i, len(self.array[0])+1, array[i-1], cell_format)
        if types == 'column':
            self.worksheet.write(len(self.array) + 1, 0, 'correlation', cell_format)
            for i in range(1, len(self.array[0])):
                self.worksheet.write(len(self.array)+1, i, array[i-1], cell_format)


    def highlightarea(self, row1, row2, column1, column2):
        """
        # highlight blocks in excel file
        :param row1: index of the first row
        :param row2: index of the second row
        :param column1: index of the first column
        :param column2: index of the second column
        :return: null
        """

        self.setColor()
        for i in range(row1, row2):
            for j in range(column1, column2):
                self.worksheet.write(i, j, self.array[i][j], self.cell_format)

    def addborder(self, row1, row2, column1, column2):
        left_border = self.workbook.add_format({"left": 1})
        right_border = self.workbook.add_format({"right": 1})
        top_border = self.workbook.add_format({"top": 1})
        bottom_border = self.workbook.add_format({"bottom": 1})
        top_left_border = self.workbook.add_format({"left": 1,"top": 1})
        top_right_border = self.workbook.add_format({"right": 1,"top": 1})
        bottom_left_border = self.workbook.add_format({"bottom": 1, "left": 1})
        bottom_right_border = self.workbook.add_format({"bottom": 1, "right": 1})
        for i in range(column1, column2):
            self.worksheet.write(row1, i, self.array[row1][i], top_border)
        for i in range(column1, column2):
            self.worksheet.write(row2, i, self.array[row1][i], bottom_border)
        for i in range(row1, row2):
            self.worksheet.write(i, column1, self.array[row1][i], left_border)
        for i in range(row1, row2):
            self.worksheet.write(i, column2, self.array[row1][i], right_border)
        self.worksheet.write(row1, column1, self.array[row1][column1], top_left_border)
        self.worksheet.write(row1, column2, self.array[row1][column2], top_right_border)
        self.worksheet.write(row2, column1, self.array[row2][column1], bottom_left_border)
        self.worksheet.write(row2, column2, self.array[row2][column2], bottom_right_border)


    def setColor(self):
        """
        # set color from a color list for highlighting excel blocks.
        :return: null
        """
        colors = ['blue', 'brown', 'cyan', 'green', 'gray', 'lime', 'magenta', 'navy', 'orange', 'pink', 'purple',
                  'red', 'silver', 'white', 'yellow']
        self.count += 1
        self.cell_format.set_color(colors[self.count])


    def closeWorkbook(self):
        """
        # close workbook to output the excel file
        :return: null
        """
        self.workbook.close()