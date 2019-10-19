import xlsxwriter
import math

class ExcelOutput:
    def __init__(self, array, file_name):
        self.array = array
        self.workbook = xlsxwriter.Workbook(file_name)
        self.worksheet = self.workbook.add_worksheet()
        self.formats = []
        self.base_format = {
            'font_name': 'Times New Roman',
            'align': 'center',
            'valign': 'vcenter'
        }

    def write_excel(self):
        """
        # write data to excel file
        :return: null
        """
        for i in range(len(self.array)):
            self.formats.append([])
            for j in range(len(self.array[0])):
                cell_format = self.workbook.add_format(self.base_format)
                if type(self.array[i][j]).__name__ == 'int' and self.array[i][j] > 0:
                    cell_format.set_bg_color('#ffd5d5')
                self.formats[i].append(cell_format)
                self.worksheet.write(i, j, self.array[i][j], self.formats[i][j])

    def add_total_score(self):
        """
        # add total score at the end of each row and column
        :return: null
        """
        cell_format = self.workbook.add_format(self.base_format)
        # cell_format.set_bg_color('yellow')
        # total score of rows
        self.worksheet.write(0, len(self.array[0]), 'total score', cell_format)
        self.worksheet.write(len(self.array), 0, 'total score', cell_format)
        for i in range(2, len(self.array)):
            count = 0
            for j in range(1, len(self.array[0])):
                count += self.array[i][j]
            self.worksheet.write(i, len(self.array[0]), count, cell_format)
        # total score of columns
        for i in range(1, len(self.array[0])):
            count = 0
            for j in range(2, len(self.array)):
                count += self.array[j][i]
            self.worksheet.write(len(self.array), i, count, cell_format)

    def add_correlation(self, array, types):
        """
        # add correlation, input type is 1D array
        :param array: 1d array, containing correlation information
        :param types: a string, either 'row' or 'column'
        :return: null
        """
        cell_format = self.workbook.add_format(self.base_format)
        # cell_format.set_bg_color('yellow')
        if types == 'row':
            self.worksheet.write(1, len(self.array[0]) + 1, 'correlation', cell_format)
            for i in range(2, len(self.array)):
                self.worksheet.write(i, len(self.array[0]) + 1, array[i - 1], cell_format)
        if types == 'column':
            self.worksheet.write(len(self.array) + 1, 0, 'item_performance', cell_format)
            for i in range(1, len(array) + 1):
                # print(len(self.array[0]))
                # print(len(array))
                # print(array[i - 1])
                if math.isnan(array[i - 1]):
                    self.worksheet.write(len(self.array) + 1, i, "nan", cell_format)
                else:
                    self.worksheet.write(len(self.array) + 1, i, array[i - 1], cell_format)

    def highlight_area(self, row1, row2, col1, col2, color):
        """
        # highlight blocks in excel file
        :param row1: index of the first row
        :param row2: index of the second row
        :param col1: index of the first column
        :param col2: index of the second column
        :param color: text color
        :return: null
        """
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.formats[i][j].set_bg_color(color)
                self.worksheet.write(i, j, self.array[i][j], self.formats[i][j])

    def add_border(self, row1, row2, col1, col2):
        border_style = 2  # bold border
        for i in range(col1, col2 + 1):
            self.formats[row1][i].set_top(border_style)
            self.worksheet.write(row1, i, self.array[row1][i], self.formats[row1][i])
            self.formats[row2][i].set_bottom(border_style)
            self.worksheet.write(row2, i, self.array[row2][i], self.formats[row2][i])
        for i in range(row1, row2 + 1):
            self.formats[i][col1].set_left(border_style)
            self.worksheet.write(i, col1, self.array[i][col1], self.formats[i][col1])
            self.formats[i][col2].set_right(border_style)
            self.worksheet.write(i, col2, self.array[i][col2], self.formats[i][col2])

    def close_workbook(self):
        """
        # close workbook to output the excel file
        :return: null
        """
        self.workbook.close()
