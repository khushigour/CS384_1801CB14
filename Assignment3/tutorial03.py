import csv
import os
import re
import shutil

keys_1 = [ 'id','full_name','country','email', 'gender','dob','blood_group','state']
keys_2 = [ 'id','first_name','last_name','country','email', 'gender','dob','blood_group','state']  

def del_create_analytics_folder():
    # del the analytics folder including subfolder
    # mkdir the analytics folder (only mkdir)
    path = os.getcwd()
    path1 = os.path.join(path,r'analytics')
    if os.path.exists(path1):
        shutil.rmtree(path1,ignore_errors=True)
        os.mkdir(path1)
    else:
        os.mkdir(path1)
    pass


def course():
    f1 = open('studentinfo_cs384.csv','r')
    reader = csv.reader(f1)
    path = os.path.join(os.getcwd(),r'analytics/course')
    os.mkdir(path)
    for row in reader:
        x = re.compile(r'^[0-9]{2}[012]{2}[A-Z]{2}[0-9]{2}$')
        if re.match(x, row[0]):
            y = row[0][4:6]
            y = y.lower()
            p = os.path.join(path,y)
            z = row[0][2:4]
            if z=='01':
                z = "btech"
            if z=='11':
                z = "mtech"
            if z=='12':
                z ="msc"
            if z=='21':
                z ="phd"
            q = os.path.join(p,z)
            a = row[0][0:2]+'_'+y+'_'+z+'.csv'
            r = os.path.join(q,a)
            if os.path.exists(p):
                if os.path.exists(q):
                    if not os.path.exists(r):
                        with open(r, 'a+', newline='') as f:
                            thewriter =csv.writer(f)
                            thewriter.writerow(keys_1) 
                    with open(r,'a+',newline='') as f:
                        thewriter = csv.writer(f) 
                        thewriter.writerow(row)
                else:
                    os.mkdir(q)
                    if not os.path.exists(r):
                        with open(r, 'a+', newline='') as f:
                            thewriter =csv.writer(f)
                            thewriter.writerow(keys_1)
                    with open(r,'a+',newline='') as f:
                        thewriter = csv.writer(f) 
                        thewriter.writerow(row)                    
            else:
                os.makedirs(q)
                if not os.path.exists(r):
                    with open(r, 'a+', newline='') as f:
                        thewriter =csv.writer(f)
                        thewriter.writerow(keys_1)
                with open(r,'a+',newline='') as f:
                    thewriter = csv.writer(f) 
                    thewriter.writerow(row)
        elif row[0]!='course':
            with open(os.path.join(path,'misc.csv'),'a+',newline='')as f:
                thewriter = csv.writer(f)
                thewriter.writerow(row)        
    pass


def country():
    f1 = open('studentinfo_cs384.csv','r')
    reader = csv.reader(f1) 
    path = os.path.join(os.getcwd(),r'analytics/country')
    os.mkdir(path)
    for row in reader:
        x = re.compile(r'^[a-zA-Z ]*$')
        if row[2]!='country':
            path1 = path+ '/' + row[2]+'.csv'
            if not os.path.exists(path1):
                with open(path1, 'a+', newline='') as f:
                    thewriter =csv.writer(f)
                    thewriter.writerow(keys_1)
            with open(path1, 'a+', newline='') as f:
                thewriter =csv.writer(f)
                thewriter.writerow(row)
        elif row[2]!='country':
            with open(path + '/misc.csv','a+',newline='')as f:
                thewriter = csv.writer(f)
                thewriter.writerow(row)                    
    pass


def email_domain_extract():

    pass


def gender():

    pass


def dob():

    pass


def state():
    
    pass


def blood_group():
  
    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():

    pass
