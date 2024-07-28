# Aniq detallarni yashirish va minimal interfeys taqdim etish.  # noqa
# https://github.com/theMirmakhmudov
# https://youtube.com/@Mirmakhmudov_coder # noqa

from abc import ABC, abstractmethod

# Abstraction class
class Document(ABC):
    @abstractmethod
    def save(self, filename):
        pass

    @abstractmethod
    def open(self, filename):
        pass

# Subclass 1
class WordDocument(Document):
    def save(self, filename):
        return f"Word document saved as {filename}.docx"

    def open(self, filename):
        return f"Word document {filename}.docx opened"

# Subclass 2
class PDFDocument(Document):
    def save(self, filename):
        return f"PDF document saved as {filename}.pdf"

    def open(self, filename):
        return f"PDF document {filename}.pdf opened"

# Create objects
word_doc = WordDocument()
pdf_doc = PDFDocument()

print(word_doc.save("example"))  # Word document saved as report.docx
print(word_doc.open("example"))  # Word document report.docx opened

print(pdf_doc.save("example"))  # PDF document saved as report.pdf
print(pdf_doc.open("example"))  # PDF document report.pdf opened
