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

del_create_analytics_folder()
student_res()
    


       
        

