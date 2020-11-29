import os
import csv
import shutil
import math
import pandas as pd

def del_create_analytics_folder():
    path = os.path.join(os.getcwd(),r'groups')
    if os.path.exists(path):
        shutil.rmtree(path,ignore_errors=True)
        os.mkdir(path)
    else:
        os.mkdir(path)
    pass


def group_allocation(filename, number_of_groups):
    # Entire Logic 
    del_create_analytics_folder()
    
    pass

filename = "Btech_2020_master_data.csv"
number_of_groups = 12
group_allocation(filename, number_of_groups)