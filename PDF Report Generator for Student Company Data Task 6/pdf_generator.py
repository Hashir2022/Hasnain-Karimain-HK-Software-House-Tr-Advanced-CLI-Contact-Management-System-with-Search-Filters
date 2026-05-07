from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Table, TableStyle
from reportlab.platypus import Paragraph, Spacer, Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

from datetime import datetime
import os

def generate_pdf(data, report_type, chart_path):

    if not os.path.exists("reports"):
        os.makedirs("reports")

    filename = f"reports/{report_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    pdf = SimpleDocTemplate(filename)

    elements = []

    styles = getSampleStyleSheet()

    title = Paragraph(
        f"<b>{report_type} Report</b>",
        styles['Title']
    )

    elements.append(title)

    elements.append(Spacer(1, 20))

    date = Paragraph(
        f"Generated on: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
        styles['Normal']
    )

    elements.append(date)

    elements.append(Spacer(1, 20))

    if report_type == "Student":

        table_data = [
            [
                "Name",
                "ID",
                "Email",
                "Course",
                "Marks",
                "Attendance"
            ]
        ]

    else:

        table_data = [
            [
                "Name",
                "ID",
                "Email",
                "Department",
                "Role",
                "Performance"
            ]
        ]

    for row in data:
        table_data.append(row)

    table = Table(table_data)

    style = TableStyle([

        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),

        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),

        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),

        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),

        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),

        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),

        ('GRID', (0, 0), (-1, -1), 1, colors.black),

    ])

    table.setStyle(style)

    elements.append(table)

    elements.append(Spacer(1, 30))

    chart = Image(chart_path, width=400, height=250)

    elements.append(chart)

    pdf.build(elements)

    print("PDF Generated Successfully!")
    print("Saved As:", filename)