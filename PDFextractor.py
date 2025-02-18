from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    return text

# Usage
pdf_text = extract_text_from_pdf("Keppra_Drug_Information.pdf")
print(pdf_text[:500])  # Preview first 500 characters
