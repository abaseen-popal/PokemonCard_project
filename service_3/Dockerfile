# Within the container i am exposing port 5000, installing the requirements and running it 
FROM python:latest

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]