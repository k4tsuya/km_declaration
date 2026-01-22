"""Module for generating and printing reports."""

from fpdf import FPDF

from src.data_generation import (
    generate_declaration_data,
    generate_purchase_data,
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
            self.cell(0, 5, line, ln=True)


def print_declaration_report() -> None:
    """Generate and print the declaration report as a PDF."""
    df = generate_declaration_data()

    total_km = df["Subtotal km"].sum()

    pdf = PDFReport()
    pdf.report = "KM Declaration Report"
    pdf.add_page()
    pdf.set_font("Arial", size=10)
    pdf.add_table(df.to_string(justify="right"))
    pdf.cell(0, 10, f"Total km: {total_km}", ln=True)
    pdf.output("km_declaration_report.pdf")


def print_purchase_report(shop_name: str) -> None:
    """Generate and print the purchase report as a PDF."""
    df = generate_purchase_data(shop_name)

    pdf = PDFReport()
    pdf.report = f"Purchase Summary Report - {shop_name}"
    pdf.add_page()
    pdf.set_font("Arial", size=10)
    pdf.add_table(df.to_string(index=False, justify="right"))
    pdf.output("purchase_report.pdf")
