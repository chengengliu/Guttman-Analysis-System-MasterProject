# Module Usage Description


## USAGE MANUAL/INTERFACE Introduction:

### Section I. Source Code Reading Instructions:

	This exceloutput.py contains helper functions and interface functions(used by other modules). No main function is maintained in 
module. The main purpose of this module is providing an interface for users to modify an excel file. 
One algorithm in this module is to calculate total score of all rows and columns provided by creating an instance of class named 'exceloutput'
Three functions, 'addcorrelation', 'highlightarea', 'addborder' manipulate input coordinates and write correspond data to an exsiting excel file.
  

### Section II. Module usage (interface):

Special notice:

    'closeWorkbook' functions is required to be applied after modifying the excel file. Otherwise, the excel file will not be exported.

1. To get the correlation, for either the student or the items/criteria:

call the function:
    ```
    return_correlation(original_data, is_student, flag)
    ```
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
    ```return_irregular_column_index(original_data, is_student)```
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

    detectDimenstion(matrix)
    sumStudentScore(matrix)
    sumItemScore(matrix)
    sortBasedOnStudent(matrix, studentSum)
    sortBasedOnItem(matrix, itemSum)
    cal_median(matrix, summation)
    cal_average(matrix, summation, number)
    retrieve_average_per_item(matrix, itemsum)
    transpose_matrix(matrix)
The above mentioned functions can be skipped while you read the code.
