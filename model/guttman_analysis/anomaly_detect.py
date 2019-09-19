
    # columns_whole_similarity = similarity_between_column_whole(transpose, ave_per_student)

    # irregular_columns = detect_item_irregular()
    # print("Similarity between columns", similarity_between_columns(matrix))
    # return irregular_columns
# def refactor_irregular_column_index(original_data, is_student):
#     student_sum = sumStudentScore(original_data)
#     item_sum = sumItemScore(original_data)
#     sorted_student = sortBasedOnStudent(original_data, student_sum)
#     sorted_item = sortBasedOnItem(sorted_student, item_sum)
#
#     # Orginal data is manipulated into either matrix(student as row) or transpose(criteria as row)
#     matrix = sorted_item
#     transpose = transpose_matrix(matrix)
#
#     student_sum.sort()
#     student_sum = list(reversed(student_sum))
#     ave_per_student = retrieve_average_per_item(matrix, student_sum)
#
#     if not is_student:
#         columns_similarity = retrieve_correlation_similarity(transpose, 'Similarity')
#         return detect_item_irregular(columns_similarity, transpose)
#     elif is_student:
#         columns_similarity = retrieve_correlation_similarity(matrix, 'Similarity')
#         return detect_item_irregular(columns_similarity, matrix)


###############################################################################
####### Any code bleow this line are not useful. For testing purpose.
###############################################################################
###############################################################################

'''
Driver function. NO NEDD to read this function AT ALL
'''


def main():
    Matrix = [[0, 1, 1, 1], [1, 1, 1, 0], [1, 1, 1, 0], [1, 1, 0, 0], [1, 2, 0, 0]]

    print(Matrix)
    studentSum = sumStudentScore(Matrix)
    itemSum = sumItemScore(Matrix)
    print(studentSum)
    print(itemSum)
    sortedMatrixStudent = sortBasedOnStudent(Matrix, studentSum)  # After sorting based on student summation.
    sortedMatrixItem = sortBasedOnItem(sortedMatrixStudent, itemSum)  # After sorting based on item summation.
    matrix = sortedMatrixItem
    print("After sorting:", matrix)

    # After sorting the data, both item_summation and student_summation records should be sorted.
    # Keep the original order unchanged.
    student_sum_copy = copy.deepcopy(studentSum)
    item_sum_copy = copy.deepcopy(itemSum)
    student_sum_copy.sort()
    item_sum_copy.sort()
    student_sum_copy = list(reversed(student_sum_copy))
    item_sum_copy = list(reversed(item_sum_copy))

    # The four variables below are not used for now, but maybe useful for later partitions.
    student_score_median = cal_median(matrix, student_sum_copy)
    item_median = cal_median(matrix, item_sum_copy)
    student_score_ave = cal_average(matrix, student_sum_copy, len(studentSum))
    item_ave = cal_average(matrix, item_sum_copy, len(itemSum))

    ave_per_item = retrieve_average_per_item(matrix, item_sum_copy)  # Average of each column. Sorted list.
    ave_per_student = retrieve_average_per_item(matrix, student_sum_copy)
    items_in_matrix = transpose_matrix(matrix)  # Perform transpose on the sorted original data.

    #####################################################################################
    # This is the result to return back to the server, a list of correlation, in the order with each columns.
    # correlation_of_columns = retrieve_correlation_columns(items_in_matrix)
    # print(correlation_of_columns)
    # print(" This is Student Distribution : ------> ", matrix)

    #
    # print("This is the Accumulation Correlation of Student: ------> ")
    # print(retrieve_correlation_columns(matrix, 'Accumulation'))
    # print("This is the Correlation of Student: ----->")
    # print(retrieve_correlation_columns(matrix, 'Correlation'))
    # print("Student, Accumulation: ", return_correlation(Matrix, True, 'Accumulation'))

    # Two lists containing similarities. Inputs are items/criteria inputs, not student matrix(not the original data).
    # columns_similarity = similarity_between_columns(items_in_matrix)
    # columns_whole_similarity = similarity_between_column_whole(items_in_matrix, ave_per_student)
    # print("Columns whole similarity", columns_whole_similarity)
    # print("columns_similarity", columns_similarity)

    # print(return_correlation(Matrix, True, 'Accumulation'))
    # print(return_correlation(Matrix, False, 'Accumulation'))

    #####################################################################################
    # This list should be returned to the server, a list of irregular columns.
    # This list contains the position of irregular columns.
    # irregular_column_items = detect_item_irregular(columns_similarity, columns_whole_similarity, items_in_matrix)
    # print("Irregular Column index: ", return_irregular_column_index(Matrix, True))

    # clean_input("hello")





if __name__ == '__main__':
    main()

