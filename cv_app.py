# -*- coding: utf-8 -*-
import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib import pagesizes
from reportlab.lib.units import inch
import io

# Configuration de la page
st.set_page_config(page_title="CV - Aminata SAGNA", page_icon="📄", layout="wide")

# === FONCTION DE GÉNÉRATION PDF ===
def generer_pdf_cv():
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=pagesizes.A4)
    elements = []
    styles = getSampleStyleSheet()

    # Styles personnalisés
    title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=20, textColor=colors.HexColor("#1f4fa3"), spaceAfter=10)
    normal_style = ParagraphStyle('NormalStyle', parent=styles['Normal'], fontSize=11)
    section_style = ParagraphStyle('SectionStyle', parent=styles['Heading2'], textColor=colors.HexColor("#1f4fa3"), fontSize=14, spaceAfter=6)

    # COLONNE GAUCHE
    left_content = []
    left_content.append(Paragraph("<b>Contact</b>", section_style))
    left_content.append(Spacer(1, 5))
    left_content.append(Paragraph("aminatasagna02000@gmail.com", normal_style))
    left_content.append(Paragraph("Sénégal, Dakar", normal_style))
    left_content.append(Paragraph("+221-78-262-70-62", normal_style))
    left_content.append(Spacer(1, 15))
    left_content.append(Paragraph("<b>Disponibilités</b>", section_style))
    left_content.append(Paragraph("Maintenant", normal_style))
    left_content.append(Spacer(1, 15))
    left_content.append(Paragraph("<b>Langues</b>", section_style))
    left_content.append(Paragraph("Français", normal_style))
    left_content.append(Paragraph("Anglais", normal_style))
    left_content.append(Paragraph("Wolof", normal_style))
    left_content.append(Spacer(1, 15))
    left_content.append(Paragraph("<b>Passions</b>", section_style))
    left_content.append(Paragraph("Danse", normal_style))
    left_content.append(Paragraph("Sport", normal_style))
    left_content.append(Paragraph("Veille technologique", normal_style))
    left_content.append(Paragraph("Lecture & écriture", normal_style))

    # COLONNE DROITE
    right_content = []
    right_content.append(Paragraph("<b>AMINATA SAGNA</b>", title_style))
    right_content.append(Paragraph("Étudiante en Géomatique", normal_style))
    right_content.append(Spacer(1, 10))
    description = """
    Étudiante en 1ère année de BTS Géomatique, je suis à la recherche d'un stage.
    Je souhaite découvrir le milieu professionnel et mettre en pratique mes compétences
    en systèmes d'information géographique (SIG), cartographie numérique et analyse spatiale.
    Sérieuse, motivée et curieuse d'apprendre, je suis prête à m'impliquer activement.
    """
    right_content.append(Paragraph(description, normal_style))
    right_content.append(Spacer(1, 15))
    right_content.append(Paragraph("<b>Compétences</b>", section_style))
    right_content.append(Paragraph("• Maîtrise des Systèmes d'Information Géographique", normal_style))
    right_content.append(Paragraph("• Cartographie numérique", normal_style))
    right_content.append(Paragraph("• Traitement et analyse des données spatiales", normal_style))
    right_content.append(Paragraph("• Word, Excel, PowerPoint", normal_style))
    right_content.append(Paragraph("• AutoCAD, QGIS, ArcGIS", normal_style))
    right_content.append(Spacer(1, 15))
    right_content.append(Paragraph("<b>Études</b>", section_style))
    right_content.append(Paragraph("<b>2024 - 2025</b> : BTS Géomatique – 1ère année", normal_style))
    right_content.append(Paragraph("Centre d'Entrepreneuriat et Développement Technique", normal_style))
    right_content.append(Spacer(1, 5))
    right_content.append(Paragraph("<b>2023 - 2024</b> : Licence 1 Maths Physique Chimie Informatique", normal_style))
    right_content.append(Paragraph("Université Alioune Diop de Bambey", normal_style))
    right_content.append(Spacer(1, 5))
    right_content.append(Paragraph("<b>2022 - 2023</b> : Licence 2 Physique Chimie", normal_style))
    right_content.append(Paragraph("Université Alioune Diop de Bambey", normal_style))
    right_content.append(Spacer(1, 5))
    right_content.append(Paragraph("<b>2021 - 2022</b> : Licence 3 Physique Chimie", normal_style))
    right_content.append(Paragraph("Université Alioune Diop de Bambey", normal_style))
    right_content.append(Spacer(1, 5))
    right_content.append(Paragraph("<b>2020 - 2021</b> : Baccalauréat (S2)", normal_style))
    right_content.append(Paragraph("Lycée de Tendouck", normal_style))

    # Table pour 2 colonnes
    data = [[left_content, right_content]]
    table = Table(data, colWidths=[2.2*inch, 4*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), colors.HexColor("#d9e2f3")),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    elements.append(table)
    
    doc.build(elements)
    buffer.seek(0)
    return buffer.getvalue()

# === AFFICHAGE STREAMLIT ===
st.title("📄 CV - Aminata SAGNA")
st.subheader("Étudiante en Géomatique")

st.markdown("---")

# Afficher le CV en texte dans la page
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 📞 Contact")
    st.write("📧 aminatasagna02000@gmail.com")
    st.write("📍 Sénégal, Dakar")
    st.write("📱 +221-78-262-70-62")
    
    st.markdown("### 📅 Disponibilité")
    st.success("**Maintenant**")
    
    st.markdown("### 🌍 Langues")
    st.write("• Français\n• Anglais\n• Wolof")
    
    st.markdown("### ❤️ Passions")
    st.write("• Danse\n• Sport\n• Veille technologique\n• Lecture & écriture")

with col2:
    st.markdown("### 👤 Profil")
    st.info("""
    Étudiante en 1ère année de BTS Géomatique, je suis à la recherche d'un stage. 
    Je souhaite découvrir le milieu professionnel et mettre en pratique mes compétences 
    en SIG, cartographie numérique et analyse spatiale.
    """)
    
    st.markdown("### 🛠 Compétences")
    st.write("• Maîtrise des SIG\n• Cartographie numérique\n• Analyse de données spatiales\n• Word, Excel, PowerPoint\n• AutoCAD, QGIS, ArcGIS")
    
    st.markdown("### 🎓 Formation")
    st.write("**2024 - 2025** : BTS Géomatique – 1ère année\n\nCentre d'Entrepreneuriat et Développement Technique")
    st.write("**2023 - 2024** : Licence 1 MPC Informatique\n\nUniversité Alioune Diop de Bambey")
    st.write("**2022 - 2023** : Licence 2 Physique Chimie\n\nUniversité Alioune Diop de Bambey")
    st.write("**2021 - 2022** : Licence 3 Physique Chimie\n\nUniversité Alioune Diop de Bambey")
    st.write("**2020 - 2021** : Baccalauréat S2\n\nLycée de Tendouck")

# Bouton de téléchargement PDF
st.markdown("---")
pdf_bytes = generer_pdf_cv()
st.download_button(
    label="📥 Télécharger mon CV en PDF",
    data=pdf_bytes,
    file_name="CV_Aminata_SAGNA.pdf",
    mime="application/pdf"
)
