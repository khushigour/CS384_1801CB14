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
    pass

 
    

def rename_Suits(folder_name):
    pass

    

def rename_How_I_Met_Your_Mother(folder_name):
    pass

    

# rename_FIR('FIR')
rename_Game_of_Thrones('Game of Thrones')
