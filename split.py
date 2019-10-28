from PyPDF2 import  PdfFileReader,PdfFileWriter

archivo = open("Big.pdf","rb")
reader = PdfFileReader(archivo)
page = reader.getNumPages()

writer = PdfFileWriter()

for i in range(page):
    if i%2 != 0:
        page = reader.getPage(i)
        writer.addPage(page)

salida = open("Impares.dpf","wb")
writer.write(salida)
salida.close()

