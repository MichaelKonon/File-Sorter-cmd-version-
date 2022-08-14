import os
import time
start_time = time.time()
path_for_download_folder = "" #####Enter here folder for sorting
path_for_sorted_files = ""  #####Enter here finish folder
all_folders_in_down_folder = os.listdir(path_for_download_folder)
all_folders_in_sort_folder = os.listdir(path_for_sorted_files)

duplicate = True # if True - copies of files will be added (DUPLICATE),
                    # if False, the file will be replaced with the one that is in the "path_for_download_folder"
check_list_duplicate = []

list_of_files_types = {'Video': ['mp4', 'mov', 'avi', 'mkv', 'wmv', '3gp', '3g2', 'mpg', 'mpeg', 'm4v',
                                 'h264', 'flv', 'rm', 'swf', 'vob'],

                        'Data': ['sql', 'sqlite', 'sqlite3', 'csv', 'dat', 'db', 'log', 'mdb', 'sav',
                                'tar', 'xml'],

                        'Audio': ['mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'mpa', 'wma', 'wpl',
                                    'cda'],

                         'Image': ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg', 'tif',
                                    'tiff'],

                        'Archive': ['zip', 'rar', '7z', 'z', 'gz', 'rpm', 'arj', 'pkg', 'deb'],

                        'Text': ['pdf', 'txt', 'doc', 'docx', 'rtf', 'tex', 'wpd', 'odt'],

                        '3d': ['stl', 'obj', 'fbx', 'dae', '3ds', 'iges', 'step'],

                        'Presentation': ['pptx', 'ppt', 'pps', 'key', 'odp'],

                        'Spreadsheet': ['xlsx', 'xls', 'xlsm', 'ods'],

                        'Font': ['otf', 'ttf', 'fon', 'fnt'],

                        'Gif': ['gif'],

                        'Installer': ['dmg', 'exe'],

                        'apk': ['apk']

                        }


os.chdir(path_for_sorted_files)

lst_file = []
for files in os.walk(path_for_sorted_files, topdown=True):
    if len(files[2]) != 0:
        lst_file.append(files[2])

for folder in lst_file:
    for file in folder:
        if file != '.DS_Store':
            check_list_duplicate.append(file)
print("These are the files in the folder where the files are moved",check_list_duplicate)

for newfolder in list_of_files_types:
    if os.path.isdir(newfolder) == True:
        pass
    else:
        os.mkdir(newfolder)

os.chdir(path_for_download_folder)

for file in all_folders_in_down_folder:
    if os.path.isdir(file) == False:
        if file != '.DS_Store':
            print(file)
        if file in check_list_duplicate:
            if path_for_download_folder != path_for_sorted_files and file in check_list_duplicate and duplicate == True:
                for typeof in list(list_of_files_types.items()):
                    for typeoftype in typeof:
                        if file.split('.')[-1] in typeoftype:
                            os.rename(os.path.abspath(file), path_for_sorted_files + '/' + typeof[0] + '/' + file.split('.')[0] + "(DUPLICATE)." + file.split('.')[1])
                            print('1')

            elif path_for_download_folder != path_for_sorted_files and file in check_list_duplicate and duplicate == False:
                for typeof in list(list_of_files_types.items()):
                    for typeoftype in typeof:
                        if file.split('.')[-1] in typeoftype:
                            os.rename(os.path.abspath(file), path_for_sorted_files + '/' + typeof[0] + '/' + file)
                            print('2')

            elif path_for_download_folder == path_for_sorted_files and file in check_list_duplicate and duplicate == True:
                for typeof in list(list_of_files_types.items()):
                    for typeoftype in typeof:
                        if file.split('.')[-1] in typeoftype:
                            os.rename(os.path.abspath(file), path_for_sorted_files + '/' + typeof[0] + '/' + file.split('.')[0] + "(DUPLICATE)." + file.split('.')[1])
                            print('3')

            elif path_for_download_folder == path_for_sorted_files and file in check_list_duplicate and duplicate == False:
                for typeof in list(list_of_files_types.items()):
                    for typeoftype in typeof:
                        if file.split('.')[-1] in typeoftype:
                            os.rename(os.path.abspath(file), path_for_sorted_files + '/' + typeof[0] + '/' + file)
                            print('4')
        elif file not in check_list_duplicate:
            for typeof in list(list_of_files_types.items()):
                for typeoftype in typeof:
                    if file.split('.')[-1] in typeoftype:
                        os.rename(os.path.abspath(file), path_for_sorted_files + '/' + typeof[0] + '/' + file)
                        print('5')

print('Done!')
print("Time spent sorting",time.time() - start_time, time.ctime())