import os 
from pathlib import Path
import logging



#logging string
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')  #print the status while running

project_name= 'cnnClassifier'


list_of_files =[
            ".git/workflows/.gitkeep",
            f"src/{project_name}/__init__.py",
            f"src/{project_name}/components/__init__.py",
            f"src/{project_name}/utils/__init__.py",
            f"src/{project_name}/config/__init__.py",
            f"src/{project_name}/config/configuration.py",
            f"src/{project_name}/pipeline/__init__.py",
            f"src/{project_name}/entity/__init__.py",
            f"src/{project_name}/constants/__init__.py",
            "config/cofig.yaml",
            "dvc.yaml",
            "params.yaml",
            "requirements.txt",
            "setup.py",
            "research/trials.ipynb",
            "templates/index.html",
            ".git/workflows/.gitkeep",

 
]

for filepath in list_of_files:
    filepath=Path(filepath)   # Converts the path in the pure form which is useful for OS
    filedir, filename = os.path.split(filepath) #Split the string from last '/' which indirectly gives filename and file filedirectory 


    if filedir!='':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating Directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filename)) or (os.path.getsize(filepath)==0):    #checks if the filename exists or not and if the file contains the code, no new file is created
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} is already exist")