# Use official Python image
FROM python:3.11-slim

# Install poppler-utils and tesseract-ocr
RUN apt-get update && apt-get install -y \
    poppler-utils \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy application files
COPY requirements.txt .
COPY extract_text.py .
COPY doc.pdf .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "extract_text.py"]
