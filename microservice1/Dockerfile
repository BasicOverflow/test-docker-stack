FROM python:3.11
 
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
 
COPY . /code/app
 
CMD ["uvicorn", "app.main:app", "--host", "microservice1", "--port", "81", "--reload"]