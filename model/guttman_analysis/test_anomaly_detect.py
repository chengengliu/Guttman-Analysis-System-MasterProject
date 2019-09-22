# This is the test script for anomaly_detect file.
# Test the performance of the functions and algorithms.
# This file should be placed under the same directory, with the file 'anomaly_detect.py'

import anomaly_detect as ad
import numpy as np



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
    # print(ad.retrieve_correlation_similarity(transpose,'Correlation'))
    # print(ad.retrieve_correlation_similarity(transpose, 'Accumulation'))
    # print(ad.retrieve_correlation_similarity(matrix, 'Correlation'))
    print(ad.retrieve_correlation_similarity(matrix,'Accumulation'))

    # New 40 test inputs:
    # Correlation
    # [0.8426690062405412, 0.43358335178260665, 0.4458322004449427, 0.43619660490818335, 0.5325267205564304,
    #  0.2847247668875715, 0.5769490038721753, 0.5354344389419204, 0.5984793679059298, 0.7308083220058053,
    #  0.6967868392539249, 0.7297882461482746, 0.7979297175725085, 0.4139036968958773, 0.8875737556140505,
    #  0.7766298364418872, 0.7970727085254296, 0.728458865048582, 0.6994524707825213, 0.5398975291179595,
    #  0.7101355595277726, 0.4395603218829221, 0.3562820265512119, 0.5367706674731029, 0.3405638970291594,
    #  0.5176897654305909, 0.3624228180307622, 0.19259042534089854, 0.23478573333859, 0.36453000918678136,
    #  0.5153815066529824, 0.3873017598749955, 0.3562170426319879, 0.33527875481408764, 0.3804052433260632,
    #  -0.07063951992837367, 0.23329289958979235, 0.12962955305521187, 0.07582837334021783, 0.02930325013657248]
    # Accumulation
    # [0.7819956293684673, 0.3977345456785508, 0.45375558322085224, 0.49646404427723895, 0.595658826507398,
    #  -0.18958800767752693, 0.7917169579909524, 0.7593422160834259, 0.7844900207522052, 0.8236361306437688,
    #  0.8200877648722983, 0.8274381577431397, 0.9479868162810284, 0.8471088275407714, 0.96945283602362,
    #  0.8997628070586728, 0.8137410203445404, 0.7874994095132332, 0.6752892207703388, 0.6397572734816374,
    #  0.5608756479770347, 0.19483438375347847, -0.07580875430855726, 0.28899147106943807, -0.026162775865975166,
    #  0.24795359296121786, -0.03560084365295577, -0.0849391170943871, -0.07428316304254796, 0.06270430720346723,
    #  0.3758081624507635, 0.12559430659594262, 0.07722827176292672, 0.06430629361582801, 0.24527693365315686,
    #  -0.1311552861817856, 0.1347310033330986, -0.01948862623792305, 0.09261127011031471, -0.03293766314631472]

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


def test_detect_full_score(transposed):
    return ad.detect_full_score(transposed)


def test_cal_scorerate_accumulated_matrix(original_data):
    student_sum = ad.sumStudentScore(original_data)
    item_sum = ad.sumItemScore(original_data)
    sorted_student = ad.sortBasedOnStudent(original_data, student_sum)
    sorted_item = ad.sortBasedOnItem(sorted_student, item_sum)

    matrix = sorted_item
    transpose = ad.transpose_matrix(matrix)

    student_sum.sort()
    student_sum = list(reversed(student_sum))
    ave_per_student = ad.retrieve_average_per_item(matrix, student_sum)

    print(matrix)
    ad.cal_scorerate_accumulated_matrix(matrix)

def test_staddv(original_data):
    student_sum = ad.sumStudentScore(original_data)
    item_sum = ad.sumItemScore(original_data)
    sorted_student = ad.sortBasedOnStudent(original_data, student_sum)
    sorted_item = ad.sortBasedOnItem(sorted_student, item_sum)

    matrix = sorted_item
    transpose = ad.transpose_matrix(matrix)

    student_sum.sort()
    student_sum = list(reversed(student_sum))
    ave_per_student = ad.retrieve_average_per_item(matrix, student_sum)

    print(ad.get_0staddv_index(matrix))


