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
        
    pass


def country():
         
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
