#================================================================
#libs

import os
import hashlib

#================================================================
#Functions

def calculate_file_hash(file_path, hash_algorithm="sha1", buffer_size=65536):
    # Initialize the chosen hashing algorithm
    hash_instance = hashlib.new(hash_algorithm)

    # Read the file in chunks to avoid loading the whole file into memory
    with open(file_path, "rb") as file:
        while chunk := file.read(buffer_size):
            hash_instance.update(chunk)

    # Return the hexadecimal representation of the hash
    return hash_instance.hexdigest()

#================================================================
#Main

#clear console
if os.system('clear'):
    os.system('cls')
print("Started...")

#Consts
targetPath = "website/"
outputFileName = 'hashes.txt'

#----------------------------------------------------------------
#Calculate hashes

temp = ''
with open(outputFileName, "w+") as writer:
    for root, dirs, files in os.walk(targetPath):
        for file in files:
            if file != outputFileName:
                file = os.path.join(root, file).replace("\\",'/')           
                temp = file[len(targetPath):] + ',' + calculate_file_hash(file) + ';'
                writer.write(temp + "\n")
                print(temp)

#----------------------------------------------------------------
#end

print("Finished!")