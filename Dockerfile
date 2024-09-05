FROM python:3.11.8

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY . /code

EXPOSE 8080

# RUN pip install --no-cache-dir pytest && pytest --disable-warnings

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
# CMD ["sh", "-c", "ls -la /code && uvicorn main:app --host 0.0.0.0 --port 8080"]
