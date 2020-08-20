import os,shutil
from PyQt5.QtWidgets import QFileDialog

def images_in_the_directorys(source_path):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(source_path):
        for file in f:
            #gets the images with the bellow ext
            if file.endswith(".jpg") or file.endswith(".png"):
                
                files.append(os.path.join(r, file))

    return files
# button.setToolTip("&lt;h1&gt;This Is Click Button&lt;h1&gt;")
def destination_dir_folder(Destination):
    list_subfolders_with_paths = [f.path for f in os.scandir(Destination) if f.is_dir()]
    a =[]
    for lists in list_subfolders_with_paths:
 
        lists = os.path.realpath(lists)
        k = os.path.basename(os.path.normpath(lists))
        # print(k)
        a.append(k)
    return(a)
def copy_files(files,source_folder,destination_folder, folders_list, location_list):
    # files = ['file1.txt', 'file2.txt', 'file3.txt']

    for Ll in location_list:
        for fl in files:
            if fl == os.path.basename(Ll):
                for folder in folders_list:
                # f = os.path.realpath(source_folder+"/"+f)
                    shutil.copy(Ll, destination_folder+"/"+folder)
    return


def folder_open():
    source_dir = "c:/"
    text_file = open("./txt_files/source_dir.txt", "r")
    n = text_file.read()
    print(n)
    text_file.close()
