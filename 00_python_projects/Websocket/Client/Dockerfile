FROM python:3

WORKDIR /app
COPY Client.py .
COPY html/ index.html
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD [ "python", "Client.py"]