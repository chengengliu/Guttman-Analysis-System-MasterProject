import xlsxwriter
import math

class ExcelOutput:
    def __init__(self, file_name):
        self.arrays = []

        self.workbook = xlsxwriter.Workbook(file_name)

        self.worksheet1 = self.workbook.add_worksheet("Irregular Items")
        self.worksheet2 = self.workbook.add_worksheet("Other Patterns")
        self.worksheets = [self.worksheet1, self.worksheet2]
        self.formats = []
        self.formats.append([])
        self.formats.append([])
        self.base_format = {
            'font_name': 'Times New Roman',
            'align': 'center',
            'valign': 'vcenter'
        }

    def add_array(self, array):
        self.arrays.append(array)

    def write_excel(self, sheet_number):
        """
        # write data to excel file
        :return: null
        """
        for i in range(len(self.arrays[sheet_number])):
            self.formats[sheet_number].append([])
            for j in range(len(self.arrays[sheet_number][0])):
                cell_format = self.workbook.add_format(self.base_format)
                if type(self.arrays[sheet_number][i][j]).__name__ == 'int' and self.arrays[sheet_number][i][j] > 0:
                    cell_format.set_bg_color('#ff5050')
                self.formats[sheet_number][i].append(cell_format)
                self.worksheets[sheet_number].write(i, j, self.arrays[sheet_number][i][j], self.formats[sheet_number][i][j])

    def add_total_score(self, sheet_number):
        """
        # add total score at the end of each row and column
        :return: null
        """
        cell_format = self.workbook.add_format(self.base_format)
        # cell_format.set_bg_color('yellow')
        # total score of rows
        self.worksheets[sheet_number].write(0, len(self.arrays[sheet_number][0]), 'total score', cell_format)
        self.worksheets[sheet_number].write(len(self.arrays[sheet_number]), 0, 'total score', cell_format)
        for i in range(2, len(self.arrays[sheet_number])):
            count = 0
            for j in range(1, len(self.arrays[sheet_number][0])):
                count += self.arrays[sheet_number][i][j]
            self.worksheets[sheet_number].write(i, len(self.arrays[sheet_number][0]), count, cell_format)
        # total score of columns
        for i in range(1, len(self.arrays[sheet_number][0])):
            count = 0
            for j in range(2, len(self.arrays[sheet_number])):
                count += self.arrays[sheet_number][j][i]
            self.worksheets[sheet_number].write(len(self.arrays[sheet_number]), i, count, cell_format)

    def add_correlation(self, array, types, sheet_number):
        """
        # add correlation, input type is 1D array
        :param array: 1d array, containing correlation information
        :param types: a string, either 'row' or 'column'
        :return: null
        """
        cell_format = self.workbook.add_format(self.base_format)
        # cell_format.set_bg_color('yellow')
        if types == 'row':
            self.worksheets[sheet_number].write(1, len(self.arrays[sheet_number][0]) + 1, 'correlation', cell_format)
            for i in range(2, len(self.arrays[sheet_number])):
                self.worksheets[sheet_number].write(i, len(self.arrays[sheet_number][0]) + 1, array[i - 1], cell_format)
        if types == 'column':
            self.worksheets[sheet_number].write(len(self.arrays[sheet_number]) + 1, 0, 'item_performance', cell_format)
            for i in range(1, len(array) + 1):
                # print(len(self.array[0]))
                # print(len(array))
                # print(array[i - 1])
                if math.isnan(array[i - 1]):
                    self.worksheets[sheet_number].write(len(self.arrays[sheet_number]) + 1, i, "nan", cell_format)
                else:
                    self.worksheets[sheet_number].write(len(self.arrays[sheet_number]) + 1, i, array[i - 1], cell_format)

    def highlight_area(self, row1, row2, col1, col2, color, sheet_number):
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
                self.formats[sheet_number][i][j].set_bg_color(color)
                self.worksheets[sheet_number].write(i, j, self.arrays[sheet_number][i][j], self.formats[sheet_number][i][j])

    def add_border(self, row1, row2, col1, col2, sheet_number):
        border_style = 2  # bold border
        for i in range(col1, col2 + 1):
            self.formats[sheet_number][row1][i].set_top(border_style)
            self.worksheets[sheet_number].write(row1, i, self.arrays[sheet_number][row1][i], self.formats[sheet_number][row1][i])
            self.formats[sheet_number][row2][i].set_bottom(border_style)
            self.worksheets[sheet_number].write(row2, i, self.arrays[sheet_number][row2][i], self.formats[sheet_number][row2][i])
        for i in range(row1, row2 + 1):
            self.formats[sheet_number][i][col1].set_left(border_style)
            self.worksheets[sheet_number].write(i, col1, self.arrays[sheet_number][i][col1], self.formats[sheet_number][i][col1])
            self.formats[sheet_number][i][col2].set_right(border_style)
            self.worksheets[sheet_number].write(i, col2, self.arrays[sheet_number][i][col2], self.formats[sheet_number][i][col2])

    def close_workbook(self):
        """
        # close workbook to output the excel file
        :return: null
        """
        self.workbook.close()
