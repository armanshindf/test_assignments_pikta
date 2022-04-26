# test_assignments_pikta
To run those modules you may activate virtual environment and install dependencies from requirements.txt
    
1.  For run first example you need folder "input" from this repository in same directory as you save the module.
It creates "task1.xlsx" Excel file parsed from json files in "input" folder. 
Number of .json files is not limited, only by python or your os restrictions.
Also, it can parse json files with other keys for headers and columns, but with the same logic as in original task.
To run, you can type "python test_task_1_json_parser.py" in venv
    
2.   To start second example module, you need to specify commandline parametres in following syntax
(in virtual environment, if you dont have requests module system-wide installed): "python test_task_2_requests.py (an IFNS code) (an OKTMMF code)".
Example values are 7840 40913000 for ifns and oktmmf parametres, e.g. "python test_task_2_requests.py 7840 40913000".
It will output data from "https://service.nalog.ru/addrno.do" to terminal for correct input data and stable internet connection,
otherwise it will throw an exception

3.  Third module also can be executed via console or ide (for example, "python test_task_3_sqlite_db.py"). It creates(if not exist) 
Sqlite3 database in the same directory as script and do some terminal output as it proceed. 
 
