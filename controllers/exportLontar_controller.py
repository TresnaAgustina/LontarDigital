from flask import Blueprint, send_file, session
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageTemplate, Frame
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import utils
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

export_lontar_blueprint = Blueprint('export_lontar', __name__)

def createLontar(text):
    # Buat dokumen PDF
    size = (20 * inch, 2.6 * inch)
    doc = SimpleDocTemplate("TemplateLontarWatermark.pdf", pagesize=size, rightMargin=12, leftMargin=12, topMargin=4, bottomMargin=0)

    # Mendefinisikan jenis font "Bali Simbar"
    pdfmetrics.registerFont(TTFont("BaliSimbar", "static/font/balisdn.ttf"))

    # Buat gaya teks
    styles = getSampleStyleSheet()
    style = styles["Normal"]
    style.leading = 42  # Spasi antarbaris
    style.fontSize = 20
    style.fontName = "BaliSimbar"
    # margin left
    style.leftIndent = 64
    # margin right
    style.rightIndent = 64

    # File background (watermark) image
    file_background = "static/svg/LontarFix.jpg"

    # Add the resized background image to each page using PageTemplate
    template = PageTemplate(
        frames=[
            Frame(
                doc.leftMargin,
                doc.bottomMargin,
                doc.width,
                doc.height,
                id='normal',
            )
        ],
        onPage=lambda c, d: c.drawImage(
            file_background,
            doc.leftMargin,
            doc.bottomMargin,
            width=doc.width,
            height=doc.height,
            preserveAspectRatio=True,
            mask='auto',  # Optional: Use 'auto' to preserve image transparency
        ),
    )

    doc.addPageTemplates([template])

    # Tambahkan teks ke dokumen
    paragraphs = [Paragraph(line, style) for line in text.split('\n')]

    # Build the document with paragraphs
    doc.build(paragraphs)

@export_lontar_blueprint.route('/lontar', methods=['GET'])
def exportLontar():
    # Retrieve the translated text from the session
    teks_result = session.get('result_text', '')

    # Check if there's content to generate a PDF
    if not teks_result:
        return "No content to export to Lontar Format"

    # Generate the PDF with watermark
    createLontar(teks_result)
    
    # Send the PDF to the user as an attachment
    return send_file("TemplateLontarWatermark.pdf", as_attachment=True)
