# Module Usage Description


## USAGE MANUAL/INTERFACE Introduction:

### Section I. Source Code Reading Instructions:

       This __init__.py file contains both helper functions(which has no relation with algorithms) and
    Algorithms implementation functions, as well as interface functions(used by other modules). This file also contains
    a main function, forinternal testing purpose, which is not meant to be read. Two interfaces functions that should be used
    by other modulesare 'return_correlation(original_data, is_student, flag)' and
    'return_irregular_column_index(original_data, is_student)', which will be introduced in further details in the following section.

### Section II. Module usage (interface):

Special notice:

    The function clean_input(original_data) must be used, since Yi Wang's package gives me the inputs with both
    columns name and rows name. 
    However, every function that relates with 'Sorting', is not useful anymore. In Yi Want's excel module, 
    he has sorted the data from easy questions to hard questions and from high competency student to low competency student.

1. To get the correlation, for either the student or the items/criteria:

call the function:
    ```
    return_correlation(original_data, is_student, flag)
    ```
<br/>
Input Description:

    Original_data: where the input is the original data (it is supposed to be nested list)
    This function assumes that the input data is sorted. However, if the data is not sorted, the function will perform sorting
    inside.

    is_student: Is a boolean variable, can be either True or False. This boolean values specifies whether you want to get
    student correlation (row), or item/criteria correlation(column). For example,
    If 'is_student' is set to True, the program will return the correlation calculated for rows.

    flag: This is for testing algorithm purpose. It is a string, can either be 'Accumulation', or 'Correlation'.
        'Accumulation' will use the accumulated value of the column/student, while 'Correlation' is simple calculate the
        data.
    Notice: Two different ways of calculating correlation are implemented and can be retrieved. Which way is better needs to
    be tested using test results.

2. To get the irregular columns:

call the function:
    ```return_irregular_index(original_data, is_student)```<br/>
Input Desciption:

    Original_data: where the input is the original data (it is supposed to be nested list)
    This function assumes that the input data is sorted. However, if the data is not sorted, the function will perform sorting
    inside.

    is_student: Is a boolean variable, can be either True or False. This boolean values specifies whether you want to get
    student correlation (row), or item/criteria correlation(column). For example,
    If 'is_student' is set to True, the program will return the correlation calculated for rows.

    Notice: For now I have not implemented the cluster algorithm for detecting unusual behaviour. This will be added in sprint3.
    Current method is to set a threshold value and to see if the value is below the threshold. （阈值）
### Section III. Helper functions:
    As mentioned in Section I, there are several helper functions only used for data re-formatting and sorting purposes.
    These functions can be skipped and has no relation with the algorithms implementations.
    The helper functions include:

    
    sumItemScore(matrix)
    transpose_matrix(matrix)
The above mentioned functions can be skipped while you read the code.

### Section IV. Furthrer Notice
The algorithms are tested (for now) under `test_anomaly_detect.py` file. 
Current(end of sprint 2) build has not received any useful test data to validate the algorithms. 
The tests performed are more like a format/math check, but not a effectiveness check. 
