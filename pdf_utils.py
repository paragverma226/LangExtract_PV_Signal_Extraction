import os
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extracts and concatenates text from all pages of a PDF."""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text() + "\n"
    return text.strip()

def save_intermediate_text(text: str, output_folder: str, base_filename: str):
    """Saves extracted PDF text to an intermediate .txt file."""
    os.makedirs(output_folder, exist_ok=True)
    text_path = os.path.join(output_folder, base_filename + ".txt")
    with open(text_path, "w", encoding="utf-8") as f:
        f.write(text)
    return text_path
