from flask import Blueprint, send_file, session
import pdfkit
from reportlab.lib.pagesizes import letter, A4, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageTemplate, Frame, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import utils
from reportlab.graphics.shapes import Ellipse, Drawing
# Import library untuk mengatur jenis font yang berbeda
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
export_lontar_blueprint = Blueprint('export_lontar', __name__)

def createLontar(str):
    # Buat dokumen PDF
    size = (20 * inch, 2.6 * inch)
    doc = SimpleDocTemplate("example.pdf", pagesize=size, rightMargin=12, leftMargin=12, topMargin=4, bottomMargin=0)
    
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
    

     # File background color
    file_background = "static/svg/LontarFix.jpg"

    # Resize the background image to fit the page
    img = utils.ImageReader(file_background)
    img_width, img_height = img.getSize()
    aspect_ratio = img_width / img_height
    target_width = doc.width
    target_height = doc.width / aspect_ratio

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
            img,
            doc.leftMargin,
            doc.bottomMargin,
            width=doc.width,
            height=doc.height,
            preserveAspectRatio=True,
        ),
    )

    doc.addPageTemplates([template])


    # Tambahkan teks ke dokumen
    text = str
    paragraphs = [Paragraph(line, style) for line in text.split('\n')]
    
    # Add Spacer after every 70 pixels
    for paragraph in paragraphs:
        
        doc.build([paragraph])

@export_lontar_blueprint.route('/lontar', methods=['GET'])
def exportLontar():
    # ambil data history dengan id 1
    # Retrieve the translated text from the session
    teks_result = session.get('result_text', '')

    
    # Check if there's content to generate a PDF
    if not teks_result:
        return "No content to export to Lontar Format"

    teks_result = createLontar(teks_result)
    return send_file("example.pdf", as_attachment=True)
