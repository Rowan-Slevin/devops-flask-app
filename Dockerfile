FROM python:3.14

WORKDIR /app

RUN pip install flask

COPY hello.py .

EXPOSE 5000

CMD ["flask", "--app", "hello", "run", "--host=0.0.0.0"]
