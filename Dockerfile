FROM mypython3:0.0.1

COPY index.py requirements.txt /src/

WORKDIR /src
RUN pip3 install -r requirements.txt

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV FLASK_APP=index.py

CMD ["flask", "run", "-h", "0.0.0.0"]