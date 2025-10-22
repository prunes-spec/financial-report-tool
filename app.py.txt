import streamlit as st
import os
from extractor import extraer_datos
from analyzer import calcular_ratios
from report_generator import generar_pdf

st.set_page_config(page_title="Informe Financiero Automático", layout="centered")
st.title("📄 Generador de Informes Financieros")
st.markdown("Sube un PDF con estados financieros para generar un informe ejecutivo automático.")

uploaded_file = st.file_uploader("Selecciona el archivo PDF", type=["pdf"])

if uploaded_file:
    temp_path = "temp_financials.pdf"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("Extrayendo datos del PDF..."):
        datos = extraer_datos(temp_path)
        ratios = calcular_ratios(datos)

    st.success("✅ Datos extraídos con éxito")
    st.subheader("Datos detectados")
    st.json(datos)

    st.subheader("Ratios calculados")
    st.json(ratios)

    if st.button("📄 Generar Informe Profesional"):
        output_path = "output/informe_ejecutivo.pdf"
        with st.spinner("Generando informe..."):
            generar_pdf(datos, ratios, "Cliente Corporativo", output_path)
        
        with open(output_path, "rb") as f:
            st.download_button(
                label="⬇️ Descargar Informe (PDF)",
                data=f,
                file_name="informe_ejecutivo.pdf",
                mime="application/pdf"
            )

    if os.path.exists(temp_path):
        os.remove(temp_path)