import requests
import json 
import pdfkit

def invoiceCreator():
    # invoice data will be an object so the data can be accessed as json data
    circle = " <circle cx='50' cy='50' r='40' stroke='green' stroke-width='4' fill='yellow' />"
    svg = "<svg width = '100' height = '100'>"+circle+"</svg>"
    file = open("file.html","w")
    file.write(svg)
    file.close()

    pdfkit.from_file("pdfTemplate/maxpower.html","output.pdf")

invoiceCreator()
