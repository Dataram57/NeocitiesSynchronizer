#================================================================
#Libs

import requests
import os
import json
import subprocess

#================================================================
#Config

websitePath = "website/"
apiUrl = "https://neocities.org/api/"
config = json.load(open('config.json', 'r'))
AuthorizationKey = "Bearer " + config['apiKey']
AuthorizationHeader = {"Authorization": AuthorizationKey}

#================================================================
#Functions

def neocities_hashes_to_array(txt):
    arr = []
    obj = json.loads(txt)["files"]
    i = len(obj)
    while i > 0:
        i -= 1
        if('sha1_hash' in obj[i]):
            arr.append([obj[i]['path'], obj[i]['sha1_hash']])
    return arr

def neocities_folders_to_array(txt):
    arr = []
    obj = json.loads(txt)["files"]
    i = len(obj)
    while i > 0:
        i -= 1
        if not ('sha1_hash' in obj[i]):
            arr.append(obj[i]['path'])
    return arr

def dim_hashes_to_array(txt):
    arr = []
    i = -1
    f = txt.index(';')
    while f > -1:
        arr.append(txt[i + 1:f].replace("\n",'').split(','))
        arr[-1][0] = arr[-1][0].strip()
        i = f
        try:
            f = txt.index(';', i + 1)
        except:
            break
    return arr

def hash_array_to_folders(arr):
    folders = []
    i = len(arr)
    currentPath = ""
    f = 0
    while i > 0:
        i -= 1
        f = arr[i][0].rfind("/")
        if f == -1:
            continue
        currentPath = arr[i][0][0:f]
        f = len(folders)
        while f > 0:
            f -= 1
            if folders[f] == currentPath:
                f = -1
        if f == 0:
            folders.append(currentPath)
    return folders

def read_file_into_string(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            return file_content
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

#================================================================
#Calc hashes and clear screen

#hashes
subprocess.run(["python", "calc_hashes.py"])

#clear
if os.system('clear'):
    os.system('cls')
print("Started...")

#================================================================
#Load tables

response = requests.get(apiUrl + '/list', headers=AuthorizationHeader)
server_hashes = neocities_hashes_to_array(response.text)
server_folders = neocities_folders_to_array(response.text)
print("Files on the server:", len(server_hashes))
local_hashes = dim_hashes_to_array(read_file_into_string('hashes.txt'))
local_folders = hash_array_to_folders(local_hashes)
print("Files in workspace:", len(local_hashes))

#================================================================
#Local Fetch and Delete functions for neocities

def download(path):
    destination = websitePath + path
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    response = requests.get(config['websiteURL'] + path)
    if response.status_code == 200:
        # Save the file to the specified directory
        with open(destination, 'wb') as f:
            f.write(response.content)
        print("File downloaded successfully")
    else:
        print("Failed to download file")

def delete(path):
    path = websitePath + path
    if os.path.exists(path):
        os.remove(path)
        print("File deleted successfully.")
    else:
        print("File does not exist.")

def delete_folder(directory):
    directory = websitePath + directory
    if os.path.exists(directory):
        os.rmdir(directory)
        print("Directory removed successfully.")
    else:
        print("Directory does not exist.")

#================================================================
#Analyze and Download

i = -1
for s in server_hashes:
    i += 1
    for l in local_hashes:
        if s[0] == l[0]:
            break
    if s[0] == l[0]:
        local_hashes.remove(l)
        server_hashes[i] = False
        if s[1] != l[1]:
            #Download and replace old file
            print("U:", l)
            download(l[0])

while True:
    try:
        server_hashes.remove(False)
    except:
        break
for s in server_hashes:
    #Download new file
    print("F:", s)
    download(s[0])

for l in local_hashes:
    #Delete old file
    print("D:", l)
    delete(l[0])

#================================================================
#Deleting useless folders

for s in server_folders:
    i = len(local_folders)
    while i > 0:
        i -= 1
        if local_folders[i] == s:
            local_folders[i] = False
for l in local_folders:
    if l != False:
        print("DF:", l)
        delete_folder(l)

#================================================================
print('Done.')