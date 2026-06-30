import fitz  # PyMuPDF
import docx


def extract_text_from_pdf(file_path: str) -> str:
    text = ""
    doc = fitz.open(file_path)

    for page in doc:
        text += page.get_text()

    return text


def extract_text_from_docx(file_path: str) -> str:
    doc = docx.Document(file_path)

    text = []
    for para in doc.paragraphs:
        text.append(para.text)

    return "\n".join(text)
