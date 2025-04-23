
import csv
from fpdf import FPDF

def export_report_csv(department, expenses, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Department', department.name])
        writer.writerow(['Allocated Budget', department.allocated_budget])
        writer.writerow([])
        writer.writerow(['Amount', 'Category', 'Description', 'Date'])
        for exp in expenses:
            writer.writerow([exp.amount, exp.category, exp.description, exp.date])

def export_report_pdf(department, expenses, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt=f"Department Report - {department.name}", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Allocated Budget: ${department.allocated_budget}", ln=True)
    pdf.ln(10)

    pdf.cell(40, 10, 'Amount', border=1)
    pdf.cell(40, 10, 'Category', border=1)
    pdf.cell(60, 10, 'Description', border=1)
    pdf.cell(40, 10, 'Date', border=1)
    pdf.ln()

    for exp in expenses:
        pdf.cell(40, 10, f"${exp.amount:.2f}", border=1)
        pdf.cell(40, 10, exp.category, border=1)
        pdf.cell(60, 10, exp.description, border=1)
        pdf.cell(40, 10, exp.date.strftime("%Y-%m-%d"), border=1)
        pdf.ln()

    pdf.output(filename)
