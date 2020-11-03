FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements/requirements.txt
EXPOSE 8000
ENTRYPOINT ["python", "main.py"]