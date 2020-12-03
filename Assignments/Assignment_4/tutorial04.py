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
    # For making individual csv files
    res_df = pd.read_csv('acad_res_stud_grades.csv')
    with open('acad_res_stud_grades.csv') as file1:
        reader = csv.DictReader(file1)
        p=1
        for row in reader:
            Grades = ['AA', 'AB', 'BB', 'BC', 'CC', 'CD', 'DD', 'F', 'I']
            roll_num = row['roll']
            misc = False
            if(row['credit_obtained'] not in Grades):
                misc = True
            path = os.path.join(os.getcwd(),'grades')
            if misc:
                f_path = os.path.join(path, 'misc.csv')
                with open(f_path, 'a+', newline='') as f:
                    headers = ['roll','sem','year','sub_code','total_credits','credit_obtained','timestamp','sub_type']
                    entries = {'roll': row['roll'],'sem': row['sem'],'year':row['year'],'sub_code':row['sub_code'], 'total_credits': row['total_credits'],
                    'credit_obtained':row['credit_obtained'],'timestamp':row['timestamp'],'sub_type':row['sub_type'] }
                    writer = csv.DictWriter(f, delimiter=',', lineterminator='\n', fieldnames = headers)
                    if p==1:
                        writer.writeheader()
                        p=0
                    writer.writerow(entries)
            else:
                f_path = os.path.join(path, roll_num + '_individual.csv')
                f=0
                if not os.path.isfile(f_path):
                    f=1

                with open(f_path,'a+', newline='') as file2:
                    headers = ['Subject', 'Credits', 'Type', 'Grade', 'Sem']
                    start1 = {'Subject':'Roll: ' + roll_num, 'Credits': None, 'Type': None, 
                    'Grade': None, 'Sem': None}
                    start2 = {'Subject':'Semester Wise Details', 'Credits': None, 'Type': None, 
                    'Grade': None, 'Sem': None}            
                    entries = {'Subject':row['sub_code'], 'Credits': row['total_credits'], 'Type': row['sub_type'], 
                    'Grade': row['credit_obtained'], 'Sem': row['sem']}
                    writer = csv.DictWriter(file2, delimiter=',', lineterminator='\n', fieldnames = headers)
                    if f==1:
                        writer.writerow(start1)
                        writer.writerow(start2)
                        writer.writeheader()
                        # f=0
                    writer.writerow(entries)

    # For making overall csv files                
    path = os.path.join(os.getcwd(),'grades')
    for file in os.listdir(path):
        if '_individual.csv' not in file:
            continue
        one_roll = ''
        for i in file:
            if i == '_':
                break
            one_roll+= i
        # print(one_roll)
        f_path = os.path.join(path, file)
        df = pd.read_csv(f_path, skiprows = 2)
        Grades = {'AA':10, 'AB':9, 'BB':8, 'BC':7, 'CC':6, 'CD':5, 'DD':4, 'I':0, 'F':0}
        df_new = df.replace({'Grade': Grades})
        # print(df_new)
        List_sem = []
        List_sem_credits = []
        List_SPI = []
        max_sem = df['Sem'].max()
        for i in range(1, max_sem+1):
            List_sem.append(i)
            if i in df['Sem']:
                Sem_credits = df.loc[df['Sem'] == i, 'Credits'].sum()
            else:
                Sem_credits = 0
            List_sem_credits.append(Sem_credits)
            SPI = (df_new.loc[df_new['Sem']==i,'Grade']*df_new.loc[df_new['Sem']==i,'Credits']).sum()
            if Sem_credits!=0:
                SPI = round(SPI/Sem_credits,2)
            else:
                SPI = 0
            List_SPI.append(SPI)
        dict = {'Semester': List_sem, 'Semester Credits': List_sem_credits, 'Semester Credits Cleared': List_sem_credits, 'SPI': List_SPI}  
        df_overall = pd.DataFrame(dict)
        df_overall.reset_index(drop=True, inplace = True)
        df_overall['Total Credits'] = df_overall['Semester Credits'].cumsum(axis = 0)
        df_overall['Total Credits Cleared'] = df_overall['Semester Credits Cleared'].cumsum(axis=0)
        df_overall['CPI'] =round((df_overall['SPI']*df_overall['Semester Credits Cleared']).cumsum(axis=0)/df_overall['Total Credits Cleared'],2)
        # print(df_overall)
        
        f1_path = os.path.join(path, one_roll + '_overall.csv')
        field_name = ['Semester','Semester Credits', 'Semester Credits Cleared', 'SPI', 'Total Credits', 'Total Credits Cleared','CPI' ]
        with open(f1_path, 'a+', newline = '') as file:
            start1 = {'Semester':'Roll: ' + one_roll,'Semester Credits':None, 'Semester Credits Cleared': None, 'SPI': None, 'Total Credits': None, 'Total Credits Cleared': None,'CPI':None }
            writer = csv.DictWriter(file, fieldnames = field_name)
            writer.writerow(start1)
            writer.writeheader()
        df_overall.to_csv(f1_path, mode = 'a', header = False, index = False)

del_create_analytics_folder()
student_res()
    


       
        

