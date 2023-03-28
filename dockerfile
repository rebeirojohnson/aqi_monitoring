FROM python:3.10.6-buster

WORKDIR /django_app

COPY . .

RUN ls

RUN pip install -r requirments.txt

ENTRYPOINT ["python"] 

CMD ["manage.py", "runserver", "0.0.0.0:8000"]

# CMD [ "python", "manage.py", "runserver"]

# RUN python manage.py runserver
