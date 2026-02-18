# -*- coding: utf-8 -*-
"""
CV Interactif - Aminata SAGNA
Développé avec Streamlit pour la présentation en ligne
"""
import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib import pagesizes
from reportlab.lib.units import inch
import io

# Configuration de la page
st.set_page_config(
    page_title="CV - Aminata SAGNA",
    page_icon="📄",
    layout="wide"
)


def generer_pdf_cv():
    """Génère le CV au format PDF en mémoire"""
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=pagesizes.A4)
    elements = []
    styles = getSampleStyleSheet()

    # Définition des styles typographiques
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontSize=20,
        textColor=colors.HexColor("#1f4fa3"),
        spaceAfter=10
    )
    normal_style = ParagraphStyle(
        'NormalStyle',
        parent=styles['Normal'],
        fontSize=11
    )
    section_style = ParagraphStyle(
        'SectionStyle',
        parent=styles['Heading2'],
        textColor=colors.HexColor("#1f4fa3"),
        fontSize=14,
        spaceAfter=6
    )

    # --- Contenu colonne gauche (informations personnelles) ---
    left_content = []
    left_content.append(Paragraph("<b>Contact</b>", section_style))
    left_content.append(Spacer(1, 5))
    left_content.append(Paragraph("aminatasagna02000@gmail.com", normal_style))
    left_content.append(Paragraph("Sénégal, Dakar", normal_style))
    left_content.append(Paragraph("+221-78-262-70-62", normal_style))
    left_content.append(Spacer(1, 15))

    left_content.append(Paragraph("<b>Disponibilité</b>", section_style))
    left_content.append(Paragraph("Immédiate", normal_style))
    left_content.append(Spacer(1, 15))

    left_content.append(Paragraph("<b>Langues</b>", section_style))
    for langue in ["Français", "Anglais", "Wolof"]:
        left_content.append(Paragraph(f"• {langue}", normal_style))
    left_content.append(Spacer(1, 15))

    left_content.append(Paragraph("<b>Centres d'intérêt</b>", section_style))
    for passion in ["Danse", "Sport", "Veille technologique", "Lecture & écriture"]:
        left_content.append(Paragraph(f"• {passion}", normal_style))

    # --- Contenu colonne droite (parcours et compétences) ---
    right_content = []
    right_content.append(Paragraph("<b>AMINATA SAGNA</b>", title_style))
    right_content.append(Paragraph("Étudiante en Géomatique", normal_style))
    right_content.append(Spacer(1, 10))

    profil_texte = """
    Étudiante en 1ère année de BTS Géomatique, je suis à la recherche d'un stage.
    Je souhaite découvrir le milieu professionnel et mettre en pratique mes compétences
    en systèmes d'information géographique (SIG), cartographie numérique et analyse spatiale.
    Sérieuse, motivée et curieuse d'apprendre, je suis prête à m'impliquer activement.
    """
    right_content.append(Paragraph(profil_texte, normal_style))
    right_content.append(Spacer(1, 15))

    right_content.append(Paragraph("<b>Compétences techniques</b>", section_style))
    competences_list = [
        "Maîtrise des Systèmes d'Information Géographique",
        "Cartographie numérique",
        "Traitement et analyse des données spatiales",
        "Word, Excel, PowerPoint",
        "AutoCAD, QGIS, ArcGIS"
    ]
    for comp in competences_list:
        right_content.append(Paragraph(f"• {comp}", normal_style))
    right_content.append(Spacer(1, 15))

    right_content.append(Paragraph("<b>Parcours académique</b>", section_style))
    formations = [
        ("2024 - 2025", "BTS Géomatique – 1ère année", "Centre d'Entrepreneuriat et Développement Technique"),
        ("2023 - 2024", "Licence 1 MPC Informatique", "Université Alioune Diop de Bambey"),
        ("2022 - 2023", "Licence 2 Physique Chimie", "Université Alioune Diop de Bambey"),
        ("2021 - 2022", "Licence 3 Physique Chimie", "Université Alioune Diop de Bambey"),
        ("2020 - 2021", "Baccalauréat Série S2", "Lycée de Tendouck")
    ]
    for annee, diplome, etablissement in formations:
        right_content.append(Paragraph(f"<b>{annee}</b> : {diplome}", normal_style))
        right_content.append(Paragraph(f"<i>{etablissement}</i>", normal_style))
        right_content.append(Spacer(1, 3))

    # Mise en page deux colonnes via Table ReportLab
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


# ==================== INTERFACE STREAMLIT ====================

st.title("📄 Aminata SAGNA")
st.subheader("Étudiante en Géomatique")
st.markdown("---")

# Mise en page principale
col_info, col_main = st.columns([1, 2])

with col_info:
    st.markdown("### 📞 Coordonnées")
    st.write("📧 aminatasagna02000@gmail.com")
    st.write("📍 Sénégal, Dakar")
    st.write("📱 +221-78-262-70-62")

    st.markdown("### 📅 Disponibilité")
    st.success("**Immédiate**")

    st.markdown("### 🌍 Langues")
    for langue in ["Français", "Anglais", "Wolof"]:
        st.write(f"• {langue}")

    st.markdown("### ❤️ Centres d'intérêt")
    for passion in ["Danse", "Sport", "Veille technologique", "Lecture & écriture"]:
        st.write(f"• {passion}")

with col_main:
    st.markdown("### 👤 Profil professionnel")
    st.info("""
    Étudiante en 1ère année de BTS Géomatique, je suis à la recherche d'un stage.
    Je souhaite découvrir le milieu professionnel et mettre en pratique mes compétences
    en SIG, cartographie numérique et analyse spatiale.
    """)

    st.markdown("### 🛠 Compétences")
    for comp in competences_list:
        st.write(f"🔹 {comp}")

    st.markdown("### 🎓 Formation")
    for annee, diplome, etablissement in formations:
        st.write(f"**{annee}** — {diplome}")
        st.caption(etablissement)

# Section téléchargement PDF
st.markdown("---")
pdf_data = generer_pdf_cv()
st.download_button(
    label="📥 Télécharger mon CV en PDF",
    data=pdf_data,
    file_name="CV_Aminata_SAGNA.pdf",
    mime="application/pdf"
)
