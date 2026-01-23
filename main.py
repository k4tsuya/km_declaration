"""Simple KM declaration script."""

from src.app import load_bank_data, purchase_dates
from src.data_filter import (
    filter_bank_number,
    filter_date,
    filter_name,
    filter_purchase_data,
    generate_declaration_data,
)
from src.report_generation import (
    print_declaration_report,
    print_purchase_report,
    print_date_report,
)

if __name__ == "__main__":
    # print_declaration_report()
    # print_purchase_report("Sligro")
    # filter_date("2025-12-24")
    # print(filter_bank_number("936"))
    # filter_name("ma")
    print_date_report("2025-12-24")
