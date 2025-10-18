import pdfplumber
import docx
from PIL import Image
import pytesseract

def extract_text(file_path):
    if file_path.endswith('.pdf'):
        with pdfplumber.open(file_path) as pdf:
            return " ".join(page.extract_text() for page in pdf.pages if page.extract_text())
    elif file_path.endswith('.docx'):
        doc = docx.Document(file_path)
        return " ".join(p.text for p in doc.paragraphs)
    elif file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        return pytesseract.image_to_string(Image.open(file_path))
    else:
        raise ValueError("Unsupported file type.")
