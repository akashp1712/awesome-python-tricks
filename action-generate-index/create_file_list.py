# -*- coding: utf-8 -*-

import glob
import json
import os

path = 'data'
extension = '.json'
metadata_file = 'data/0_metadata.json'

# if given empty path, it starts from the current directory
files = [f for f in glob.glob(path + "**/*" + extension, recursive=True)]


file_list = []

for file in files:
    # Construct the metadata json
    filename = os.path.basename(file)
    file_list.append(filename)

metadata = {}
metadata.setdefault("files", file_list)
# add to the file
with open(metadata_file, 'r+') as f:
    f.write(json.dumps(metadata, indent=1))
    f.close()
