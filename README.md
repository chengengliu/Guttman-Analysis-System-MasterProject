Instructions for Building and Executing

Step1. Install Python

Makes sure you have python 3 and pip installed. Python 3.7 was confirmed to work, lower versions of Python 3 were not tested.

Python 2.x were confirmed NOT working.



Step2. Install Python librarys

pip3 install 'flask>=1.1.1' pandas xlsxwriter xlrd
If you do not have a shortcut for pip, use

python3 -m pip install 'flask>=1.1.1' pandas xlsxwriter xlrd
Please notice some lower versions of flask were confirmed NOT working.


Step3. Install Git, and clone our repo

git -c http.sslVerify=false clone https://bitbucket.cis.unimelb.edu.au:8445/scm/swen900142019rvquoll/swen90014-2019-rv-quoll.git


Step4. Run

cd swen90014-2019-rv-quoll
flask run

If you do not have a shortcut for flask, use

python3 -m flask run
The server should be listening on http://127.0.0.1:5000 (defualt setting of flask)


Step5. Test

You could use [repo_root_path]/testdata/SampleAssessmentResult.xlsx as test data.
If you are going to use your own test data, please notice that the format of the Excel file must follow all rules below:

a) File extension MUST be .xls or .xlsx
b) Marked data MUST exist in the first worksheet
c) Column A of that worksheet MUST be student name (or id).
d) Row 1 MUST be item name (or id).
e) Starting from column B and row 2, mark data MUST present.
f) No other data like "total" column or row allowed. Those will be automatically calculated by our program.

//Update readMe in 21 Sep 2019

Rubric Integrity Checker

This is the repository for Team Quoll

Instructions:

`git -c http.sslVerify=false clone https://bitbucket.cis.unimelb.edu.au:8445/scm/swen900142019rvquoll/swen90014-2019-rv-quoll.git`

`cd swen90014-2019-rv-quoll`

`pip3 install Flask pandas xlsxwriter xlrd`

`flask run`
