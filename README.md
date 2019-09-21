# Instructions for Building and Executing

## Run On Our Temporary Server

Simply go to http://45.113.232.214/index.html

You could use **[repo_root_path]/testdata/SampleAssessmentResult.xlsx** as test data.
If you are going to use your own test data, please follow Step5 below.

## Run On Your Local PC

### Step1. Install Python

Makes sure you have `python3` and `pip` installed. `Python 3.7` was confirmed to work, lower versions of `Python3` were not tested.

`Python 2.x` were confirmed **NOT** working.


### Step2. Install Python librarys

`pip3 install 'flask>=1.1.1' pandas xlsxwriter xlrd`

If you do not have a shortcut for pip, use:
`python3 -m pip install 'flask>=1.1.1' pandas xlsxwriter xlrd`

Please notice some lower versions of flask were confirmed **NOT** working.


### Step3. Install Git, and clone our repo

`git -c http.sslVerify=false clone https://bitbucket.cis.unimelb.edu.au:8445/scm/swen900142019rvquoll/swen90014-2019-rv-quoll.git`


### Step4. Run

`cd swen90014-2019-rv-quoll`

`flask run`

If you do not have a shortcut for flask, use:
`python3 -m flask run`

The server should be listening on http://127.0.0.1:5000 (defualt setting of flask)


### Step5. Test

You could use **[repo_root_path]/testdata/SampleAssessmentResult.xlsx** as test data.

**Note:**
In this sprint, we have not handled possible errors or exceptions. 
If you are going to use your own test data, please notice that the format of the Excel file must follow all rules below:

1. File extension **MUST** be .xls or .xlsx
2. Marked data **MUST** exist in the first worksheet
3. Column A of that worksheet MUST be student name (or id).
4. Row 1 **MUST** be item name (or id).
5. Starting from column B and row 2, mark data **MUST** present.
6. No other data like "total" column or row allowed. Those will be automatically calculated by our program.


### Instructions Summary:

`git -c http.sslVerify=false clone https://bitbucket.cis.unimelb.edu.au:8445/scm/swen900142019rvquoll/swen90014-2019-rv-quoll.git`

`cd swen90014-2019-rv-quoll`

`pip3 install Flask pandas xlsxwriter xlrd`

`flask run`
