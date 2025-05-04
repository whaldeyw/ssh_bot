FROM python:3.10

WORKDIR /app

RUN pip install aiogram

COPY . .

RUN pip install -r requirements.txt

CMD ["python" , "run.py"]