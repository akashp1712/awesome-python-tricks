# -*- coding: utf-8 -*-

import glob
import json
import os


def update_readme_file(new_file_list, data_folder_path, readme_file_path):
    # Inner function
    def generate_content(content_data):

        name = content_data['name']  # Type: str
        desc = content_data['desc']  # Type: str
        code = content_data['code']  # Type: list<str>

        template = ["- ### {}".format(name),
                    "\n",
                    "{}".format(desc),
                    "\n",
                    "```python",
                    "\n"]

        for line in code:
            template.append(str(line))
            template.append("\n")

        template.append("```")
        template.append("\n")

        return template

    readme_content = []
    # read the content of each file and append
    for file in new_file_list:
        file_path = os.path.join(data_folder_path, file)

        with open(file_path) as json_file:
            json_data = json.load(json_file)
            data = json_data['data']

        readme_content += generate_content(data)

    with open(readme_file_path, 'a+') as f:
        print(readme_content)
        f.writelines(readme_content)

    return True

def update_metadata_file(file_list, metadata_file_path):
    file_list.sort()

    metadata = {}
    metadata.setdefault("files", file_list)
    # add to the file
    with open(metadata_file_path, 'w+') as f:
        f.write(json.dumps(metadata, indent=1))

    return True

def get_data_files(data_folder_path):
    extension = '.json'

    # if given empty path, it starts from the current directory
    files = [f for f in
             glob.glob(data_folder_path + "**/*" + extension, recursive=True)]
    file_list = []

    for file in files:
        # Construct the metadata json
        filename = os.path.basename(file)
        file_list.append(filename)

    file_list.sort()
    return file_list


def get_current_files(metadata_file_path):
    with open(metadata_file_path) as json_file:
        data = json.load(json_file)
        return data['files']


if __name__ == '__main__':

    ## Algorithm
    # 1. Read existing metadata file and get the list of files
    # 2. Read all files from the `/data` folder
    # 3. Figure out the list of new files
    # 4. Update metadata file if required
    # 5. Write new content to README.md if required (Define template and describe)

    # Constants
    DATA_FOLDER_PATH = 'data'
    README_FILE_PATH = 'README.md'
    METADATA_FILE_PATH = os.path.join(DATA_FOLDER_PATH, '0_metadata.json')

    # 1. Read existing metadata file and get the list of files
    list_current_files = get_current_files(
        metadata_file_path=METADATA_FILE_PATH)
    print("Current files:" + str(list_current_files))

    # 2. Read all files from the `/data` folder
    list_updated_files = get_data_files(data_folder_path=DATA_FOLDER_PATH)
    print("Updated files: " + str(list_updated_files))

    # 3. Figure out the list of new files
    list_new_files = (list(set(list_updated_files) - set(list_current_files)))
    print("New files: " + str(list_new_files))

    # 4. Update metadata file if required
    if list_new_files:
        status = update_metadata_file(file_list=list_updated_files,
                             metadata_file_path=METADATA_FILE_PATH)
        print("Updated metadata file: " + str(status))

    if list_new_files:
        # 5. Append new content to README.md if required
        status = update_readme_file(new_file_list=list_new_files,
                           data_folder_path=DATA_FOLDER_PATH,
                           readme_file_path=README_FILE_PATH)
        print("Updated Readme file: " + str(status))

