from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from datetime import datetime

services = {
    1: {"name": "Service 1"},
    2: {"name": "Service 2"},
    3: {"name": "Service 3"},
    4: {"name": "Service 4"},
    5: {"name": "Service 5"},
    6: {"name": "Service 6"},
    7: {"name": "Service 7"},
    8: {"name": "Service 8"},
    9: {"name": "Service 9"},
}

def create_pdf(output_path, services, ism_familiya, sharif,registrant):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    sarlavha = (f"EURO ASIA PROJECT TOMONIDAN ”{ism_familiya}\n"
                f"{sharif}” GA TAKLIF ETILGAN XIZMATLAR\n"
                "RO’YXATI")
    
    c.drawImage(r"/home/amirjon/Telegram_Channels_Bot/Bytefy-Company-Telegram-Bot/bot/pdfconvertor.png", 0, 0, width, height)
    
    c.setFont("Helvetica-Bold", 12)

    header_y_offset = height - 115 * mm  
    text_lines = sarlavha.split('\n')
    for line in text_lines:
        text_width = c.stringWidth(line, "Helvetica-Bold", 12)
        header_x_offset = (width - text_width) / 2  
        c.drawString(header_x_offset, header_y_offset, line)
        header_y_offset -= 14  
    # Draw the date
    now = datetime.now()
    day = now.day
    month = now.month
    year = now.year
    date = f"{day}/{month}/{year}"
    c.setFont("Helvetica-Bold", 11)  
    c.drawString(143, 450.5, date)
    # ============================================
    c.setFont("Helvetica-Bold", 11)  
    c.drawString(500, 450, '123456789')
    
    x_offset = 27 * mm  
    y_offset = 141 * mm  
    cell_height = 7.3 * mm  

    c.setFont("Helvetica", 12)  
    for i in range(1, 10):
        service_name = services[i]["name"] if i in services else ""
        c.drawString(x_offset, y_offset, service_name)
        y_offset -= cell_height
    c.setFont("Helvetica-Bold", 12)  
    c.drawString(423, 175, registrant)

    c.save()

create_pdf(r"/home/amirjon/Telegram_Channels_Bot/Bytefy-Company-Telegram-Bot/invoyslar/outpud.pdf", services, "Azamjon Olimov", " ","Amirjon Karimov")
