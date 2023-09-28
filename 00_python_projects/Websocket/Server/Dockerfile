FROM python:3

WORKDIR /app
COPY Server.py .
COPY html/ html/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD [ "python", "Server.py"]
