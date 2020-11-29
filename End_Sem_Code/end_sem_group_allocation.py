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
    initial_path = os.path.join(os.getcwd(),r'groups')
    df = pd.read_csv(filename)
    df['Branch'] = df['Roll'].str.extract(r'([A-Za-z]{2})')
    Branches = df['Branch'].unique()

    # Part-1 Batch_Strength file is created
    df_Strength = pd.DataFrame(df['Branch'].value_counts().reset_index().values,columns =['BRANCH_CODE', 'STRENGTH'])
    df_Strength= df_Strength.sort_values(by =['STRENGTH', 'BRANCH_CODE'] , ascending=[0,1])
    path_1 = os.path.join(initial_path,r'Batch_Strength.csv')
    df_Strength.to_csv(path_1, header = True, index = False)

    # Part-2 Branch.csv file is created
    for i in Branches:
        df_Branch = df[df['Branch']==i]
        df_Branch = df_Branch.iloc[:,:-1]
        df_Branch = df_Branch.sort_values(by = 'Roll')
        Branch_name = i +'.csv'
        path_2 = os.path.join(initial_path,Branch_name)
        df_Branch.to_csv(path_2, header = True, index = False)
    pass

filename = "Btech_2020_master_data.csv"
number_of_groups = 12
group_allocation(filename, number_of_groups)