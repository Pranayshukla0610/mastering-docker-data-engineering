# Layer 1
FROM python:3.12-slim

# Layer 2
WORKDIR /app

# Layer 3
COPY requirements.txt .

# Layer 4
RUN pip install --no-cache-dir -r requirements.txt

# Layer 5
COPY . .

# Layer 6
CMD ["python", "app/main.py"]