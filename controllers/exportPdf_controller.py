from flask import Blueprint, send_file, session
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


export_pdf_blueprint = Blueprint('export_pdf', __name__)

# Fungsi untuk menghasilkan file PDF
def create_pdf(str):
    title = session.get('title','')
    # Get the current time
    now = datetime.now()
    # Format the time
    current_date = now.strftime("%d-%m-%Y")
    # Buat dokumen PDF
    doc = SimpleDocTemplate(title+" "+current_date+".pdf", pagesize=letter)
    elements = []
    # Mendefinisikan jenis font "Bali Simbar"
    pdfmetrics.registerFont(TTFont("BaliSimbar", "static/font/balisdn.ttf"))


    # Buat gaya teks
    styles = getSampleStyleSheet()
    style = styles["Normal"]
    style.leading = 42  # Spasi antarbaris
    style.fontSize = 18
    style.fontName = "BaliSimbar"

    # Tambahkan teks ke dokumen
    text = str
    paragraph = Paragraph(text, style)
    elements.append(paragraph)

    # Build the PDF document
    doc.build(elements)

# Route untuk eksport PDF
@export_pdf_blueprint.route('/pdf', methods=['GET'])
def export_pdf():
    # Get the current time
    now = datetime.now()
    # Format the time
    current_date = now.strftime("%d-%m-%Y")
    # Retrieve the translated text from the session
    teks_result = session.get('result_text', '')
    title = session.get('title','')
    # data = request.get_json()
    # teks_result = data['data']

    print('Teks Result: '+ teks_result)

    # Check if there's content to generate a PDF
    if not teks_result:
        return "No content to export to PDF"

    create_pdf(teks_result)

    return send_file(title+" "+current_date+".pdf", as_attachment=True)
