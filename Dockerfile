FROM python:3.5-slim
WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "app.py"]
