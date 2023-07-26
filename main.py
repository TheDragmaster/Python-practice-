from PyPDF2 import PdfReader, PdfWriter

def create_pdf(filename):
    write = PdfWriter()
    page = page[0]
    page.scale_by()
    page.rotate()
    page.compress_content_streams()
    write.add_blank_page(210, 297)
    with open(filename, 'wb') as file:
        write.write(file)

if __name__ == "__main__":
    create_pdf('new.pdf')