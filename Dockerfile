FROM mypython3:0.0.1

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV FLASK_APP=index.py

WORKDIR /src
COPY requirements.txt /src/
RUN pip3 install -r requirements.txt
COPY index.py /src/

CMD ["flask", "run", "-h", "0.0.0.0"]