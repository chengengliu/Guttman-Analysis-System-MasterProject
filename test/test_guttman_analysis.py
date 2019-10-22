import unittest
import model.guttman_analysis as ad
import model.file_importing as fi


class GuttmanAnalysisTestCase(unittest.TestCase):

    def setUp(self) -> None:
        # The path should be configured as the full path of the test data file. TODO: I don't really understand why the relative path not working.
        path = "/Users/Apple/Documents/Google-Sync/SWEN90014 Master Project/Project/swen90014-2019-rv-quoll" \
               "/testdata/SampleAssessmentResult.xlsx"
        self.data = fi.readfile(path)
        self.data = fi.transpose(self.data)
        fi.sort_2d_array_mark(self.data)
        # After reading from excel_importing module, the data read transformed as original_data.
        # Here only performing unit test for guttman-analysis module and aussmes that the data imported are correct.
        self.original_data = [
            ['', 'etc…', 'Recognises steps in the teaching and learning cycle.', 'Defines 21st century competencies',
             'etc…', 'etc…', 'etc…', 'etc…', 'Distinguishes between competence and content.',
             'Identifies levels of competence.', 'etc…',
             'Interprets learning progressions describing increasing competence.',
             'Describes methods for assessment of competence.',
             'Connects teaching and learning cycle to classroom practice.',
             'Distinguishes between evidence and inference.', 'Lists methods of evidence collection.', 'etc…',
             'Explains plan for meeting student needs.', 'Uses teaching and learning cycle to plan instruction.',
             'etc…', 'etc…', 'etc…', 'etc…'],
            ['student_id', '2.1.1', '1.3.1', '1.1.1', '3.1.1', '2.1.2', '3.1.2', '3.1.3', '1.2.1', '1.1.2', '4.1.1',
             '1.1.3', '1.2.2', '1.3.2', '1.4.1', '1.4.2', '4.1.2', '1.2.3', '1.3.3', '2.1.3', '2.1.4', '3.1.4',
             '4.1.3'],
            ['664', 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            ['674', 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            ['686', 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            ['671', 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            ['670', 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            ['679', 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['682', 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            ['683', 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            ['656', 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['662', 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['681', 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['663', 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['654', 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            ['676', 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['677', 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['657', 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['680', 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['653', 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['666', 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['675', 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['669', 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['690', 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['652', 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['684', 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['678', 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['687', 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['658', 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['655', 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['659', 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['685', 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['673', 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['651', 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['661', 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['688', 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['667', 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['660', 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['668', 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['672', 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['689', 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['665', 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        # Data after cleaning. The data that is supposed to be parsed to Guttman Analysis module to process with.
        self.data_shoudlbe = [[1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.data_first_row_one = ad.clean_input(self.original_data)
        # Manipulate the data so that the first element in the list has zero standard deviation.
        self.data_first_row_one[0] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        # transposed data
        self.transposed_data = ad.transpose_matrix(self.data_shoudlbe)

    # Test if the clean_input function.
    def test_clean_input(self):
        self.assertTrue(ad.clean_input(self.original_data) == self.data_shoudlbe)

    # Manually calculated the sum of each question, among all the questions.
    def test_sum_item_Score(self):
        sum_mark_shouldbe = [37, 34, 32, 32, 29, 28, 28, 21, 18, 11, 8, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0]
        self.assertTrue(ad.sum_item_score(self.data_shoudlbe) == sum_mark_shouldbe)

    def test_transpose_matrix(self):
        self.assertTrue(ad.transpose_matrix(self.data_shoudlbe) == fi.transpose(self.data_shoudlbe))

    def test_detect_full_score(self):
        full_mark_shouldbe = []
        for i in range(len(self.data_shoudlbe)):
            full_mark_shouldbe.append(1)
        self.assertTrue(full_mark_shouldbe, ad.detect_full_score(self.data_shoudlbe))
    # The behaviour of cal_scorerate_accumulated_matrix has two branches and the behaviour will be different for these two
    # kind of inputs.
    # When the input is student, (row is student score),
    def test_cal_scorerate_accumulated_matrix_student(self):
        is_student = True
        accumulated_shouldbe = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.875, 0.8888888888888888, 0.9, 0.9090909090909091, 0.8333333333333334, 0.8461538461538461, 0.8571428571428571, 0.8666666666666667, 0.875, 0.8235294117647058, 0.7777777777777778, 0.7368421052631579, 0.7, 0.6666666666666666, 0.6363636363636364]
        self.assertTrue(ad.cal_scorerate_accumulated_matrix(self.data_shoudlbe, is_student)[0] == accumulated_shouldbe)

    def test_cal_scorerate_accumulated_matrix_item(self):
        is_student = False
        accumulated_shouldb = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                               0.9444444444444444, 0.9473684210526315, 0.95, 0.9523809523809523, 0.9545454545454546,
                               0.9565217391304348, 0.9583333333333334, 0.96, 0.9615384615384616, 0.9629629629629629, 0.9642857142857143, 0.9655172413793104, 0.9666666666666667, 0.967741935483871, 0.96875, 0.9696969696969697, 0.9705882352941176, 0.9714285714285714, 0.9722222222222222, 0.972972972972973, 0.9473684210526315, 0.9487179487179487, 0.925]
        self.assertTrue(ad.cal_scorerate_accumulated_matrix(ad.transpose_matrix(self.data_shoudlbe),is_student)[0] == accumulated_shouldb)
    def test_get0staddv_index(self):
        self.assertTrue(ad.get_0staddv_index(self.data_first_row_one)==[0])
    def test_in_danger_list(self):
        self.assertTrue(ad.in_danger_list(ad.get_0staddv_index(self.data_first_row_one),0))

    # The following test suites are testing the main algorithms. Since both correlation and similarity calculation
    # use the function retrieve_correlation_similarity(). This function is where the main logic is implemented.
    # Fow now, the test cases can not be judged if it is correct, or not. Since the answer is not given from the client.
    # We can only make test cases and see if the program outputs any illegal output.
    def test_return_irregular_index(self):
        data = self.data_shoudlbe
        cleaned_data =ad.clean_input(data)
        transposed = ad.transpose_matrix(cleaned_data)
        for flag in ['Accumulation', 'Similarity', 'Correlation']:
            item = ad.irregular_calculation(data, flag, True)
            for i in item:
                self.assertTrue(-1<=i<=1)
            item = ad.irregular_calculation(data,flag, True)
            for i in item:
                self.assertTrue(-1<=i<=1)
            item = ad.irregular_calculation(transposed,flag,False)
            for i in item:
                self.assertTrue(-1<=i<=1)

    def test_irregular_box(self):
        self.assertTrue(ad.irregular_box(self.data_shoudlbe)[0] == (0, 6, (24, 38)))
    def test_get_neighbours(self):
        self.assertTrue(ad.get_neighbours(1) == [(0, -1), (0, 1), (-1, 0), (1, 0)])
    def test_calculate_radius(self):
        self.assertTrue(ad.calculate_radius(self.data_shoudlbe) == 4)
    def test_odd_cells(self):
        self.assertTrue(ad.odd_cells(self.data_shoudlbe).__len__() ==11)
    # self.assertTrue(self.data_first_row_one == ad.detect_full_score(self.data_shoudlbe))
    # def test_
    # def test_get_0staddv_index(self):
    #     self.assertTrue(ad.get_0staddv_index(self.data_first_row_zero) == [0])
    #
    # def test_in_danger_list(self):
    #     self.assertTrue(ad.in_danger_list(ad.get_0staddv_index(self.data_first_row_zero), 0))
    #
    # def test_data_clean(self):
    #     data_cleaned = ad.clean_input(self.data)
    #     self.assertTrue(data_cleaned == self.data_should_be)
    #
    #
    # def test_transpose_matrix(self):
    #     self.assertTrue(self.data == ad.transpose_matrix(ad.transpose_matrix(self.data)))

    # def test_retrieve_correlation_similarity(self):
    #     data = ad.clean_input(self.data)
    #     data_trans = ad.transpose_matrix(data)
    #     for flag in ['Accumulation', 'Similarity', 'Correlation']:
    #         item = ad.retrieve_correlation_similarity(data, flag)
    #         for i in item:
    #             self.assertTrue(-1 <= i <= 1)
    #         item = ad.retrieve_correlation_similarity(data_trans, flag)
    #         for i in item:
    #             self.assertTrue(-1 <= i <= 1)
