FROM python:3.10.6-buster

COPY . .

RUN pip install -r requirments.txt

WORKDIR /django_app



ENTRYPOINT ["python"] 

CMD ["manage.py", "runserver", "0.0.0.0:8000"]

# CMD [ "python", "manage.py", "runserver"]

# RUN python manage.py runserver
