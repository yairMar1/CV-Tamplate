import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors


def create_perfect_cv_optimized():
    pdf_path = "Write here how you want call the file + .pdf at the end"

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        topMargin=0.5 * cm,
        bottomMargin=0.5 * cm,
        leftMargin=1.4 * cm,
        rightMargin=1.4 * cm
    )

    styles = getSampleStyleSheet()

    dark = colors.HexColor("#2C3E50")
    header = colors.HexColor("#34495E")
    blue = colors.HexColor("#2980B9")

    # Text styles
    style_name = ParagraphStyle(
        "Name", parent=styles["h1"], fontName="Helvetica-Bold",
        fontSize=22, leading=26, textColor=header, alignment=1
    )

    style_contact = ParagraphStyle(
        "Contact", parent=styles["Normal"], fontName="Helvetica",
        fontSize=10, leading=12, textColor=dark, alignment=1
    )

    style_section = ParagraphStyle(
        "SectionHeader", parent=styles["h2"], fontName="Helvetica-Bold",
        fontSize=12, leading=14, textColor=header, spaceAfter=4
    )

    style_body = ParagraphStyle(
        "Body", parent=styles["Normal"], fontName="Helvetica",
        fontSize=10, leading=12, textColor=dark,
        alignment=4,
        spaceAfter=3
    )

    style_project_title = ParagraphStyle(
        "ProjectTitle", parent=style_body, fontName="Helvetica-Bold",
        fontSize=10.5, leading=12, spaceAfter=2
    )

    style_bullet = ParagraphStyle(
        "Bullet", parent=style_body, fontSize=10, leading=12,
        leftIndent=10, bulletIndent=5
    )

    content = []

    # ================================
    # HEADER
    # ================================
    content.append(Paragraph("Your Name", style_name))

    contacts = f'''
        Location | Phone Number |
        <a href="mailto:your-email-link"><font color="{blue}">Email</font></a> |
        <a href="your-linkedin-link"><font color="{blue}">LinkedIn</font></a> |
        <a href="your-github-link"><font color="{blue}">GitHub</font></a>
    '''
    content.append(Paragraph(contacts, style_contact))
    content.append(Spacer(1, 0.1 * cm))  # Reduced header space

    # ================================
    # SUMMARY
    # ================================
    content.append(Paragraph("Summary", style_section))
    summary_line1 = "The first line of the summary should be a general overview of you — your background and key traits."
    summary_line2 = "The second line should take a little dive into the technologies you have acquired, of course, appropriate for the job."
    summary_line3 = "The third line tells your story and highlights your suitability for the position."
    content.append(Paragraph(summary_line1, style_body))
    content.append(Paragraph(summary_line2, style_body))
    content.append(Paragraph(summary_line3, style_body))
    content.append(Spacer(1, 0.1 * cm))

    # ================================
    # EDUCATION
    # ================================
    content.append(Paragraph("Education", style_section))
    uni_text = """
        Degree name | University | Years | GPA (optional)
    """

    content.append(Paragraph(uni_text, style_body))
    content.append(Spacer(1, 0.1 * cm))

    coursera_text = f"""
    If you have any certifications, you can add them here.
    Course/Certification name | Institution | Years | Link to certificate (optional)
    """
    content.append(Paragraph(coursera_text, style_body))
    content.append(Spacer(1, 0.1 * cm))

    # ================================
    # PROJECTS (4 Projects)
    # ================================
    content.append(Paragraph("Selected Projects", style_section))

    projects = [
        # The structure of your project should be as follows:
        # {
        #     "title": "Project Title" | "Technologies Used",
        #     "link": "Link to your project",
        #     "points": [
        #         Try to summarize in two lines what you learned from this project or which skills you demonstrated in it.
        #         "First line of your project summary",
        #         "Second line of your project summary"
        #     ]
        # },
        # {
        #     "title": "Project Title" | "Technologies Used",
        #     "link": "Link to your project",
        #     "points": [
        #         "First line of your project summary",
        #         "Second line of your project summary"
        #     ]
        # },

        # You can add 3 to 4 projects for this section.
    ]

    for p in projects:
        title = f'{p["title"]} | <a href="{p["link"]}"><font color="{blue}">[{p.get("link_label", "GitHub")}]</font></a>'
        content.append(Paragraph(title, style_project_title))

        for point in p["points"]:
            content.append(Paragraph(f"\u2022 {point}", style_bullet))

        content.append(Spacer(1, 0.1 * cm))
    content.append(Spacer(1, 0.05 * cm))

    # ================================
    # TECHNICAL SKILLS
    # ================================
    content.append(Paragraph("Technical Skills", style_section))
    skills = """
    You can add your skills here, but try to keep it concise and relevant to the job you are applying for.
    For example, list specific web/frontend/backend programming skills — with each type of skill on a separate line.
    
    for example:
    <b>Web & Mobile:</b> React, Node.js, Spring Boot, HTML, CSS, Firebase, Android (Kotlin).<br/>
    <b>Databases:</b> SQL (MySQL, Supabase), NoSQL (Firestore, MongoDB).<br/>
    <b>Cloud:</b> AWS (EC2, CloudWatch), Firebase.<br/>
    <b>AI/ML:</b> Deep Learning, TensorFlow, Transformers, HuggingFace.<br/>
    <b>Tools:</b> Git, Linux, Valgrind, Claude Code, GitHub Copilot.
    """
    content.append(Paragraph(skills, style_body))
    content.append(Spacer(1, 0.1 * cm))

    # ================================
    # EXPERIENCE
    # ================================
    content.append(Paragraph("Name of Your experience", style_section))

    content.append(Paragraph("<b>Name os the experience | where it happened | Years</b>", style_body))
    content.append(Paragraph(
        "First line of your experience summary.</br>",
        "Second line of your experience summary.",
        style_body))
    content.append(Spacer(1, 0.1 * cm))

    content.append(Paragraph("<b>Military experience (optional)</b>", style_body))
    content.append(
        Paragraph("What strengths did you gain? ,what qualities did you develop during your military service?",
                  style_body))
    content.append(Spacer(1, 0.1 * cm))

    content.append(Paragraph("<b>volunteering</b>", style_body))
    content.append(Paragraph(
        "What did you do and get from volunteering? What skills did you develop?",
        style_body))

    # ================================
    # LANGUAGES
    # ================================
    content.append(Spacer(1, 0.1 * cm))
    content.append(Paragraph("Languages", style_section))
    content.append(Paragraph(" for example: Hebrew - Native | English - Proficient", style_body))

    # Build the PDF
    doc.build(content)
    print(f"\nCV created successfully: {os.path.abspath(pdf_path)}")


if __name__ == "__main__":
    create_perfect_cv_optimized()
