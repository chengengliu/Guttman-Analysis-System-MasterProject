import unittest
import xlsxwriter
import model.excel_processing.ExcelOutput as ep
import model.file_importing as fi

class ExcelOutputTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.array = [['Excel', 'task1', 'task2', 'task3', 'task4'],
                      ['student1', 1, 2, 0, 1], ['student2', 0, 1, 0, 1], ['student3', 1, 1, 1, 0]]
        self.file_name = 'test.xlsx'
        self.excel = ep.ExcelOutput(self.array, self.file_name)

    def test_write_to_excel(self):
        ep.ExcelOutput.write_excel(self.excel)
        ep.ExcelOutput.close_workbook(self.excel)
        array = fi.readfile(self.file_name)
        self.assertTrue(array[1][1] == self.array[1][1])

    def test_add_total_score(self):
        ep.ExcelOutput.write_excel(self.excel)
        ep.ExcelOutput.add_total_score(self.excel)
        ep.ExcelOutput.close_workbook(self.excel)
        array = fi.readfile(self.file_name)
        array = fi.transpose(array)
        self.assertTrue(array[1][5] == 4)

    def test_add_correlation(self):
        ep.ExcelOutput.write_excel(self.excel)
        ep.ExcelOutput.add_total_score(self.excel)
        ep.ExcelOutput.add_correlation(self.excel, [5,5,5,5], 'row')
        ep.ExcelOutput.close_workbook(self.excel)
        array = fi.readfile(self.file_name)
        array = fi.transpose(array)
        self.assertTrue(array[1][6] == 5)
