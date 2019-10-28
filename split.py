from PyPDF2 import PdfFileReader, PdfFileWriter

documento = open("Big.pdf","rb")
pdf = PdfFileReader(documento)

Pareswriter   = PdfFileWriter()
Impareswriter = PdfFileWriter()

for i in range(pdf.getNumPages()):
    PaginaActual = pdf.getPage(i)
    if i % 2 == 0:
        Pareswriter.addPage(PaginaActual)
    else:
        Impareswriter.addPage(PaginaActual)

with open("Pares.pdf", "wb") as f:
    Pareswriter.write(f)

with open("Impares.pdf", "wb") as g:
    Impareswriter.write(g)
