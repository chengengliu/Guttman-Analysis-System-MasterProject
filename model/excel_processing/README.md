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
