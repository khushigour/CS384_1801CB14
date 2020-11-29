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

    #Part-4 Stat.csv file is creating
    head_4= []
    for i in range(1,number_of_groups+1):
        count_of_o = len(str(number_of_groups))-len(str(i))
        group_name = 'Group_G'+'0'*count_of_o +str(i) + '.csv'
        head_4.append(group_name)
    
    df_stats = pd.DataFrame(head_4, columns = ['group'])
    left = 0
    for i in df_Strength['BRANCH_CODE']:
        y = int(df_Strength[df_Strength['BRANCH_CODE']==i]['STRENGTH'])
        x = math.floor(y/number_of_groups)
        df_stats.loc[:,i] = x
        z = y - x*number_of_groups
        for j in df_stats[i]:
            index = left%number_of_groups
            df_stats.loc[index , i] = j+1
            left +=1
            z-=1
            if z==0:
                break
    
    col_list= list(df_stats)
    col_list.remove('group')
    sum_of_group = list(df_stats[col_list].sum(axis=1))
    df_stats.insert(1,'total',sum_of_group)
    path_4 = os.path.join(initial_path,r'stats_grouping.csv')
    df_stats.to_csv(path_4, header = True, index = False)

    #Part-3 Group_GXX files are created
    initial_val = {}
    for i in df_Strength['BRANCH_CODE']:
        initial_val[i] = 0

    for i in df_stats['group']:
        col_names = ['Roll', 'Name', 'Email']
        df_final_groups = pd.DataFrame(columns = col_names)
        for j in df_Strength['BRANCH_CODE']:
            no_in_group = int(df_stats[df_stats['group']==i][j])
            df_G = df[df['Branch']==j][initial_val[j]:initial_val[j]+no_in_group]
            initial_val[j] = initial_val[j]+no_in_group
            df_final_groups = pd.concat([df_final_groups,df_G],ignore_index=True)
        df_final_groups = df_final_groups.drop(df_final_groups.columns[-1], axis = 1)
        path_3 = os.path.join(initial_path,i)
        df_final_groups.to_csv(path_3, header = True, index = False)
    pass

filename = "Btech_2020_master_data.csv"
number_of_groups = 12
group_allocation(filename, number_of_groups)