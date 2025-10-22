import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def crear_grafico_ratios(ratios):
    nombres = list(ratios.keys())
    valores = [v * 100 for v in ratios.values()]

    plt.figure(figsize=(6, 3))
    plt.bar(nombres, valores, color='#0057b8')
    plt.ylabel('Porcentaje (%)')
    plt.title('Ratios Clave')
    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return buf

def generar_pdf(datos, ratios, empresa, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    styles = getSampleStyleSheet()
    style_title = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=14,
        textColor=colors.HexColor("#002366")
    )
    style_heading = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=10,
        textColor=colors.HexColor("#0057b8")
    )

    story = []
    story.append(Paragraph("Informe Financiero Ejecutivo", style_title))
    story.append(Paragraph(f"Cliente: {empresa}", styles["Normal"]))
    story.append(Spacer(1, 12))

    # Datos financieros
    story.append(Paragraph("Indicadores Financieros", style_heading))
    data_fin = [
        ["Concepto", "Valor"],
        ["Ingresos", f"${datos['ingresos']}"],
        ["EBITDA", f"${datos['ebitda']}"],
        ["Activo Total", f"${datos['activo_total']}"],
        ["Patrimonio", f"${datos['patrimonio']}"]
    ]
    table_fin = Table(data_fin, col
