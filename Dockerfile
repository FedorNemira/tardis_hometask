FROM python 3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED

WORKDIR /app

RUN apt-get update
RUN apt-get install gcc libc-dev libffi-dev jpeg-dev zlib-dev libjpeg
RUN apt-get install postgresql-dev


RUN pip install --upgrade pip


COPY ./requirements.txt . 


RUN pip install -r requirements.txt


COPY . .
ENTRYPOINT ["/app/entrypoint.sh"]