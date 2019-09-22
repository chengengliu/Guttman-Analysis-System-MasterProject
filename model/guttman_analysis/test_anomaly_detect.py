# This is the test script for anomaly_detect file.
# Test the performance of the functions and algorithms.
# This file should be placed under the same directory, with the file 'anomaly_detect.py'

import test_stddv as ad
import numpy as np
import file_import as fi



# def test_return_correlation(original_data):
#     student_sum = ad.sumStudentScore(original_data)
#     item_sum = ad.sumItemScore(original_data)
#     sorted_student = ad.sortBasedOnStudent(original_data, student_sum)
#     sorted_item = ad.sortBasedOnItem(sorted_student, item_sum)
#
#     matrix = sorted_item
#     transpose = ad.transpose_matrix(matrix)
#     # For student== true and 'Correlation'
#     # print(ad.retrieve_correlation_similarity(transpose,'Correlation'))
#     # print(ad.retrieve_correlation_similarity(transpose, 'Accumulation'))
#     # print(ad.retrieve_correlation_similarity(matrix, 'Correlation'))
#     print("Accumulation ")
#     print(ad.retrieve_correlation_similarity(matrix,'Accumulation'))
#
#
# def refactor_similarity_test(original_data, is_student):
#     student_sum = ad.sumStudentScore(original_data)
#     item_sum = ad.sumItemScore(original_data)
#     sorted_student = ad.sortBasedOnStudent(original_data, student_sum)
#     sorted_item = ad.sortBasedOnItem(sorted_student, item_sum)
#
#     matrix = sorted_item
#     transpose = ad.transpose_matrix(matrix)
#
#     student_sum.sort()
#     student_sum = list(reversed(student_sum))
#     ave_per_student = ad.retrieve_average_per_item(matrix, student_sum)
#
#     if not is_student:
#         similarity = ad.retrieve_correlation_similarity(transpose, 'Similarity')
#         print()
#         print(similarity)
#         print()
#         return ad.detect_item_irregular(similarity, transpose)
#     elif is_student:
#         similarity = ad.retrieve_correlation_similarity(matrix, 'Similarity')
#         print()
#         print(similarity)
#         print()
#
#         return ad.detect_item_irregular(similarity, matrix)
#
#
# def test_detect_full_score(transposed):
#     return ad.detect_full_score(transposed)
#
#
# def test_cal_scorerate_accumulated_matrix(original_data):
#     student_sum = ad.sumStudentScore(original_data)
#     item_sum = ad.sumItemScore(original_data)
#     sorted_student = ad.sortBasedOnStudent(original_data, student_sum)
#     sorted_item = ad.sortBasedOnItem(sorted_student, item_sum)
#
#     matrix = sorted_item
#     transpose = ad.transpose_matrix(matrix)
#
#     student_sum.sort()
#     student_sum = list(reversed(student_sum))
#     ave_per_student = ad.retrieve_average_per_item(matrix, student_sum)
#
#     print(matrix)
#     ad.cal_scorerate_accumulated_matrix(matrix)
#
# def test_staddv(original_data):
#     student_sum = ad.sumStudentScore(original_data)
#     item_sum = ad.sumItemScore(original_data)
#     sorted_student = ad.sortBasedOnStudent(original_data, student_sum)
#     sorted_item = ad.sortBasedOnItem(sorted_student, item_sum)
#
#     matrix = sorted_item
#     transpose = ad.transpose_matrix(matrix)
#
#     student_sum.sort()
#     student_sum = list(reversed(student_sum))
#     ave_per_student = ad.retrieve_average_per_item(matrix, student_sum)
#
#     print(ad.get_0staddv_index(matrix))
#
#
# def test_skip(original_data):
#     student_sum = ad.sumStudentScore(original_data)
#     item_sum = ad.sumItemScore(original_data)
#     sorted_student = ad.sortBasedOnStudent(original_data, student_sum)
#     sorted_item = ad.sortBasedOnItem(sorted_student, item_sum)
#
#     matrix = sorted_item
#     transpose = ad.transpose_matrix(matrix)
#
#     student_sum.sort()
#     student_sum = list(reversed(student_sum))
#     ave_per_student = ad.retrieve_average_per_item(matrix, student_sum)
#
#
#     danger_list = ad.get_0staddv_index(matrix)
#
#



def main():
    data = fi.readfile("/Users/Apple/Documents/Google-Sync/SWEN90014 Master Project/Project/swen90014-2019-rv-quoll/testdata/SampleAssessmentResult.xlsx")
    data = fi.transpose(data)
    fi.sort_2d_array(data)
    # for i in data:
    #     print(i)
    # print(len(data))

    data = ad.clean_input(data)
    print(data)
    print(len(data))
    data[0] = [0,0,0,0,0,0,0]
    # data[39] = [3,2,3,2,2,2,2]
    print(data)

    coor_item = ad.retrieve_correlation_similarity(data, 'Accumulation')
    print(coor_item)
    print(ad.get_0staddv_index(data))

    scorerate_accumulated = ad.cal_scorerate_accumulated_matrix(data)
    print(scorerate_accumulated)
    print(ad.get_0staddv_index(scorerate_accumulated))


def test_


if __name__ == '__main__':
    main()