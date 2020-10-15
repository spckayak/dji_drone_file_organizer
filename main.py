#!/usr/bin/env python
import json, os
dirc = r"C:\Users\perez\Desktop\Ryan_Wedding"

def fileStructureBuild(dirc): #Build JSON Object, with file structure
    file_structure = {}
    file_structure['root_dir'] = str(dirc)
    structure = [] #List used for file of directories
    for root, directory, files in os.walk(dirc):
        for file in files:
            structure.append(os.path.join(root, file)) #Append Directory Path to file structure
    file_structure['availble_files'] = structure
    return file_structure


def preCheck(dirc): #Function to check vars file
    varsFile = dirc + r"\\vars.json"
    test = True
    if os.path.isfile(varsFile) and test == False: # If file exists
        try: #Load Json
            with open(varsFile) as json_file:
                data = json.loads(json_file)
        except: #File exists, no JSON found
            print("File exists, but no json found")
    else: #No file file found
        data = fileStructureBuild(dirc)
        with open(varsFile, 'w+') as json_file:
            json.dump(data, json_file)
    return data

if __name__ == "__main__":
    preCheck(dirc)

# def preCheck():
#Function to check vars file, to ensure varibles are set. 

#rewrite filenames with dateTime
#Seperate Images with 


#def define_vars():
#function to write or modify vars file