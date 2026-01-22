"""Simple KM declaration script."""

from src.app import load_bank_data, purchase_dates
from src.data_generation import (
    generate_declaration_data,
    generate_purchase_data,
)
from src.report_generation import (
    print_declaration_report,
    print_purchase_report,
)

if __name__ == "__main__":
    print_declaration_report()
    print_purchase_report("Sligro")
