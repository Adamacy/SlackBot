FROM python:3

ADD main.py ./
COPY url.txt ./

RUN pip install requests
RUN pip install schedule

CMD [ "python", "./main.py" ]
