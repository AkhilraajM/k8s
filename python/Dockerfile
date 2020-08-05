FROM python:3.8.5-buster

WORKDIR /app

COPY requirement.txt .

RUN pip install -r requirement.txt

COPY /app .

CMD ["python","index.py"]
