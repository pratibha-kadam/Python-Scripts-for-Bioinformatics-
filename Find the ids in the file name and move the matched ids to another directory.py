import os
import re
import shutil
out_file = open("EPTB_ids_no_file.txt","w")
id_list = open("EPTB_ids.txt").read().splitlines()
file_list = open("all_vcf.txt").read().splitlines()
# id_list = ["1","2","3","23","60"]
# file_list = ["1.tab","2.tab","3.tab","4.tab","5.tab","6.tab","7.tab","11.tab","23.tab"]

EPTB_files= []
EPTB_not_found = []

# Iterate through the ID list and check if it is present in the file_list
for id in id_list:
    # Create the expected file name by appending '.tab' to the id
    file_name = f"{id}.tab"
    
    # Check if the file is present in the file_list
    if file_name in file_list:
        EPTB_files.append(file_name)  # Add to PTB if found
    else:
        # EPTB_not_found.append(id)  # Add to PTB_not_found if not found
        out_file.write(id+"\n")
# Print the results
# print("PTB files:", PTB)
#print("EPTB_not_found IDs:", EPTB_not_found)
# print(len(EPTB_files))
# print(len(EPTB_not_found))

# Move the files from one source to another
source = "."
destination = "./EPTB-files"

for f in EPTB_files:
    src_path = os.path.join(source, f)
    src_des = os.path.join(destination,f)
    print(f)
    shutil.move(src_path,src_des)


