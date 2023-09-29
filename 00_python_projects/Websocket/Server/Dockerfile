FROM python:3

WORKDIR /app
COPY Server.py .
COPY templates/ templates/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 80
CMD [ "python", "Server.py"]
