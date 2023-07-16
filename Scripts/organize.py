from fileinput import filename
import os
import shutil
############################################################
def criatedir(endDir,foldername):
    for file in getPathfiles:#for loop to list(getPathfiles)
        if file.endswith((endDir)):#if the files name end docx git this file
            if not os.path.exists(foldername):#if not Word files exst 
                os.mkdir(foldername)#criate folder "Word files"
            shutil.copy(file ,foldername)# copy the file dirictory in folder "Word files"
            if file != "organize.py":
                os.remove(file)# remove the file 
                print("Done!")
############################################################
file_path=os.path.dirname(os.path.realpath(__file__))#the file path
getPathfiles=os.listdir(file_path)#list in files
############################################################
criatedir(".rtf","Word files")
criatedir(".pdf","PDF files")
criatedir(".docx","Word files")
criatedir(".mp4","videw files")
criatedir(".mp3","Voise files")
criatedir(".exe","EXE files")
criatedir(".jar","EXE files")
criatedir(".gz","ZIP files")
criatedir(".rar","ZIP files")
criatedir(".txt","TEXT files")
criatedir(".php","PHP files")
criatedir(".zip","ZIP files")
criatedir(".jpg","PNG files")
criatedir(".png","PNG files")
criatedir(".PNG","PNG files")
criatedir(".jpeg","PNG files")
criatedir(".ini","EXE files")
criatedir(".html","HTML files")
criatedir(".xlsx","Word files")
criatedir(".fprg","flowtchart files")
criatedir(".py","Python files")
############################################################