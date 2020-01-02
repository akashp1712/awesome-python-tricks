FROM python:3.8.1-alpine3.10

LABEL "com.github.actions.name"="Generate Index"
LABEL "com.github.actions.description"="Automatically list out files in json format and write to a file"
LABEL "com.github.actions.icon"="corner-up-left"
LABEL "com.github.actions.color"="red"

LABEL "repository"="https://github.com/akashp1712/python-everyday/generate-index"
LABEL "homepage"=""
LABEL "maintainer"="Akash <akashp1712@gmail.com>"

ADD create_file_list.py /create_file_list.py
ENTRYPOINT ["python", "/create_file_list.py"]
