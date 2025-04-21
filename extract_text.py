import os
from pdf2image import convert_from_path
import pytesseract

PDF_PATH = "doc.pdf"
OUTPUT_TEXT = "output.txt"

def pdf_to_text(pdf_path, output_path):
    print("Converting PDF pages to images...")
    pages = convert_from_path(pdf_path, 300)
    text = ""
    for i, page in enumerate(pages):
        print(f"Processing page {i+1}/{len(pages)}...")
        text += pytesseract.image_to_string(page, lang="eng") + "\n---PAGE BREAK---\n"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Text extraction complete. Output saved to '{output_path}'.")

if __name__ == "__main__":
    pdf_to_text(PDF_PATH, OUTPUT_TEXT)
