# FROM ubuntu:22.04
FROM python:3.10

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# RUN useradd --create-home appuser
# USER appuser

COPY . .

# ENV API_KEY=SOMETHING # environment variable

EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] #command you run when starting the container. one command per container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#  or 

# ENTRYPOINT ["pyhton3", "-m", "hhtp.server"]
# CMD ["8000"] #can override arguments    in docker run cmd. docke run image 5000

