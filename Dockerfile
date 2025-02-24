FROM python:3.12.9
ENV PYTHONUNBUFFERED=1
RUN mkdir /app
WORKDIR /app
RUN pip install --upgrade pip 
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "todoproject/manage.py", "runserver", "0.0.0.0:8000"]
