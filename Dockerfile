FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

VOLUME ["/app/data", "/app/models"]

# Using 'sh -c' to chain the commands
CMD ["sh", "-c", "python src/collect.py && python src/processing.py && python src/train.py && python src/eval.py"]