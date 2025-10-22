import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

def crear_grafico_ratios(ratios):
    nombres = list(ratios.keys())
    valores = list(ratios.values())

    plt.figure(figsize=(6, 3))
    plt.bar(nombres, valores, color='#0057b8')
    plt.ylabel('Valor')
    plt.title('Ratios Clave')
    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()
    return img_base64

def generar_pdf(datos, ratios, empresa, output_path):
    grafico_b64 = crear_grafico_ratios(ratios)

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('report_template.html')

    def format_number(x):
        if x == 0:
            return "N/A"
        return f"{x:,.0f}".replace(",", ".")

    def format_percent(x):
        if x == 0:
            return "N/A"
        return f"{x:.2%}"

    html_out = template.render(
        empresa=empresa,
        datos={k: format_number(v) for k, v in datos.items()},
        ratios={k: format_percent(v) for k, v in ratios.items()},
        grafico_b64=grafico_b64
    )

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    HTML(string=html_out).write_pdf(output_path)