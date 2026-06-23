from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


class ReportGenerator:

    def generate_report(
        self,
        filename,
        report_text
    ):

        doc = SimpleDocTemplate(
            filename
        )

        styles = getSampleStyleSheet()

        content = []

        content.append(
            Paragraph(
                "SOCShield Incident Report",
                styles["Title"]
            )
        )

        content.append(
            Spacer(1, 12)
        )

        content.append(
            Paragraph(
                report_text.replace(
                    "\n",
                    "<br/>"
                ),
                styles["BodyText"]
            )
        )

        doc.build(content)

        return filename