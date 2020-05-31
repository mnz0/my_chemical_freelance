#import nuke
import os
import sys
import errno #for folder exist exception



#ask_panel = nuke.Panel("Set path")
#path = ask_panel.addFilenameSearch('file path', '/tmp')

#if nuke.ask("Build folder tree?"):
    #make_folders()

#project_path = path
project_path = "d:\\_work\\RAID_TEST\\IN\\" 


current_dir = ''
SHOT_NAME = ""

folder_default_pattern = {
    "project_folder" : ["SRC", "WORK", "OUT"],
    "work_folder" : ["nuke", "track", "houdini"], 
    "out_folder" : ["DAILIES","DPX"]
}

file_types = {
	'media_formats': ['dpx', 'exr', 'png', 'tiff', 'jpeg', 'hdr', 'rat', 'tga'], 
	'media_containers': ['mp4', 'mov', 'avi', 'mpeg', 'webm'],  
	'archives': ['zip', 'rar', '7zip', 'tar']} 

def get_files_and_folders_name(file_path_folder):
    
	folder_list = []
	file_list = []
	archives = []

	for f_check in os.listdir(file_path_folder):

		to_check = os.path.join(file_path_folder, f_check)  

		if os.path.isfile(to_check) and os.path.splitext(to_check)[1][1:] in file_types['media_formats']:
			 file_list.append(to_check)

		if os.path.isfile(to_check) and os.path.splitext(to_check)[1][1:] in file_types['media_containers']:
			 file_list.append(to_check)

		if os.path.isfile(to_check) and os.path.splitext(to_check)[1][1:] in file_types['archives']:
			 archives.append(to_check)

		if os.path.isdir(to_check): # Folder section 
			folder_list.append(to_check)
			
	return file_list, folder_list, archives

def make_folders(file_path):
	try:
		os.mkdir(file_path)
		print("Folder {} was created".format(file_path))
	except OSError as e:
		if e.errno == errno.EEXIST:
			print('File or folder exist. Directory not created.')
		else:
			raise
		
def show_content(data_list): #Test function

	if (data_list)[0]:
		for i in data_list[0]:
			print(i)

	if (data_list)[1]:
		for i in data_list[1]:
			print(i)

	if (data_list)[2]:
		for i in data_list[2]:
			print(i)

	else: print("Nothing here")




lst = get_files_and_folders_name(project_path)

show_content(lst)


