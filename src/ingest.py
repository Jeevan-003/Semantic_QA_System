from pathlib import Path
import fitz


class DocumentIngestor:
    def __init__(self, input_directory: str):
        self.input_directory = Path(input_directory)

    def get_pdf_files(self):
        return list(self.input_directory.glob("*.pdf"))

    def extract_pdf(self, pdf_path: Path):
        pages = []

        document = fitz.open(pdf_path)

        for page_number, page in enumerate(document, start=1):

            text = page.get_text("text")

            if text.strip():

                pages.append(
                    {
                        "file_name": pdf_path.name,
                        "page_number": page_number,
                        "text": text.strip()
                    }
                )

        document.close()

        return pages

    def load_documents(self):
        all_pages = []

        pdf_files = self.get_pdf_files()

        print(f"Found {len(pdf_files)} PDF(s).\n")

        for pdf in pdf_files:

            print(f"Reading: {pdf.name}")

            pages = self.extract_pdf(pdf)

            all_pages.extend(pages)

            print(f"Extracted {len(pages)} pages.\n")

        print(f"Total Pages: {len(all_pages)}")

        return all_pages