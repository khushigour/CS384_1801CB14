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
    f1 = open('studentinfo_cs384.csv','r')
    reader = csv.reader(f1)
    path = os.path.join(os.getcwd(),r'analytics/email_domain')
    os.mkdir(path)
    for row in reader:
        x = re.compile(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z.]{2,10}$')
        if re.match(x,row[3]):
            y = row[3].index('@')+1
            s=''
            while(row[3][y]!='.'):
                s += row[3][y]
                y+=1
            path1= path  +'/' + s +'.csv'
            if not os.path.exists(path1):
                with open(path1, 'a+', newline='') as f:
                    thewriter =csv.writer(f)
                    thewriter.writerow(keys_1)
            with open(path1, 'a+', newline='') as f:
                thewriter = csv.writer(f)
                thewriter.writerow(row)
        else:
            with open(path + '/misc.csv','a+',newline='')as f:
                thewriter = csv.writer(f)
                thewriter.writerow(row)
    pass


def gender():
    f1 = open('studentinfo_cs384.csv','r')
    reader = csv.reader(f1)
    path = os.path.join(os.getcwd(),r'analytics/gender')
    os.mkdir(path)
    for row in reader:
        x = re.compile(r'^Female|Male$')
        if re.match(x,row[4]):
            path1 = path +'/' + row[4].lower() + '.csv'
            if not os.path.exists(path1):
                with open(path1, 'a+', newline='') as f:
                    thewriter =csv.writer(f)
                    thewriter.writerow(keys_1)
            with open(path1, 'a+', newline='') as f:
                thewriter = csv.writer(f)
                thewriter.writerow(row) 
        elif row[4]!= 'gender':
            with open(path + '/misc.csv','a+',newline='')as f:
                thewriter = csv.writer(f)
                thewriter.writerow(row)
    pass


def dob():
    f1 = open('studentinfo_cs384.csv','r')
    reader = csv.reader(f1)
    path = os.path.join(os.getcwd(),r'analytics/dob')
    os.mkdir(path)
    for row in reader:
        x = re.compile(r'^[0-9]{1,2}-[0-9]{1,2}-[0-9]{4}$')
        if re.match(x, row[5]):
            y = int(row[5][-4:])
            if y>=1995 and y<=1999:
                path1 = path + '/bday_1995_1999.csv'
                if not os.path.exists(path1):
                    with open(path1, 'a+', newline='') as f:
                        thewriter =csv.writer(f)
                        thewriter.writerow(keys_1)
                with open(path1, 'a+', newline='') as f:
                    thewriter = csv.writer(f)
                    thewriter.writerow(row)                
            if y>=2000 and y<=2004:
                path2 = path + '/bday_2000_2004.csv'
                if not os.path.exists(path2):
                    with open(path2, 'a+', newline='') as f:
                        thewriter =csv.writer(f)
                        thewriter.writerow(keys_1)
                with open(path2, 'a+', newline='') as f:
                    thewriter = csv.writer(f)
                    thewriter.writerow(row) 
            if y>=2005 and y<=2009:
                path3 = path + '/bday_2005_2009.csv'
                if not os.path.exists(path3):
                    with open(path3, 'a+', newline='') as f:
                        thewriter =csv.writer(f)
                        thewriter.writerow(keys_1)
                with open(path3, 'a+', newline='') as f:
                    thewriter = csv.writer(f)
                    thewriter.writerow(row) 
            if y>=2010 and y<=2014:
                path4 = path + '/bday_2010_2014.csv'
                if not os.path.exists(path4):
                    with open(path4, 'a+', newline='') as f:
                        thewriter =csv.writer(f)
                        thewriter.writerow(keys_1)
                with open(path4, 'a+', newline='') as f:
                    thewriter = csv.writer(f)
                    thewriter.writerow(row) 
            if y>=2015 and y<=2020:
                path5 = path + '/bday_2015_2020.csv'
                if not os.path.exists(path5):
                    with open(path5, 'a+', newline='') as f:
                        thewriter =csv.writer(f)
                        thewriter.writerow(keys_1)
                with open(path5, 'a+', newline='') as f:
                    thewriter = csv.writer(f)
                    thewriter.writerow(row) 
        elif row[5]!='dob':
            with open(path + '/misc.csv', 'a+', newline='') as f:
                thewriter = csv.writer(f)
                thewriter.writerow(row) 
    pass


def state():
    
    pass


def blood_group():
  
    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():

    pass
