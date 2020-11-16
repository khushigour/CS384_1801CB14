import os
import csv
import shutil
import pandas as pd

def del_create_analytics_folder():
    # del the analytics folder including subfolder
    # mkdir the analytics folder (only mkdir)
    path = os.path.join(os.getcwd(),r'grades')
    if os.path.exists(path):
        shutil.rmtree(path,ignore_errors=True)
        os.mkdir(path)
    else:
        os.mkdir(path)
    pass

def student_res():
    pass

del_create_analytics_folder()
# student_res()
    


       
        

