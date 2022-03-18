FROM python:3

ADD main.py ./
COPY url.txt ./

RUN pip install requests
RUN pip install schedule
RUN pip install datetime

ENV TZ=Europe/Warsaw

CMD [ "python", "-u", "./main.py" ]
