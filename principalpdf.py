from PyPDF2 import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
import subprocess

w, h = letter

packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)
can.setFillColorRGB(1, 0, 0)
can.setFont("Times-Roman", 14)
can.drawString(72, 655, "Segundo ingreso de informacion")
can.save()

packet.seek(0)
new_pdf = PdfReader(packet)

existing_pdf = PdfReader(open("original.pdf", "rb"))
output = PdfWriter()

page = existing_pdf.pages[0]
page.merge_page(new_pdf.pages[0])
output.add_page(page)

outputStream = open("muestra.pdf", "wb")
output.write(outputStream)
outputStream.close()

subprocess.Popen(['muestra.pdf'], shell=True)