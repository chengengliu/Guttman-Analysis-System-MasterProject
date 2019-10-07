import unittest
import model.file_importing as fi


class FileImportTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.data = fi.readfile("./testdata/SampleAssessmentResult.xlsx")
        self.array = [['test', 'task1', 'task2'], ['student1', 1, 2], ['student2', 3, 4]]

    def test_read_file(self):
        array = fi.readfile("./testdata/SampleAssessmentResult.xlsx")
        self.assertTrue(array[4][3] == 0)

    def test_transpose(self):
        array = self.array
        array = fi.transpose(array)
        self.assertTrue(array[1][2] == 3)

    def test_sort_2d_array(self):
        array = self.array
        fi.sort_2d_array(array)
        self.assertTrue(array[1][1] == 4)
