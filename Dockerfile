FROM python:3.8
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt --user 
COPY . .
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]