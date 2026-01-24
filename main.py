"""Simple KM declaration script."""

from src.app import load_bank_data, purchase_dates
from src.data_filter import (
    filter_bank_number,
    filter_dates,
    filter_name,
    filter_purchase_data,
    generate_declaration_data,
)
from src.report_generation import (
    print_bank_number_search,
    print_date_report,
    print_declaration_report,
    print_name_search,
    print_purchase_report,
)

if __name__ == "__main__":
    # print_declaration_report()
    # print_purchase_report("Sligro")
    # print(filter_bank_number("936"))
    # filter_name("ma")
    # filter_purchase_date("2025-12-23", "2025-12-24")
    # print_bank_number_search("936")
    # print_name_search("ma")
    print_date_report("2025-12-23", "2025-12-24")
