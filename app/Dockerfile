FROM python:3.9-slim

COPY ./pixie /app/pixie
COPY ./requirements.txt /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "pixie.main:app", "--host=0.0.0.0", "--reload"]


