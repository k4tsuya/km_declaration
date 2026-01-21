"""Simple KM declaration script."""

from src.app import load_bank_data, purchase_dates
from src.reports import (
    generate_purchase_report,
    generate_report,
)

if __name__ == "__main__":
    load_bank_data()
    generate_report()
