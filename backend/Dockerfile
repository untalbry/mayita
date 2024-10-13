FROM python:3.10-slim
WORKDIR /backend/src
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080

CMD ["python", "-m", "src.app"]
