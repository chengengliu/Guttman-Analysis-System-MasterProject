# This is the unit test for anomaly_detect file.
# Test the performance of the functions and algorithms.
# This file should be placed under the same directory, with the file 'anomaly_detect.py'

import anomaly_detect as ad



def file_read(file):
    print()

def test_return_correlation(original_data):
    student_sum = ad.sumStudentScore(original_data)
    item_sum = ad.sumItemScore(original_data)
    sorted_student = ad.sortBasedOnStudent(original_data, student_sum)
    sorted_item = ad.sortBasedOnItem(sorted_student, item_sum)

    matrix = sorted_item
    transpose = ad.transpose_matrix(matrix)
    # For student== true and 'Correlation'
    print(ad.retrieve_correlation_similarity(transpose,'Correlation'))
    print(ad.retrieve_correlation_similarity(transpose, 'Accumulation'))
    print(ad.retrieve_correlation_similarity(matrix, 'Correlation'))
    print(ad.retrieve_correlation_similarity(matrix,'Accumulation'))


    # original_input
    # [-0.18118621784789712, -0.5395620726159658, -0.15309310892394862, -0.2958758547680685]
    # [-0.18118621784789712, 0.8384051598086931, 0.6880131155392438, -0.2958758547680685]
    # [0.5222329678670935, 0.44156247593084647, 0.4415624759308465, -0.31100423396407306, 0.0]
    # [0.5222329678670935, 0.8897395944346991, 0.8897395944346991, 0.5396491510576825, 0.0]

    # Wang Yi's input:
    # [0.1591650066335189, -0.09716878364870321, 0.1742083652267312, 0.17330020307776273, 0.31988401440957376,
    #  0.5700327796711772, 0.40193447954731776, 0.6486042082426058]
    # [0.1591650066335189, 0.9115301084858436, 0.9681743752867544, 0.9418404471451012, 0.9536171342063858,
    #  0.9453740812339286, 0.715651212141974, 0.6486042082426058]
    # [-0.1930976411097092, 0.07273929674533079, 0.019185907182890167, -0.05735185806021776, -0.0670800041782233,
    #  0.35054219842047446, 0.3781706433735665, 0.5136430583119075, 0.5091860489526062, 0.4040955879829151,
    #  0.5068560600638237]
    # [-0.1930976411097092, 0.8256418923363807, 0.9092260952108829, 0.9175822532571676, 0.9319427880757631,
    #  0.9236035212357172, 0.8744812932251769, 0.8717264416642472, 0.7356302376707533, 0.5609434495607353,
    #

    # 整体output：
    # [-0.18118621784789712, -0.5395620726159658, -0.15309310892394862, -0.2958758547680685]
    # [-0.18118621784789712, 0.8384051598086931, 0.6880131155392438, -0.2958758547680685]
    # [0.5222329678670935, 0.44156247593084647, 0.4415624759308465, -0.31100423396407306, 0.0]
    # [0.5222329678670935, 0.8897395944346991, 0.8897395944346991, 0.5396491510576825, 0.0]
    # [0.1591650066335189, -0.09716878364870321, 0.1742083652267312, 0.17330020307776273, 0.31988401440957376,
    #  0.5700327796711772, 0.40193447954731776, 0.6486042082426058]
    # [0.1591650066335189, 0.9115301084858436, 0.9681743752867544, 0.9418404471451012, 0.9536171342063858,
    #  0.9453740812339286, 0.715651212141974, 0.6486042082426058]
    # [-0.1930976411097092, 0.07273929674533079, 0.019185907182890167, -0.05735185806021776, -0.0670800041782233,
    #  0.35054219842047446, 0.3781706433735665, 0.5136430583119075, 0.5091860489526062, 0.4040955879829151,
    #  0.5068560600638237]
    # [-0.1930976411097092, 0.8256418923363807, 0.9092260952108829, 0.9175822532571676, 0.9319427880757631,
    #  0.9236035212357172, 0.8744812932251769, 0.8717264416642472, 0.7356302376707533, 0.5609434495607353,
    #  0.5068560600638237]


# def test_return_irregualr_column_index(original_data, is_student):
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
#     # Calculate similarities between columns:
#     if not is_student:
#         similarity = ad.similarity_between_columns(transpose)
#         print()
#         print(similarity)
#         print()
#         return ad.detect_item_irregular(similarity, transpose)
#     elif is_student:
#         similarity = ad.similarity_between_columns(matrix)
#         print()
#         print(similarity)
#         print()
#
#         return ad.detect_item_irregular(similarity, matrix)

def refactor_similarity_test(original_data, is_student):
    student_sum = ad.sumStudentScore(original_data)
    item_sum = ad.sumItemScore(original_data)
    sorted_student = ad.sortBasedOnStudent(original_data, student_sum)
    sorted_item = ad.sortBasedOnItem(sorted_student, item_sum)

    matrix = sorted_item
    transpose = ad.transpose_matrix(matrix)

    student_sum.sort()
    student_sum = list(reversed(student_sum))
    ave_per_student = ad.retrieve_average_per_item(matrix, student_sum)

    if not is_student:
        similarity = ad.retrieve_correlation_similarity(transpose, 'Similarity')
        print()
        print(similarity)
        print()
        return ad.detect_item_irregular(similarity, transpose)
    elif is_student:
        similarity = ad.retrieve_correlation_similarity(matrix, 'Similarity')
        print()
        print(similarity)
        print()

        return ad.detect_item_irregular(similarity, matrix)





def main():
    file_read("1")
    # Input from Yi Wang's package.
    sample_input = [[1, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0, 0],
                    [0, 1, 1, 1, 1, 1, 1, 0], [1, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1, 1, 1],
                    [1, 1, 0, 0, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 0, 1]]

    original_input = [[0, 1, 1, 1], [1, 1, 1, 0], [1, 1, 1, 0], [1, 1, 0, 0], [1, 2, 0, 0]]
    test_return_correlation(original_input)
    test_return_correlation(sample_input)

    # print("Student Irregular  Original: ", test_return_irregualr_column_index(original_input,True))
    # print("Column Irregular Original:  ", test_return_irregualr_column_index(original_input, False))
    # print("Student Irregular Sample Input: ", test_return_irregualr_column_index(sample_input, True))
    # print("Column Irregular Sample Input: ",test_return_irregualr_column_index(sample_input, False))

    # Similarity 的阈值不好。When the threshold is 0.5:
    # i is ::::: ->  (0.4353954059492991, 3)
    # Student Irregular  Original:  [3]
    # i is ::::: ->  (0.2886751345948129, 3)
    # Column Irregular Original:   [3]
    # i is ::::: ->  (0.47719427922241614, 9)
    # i is ::::: ->  (0.5948190167920577, 10)
    # Student Irregular Sample Input:  [9]
    # i is ::::: ->  (0.5447172541558802, 6)
    # i is ::::: ->  (0.6823964588860406, 4)
    # Column Irregular Sample Input:  []
    print(" NEW TEST: ")
    print()
    print("Student Irregular  Original: ", refactor_similarity_test(original_input,True))
    print("Column Irregular Original:  ", refactor_similarity_test(original_input, False))
    print("Student Irregular Sample Input: ", refactor_similarity_test(sample_input, True))
    print("Column Irregular Sample Input: ",refactor_similarity_test(sample_input, False))





if __name__ == '__main__':
    main()