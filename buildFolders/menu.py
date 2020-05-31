import nuke
import build_prog_folders
import make_shot_folder

menu=nuke.menu('Nuke')
menu.addCommand('my_chemical_freelance/buildFolders/build_prog_folders') #lambda:build_prog_folders
menu.addCommand('my_chemical_freelance/buildFolders/make_shot_folder')  #lambda:make_shot_folder