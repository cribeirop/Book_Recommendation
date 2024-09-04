FROM python:3.11.8

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8080

# RUN pip install --no-cache-dir pytest && pytest --disable-warnings

CMD ["uvicorn", "app.main:app", "--host", "localhost", "--port", "8080"]
