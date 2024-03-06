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

response = requests.get(apiUrl + '/list', headers={"Authorization": AuthorizationKey})
server_hashes = neocities_hashes_to_array(response.text)
print("Files on the server:", len(server_hashes))
local_hashes = dim_hashes_to_array(read_file_into_string('hashes.txt'))
print("Files in workspace:", len(local_hashes))

#================================================================
#Neocities functions

def remote_delete(path):

    return

def remote_upload(path, pathSource):

    return

#================================================================
#Analyze and Update

#post_data = {
#    'password': config['password']
#}
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
            #Upload and replace old file
            print("M:", l)
            #post_data['command'] = 'M'
            #post_data['target'] = l[0]
            #post_data['hash'] = l[1]
            #file = open(websitePath + l[0], 'rb')
            #response = requests.post(config['address'], data = post_data, files = {'file': (l[0], file)})
            #print(response.text)

while True:
    try:
        server_hashes.remove(False)
    except:
        break
for s in server_hashes:
    #Delete file
    print("D:", s)
    #remote_delete(s[0])
    #post_data['command'] = 'D'
    #post_data['target'] = s[0]
    #response = requests.post(config['address'], data = post_data)
    #print(response.text)

for l in local_hashes:
    #Upload new file
    print("A:", l)
    #remote_delete(s[0])
    #post_data['command'] = 'A'
    #post_data['target'] = l[0]
    #post_data['hash'] = l[1]
    #file = open(websitePath + l[0], 'rb')
    #response = requests.post(config['address'], data = post_data, files = {'file': (l[0], file)})
    #print(response.text)

print('Done.')