# Instructions for Building and Executing

## Run On Our Temporary Server

Simply go to http://45.113.232.214/index.html

You could use **[repo_root_path]/testdata/SampleAssessmentResult.xlsx** as test data.
If you are going to use your own test data, please follow Step5 below.

## Run On Your Local PC

### Step1. Install Python

Makes sure you have `python3` and `pip` installed. `Python 3.7` was confirmed to work, lower versions of `Python3` were not tested.

`Python 2.x` were confirmed **NOT** working.


### Step2. Install Python libraries

`pip3 install 'flask>=1.1.1' pandas xlsxwriter xlrd`

If you do not have a shortcut for pip, use
`python3 -m pip install 'flask>=1.1.1' pandas xlsxwriter xlrd`
instead.

Please notice some lower versions of flask were confirmed **NOT** working.


### Step3. Install Git, and clone our repo

`git -c http.sslVerify=false clone https://bitbucket.cis.unimelb.edu.au:8445/scm/swen900142019rvquoll/swen90014-2019-rv-quoll.git`


### Step4. Run

`cd swen90014-2019-rv-quoll`

`flask run`

If you do not have a shortcut for flask, use
`python3 -m flask run`

The server should be listening on http://127.0.0.1:5000 (defualt setting of flask)


### Step5. Test
To run all back-end unit tests: `python3 test.py` 

For mannual test, you could use **[repo_root_path]/testdata/SampleAssessmentResult.xlsx** as test data.

**Note:**
In this sprint, we have not handled possible errors or exceptions yet. 
If you are going to use your own test data, please notice that the format of the Excel file must follow all rules below:

1. File extension **MUST** be .xls or .xlsx
2. Marked data **MUST** exist in the first worksheet
3. Column A of that worksheet **MUST** be student name (or id).
4. Row 1 **MUST** be item name (or id).
5. Starting from column B and row 2, mark data **MUST** present.
6. No other data like "total" column or row allowed. Those will be automatically calculated by our program.<br/>

# Code Commit and Branch Policy
## Branch Policy:
    1. Every team member should keep one branch at least, under their control, for which they should develop the project and add features. 
    2. The 'master' branch is under the control of Baigong Li. Every pull requests made by other team members must be 
    reviewed by him, before the pull request is closed. 
    3. There is no need to create one branch for each feature that the team member developed. However, if you do feel 
    like it is better to do so, feel free to add branch that named with the feature name. The naming should be clear 
    and in-confusing, so that other team members an easily get the ideas of the branch. 
    4. After sprint finished, branches can be closed, in order to reduce confusion in later sprint 3. 
<br />

## Commit Policy:
    1. Every team member who wants to commit to the project, must not push their code directly to the master branch. 
    2. Every team member who submits the pull request, must have another team member's review, if your current work has 
    modified his/her code. 
    3. Every team member who modified other team member's code, must inform him/her. 
    4. Every team member who wants to merge own branch to the master branch/create pull requests to master branch, must 
    be review by Baigong Li before closing pull requests, since he is in charge of combining front-end and back-end together. 
