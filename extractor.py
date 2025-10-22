import pdfplumber
import re

def extraer_datos(pdf_path):
    texto_completo = ""
    with pdfplumber.open(pdf_path) as pdf:
        for pagina in pdf.pages:
            if pagina.extract_text():
                texto_completo += pagina.extract_text() + "\n"

    texto = texto_completo.lower()
    
    def buscar_valor(texto, patrones):
        for patron in patrones:
            lineas = [l for l in texto.split("\n") if patron in l]
            for linea in lineas:
                numeros = re.findall(r"[\d,\.]+", linea)
                if numeros:
                    val = numeros[-1].replace(",", "").replace(".", "")
                    try:
                        return float(val)
                    except:
                        continue
        return 0.0

    datos = {
        "ingresos": buscar_valor(texto, ["ingreso", "venta", "revenue", "operacion"]),
        "ebitda": buscar_valor(texto, ["ebitda", "resultado operativo", "margen operativo"]),
        "activo_total": buscar_valor(texto, ["activo total", "total activo", "activos"]),
        "pasivo_total": buscar_valor(texto, ["pasivo total", "total pasivo", "pasivos"]),
        "patrimonio": buscar_valor(texto, ["patrimonio", "capital", "equity"]),
    }
    return datos