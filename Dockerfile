FROM python:3.7-alpine
ADD predict.py /
ADD hemingLib /hemingLib
WORKDIR /home/jc/Documents/project/my_new_docker_build/
RUN pip3 install python-dateutil & pip3 install datetime
CMD [ "python3", "./predict.py"]
