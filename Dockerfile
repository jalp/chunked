FROM python:3.4
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
EXPOSE 5000
CMD gunicorn app:app -w 2 -b :5000
