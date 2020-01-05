FROM python:3.8.1-alpine3.10

LABEL "com.github.actions.name"="Generate Readme from data"
LABEL "com.github.actions.description"="Automatically generate readme from the json data files"
LABEL "com.github.actions.icon"="corner-up-left"
LABEL "com.github.actions.color"="red"

LABEL "repository"="https://github.com/akashp1712/python-everyday/generate-readme"
LABEL "homepage"=""
LABEL "maintainer"="Akash <akashp1712@gmail.com>"

ADD main.py /main.py
ENTRYPOINT ["python", "/main.py"]
