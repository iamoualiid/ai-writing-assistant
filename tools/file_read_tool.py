import fitz  # PyMuPDF

def read_pdf(file_path):
    """
    Read and extract text from each page of the given PDF file.
    Returns a list of dictionaries with page numbers and corresponding text.
    """
    try:
        doc = fitz.open(file_path)
        pages = []

        for page_number in range(len(doc)):
            page = doc[page_number]
            text = page.get_text()
            pages.append({
                "page": page_number + 1,
                "text": text
            })

        return pages
    except Exception as e:
        print("PDF reading error:", e)
        return []
