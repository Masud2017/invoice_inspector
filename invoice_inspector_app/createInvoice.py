# Invoice generation and pdf convertion will be placed in this moudle
import os
import sys
import cv2

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

def createInvoice():
     # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    pdf = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    pdf.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    pdf.showPage()
    pdf.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
def createPdf(invoice):
    pass
def createImage(invoice,type):
    pass