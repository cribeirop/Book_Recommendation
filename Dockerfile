FROM python:3.11.8

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

COPY gutenberg_book_deer.csv /app/gutenberg_book_deer.csv

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]