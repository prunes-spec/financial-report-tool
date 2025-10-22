def calcular_ratios(datos):
    ingresos = datos["ingresos"]
    ebitda = datos["ebitda"]
    activo = datos["activo_total"]
    pasivo = datos["pasivo_total"]
    patrimonio = datos["patrimonio"]

    ratios = {
        "margen_ebitda": round(ebitda / ingresos, 4) if ingresos else 0,
        "endeudamiento": round(pasivo / activo, 4) if activo else 0,
        "roa": round(ebitda / activo, 4) if activo else 0,
        "roe": round(ebitda / patrimonio, 4) if patrimonio else 0,
    }
    return ratios