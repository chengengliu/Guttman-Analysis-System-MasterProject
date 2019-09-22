import unittest
import model.guttman_analysis as ad
import model.file_importing as fi


class GuttmanAnalysisTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.data = fi.readfile("./testdata/SampleAssessmentResult.xlsx")
        self.data = fi.transpose(self.data)
        fi.sort_2d_array(self.data)

        self.data_should_be = [[3, 2, 3, 2, 0, 2, 2], [3, 2, 3, 2, 0, 2, 2],
                               [3, 2, 3, 2, 0, 2, 2], [3, 2, 3, 1, 0, 2, 2],
                               [3, 2, 3, 2, 0, 2, 0], [3, 2, 2, 1, 2, 0, 0],
                               [3, 2, 2, 1, 2, 0, 0], [3, 2, 2, 1, 0, 2, 0],
                               [1, 2, 3, 2, 0, 0, 2], [3, 2, 0, 0, 1, 1, 2],
                               [3, 2, 1, 1, 2, 0, 0], [3, 2, 1, 1, 2, 0, 0],
                               [3, 2, 1, 1, 1, 1, 0], [3, 2, 2, 1, 1, 0, 0],
                               [3, 0, 2, 1, 2, 0, 0], [3, 2, 1, 1, 1, 0, 0],
                               [3, 2, 0, 1, 1, 1, 0], [3, 2, 2, 1, 0, 0, 0],
                               [3, 2, 2, 1, 0, 0, 0], [3, 2, 1, 1, 1, 0, 0],
                               [3, 1, 2, 1, 1, 0, 0], [3, 2, 1, 1, 1, 0, 0],
                               [1, 1, 2, 1, 1, 1, 0], [3, 2, 1, 1, 0, 0, 0],
                               [0, 2, 3, 1, 1, 0, 0], [3, 2, 1, 1, 0, 0, 0],
                               [0, 2, 3, 1, 1, 0, 0], [3, 1, 0, 1, 1, 0, 0],
                               [0, 1, 2, 2, 1, 0, 0], [0, 2, 1, 1, 2, 0, 0],
                               [1, 1, 1, 1, 1, 0, 0], [3, 2, 0, 0, 0, 0, 0],
                               [3, 2, 0, 0, 0, 0, 0], [3, 1, 1, 0, 0, 0, 0],
                               [1, 2, 1, 1, 0, 0, 0], [0, 2, 1, 1, 0, 0, 0],
                               [0, 1, 0, 1, 1, 1, 0], [3, 0, 0, 0, 0, 0, 0],
                               [0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0]]

        self.data_first_row_zero = ad.clean_input(self.data)
        # Manipulate the data so that the first element in the list has zero standard deviation.
        self.data_first_row_zero[0] = [0, 0, 0, 0, 0, 0, 0]
        # transposed data
        self.data_trans = ad.transpose_matrix(self.data)

    def test_get_0staddv_index(self):
        self.assertTrue(ad.get_0staddv_index(self.data_first_row_zero) == [0])

    def test_in_danger_list(self):
        self.assertTrue(ad.in_danger_list(ad.get_0staddv_index(self.data_first_row_zero), 0))

    def test_data_clean(self):
        data_cleaned = ad.clean_input(self.data)
        self.assertTrue(data_cleaned == self.data_should_be)

    def test_detectDimension(self):
        dimension_should_be = (len(self.data), len(self.data[0]))
        self.assertTrue(ad.detectDimenstion(self.data) == dimension_should_be)

    def test_transpose_matrix(self):
        self.assertTrue(self.data == ad.transpose_matrix(ad.transpose_matrix(self.data)))

    # The following test suites are testing the main algorithms. Since both correlation and similarity calculation
    # use the function retrieve_correlation_similarity(). This function is where the main logic is implemented.
    # Fow now, the test cases can not be judged if it is correct, or not. Since the answer is not given from the client.
    # We can only make test cases and see if the program outputs any illegal output.
    def test_retrieve_correlation_similarity(self):
        data = ad.clean_input(self.data)
        data_trans = ad.transpose_matrix(data)
        for flag in ['Accumulation', 'Similarity', 'Correlation']:
            item = ad.retrieve_correlation_similarity(data, flag)
            for i in item:
                self.assertTrue(-1 <= i <= 1)
            item = ad.retrieve_correlation_similarity(data_trans, flag)
            for i in item:
                self.assertTrue(-1 <= i <= 1)
