import os 
import re
def rename_FIR(folder_name):
    x = os.getcwd() 
    path = os.path.join(os.getcwd(),'Subtitles/' + folder_name)
    os.chdir(path)
    pattern1 = re.compile(r"([Episode|Ep] )([0-9]*)")
    pattern3 = re.compile(r'(mp4|srt)')
    padding_ep = int(input('Padding for Episode for FIR: '))
    for file in os.listdir(path):
        season_ep = pattern1.search(file)
        ep_no = season_ep.group(2)
        if padding_ep< len(str(ep_no)):
            padding_ep = len(str(ep_no))
        end = pattern3.search(file)
        initial_path = os.path.join(path,file)
        new_name = 'FIR'+ ' - Episode ' +((padding_ep) - len(str(ep_no)))*'0' + str(ep_no)  + '.'+ end.group()
        final_path = os.path.join(path,new_name)
        if os.path.isfile(final_path):
            os.remove(initial_path)
        else:
            os.rename(initial_path, new_name)
    os.chdir(x)   
    

def rename_Game_of_Thrones(folder_name):
    x = os.getcwd() 
    path = os.path.join(os.getcwd(),'Subtitles/' + folder_name)
    os.chdir(path)
    pattern1 = re.compile(r'([0-9]*)x([0-9]*)')
    pattern2 = re.compile(r'(- )([A-Za-z ]+)')
    pattern3 = re.compile(r'(mp4|srt)')
    padding_s = int(input('Padding for Season for Game of Thrones: '))
    padding_ep = int(input('Padding for Episode for Game of Thrones: '))
    for file in os.listdir(path):
        season_ep = pattern1.search(file)
        season_no = int(season_ep.group(1))
        if padding_s< len(str(season_no)):
            padding_s = len(str(season_no))
        ep_no = int(season_ep.group(2))
        if padding_ep<len(str(ep_no)):
            padding_ep = len(str(ep_no))
        ep_name = pattern2.search(file)
        end = pattern3.search(file)
        initial_path = os.path.join(path,file)
        new_name = 'Game of Thrones'+ ' - Season ' + ((padding_s)-len(str(season_no)))*'0' + str(season_no) + ' Episode ' +((padding_ep) - len(str(ep_no)))*'0' + str(ep_no)  + ' - ' + str(ep_name.group(2)) + '.'+ end.group()
        final_path = os.path.join(path,new_name)
        if os.path.isfile(final_path):
            os.remove(initial_path)
        else:
            os.rename(initial_path, new_name)
    os.chdir(x)



def rename_Sherlock(folder_name):
    x = os.getcwd() 
    path = os.path.join(os.getcwd(),'Subtitles/' + folder_name)
    os.chdir(path)
    pattern1 = re.compile(r'([0-9]*)\.?E([0-9]*)')
    pattern3 = re.compile(r'(mp4|srt)')
    padding_s = int(input('Padding for Season for Sherlock: '))
    padding_ep = int(input('Padding for Episode for Sherlock: '))
    for file in os.listdir(path):
        season_ep = pattern1.search(file)
        season_no = int(season_ep.group(1))
        if padding_s< len(str(season_no)):
            padding_s = len(str(season_no))
        ep_no = int(season_ep.group(2))
        if padding_ep<len(str(ep_no)):
            padding_ep = len(str(ep_no))
        end = pattern3.search(file)
        initial_path = os.path.join(path,file)
        new_name = 'Sherlock'+ ' - Season ' + ((padding_s)-len(str(season_no)))*'0' + str(season_no) + ' Episode ' +((padding_ep) - len(str(ep_no)))*'0' + str(ep_no) + '.'+ end.group()
        final_path = os.path.join(path,new_name)
        if os.path.isfile(final_path):
            os.remove(initial_path)
        else:
            os.rename(initial_path, new_name)
    os.chdir(x)

 
    

def rename_Suits(folder_name):
    x = os.getcwd() 
    path = os.path.join(os.getcwd(),'Subtitles/' + folder_name)
    os.chdir(path)
    pattern1 = re.compile(r'([0-9]*)x([0-9]*)')
    pattern2 = re.compile(r'(- )([A-Za-z ]+)')
    pattern3 = re.compile(r'(mp4|srt)')
    padding_s = int(input('Padding for Season for Suits: '))
    padding_ep = int(input('Padding for Episode for Suits: '))
    for file in os.listdir(path):
        season_ep = pattern1.search(file)
        season_no = int(season_ep.group(1))
        if padding_s< len(str(season_no)):
            padding_s = len(str(season_no))
        ep_no = int(season_ep.group(2))
        if padding_ep<len(str(ep_no)):
            padding_ep = len(str(ep_no))
        ep_name = pattern2.search(file)
        end = pattern3.search(file)
        initial_path = os.path.join(path,file)
        new_name = 'Suits'+ ' - Season ' + ((padding_s)-len(str(season_no)))*'0' + str(season_no) + ' Episode ' +((padding_ep) - len(str(ep_no)))*'0' + str(ep_no)  + ' - ' + str(ep_name.group(2)) + '.'+ end.group()
        final_path = os.path.join(path,new_name)
        if os.path.isfile(final_path):
            os.remove(initial_path)
        else:
            os.rename(initial_path, new_name)
    os.chdir(x)

    

def rename_How_I_Met_Your_Mother(folder_name):
    x = os.getcwd()
    path = os.path.join(os.getcwd(),'Subtitles/' + folder_name)
    os.chdir(path)
    pattern1 = re.compile(r'([0-9]*)x([0-9]*)')
    pattern3 = re.compile(r'(mp4|srt)')
    padding_s = int(input('Padding for Season for How I Met Your Mother: '))
    padding_ep = int(input('Padding for Episode for How I Met Your Mother: '))
    for file in os.listdir(path):
        season_ep = pattern1.search(file)
        season_no = season_ep.group(1)
        if padding_s< len(str(season_no)):
            padding_s = len(str(season_no))
        ep_no = int(season_ep.group(2))
        if padding_ep<len(str(ep_no)):
            padding_ep = len(str(ep_no))
        a = re.split('\.HDTV|\.FoV|\.720p|\.1080p|\.en', str(file))
        y = re.split(' - ', a[0])
        ep_name = y[-1]
        end = pattern3.search(file)
        if ep_name !='':
            initial_path = os.path.join(path,file)
            new_name = 'How I Met Your Mother'+ ' - Season ' + ((padding_s)-len(str(season_no)))*'0' + str(season_no) + ' Episode ' +((padding_ep) - len(str(ep_no)))*'0' + str(ep_no)  + ' - ' + ep_name + '.'+ end.group()
            final_path = os.path.join(path,new_name)
            os.rename(initial_path, new_name)
        else:
            continue
    os.chdir(x)

x = input('''
Enter 1 for 'FIR' series
Enter 2 for 'Game of Thrones' series
Enter 3 for 'Sherlock' series
Enter 4 for 'Suits' series
Enter 5 for 'How I Met Your Mother' series
''')   

if x =='1':
    rename_FIR('FIR')
if x =='2':
    rename_Game_of_Thrones('Game of Thrones')
if x =='3':
    rename_Sherlock('Sherlock')
if x =='4':
    rename_Suits('Suits')
if x =='5':
    rename_How_I_Met_Your_Mother('How I Met Your Mother')