def test_skip(original_data):
    student_sum = ad.sumStudentScore(original_data)
    item_sum = ad.sumItemScore(original_data)
    sorted_student = ad.sortBasedOnStudent(original_data, student_sum)
    sorted_item = ad.sortBasedOnItem(sorted_student, item_sum)

    matrix = sorted_item
    transpose = ad.transpose_matrix(matrix)

    student_sum.sort()
    student_sum = list(reversed(student_sum))
    ave_per_student = ad.retrieve_average_per_item(matrix, student_sum)


    danger_list = ad.get_0staddv_index(matrix)





def main():
    file_read("1")
    # Input from Yi Wang's package.
    sample_input = [[1, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0, 0],
                    [0, 1, 1, 1, 1, 1, 1, 0], [1, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1, 1, 1],
                    [1, 1, 0, 0, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 0, 1]]

    original_input = [[1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 1, 0], [1, 1, 0, 0], [1, 2, 0, 0]]
    # test_return_correlation(original_input)
    # test_return_correlation(sample_input)
    np.seterr(divide='ignore', invalid='ignore')



    real_input = [[3, 2, 3, 2, 0, 2, 2], [3, 2, 3, 2, 0, 2, 2], [3, 2, 3, 2, 0, 2, 2], [3, 2, 3, 1, 0, 2, 2], [3, 2, 3, 2, 0, 0, 2], [3, 2, 2, 1, 2, 0, 0], [3, 2, 2, 1, 2, 0, 0], [3, 2, 2, 1, 0, 0, 2], [1, 2, 3, 2, 0, 2, 0], [3, 2, 0, 0, 1, 2, 1], [3, 2, 1, 1, 2, 0, 0], [3, 2, 1, 1, 2, 0, 0], [3, 2, 1, 1, 1, 0, 1], [3, 2, 2, 1, 1, 0, 0], [3, 0, 2, 1, 2, 0, 0], [3, 2, 1, 1, 1, 0, 0], [3, 2, 0, 1, 1, 0, 1], [3, 2, 2, 1, 0, 0, 0], [3, 2, 2, 1, 0, 0, 0], [3, 2, 1, 1, 1, 0, 0], [3, 1, 2, 1, 1, 0, 0], [3, 2, 1, 1, 1, 0, 0], [1, 1, 2, 1, 1, 0, 1], [3, 2, 1, 1, 0, 0, 0], [0, 2, 3, 1, 1, 0, 0], [3, 2, 1, 1, 0, 0, 0], [0, 2, 3, 1, 1, 0, 0], [3, 1, 0, 1, 1, 0, 0], [0, 1, 2, 2, 1, 0, 0], [0, 2, 1, 1, 2, 0, 0], [1, 1, 1, 1, 1, 0, 0], [3, 2, 0, 0, 0, 0, 0], [3, 2, 0, 0, 0, 0, 0], [3, 1, 1, 0, 0, 0, 0], [1, 2, 1, 1, 0, 0, 0], [0, 2, 1, 1, 0, 0, 0], [0, 1, 0, 1, 1, 0, 1], [3, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

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
    # print(" NEW TEST: ")
    # print()
    # print("Student Irregular  Original: ", refactor_similarity_test(real_input,True))
    # print("Column Irregular Original:  ", refactor_similarity_test(real_input, False))
    # print("Student Irregular Sample Input: ", refactor_similarity_test(real_input, True))
    # print("Column Irregular Sample Input: ",refactor_similarity_test(real_input, False))


    test_return_correlation(real_input)



    student_sum = ad.sumStudentScore(original_input)
    item_sum = ad.sumItemScore(original_input)
    sorted_student = ad.sortBasedOnStudent(original_input, student_sum)
    sorted_item = ad.sortBasedOnItem(sorted_student, item_sum)

    matrix = sorted_item
    transpose = ad.transpose_matrix(matrix)

    student_sum.sort()
    student_sum = list(reversed(student_sum))
    ave_per_student = ad.retrieve_average_per_item(matrix, student_sum)


    # print(test_detect_full_score(transpose))
    #
    # print(test_cal_scorerate_accumulated_matrix(original_input))

    # test_staddv(original_input)

    # test_skip()






if __name__ == '__main__':
    main()