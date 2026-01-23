"""Module for generating and printing reports."""

from fpdf import FPDF, Align

from src.data_filter import (
    generate_declaration_data,
    filter_purchase_data,
    filter_date,
    filter_bank_number,
    filter_name,
)


class PDFReport(FPDF):
    """PDF Report Layout."""

    report = ""

    def header(self) -> None:
        """Create the header for the PDF report."""
        self.set_font("Courier", "B", 10)
        self.cell(0, 10, f"{self.report}", ln=True, align="L")

    def add_table(self, data: str) -> None:
        """Add a table to the PDF report."""
        self.set_font("Courier", size=8)

        for line in data.split("\n"):
            self.cell(0, 5, line, ln=True, align="L")


def print_declaration_report() -> None:
    """Generate and print the declaration report as a PDF."""
    df = generate_declaration_data()

    total_km = df["Subtotal km"].sum()

    pdf = PDFReport()
    pdf.report = "KM Declaration Report"
    pdf.add_page()
    pdf.set_font("Courier", size=8)
    pdf.add_table(df.to_string(justify="right"))
    pdf.cell(0, 10, f"Total km: {total_km}", ln=True)
    pdf.output("km_declaration_report.pdf")
    print("Declaration report generated: km_declaration_report.pdf")


def print_purchase_report(shop_name: str) -> None:
    """Generate and print the purchase report as a PDF."""
    df = filter_purchase_data(shop_name)

    pdf = PDFReport()
    pdf.report = f"Purchase Summary Report - {shop_name}"
    pdf.add_page()
    pdf.set_font("Courier", size=8)
    pdf.cell(0, 5, "_" * 60)
    pdf.ln()
    pdf.add_table(df.to_string(index=False, justify="right"))
    pdf.output("purchase_report.pdf")
    print("Purchase report generated: purchase_report.pdf")


def print_date_report(purchase_date: str) -> None:
    """Generate and print the date-specific report as a PDF."""
    df = filter_date(purchase_date)

    pdf = PDFReport()
    pdf.report = f"Date Report - {purchase_date}"
    pdf.add_page()
    pdf.set_font("Courier", size=8)

    table = [
        ("IBAN", 35, "L"),
        ("Counter Party", 60, "L"),
        ("Amount", 15, "R"),
        ("Description", 80, "L")[:10],
    ]

    for title, width, _ in table:
        pdf.cell(width, 5, title, align="L")
    pdf.ln()

    for _, row in df.iterrows():
        for title, width, align in table:
            pdf.cell(width, 5, str(row[title])[:40], align=align)
        pdf.ln()

    pdf.output("date_report.pdf")
    print("Date report generated: date_report.pdf")
