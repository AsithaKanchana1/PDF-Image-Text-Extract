# <sub><sub>_`PDF-Text-Extract`_ </sub></sub>

# PDF Text Extraction with Docker

A simple, reproducible workflow to extract all text from a PDF (using OCR) in a Docker container, saving the result as a text file.

This workflow is ideal for developers and students who want to convert PDF documents (including scanned/image-based PDFs) to plain text, without needing to manually install OCR tools or handle dependencies.

---

## 🛠️ Features

- Extracts text from any PDF, including scanned/image-based documents, using Tesseract OCR.
- All dependencies managed via Docker for maximum reproducibility.
- Output is a plain text file (`output.txt`).
- Works on any OS with Docker installed.

---

## 🚀 Usage

### 1. Place your PDF in the project directory

Make sure your PDF is named `doc.pdf` and is in the same folder as your code and Dockerfile.

### 2. Build the Docker image

```bash
docker build -t text-extract .
```

### 3. Run the container

```bash
docker run --rm -v "$PWD:/app" text-extract
```

Or

```powershell
docker run --rm -v "${PWD}:/app" text-extract
```

- The `-v "$PWD:/app"` and `${PWD}` are flags that mounts your working directory, saving `output.txt` to your local folder after processing.

### 4. Get your results

After running, you'll have `output.txt` in your project folder, containing all the extracted text.

---

## ⚙️ How it Works

- The container runs `extract_text.py`, which:
  - Converts each page of `doc.pdf` to an image (with `pdf2image`)
  - Runs OCR (with `pytesseract`) on each image
  - Concatenates the results and writes to `output.txt`

---

## 🐋 Dockerfile Highlights

- Based on `python:3.11-slim`
- Installs OCR and PDF dependencies (`tesseract-ocr`, `poppler-utils`)
- Installs Python packages (`pdf2image`, `pytesseract`, `Pillow`)
- Copies your code and PDF
- Runs the extractor script at container start

---


## 🗂️ Customization

- To use a different PDF, change its name to `doc.pdf` or adjust the script's `PDF_PATH`.
- Script can be modified for batch processing, alternative outputs, or other OCR languages.

---

## 🏷️ License

This project is for educational and personal use. Please respect copyright of the documents you process.

---

## 👨‍💻 Developed By

A software engineering student specializing in mobile and web development with React, Python, and Docker.
Asitha Kanchana

---