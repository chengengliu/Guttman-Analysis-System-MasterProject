import unittest
import model.file_importing as fi


class FileImportTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.path = "/Users/Apple/Documents/Google-Sync/SWEN90014 Master Project/Project/swen90014-2019-rv-quoll/testdata/SampleAssessmentResult.xlsx"
        self.data = fi.readfile(self.path)
        self.array = [['test', 'task1', 'task2'], ['student1', 1, 2], ['student2', 3, 4]]

    def test_read_file(self):
        array = fi.readfile(self.path)
        self.assertTrue(array[0][1][1]==1.0)

    def test_transpose(self):
        array = self.array
        array = fi.transpose(array)
        self.assertTrue(array[1][2] == 3)

    def test_sort_2d_array(self):
        fi.sort_2d_array_mark(self.array)
        print(self.array)
        self.assertTrue(self.array[2][2] == 4)
