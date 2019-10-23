# Module Usage Description


### Section I. Source Code Reading Instructions:

       This __init__.py file contains both helper functions(which has no relation with algorithms) and
    Algorithms implementation functions, as well as interface functions(used by other modules).
     Two interfaces functions that should be used by other modules are 'return_correlation(original_data, is_student, flag)' and
    'return_irregular_index(original_data, is_student,flag)', which will be introduced in further details in the following section.
   
However, even though we have two interfaces provided and actually used in ```app.py```, the main irregular detection is performed
under the function ```return_irregular_index```. In ```app.py``` we use ```return_irregular_index``` with ```flag``` default to 
```'Accumulation''``` since the result of applying ```'Accumulation''``` algorithm is the most accurate one. We do provide another 
algorithm for detecting irregular pattern, which is to calculate the local ```Similarity``` value of each item and pick any 
irregular. ```Similarity``` is defined as the cosine value between the current data and other data that is within the range. 
Whether to use ```Accumulation ``` or ```Similarity``` is the developer's choice. The flag ```Correlation``` is used only for local
excel exporting but not sent to the front-end page and you can see that in ```app.py```.
<br>
<br>
For the box detection and odd cells:
    
    in function odd_cells(matrix) and irregular_box(matrix)

<br>
For adjusting the threshold of irregular detection(currently our algorithm has the result of 19/20 when performs the regular 
data generation test). If you do want to adjust the threshold to adapt to your desired sensitivity, please go to the function:
    
    detect_item_rregualr(similarities, matrix) 
   


### Section II. Module usage (interface):


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

2. To get the irregular columns/irregualr student:

call the function:
    ```return_irregular_index(original_data, is_student,flag)```<br/>
Input Desciption:

    Original_data: where the input is the original data (it is supposed to be nested list)
    This function assumes that the input data is sorted. However, if the data is not sorted, the function will perform sorting
    inside.

    is_student: Is a boolean variable, can be either True or False. This boolean values specifies whether you want to get
    student correlation (row), or item/criteria correlation(column). For example,
    If 'is_student' is set to True, the program will return the correlation calculated for rows.

    Notice: For now I have not implemented the cluster algorithm for detecting unusual behaviour. This will be added in sprint3.
    Current method is to set a threshold value and to see if the value is below the threshold. 
3. To get the box: 

call the function:
    
    ```irregular_box(matrix)``` where the matrix is the input data.
4. To get the odd cells:

call the fucntion:
    
    odd_cells(matrix) where the matrix is the input data. 
### Section III. Helper functions:
    As mentioned in Section I, there are several helper functions only used for data re-formatting and sorting purposes.
    These functions can be skipped and has no relation with the algorithms implementations.
    The helper functions include:

    clean_input(original_data)
    sum_item_score(matrix)
    detect_full_score(matrix)
    cal_scorerate_accumulated_matrix(matrix, is_student)
    get_0staddv_index(matrix)
    in_danger_list(danger_list, current_index)
    irregular_calculation(matrix, flag, is_student)
    transpose_matrix(matrix)
The above mentioned functions can be skipped while you read the code.

