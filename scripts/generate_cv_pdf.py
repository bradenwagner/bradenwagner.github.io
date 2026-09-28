"""Generate Braden Wagner's one-page PDF CV.

Edit the content constants near the top of this file, then run the script.
The review copy is written to output/pdf and the website copy to files.
"""

from pathlib import Path
from shutil import copy2

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    HRFlowable,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


NAME = "Braden Wagner"
ROLE = "Ph.D. Student in Economics"
INSTITUTION = "University of Virginia"
LOCATION = "Charlottesville, Virginia"
EMAIL = "dmj3yd@virginia.edu"
DEPARTMENT_URL = "https://economics.virginia.edu/people/braden-wagner"
LINKEDIN_URL = "https://www.linkedin.com/in/bradenwagner"
SITE_URL = "https://bradenwagner.github.io"

NAVY = colors.HexColor("#172B4D")
ORANGE = colors.HexColor("#C85A24")
GRAY = colors.HexColor("#52606D")
LIGHT_GRAY = colors.HexColor("#D9DEE6")


def register_fonts() -> tuple[str, str]:
    """Use common Windows fonts when available and safe PDF fonts otherwise."""
    arial = Path("C:/Windows/Fonts/arial.ttf")
    arial_bold = Path("C:/Windows/Fonts/arialbd.ttf")
    if arial.exists() and arial_bold.exists():
        pdfmetrics.registerFont(TTFont("CVSans", str(arial)))
        pdfmetrics.registerFont(TTFont("CVSans-Bold", str(arial_bold)))
        return "CVSans", "CVSans-Bold"
    return "Helvetica", "Helvetica-Bold"


def build_cv(output_path: Path) -> None:
    regular_font, bold_font = register_fonts()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    document = SimpleDocTemplate(
        str(output_path),
        pagesize=LETTER,
        rightMargin=0.72 * inch,
        leftMargin=0.72 * inch,
        topMargin=0.62 * inch,
        bottomMargin=0.55 * inch,
        title=f"{NAME} - Curriculum Vitae",
        author=NAME,
        subject="Curriculum Vitae",
    )

    base = getSampleStyleSheet()
    styles = {
        "name": ParagraphStyle(
            "CVName",
            parent=base["Title"],
            fontName=bold_font,
            fontSize=25,
            leading=28,
            textColor=NAVY,
            alignment=TA_LEFT,
            spaceAfter=2,
        ),
        "role": ParagraphStyle(
            "CVRole",
            parent=base["Normal"],
            fontName=regular_font,
            fontSize=10.5,
            leading=14,
            textColor=GRAY,
        ),
        "contact": ParagraphStyle(
            "CVContact",
            parent=base["Normal"],
            fontName=regular_font,
            fontSize=8.7,
            leading=12,
            textColor=GRAY,
            alignment=TA_RIGHT,
        ),
        "section": ParagraphStyle(
            "CVSection",
            parent=base["Heading2"],
            fontName=bold_font,
            fontSize=9.5,
            leading=12,
            textColor=ORANGE,
            spaceBefore=13,
            spaceAfter=5,
            uppercase=True,
        ),
        "entry": ParagraphStyle(
            "CVEntry",
            parent=base["Normal"],
            fontName=regular_font,
            fontSize=9.5,
            leading=13.5,
            textColor=NAVY,
            spaceAfter=5,
        ),
        "entry_bold": ParagraphStyle(
            "CVEntryBold",
            parent=base["Normal"],
            fontName=bold_font,
            fontSize=9.8,
            leading=13.5,
            textColor=NAVY,
            spaceAfter=1,
        ),
        "date": ParagraphStyle(
            "CVDate",
            parent=base["Normal"],
            fontName=regular_font,
            fontSize=9,
            leading=13,
            textColor=GRAY,
            alignment=TA_RIGHT,
        ),
        "footer": ParagraphStyle(
            "CVFooter",
            parent=base["Normal"],
            fontName=regular_font,
            fontSize=7.7,
            textColor=GRAY,
        ),
    }

    header_left = [
        Paragraph(NAME, styles["name"]),
        Paragraph(f"{ROLE}<br/>{INSTITUTION} - {LOCATION}", styles["role"]),
    ]
    header_right = Paragraph(
        f'<link href="mailto:{EMAIL}" color="#172B4D">{EMAIL}</link><br/>'
        f'<link href="{DEPARTMENT_URL}" color="#172B4D">Department profile</link><br/>'
        f'<link href="{LINKEDIN_URL}" color="#172B4D">LinkedIn</link>',
        styles["contact"],
    )
    header = Table([[header_left, header_right]], colWidths=[4.7 * inch, 2.15 * inch])
    header.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )

    story = [
        header,
        Spacer(1, 10),
        HRFlowable(width="100%", thickness=1.6, color=ORANGE, spaceAfter=4),
        Paragraph("RESEARCH INTERESTS", styles["section"]),
        Paragraph("Industrial organization; applied microeconomics", styles["entry"]),
        Paragraph("EDUCATION", styles["section"]),
    ]

    education = Table(
        [
            [Paragraph("University of Virginia", styles["entry_bold"]), Paragraph("In progress", styles["date"])],
            [Paragraph("Ph.D. in Economics", styles["entry"]), ""],
            [Paragraph("Baylor University", styles["entry_bold"]), Paragraph("2022", styles["date"])],
            [Paragraph("Economics, Finance, and Mathematics", styles["entry"]), ""],
        ],
        colWidths=[5.8 * inch, 1.05 * inch],
    )
    education.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ("SPAN", (0, 1), (1, 1)),
                ("SPAN", (0, 3), (1, 3)),
            ]
        )
    )
    story.extend(
        [
            education,
            Paragraph("TEACHING EXPERIENCE", styles["section"]),
            Paragraph("<b>University of Virginia</b>", styles["entry_bold"]),
            Paragraph("Industrial Organization - Teaching Assistant", styles["entry"]),
            Paragraph("Intermediate Microeconomics - Teaching support and tutoring", styles["entry"]),
            Spacer(1, 18),
            HRFlowable(width="100%", thickness=0.6, color=LIGHT_GRAY, spaceAfter=6),
            Paragraph(
                f'<link href="{SITE_URL}" color="#52606D">{SITE_URL.removeprefix("https://")}</link>',
                styles["footer"],
            ),
        ]
    )

    document.build(story)


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    review_pdf = repo_root / "output" / "pdf" / "braden-wagner-cv.pdf"
    website_pdf = repo_root / "files" / "braden-wagner-cv.pdf"
    build_cv(review_pdf)
    website_pdf.parent.mkdir(parents=True, exist_ok=True)
    copy2(review_pdf, website_pdf)
    print(f"Generated {website_pdf}")


if __name__ == "__main__":
    main()
