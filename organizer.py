import os
import shutil


print(os.getcwd())

def organize_stuff(path):
    files = os.listdir(path)
    for file in files:   
        # print(file)
        if os.path.isfile(file):
            extension = file.split('.')[1]
            print(file.split())
            # # move images to image folder
            if 'jpg' in file.split('.') or 'png' in file.split('.'):
                check_type_and_move(extension, file, path, 'images')


            # move videos to videos folder
            if 'mp4' in file.split('.') or 'mkv' in file.split('.'):
                check_type_and_move(extension, file, path, 'videos')


            # move applications to image applications fodler
            if 'exe' in file.split('.') or 'deb' in file.split('.'):
                check_type_and_move(extension, file, path, 'applications')

            # move zip to image compressed folders
            if 'rar' in file.split('.') or 'zip' in file.split('.') or 'tar' in file.split('.') or 'gz' in file.split('.'):
                check_type_and_move(extension, file, path, 'compressed')

            # move docs to  documents folder
            if 'docx' in file.split('.') or 'pdf' in file.split('.'):
                check_type_and_move(extension, file, path, 'documents')


def check_type_and_move(extension, file_name, source_folder, destination_folder):
    if not os.path.exists(source_folder+destination_folder+'/'):
         os.makedirs(source_folder+destination_folder+'/')
    shutil.move(source_folder+file_name, source_folder+destination_folder+"/")

organize_stuff(os.getcwd()+"/")