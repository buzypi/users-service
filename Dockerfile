FROM python:3.9

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV FLASK_APP=index.py

WORKDIR /src
RUN apt-get update && apt-get -y install libgirepository1.0-dev \
  && rm -rf /var/lib/apt/lists/*
COPY requirements.txt /src/
RUN pip3 install -r requirements.txt
COPY index.py /src/

CMD ["flask", "run", "-h", "0.0.0.0"]
