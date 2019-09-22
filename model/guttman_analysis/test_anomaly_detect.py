# This is the test script for anomaly_detect file.
# Test the performance of the functions and algorithms.
# This file should be placed under the same directory, with the file 'anomaly_detect.py'

import __init__ as ad
import numpy as np
import file_import as fi



def main():
    # Read from the file. This module is out of the scope of the current module.
    # Assume the module is corret.
    data = fi.readfile(
        "/Users/Apple/Documents/Google-Sync/SWEN90014 Master Project/Project/swen90014-2019-rv-quoll/testdata/SampleAssessmentResult.xlsx")
    data = fi.transpose(data)
    fi.sort_2d_array(data)

    data_should_be = [[3, 2, 3, 2, 0, 2, 2], [3, 2, 3, 2, 0, 2, 2], [3, 2, 3, 2, 0, 2, 2], [3, 2, 3, 1, 0, 2, 2],
                      [3, 2, 3, 2, 0, 2, 0], [3, 2, 2, 1, 2, 0, 0], [3, 2, 2, 1, 2, 0, 0], [3, 2, 2, 1, 0, 2, 0],
                      [1, 2, 3, 2, 0, 0, 2], [3, 2, 0, 0, 1, 1, 2], [3, 2, 1, 1, 2, 0, 0], [3, 2, 1, 1, 2, 0, 0],
                      [3, 2, 1, 1, 1, 1, 0], [3, 2, 2, 1, 1, 0, 0], [3, 0, 2, 1, 2, 0, 0], [3, 2, 1, 1, 1, 0, 0],
                      [3, 2, 0, 1, 1, 1, 0], [3, 2, 2, 1, 0, 0, 0], [3, 2, 2, 1, 0, 0, 0], [3, 2, 1, 1, 1, 0, 0],
                      [3, 1, 2, 1, 1, 0, 0], [3, 2, 1, 1, 1, 0, 0], [1, 1, 2, 1, 1, 1, 0], [3, 2, 1, 1, 0, 0, 0],
                      [0, 2, 3, 1, 1, 0, 0], [3, 2, 1, 1, 0, 0, 0], [0, 2, 3, 1, 1, 0, 0], [3, 1, 0, 1, 1, 0, 0],
                      [0, 1, 2, 2, 1, 0, 0], [0, 2, 1, 1, 2, 0, 0], [1, 1, 1, 1, 1, 0, 0], [3, 2, 0, 0, 0, 0, 0],
                      [3, 2, 0, 0, 0, 0, 0], [3, 1, 1, 0, 0, 0, 0], [1, 2, 1, 1, 0, 0, 0], [0, 2, 1, 1, 0, 0, 0],
                      [0, 1, 0, 1, 1, 1, 0], [3, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0]]


    test_data_clean(data, data_should_be)
    test_detectDimension(data)

    data = ad.clean_input(data)

    # Manipulate the data so that the first element in the list has zero standard deviation.
    data[0] = [0, 0, 0, 0, 0, 0, 0]
    test_get_0staddv_index(data)
    test_in_danger_list(data)

    # Put the data to original data.
    data[0] = [3, 2, 3, 2, 0, 2, 2]



    # The following test suites are testing the main algorithms. Since both correlation and similarity calculation
    # use the function retrieve_correlation_similarity(). This function is where the main logic is implemented.
    # Fow now, the test cases can not be judged if it is correct, or not. Since the answer is not given from the client.
    # We can only make test cases and see if the program outputs any illegal output.
    test_retrieve_correlation_similarity(data, 'Accumulation')
    test_retrieve_correlation_similarity(data, 'Similarity')
    test_retrieve_correlation_similarity(data, 'Correlation')

    # Test the transpose of data.
    test_transpose_matrix(data)

    data = ad.transpose_matrix(data)
    test_retrieve_correlation_similarity(data, 'Accumulation')
    test_retrieve_correlation_similarity(data, 'Similarity')
    test_retrieve_correlation_similarity(data, 'Correlation')



def test_get_0staddv_index(data):
    assert ad.get_0staddv_index(data) == [0]


def test_in_danger_list(data):
    index = 0
    assert ad.in_danger_list(ad.get_0staddv_index(data), index) == True


def test_data_clean(data_input, data_should_be):
    print(data_input)
    data_cleaned = ad.clean_input(data_input)
    print(data_cleaned)
    assert data_cleaned == data_should_be


def test_detectDimension(data):
    dimension_should_be = (len(data), len(data[0]))
    assert ad.detectDimenstion(data) == dimension_should_be

def test_transpose_matrix(data):
    assert data == ad.transpose_matrix(ad.transpose_matrix(data))



def test_retrieve_correlation_similarity(matrix, flag):
    item = ad.retrieve_correlation_similarity(matrix, flag)
    for i in item:
        assert   -1 <= i <=1
    print(item)


if __name__ == '__main__':
    main()
