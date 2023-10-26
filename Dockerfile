FROM python:3.9.18-alpine3.18
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--reload"]
