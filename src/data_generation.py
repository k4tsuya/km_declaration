"""Module for generating data from bank transactions."""

import pandas as pd

from .app import count_shop_visits, purchase_dates, shop_distance


def generate_declaration_data() -> pd.DataFrame:
    """Generate and print a report."""
    report_data = {}

    report_data["Visit count"] = count_shop_visits()
    report_data["Distance"] = shop_distance()
    report_data["Subtotal km"] = {
        shop: report_data["Visit count"][shop] * report_data["Distance"][shop]
        for shop in report_data["Visit count"]
    }

    return pd.DataFrame(report_data)


def generate_purchase_data(
    shop_name: str,
) -> pd.DataFrame:
    """Generate and print a purchase report for a specific shop."""
    report_data = purchase_dates(shop_name)

    return pd.DataFrame(report_data[shop_name])
