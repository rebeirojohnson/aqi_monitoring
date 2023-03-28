FROM python:3.10.6-buster

COPY . .

WORKDIR /django_app


RUN pip install -r requirments.txt

ENTRYPOINT ["python"] 

CMD ["manage.py", "runserver", "0.0.0.0:8000"]

# CMD [ "python", "manage.py", "runserver"]

# RUN python manage.py runserver
